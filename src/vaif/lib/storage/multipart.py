"""Multipart upload coordinator.

Implements the three-step protocol:
    POST /storage/multipart/create
    POST /storage/multipart/{id}/part-url + PUT bytes  (looped, concurrent)
    POST /storage/multipart/{id}/complete
"""

from __future__ import annotations

import asyncio
from typing import Any, Dict, List, Optional

import httpx

from .errors import UploadError, ChunkUploadError, UploadCancelledError
from ._input import UploadInput, iter_chunks
from ._progress import ProgressEvent


async def _retry(
    fn: Any,
    *,
    attempts: int = 3,
    base_delay: float = 1.0,
    on_attempt: Optional[Any] = None,
) -> Any:
    last: Optional[BaseException] = None
    for attempt in range(1, attempts + 1):
        try:
            return await fn(attempt)
        except UploadCancelledError:
            raise
        except (httpx.HTTPError, ChunkUploadError) as exc:
            last = exc
            if attempt >= attempts:
                break
            delay = base_delay * (2 ** (attempt - 1))
            await asyncio.sleep(delay)
    assert last is not None
    raise last


async def run_multipart(
    *,
    http: httpx.AsyncClient,
    base_url: str,
    api_key: Optional[str],
    bucket: str,
    path: str,
    file: UploadInput,
    total_bytes: int,
    content_type: str,
    chunk_size: int,
    concurrency: int,
    metadata: Optional[Dict[str, Any]],
    on_progress: Optional[Any],
    cancel_event: asyncio.Event,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {}
    if api_key:
        headers["authorization"] = f"Bearer {api_key}"
        headers["x-vaif-key"] = api_key

    def _check_cancel() -> None:
        if cancel_event.is_set():
            raise UploadCancelledError()

    # 1. Create
    _check_cancel()
    create_body: Dict[str, Any] = {
        "bucket": bucket,
        "path": path,
        "contentType": content_type,
    }
    if metadata:
        create_body["metadata"] = metadata
    create_url = _join(base_url, "/storage/multipart/create")
    res = await http.post(
        create_url,
        json=create_body,
        headers={**headers, "content-type": "application/json"},
    )
    if res.status_code >= 400:
        raise UploadError(
            f"create failed: {res.status_code} {res.text[:200]}",
            code="create_failed",
        )
    create_data = res.json()
    upload_id: str = create_data["uploadId"]

    # 2. Slice + collect (we materialize parts into memory like the JS SDK does;
    # acceptable for MVP — large files are chunked but fully loaded).
    chunks: List[bytes] = []
    async for chunk in iter_chunks(file, chunk_size):
        chunks.append(chunk)

    completed: List[Dict[str, Any]] = []
    completed_lock = asyncio.Lock()
    bytes_uploaded = 0
    bytes_lock = asyncio.Lock()

    sem = asyncio.Semaphore(concurrency)

    async def upload_part(part_number: int, body: bytes) -> Dict[str, Any]:
        async def attempt(_n: int) -> Dict[str, Any]:
            _check_cancel()
            url_url = _join(
                base_url, f"/storage/multipart/{upload_id}/part-url"
            )
            url_res = await http.post(
                url_url,
                json={"partNumber": part_number},
                headers={**headers, "content-type": "application/json"},
            )
            if url_res.status_code >= 400:
                raise ChunkUploadError(
                    f"part-url failed: {url_res.status_code}",
                    code="part_url_failed",
                    part_number=part_number,
                    attempts=_n,
                )
            put_url = url_res.json()["url"]
            _check_cancel()
            put_res = await http.put(
                put_url,
                content=body,
                headers={"content-type": content_type},
            )
            if put_res.status_code >= 400:
                raise ChunkUploadError(
                    f"chunk PUT failed: {put_res.status_code}",
                    code="chunk_failed",
                    part_number=part_number,
                    attempts=_n,
                )
            etag = put_res.headers.get("etag") or f"{upload_id}-{part_number}"
            return {"partNumber": part_number, "etag": etag, "size": len(body)}

        async with sem:
            return await _retry(attempt, attempts=3, base_delay=1.0)

    async def worker(part_number: int, body: bytes) -> None:
        nonlocal bytes_uploaded
        result = await upload_part(part_number, body)
        async with completed_lock:
            completed.append(result)
        async with bytes_lock:
            bytes_uploaded += len(body)
            if on_progress is not None:
                try:
                    pct = (bytes_uploaded / total_bytes * 100.0) if total_bytes else 0.0
                    res = on_progress(
                        ProgressEvent(
                            loaded=bytes_uploaded,
                            total=total_bytes,
                            percent=pct,
                        )
                    )
                    if asyncio.iscoroutine(res):
                        await res
                except Exception:  # noqa: BLE001
                    pass

    tasks = [
        asyncio.create_task(worker(i + 1, chunk)) for i, chunk in enumerate(chunks)
    ]
    try:
        await asyncio.gather(*tasks)
    except UploadCancelledError:
        for t in tasks:
            if not t.done():
                t.cancel()
        # Best-effort abort
        try:
            await http.post(
                _join(base_url, f"/storage/multipart/{upload_id}/abort"),
                json={"uploadId": upload_id},
                headers={**headers, "content-type": "application/json"},
            )
        except Exception:  # noqa: BLE001
            pass
        raise

    _check_cancel()

    # 3. Complete
    completed.sort(key=lambda p: p["partNumber"])
    complete_url = _join(base_url, f"/storage/multipart/{upload_id}/complete")
    res = await http.post(
        complete_url,
        json={
            "uploadId": upload_id,
            "bucket": bucket,
            "path": path,
            "parts": completed,
        },
        headers={**headers, "content-type": "application/json"},
    )
    if res.status_code >= 400:
        raise UploadError(
            f"complete failed: {res.status_code} {res.text[:200]}",
            code="complete_failed",
        )
    return res.json()


def _join(base: str, suffix: str) -> str:
    if base.endswith("/"):
        base = base[:-1]
    if not suffix.startswith("/"):
        suffix = "/" + suffix
    return base + suffix


