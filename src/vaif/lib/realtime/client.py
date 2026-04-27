"""RealtimeClient — WebSocket orchestrator with reconnect + heartbeat.

This is the Python analogue of ``packages/sdk-js/src/lib/realtime/client.ts``,
trimmed to the MVP surface. Differences from the JS SDK:

- No SSE fallback (WebSocket only)
- No auth token refresh
- No client-side rate limiting
- Auth: Bearer ``api_key`` in the WebSocket sub-protocols / query string

Use the ``Realtime`` alias from ``vaif.lib.realtime`` for a clean DX.
"""

from __future__ import annotations

import json
import random
import asyncio
import logging
from typing import Any, Dict, Union, Optional
from urllib.parse import urlsplit, urlunsplit

try:
    import websockets
    from websockets.exceptions import ConnectionClosed

    # websockets v13 split into legacy + new asyncio API. Try the new one first.
    try:
        from websockets.asyncio.client import (  # type: ignore[import-not-found]
            ClientConnection as _WsClient,
        )
    except ImportError:  # pragma: no cover — old websockets fallback
        from websockets.legacy.client import (  # type: ignore[import-not-found,no-redef]
            WebSocketClientProtocol as _WsClient,
        )
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "The realtime extra is required: install with `pip install vaif[realtime]`"
    ) from exc

from .channel import Channel
from .errors import ConnectionError as RTConnectionError
from .errors import ProtocolError, RealtimeError
from .protocol import (
    Ping,
    Subscribe,
    Subscribed,
    Unsubscribed,
    ServerError,
    ClientMessage,
    ServerMessage,
    dump_client_message,
    parse_server_message,
)

log = logging.getLogger("vaif.realtime")


# Default config values mirror the JS SDK.
DEFAULT_INITIAL_RECONNECT_MS = 1_000
DEFAULT_MAX_RECONNECT_MS = 30_000
DEFAULT_RECONNECT_JITTER = 0.3
DEFAULT_BACKOFF_MULT = 2.0
DEFAULT_HEARTBEAT_INTERVAL_S = 30.0
DEFAULT_HEARTBEAT_TIMEOUT_S = 10.0
DEFAULT_CONNECT_TIMEOUT_S = 10.0


def _compute_backoff_delay(
    attempt: int,
    initial_ms: int = DEFAULT_INITIAL_RECONNECT_MS,
    max_ms: int = DEFAULT_MAX_RECONNECT_MS,
    multiplier: float = DEFAULT_BACKOFF_MULT,
    jitter: float = DEFAULT_RECONNECT_JITTER,
) -> float:
    """Exponential backoff with symmetric jitter (±jitter fraction). Returns seconds."""

    base = min(initial_ms * (multiplier ** max(0, attempt - 1)), max_ms)
    if jitter > 0:
        spread = base * jitter
        base = base + random.uniform(-spread, spread)
    return max(0.0, base) / 1000.0


def _ws_is_closed(ws: Any) -> bool:
    """Version-agnostic 'is the socket closed' check."""

    # New API: ClientConnection has .state which compares to State.OPEN.
    state = getattr(ws, "state", None)
    if state is not None:
        # state.name is "OPEN" / "CLOSED" / "CLOSING" / "CONNECTING"
        return getattr(state, "name", "") != "OPEN"
    # Legacy API: WebSocketClientProtocol has .open boolean.
    open_attr = getattr(ws, "open", None)
    if open_attr is not None:
        return not bool(open_attr)
    return False


def _http_to_ws(base_url: str) -> str:
    """Translate http(s)://host/path to ws(s)://host/path/realtime."""

    parts = urlsplit(base_url)
    scheme = "wss" if parts.scheme in ("https", "wss") else "ws"
    path = parts.path.rstrip("/") + "/realtime"
    return urlunsplit((scheme, parts.netloc, path, parts.query, parts.fragment))


