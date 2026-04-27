"""Public ``upload()`` entry point + ``UploadHandle``.

Usage::

    from vaif.lib.storage import upload

    # awaitable form:
    result = await upload(
        vaif, bucket="avatars", path="me.jpg",
        file=open("me.jpg", "rb"), content_type="image/jpeg",
    )

    # handle form (cancel / progress):
    handle = upload(vaif, bucket=..., path=..., file=..., on_progress=cb)
    result = await handle
    # or: await handle.cancel()
"""

from __future__ import annotations

import asyncio
from typing import Any, Dict, Generator, Optional

import httpx

from .errors import UploadError, UploadCancelledError
from ._input import UploadInput, total_size, read_all
from ._progress import ProgressEvent
from .multipart import run_multipart


DEFAULT_MULTIPART_THRESHOLD = 5 * 1024 * 1024  # 5 MiB
DEFAULT_CHUNK_SIZE = 5 * 1024 * 1024
DEFAULT_CONCURRENCY = 3


class UploadHandle:
    """Awaitable handle returned by :func:`upload`.

    ``await handle`` resolves to the ``UploadResult`` dict. ``await handle.cancel()``
    aborts the in-flight upload (best-effort: also asks the server to abort).
    """

    def __init__(
        self,
        coro_factory: Any,
        cancel_event: asyncio.Event,
    ) -> None:
        self._cancel_event = cancel_event
        self._task: asyncio.Task[Dict[str, Any]] = asyncio.ensure_future(
            coro_factory()
        )

    def __await__(self) -> Generator[Any, None, Dict[str, Any]]:
        return self._task.__await__()

    async def cancel(self) -> None:
        self._cancel_event.set()
        try:
            await self._task
        except (asyncio.CancelledError, UploadCancelledError):
            pass
        except Exception:  # noqa: BLE001
            pass

    @property
    def done(self) -> bool:
        return self._task.done()


def upload(
    client: Any,
    *,
    bucket: str,
    path: str,
    file: UploadInput,
    content_type: str = "application/octet-stream",
    metadata: Optional[Dict[str, Any]] = None,
    cache_control: Optional[str] = None,
    upsert: bool = False,
    multipart_threshold: int = DEFAULT_MULTIPART_THRESHOLD,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    concurrency: int = DEFAULT_CONCURRENCY,
    on_progress: Optional[Any] = None,
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    http_client: Optional[httpx.AsyncClient] = None,
) -> UploadHandle:
    """Upload ``file`` to the configured storage bucket.

    Returns an :class:`UploadHandle` — ``await`` it for the result, or call
    ``handle.cancel()`` to abort.

    Below ``multipart_threshold`` bytes the upload is sent in one POST;
    above it the multipart flow is used. File-likes whose size cannot be
    determined are always uploaded multipart.

    The ``client`` argument may be a ``vaif.Vaif`` / ``vaif.AsyncVaif`` instance
    (we read ``base_url`` and ``api_key``); pass ``base_url=`` / ``api_key=``
    explicitly to override.
    """

    resolved_base = base_url or (
        str(getattr(client, "base_url", "")) if client is not None else ""
    )
    if not resolved_base:
        resolved_base = "https://api.vaif.studio"
    resolved_key = api_key
    if resolved_key is None and client is not None:
        resolved_key = getattr(client, "api_key", None)

    cancel_event = asyncio.Event()

    async def run() -> Dict[str, Any]:
        size = total_size(file)
        force_multipart = size == 0  # unknown size → must use multipart
        use_multipart = force_multipart or size >= multipart_threshold

        owns_http = http_client is None
        http: httpx.AsyncClient = http_client or httpx.AsyncClient(timeout=60.0)
        try:
            if use_multipart:
                # If size unknown, we still need to materialize chunks; iter_chunks
                # handles that.  We pass total_bytes for progress math (0 if unknown).
                return await run_multipart(
                    http=http,
                    base_url=resolved_base,
                    api_key=resolved_key,
                    bucket=bucket,
                    path=path,
                    file=file,
                    total_bytes=size,
                    content_type=content_type,
                    chunk_size=chunk_size,
                    concurrency=concurrency,
                    metadata=metadata,
                    on_progress=on_progress,
                    cancel_event=cancel_event,
                )
            return await _run_oneshot(
                http=http,
                base_url=resolved_base,
                api_key=resolved_key,
                bucket=bucket,
                path=path,
                file=file,
                total_bytes=size,
                content_type=content_type,
                metadata=metadata,
                cache_control=cache_control,
                upsert=upsert,
                on_progress=on_progress,
                cancel_event=cancel_event,
            )
        finally:
            if owns_http:
                await http.aclose()

    return UploadHandle(run, cancel_event)


async def _run_oneshot(
    *,
    http: httpx.AsyncClient,
    base_url: str,
    api_key: Optional[str],
    bucket: str,
    path: str,
    file: UploadInput,
    total_bytes: int,
    content_type: str,
    metadata: Optional[Dict[str, Any]],
    cache_control: Optional[str],
    upsert: bool,
    on_progress: Optional[Any],
    cancel_event: asyncio.Event,
) -> Dict[str, Any]:
    if cancel_event.is_set():
        raise UploadCancelledError()
    body = await read_all(file)
    if cancel_event.is_set():
        raise UploadCancelledError()
    headers: Dict[str, str] = {
        "content-type": content_type,
        "x-bucket": bucket,
        "x-path": path,
    }
    if api_key:
        headers["authorization"] = f"Bearer {api_key}"
        headers["x-vaif-key"] = api_key
    if cache_control:
        headers["cache-control"] = cache_control
    if upsert:
        headers["x-upsert"] = "true"
    if metadata:
        import json

        headers["x-metadata"] = json.dumps(metadata)
    url = base_url.rstrip("/") + "/storage/upload"
    res = await http.post(url, content=body, headers=headers)
    if res.status_code >= 400:
        raise UploadError(
            f"upload failed: {res.status_code} {res.text[:200]}",
            code="upload_failed",
        )
    if on_progress is not None:
        try:
            r = on_progress(
                ProgressEvent(loaded=len(body), total=len(body), percent=100.0)
            )
            if asyncio.iscoroutine(r):
                await r
        except Exception:  # noqa: BLE001
            pass
    return res.json()
