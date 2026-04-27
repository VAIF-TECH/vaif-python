"""Channel — represents one named subscription on the realtime connection."""

from __future__ import annotations

import asyncio
import inspect
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Tuple,
    Union,
    Callable,
    Optional,
    Awaitable,
)

from .errors import SubscriptionError
from .protocol import (
    Broadcast,
    DbChange,
    PresenceJoin,
    PresenceLeave,
    PresenceSync,
    PresenceTrack,
    PresenceUntrack,
    Subscribe,
    Unsubscribe,
    BroadcastReceived,
    ServerMessage,
)

if TYPE_CHECKING:
    from .client import RealtimeClient


# A handler may be a sync or async callable.
Handler = Callable[..., Union[None, Awaitable[None]]]


class Channel:
    """One realtime subscription. Use ``rt.channel(name)`` to obtain instances."""

    def __init__(self, name: str, client: "RealtimeClient") -> None:
        if not name:
            raise ValueError("channel name must be a non-empty string")
        self.name = name
        self._client = client
        self._broadcast_handlers: Dict[str, List[Handler]] = {}
        self._db_handlers: List[Tuple[Dict[str, Any], Handler]] = []
        self._presence_handlers: Dict[str, List[Handler]] = {
            "sync": [],
            "join": [],
            "leave": [],
        }
        self._subscribed = False
        self._subscribe_event = asyncio.Event()

    # ─── Public registration API ────────────────────────────────────────

    def on(
        self,
        kind: str,
        opts_or_handler: Union[Dict[str, Any], Handler],
        handler: Optional[Handler] = None,
    ) -> "Channel":
        """Register a handler.

        Forms accepted (mirrors the JS SDK):

        - ``channel.on("broadcast", {"event": "msg"}, handler)``
        - ``channel.on("postgres_changes", {"event": "INSERT", "table": "x"}, handler)``
        - ``channel.on("presence", {"event": "sync"}, handler)``  (event: sync|join|leave)

        Returns ``self`` for chaining.
        """

        if handler is None:
            # No-options form: opts_or_handler is the handler itself.
            opts: Dict[str, Any] = {}
            cb = opts_or_handler  # type: ignore[assignment]
        else:
            opts = opts_or_handler  # type: ignore[assignment]
            cb = handler
        if not callable(cb):
            raise TypeError("handler must be callable")

        if kind == "broadcast":
            event = opts.get("event", "*")
            self._broadcast_handlers.setdefault(event, []).append(cb)
        elif kind == "postgres_changes":
            self._db_handlers.append((opts, cb))
        elif kind == "presence":
            event = opts.get("event", "sync")
            if event not in self._presence_handlers:
                raise ValueError(f"unknown presence event: {event!r}")
            self._presence_handlers[event].append(cb)
        else:
            raise ValueError(f"unknown channel event kind: {kind!r}")
        return self

    def on_broadcast(
        self, event: str = "*"
    ) -> Callable[[Handler], Handler]:
        """Decorator form: ``@channel.on_broadcast(event="msg")``."""

        def deco(fn: Handler) -> Handler:
            self.on("broadcast", {"event": event}, fn)
            return fn

        return deco

    def on_postgres_changes(
        self, **filter: Any
    ) -> Callable[[Handler], Handler]:
        def deco(fn: Handler) -> Handler:
            self.on("postgres_changes", filter, fn)
            return fn

        return deco

    def on_presence(
        self, event: str = "sync"
    ) -> Callable[[Handler], Handler]:
        def deco(fn: Handler) -> Handler:
            self.on("presence", {"event": event}, fn)
            return fn

        return deco

    # ─── Public action API ──────────────────────────────────────────────

    async def subscribe(self, *, timeout: float = 10.0) -> "Channel":
        """Send a ``subscribe`` message and wait for the ``subscribed`` ack."""

        self._subscribe_event.clear()
        await self._client._send(Subscribe(channel=self.name))
        try:
            await asyncio.wait_for(self._subscribe_event.wait(), timeout=timeout)
        except asyncio.TimeoutError as exc:
            raise SubscriptionError(
                f"subscribe timed out after {timeout}s",
                code="subscribe_timeout",
                channel=self.name,
            ) from exc
        return self

    async def unsubscribe(self) -> None:
        await self._client._send(Unsubscribe(channel=self.name))
        self._subscribed = False

    async def send_broadcast(
        self, event: str, payload: Optional[Dict[str, Any]] = None
    ) -> None:
        await self._client._send(
            Broadcast(channel=self.name, event=event, payload=payload)
        )

    async def track(self, state: Optional[Dict[str, Any]] = None) -> None:
        await self._client._send(PresenceTrack(state=state))

    async def untrack(self) -> None:
        await self._client._send(PresenceUntrack())

    # ─── Internal: dispatch from the client read loop ───────────────────

    async def _dispatch(self, msg: ServerMessage) -> None:
        """Called by the client when a server message targets this channel.

        The client filters by channel name; this method only sees messages
        belonging to this Channel.
        """

        if isinstance(msg, BroadcastReceived):
            handlers = list(self._broadcast_handlers.get(msg.event, []))
            handlers += list(self._broadcast_handlers.get("*", []))
            await self._invoke_all(handlers, msg.payload or {})
        elif isinstance(msg, DbChange):
            for opts, cb in self._db_handlers:
                if not _matches_db_filter(opts, msg):
                    continue
                await self._invoke_all([cb], _db_change_to_payload(msg))
        elif isinstance(msg, PresenceSync):
            await self._invoke_all(self._presence_handlers["sync"], msg.state)
        elif isinstance(msg, PresenceJoin):
            await self._invoke_all(
                self._presence_handlers["join"],
                {"key": msg.key, "current": msg.current, "joined": msg.joined},
            )
        elif isinstance(msg, PresenceLeave):
            await self._invoke_all(
                self._presence_handlers["leave"],
                {"key": msg.key, "current": msg.current, "left": msg.left},
            )

    def _mark_subscribed(self) -> None:
        self._subscribed = True
        self._subscribe_event.set()

    @staticmethod
    async def _invoke_all(handlers: List[Handler], payload: Any) -> None:
        for cb in handlers:
            try:
                result = cb(payload)
                if inspect.isawaitable(result):
                    await result
            except Exception:  # noqa: BLE001 — handler errors must not kill the read loop
                # Swallow handler errors; mirrors JS SDK behaviour.
                continue


def _matches_db_filter(opts: Dict[str, Any], msg: DbChange) -> bool:
    """Match a postgres_changes filter against an incoming db_change message.

    Filter keys (all optional):
        - ``event``: INSERT | UPDATE | DELETE | * (default *)
        - ``schema``: schema name
        - ``table``: table name
    """

    want_event = opts.get("event", "*")
    if want_event != "*" and want_event != msg.op:
        return False
    want_schema = opts.get("schema")
    if want_schema is not None and want_schema != msg.schema_name:
        return False
    want_table = opts.get("table")
    if want_table is not None and want_table != msg.table:
        return False
    return True


def _db_change_to_payload(msg: DbChange) -> Dict[str, Any]:
    """Translate a db_change message into the JS SDK's PostgresChangesPayload shape."""

    return {
        "schema": msg.schema_name,
        "table": msg.table,
        "eventType": msg.op,
        "new": msg.record,
        "old": msg.old_record,
        "commit_timestamp": msg.ts,
    }