class RealtimeClient:
    """A single realtime WebSocket connection plus a registry of Channels.

    Usage::

        from vaif.lib.realtime import Realtime

        rt = Realtime(client=vaif)
        await rt.connect()
        ch = rt.channel("room:1")
        await ch.subscribe()
        ...
        await rt.disconnect()

    Or as an async context manager::

        async with Realtime(client=vaif).connect_cm() as rt:
            ...
    """

    def __init__(
        self,
        client: Any = None,
        *,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        reconnect: bool = True,
        heartbeat_interval: float = DEFAULT_HEARTBEAT_INTERVAL_S,
        heartbeat_timeout: float = DEFAULT_HEARTBEAT_TIMEOUT_S,
        connect_timeout: float = DEFAULT_CONNECT_TIMEOUT_S,
        max_reconnect_attempts: Optional[int] = None,
    ) -> None:
        if url is None:
            if client is None:
                raise ValueError("either `client` or `url` must be provided")
            base = str(getattr(client, "base_url", "") or "https://api.vaif.studio")
            url = _http_to_ws(base)
        if api_key is None and client is not None:
            api_key = getattr(client, "api_key", None)
        self._url = url
        self._api_key = api_key
        self._reconnect_enabled = reconnect
        self._heartbeat_interval = heartbeat_interval
        self._heartbeat_timeout = heartbeat_timeout
        self._connect_timeout = connect_timeout
        self._max_reconnect_attempts = max_reconnect_attempts

        self._ws: Optional[Any] = None
        self._channels: Dict[str, Channel] = {}
        self._read_task: Optional[asyncio.Task[None]] = None
        self._heartbeat_task: Optional[asyncio.Task[None]] = None
        self._reconnect_task: Optional[asyncio.Task[None]] = None
        self._closed = False
        self._connected_event = asyncio.Event()
        self._intentional_close = False
        self._reconnect_attempt = 0

    # ─── Public ──────────────────────────────────────────────────────────

    @property
    def is_connected(self) -> bool:
        return self._ws is not None and not self._closed and not _ws_is_closed(self._ws)

    async def connect(self) -> "RealtimeClient":
        await self._open_socket()
        return self

    async def disconnect(self) -> None:
        self._intentional_close = True
        self._closed = True
        for task in (self._heartbeat_task, self._reconnect_task, self._read_task):
            if task is not None and not task.done():
                task.cancel()
        if self._ws is not None:
            try:
                await self._ws.close()
            except Exception:  # noqa: BLE001
                pass
        self._ws = None

    def channel(self, name: str) -> Channel:
        ch = self._channels.get(name)
        if ch is None:
            ch = Channel(name, self)
            self._channels[name] = ch
        return ch

    async def __aenter__(self) -> "RealtimeClient":
        return await self.connect()

    async def __aexit__(self, *_: Any) -> None:
        await self.disconnect()

    # ─── Internal ────────────────────────────────────────────────────────

    def _build_url(self) -> str:
        if self._api_key:
            sep = "&" if "?" in self._url else "?"
            return f"{self._url}{sep}token={self._api_key}"
        return self._url

    async def _open_socket(self) -> None:
        url = self._build_url()
        headers: Dict[str, str] = {}
        if self._api_key:
            headers["x-vaif-key"] = self._api_key

        # ``connect()`` accepts different header kwargs across versions:
        # >=13: additional_headers; <13: extra_headers.
        connect_kwargs: Dict[str, Any] = {
            "ping_interval": None,
            "max_size": 10 * 1024 * 1024,
        }
        if headers:
            try:
                import inspect as _inspect

                params = _inspect.signature(websockets.connect).parameters  # type: ignore[attr-defined]
                if "additional_headers" in params:
                    connect_kwargs["additional_headers"] = list(headers.items())
                else:
                    connect_kwargs["extra_headers"] = list(headers.items())
            except Exception:  # noqa: BLE001
                connect_kwargs["additional_headers"] = list(headers.items())

        try:
            self._ws = await asyncio.wait_for(
                websockets.connect(url, **connect_kwargs),  # type: ignore[attr-defined]
                timeout=self._connect_timeout,
            )
        except asyncio.TimeoutError as exc:
            raise RTConnectionError(
                f"connect timed out after {self._connect_timeout}s",
                code="connect_timeout",
            ) from exc
        except Exception as exc:  # noqa: BLE001
            raise RTConnectionError(
                f"connect failed: {exc}", code="connect_failed"
            ) from exc

        self._closed = False
        self._intentional_close = False
        self._reconnect_attempt = 0
        self._connected_event.set()
        self._read_task = asyncio.create_task(
            self._read_loop(), name="vaif-realtime-read"
        )
        self._heartbeat_task = asyncio.create_task(
            self._heartbeat_loop(), name="vaif-realtime-hb"
        )
        # Resubscribe channels (e.g. after a reconnect).
        for name in list(self._channels.keys()):
            try:
                await self._send(Subscribe(channel=name))
            except Exception as exc:  # noqa: BLE001
                log.debug("resubscribe failed for %s: %s", name, exc)

    async def _read_loop(self) -> None:
        ws = self._ws
        if ws is None:
            return
        try:
            async for raw in ws:
                if isinstance(raw, (bytes, bytearray)):
                    raw = raw.decode("utf-8", errors="replace")
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError as exc:
                    log.warning("realtime: bad JSON from server: %s", exc)
                    continue
                try:
                    msg = parse_server_message(data)
                except Exception as exc:  # noqa: BLE001
                    log.warning("realtime: protocol error: %s — raw=%r", exc, data)
                    raise ProtocolError(str(exc)) from exc
                await self._handle_server_message(msg)
        except ConnectionClosed:
            pass
        except ProtocolError:
            # Treat as a transport failure → reconnect.
            pass
        except asyncio.CancelledError:
            raise
        except Exception as exc:  # noqa: BLE001
            log.warning("realtime: read loop crashed: %s", exc)
        finally:
            await self._on_socket_closed()

    async def _handle_server_message(self, msg: ServerMessage) -> None:
        # Acks first.
        if isinstance(msg, Subscribed):
            ch = self._channels.get(msg.channel)
            if ch is not None:
                ch._mark_subscribed()
            return
        if isinstance(msg, Unsubscribed):
            return
        if isinstance(msg, ServerError):
            log.warning(
                "realtime: server error %s: %s (channel=%s)",
                msg.code,
                msg.message,
                msg.channel,
            )
            return
        # Pong is handled by the heartbeat loop via ws.recv? We don't track here.
        if msg.type == "pong":  # type: ignore[union-attr]
            return
        # Channel-targeted events.
        channel_name = getattr(msg, "channel", None)
        if channel_name is not None:
            ch = self._channels.get(channel_name)
            if ch is not None:
                await ch._dispatch(msg)
            return
        # Presence sync may carry channel inside; otherwise broadcast to all.
        for ch in self._channels.values():
            await ch._dispatch(msg)

    async def _heartbeat_loop(self) -> None:
        try:
            while not self._closed and self._ws is not None:
                await asyncio.sleep(self._heartbeat_interval)
                if self._ws is None or _ws_is_closed(self._ws):
                    return
                try:
                    await self._send(Ping(ts=asyncio.get_event_loop().time()))
                except Exception:  # noqa: BLE001
                    # If we can't send a ping the read loop will see the close
                    return
                # We don't strictly track the pong; if the socket dies the
                # read loop terminates and triggers reconnect.
        except asyncio.CancelledError:
            raise

    async def _on_socket_closed(self) -> None:
        ws = self._ws
        self._ws = None
        if ws is not None:
            try:
                await ws.close()
            except Exception:  # noqa: BLE001
                pass
        if self._intentional_close or not self._reconnect_enabled:
            return
        if self._reconnect_task is not None and not self._reconnect_task.done():
            return
        self._reconnect_task = asyncio.create_task(
            self._reconnect_loop(), name="vaif-realtime-reconnect"
        )

    async def _reconnect_loop(self) -> None:
        try:
            while not self._intentional_close and self._reconnect_enabled:
                self._reconnect_attempt += 1
                if (
                    self._max_reconnect_attempts is not None
                    and self._reconnect_attempt > self._max_reconnect_attempts
                ):
                    return
                delay = _compute_backoff_delay(self._reconnect_attempt)
                log.debug(
                    "realtime: reconnect #%d in %.2fs",
                    self._reconnect_attempt,
                    delay,
                )
                await asyncio.sleep(delay)
                if self._intentional_close:
                    return
                try:
                    await self._open_socket()
                    return
                except RealtimeError as exc:
                    log.debug("realtime: reconnect attempt failed: %s", exc)
                    continue
        except asyncio.CancelledError:
            raise

    async def _send(self, msg: Union[ClientMessage, Dict[str, Any]]) -> None:
        if self._ws is None:
            raise RTConnectionError("not connected", code="not_connected")
        if isinstance(msg, dict):
            payload = msg
        else:
            payload = dump_client_message(msg)
        try:
            await self._ws.send(json.dumps(payload))
        except ConnectionClosed as exc:
            raise RTConnectionError(
                f"send failed: connection closed: {exc}", code="send_closed"
            ) from exc
