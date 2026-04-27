# Storage Quickstart

The `vaif.lib.storage` module uploads files to your Vaif Storage buckets with
automatic multipart support, concurrent chunk uploads, retries, progress
callbacks, and cancellation.

## Basic upload

```python
import asyncio
from vaif import AsyncVaif
from vaif.lib.storage import upload

async def main():
    vaif = AsyncVaif(api_key="...")
    result = await upload(
        vaif,
        bucket="avatars",
        path="me.jpg",
        file="/path/to/me.jpg",
        content_type="image/jpeg",
    )
    print(result["path"], result.get("etag"))

asyncio.run(main())
```

`file=` accepts:
- a path (`str` or `pathlib.Path`)
- raw `bytes` / `bytearray` / `memoryview`
- any binary file-like object (`BinaryIO`, `io.BytesIO`, an open file handle)

## Progress callbacks

```python
async def on_progress(p):
    print(f"{p.percent:.0f}% ({p.loaded}/{p.total})")

handle = upload(vaif, bucket="b", path="big.bin", file=path, on_progress=on_progress)
result = await handle
```

The callback may be sync or async. It is called per completed chunk for
multipart uploads, or once at completion for one-shot uploads.

## Cancellation

```python
handle = upload(vaif, bucket="b", path="big.bin", file=path)
# elsewhere:
await handle.cancel()
```

Cancel sends a best-effort `POST /storage/multipart/{id}/abort` to the server
to clean up. Awaiting a cancelled handle raises `UploadCancelledError`.

## Multipart tuning

```python
handle = upload(
    vaif,
    bucket="b",
    path="huge.bin",
    file=path,
    multipart_threshold=10 * 1024 * 1024,  # default 5 MB
    chunk_size=5 * 1024 * 1024,             # default 5 MB
    concurrency=3,                          # default 3
)
```

Files at or above `multipart_threshold` use the multipart flow. Each chunk is
retried up to 3 times with exponential backoff (1s, 2s, 4s).

## Direct signed-URL upload

For S3-compatible signed PUT URLs (e.g. from `vaif.storage.create_upload_url`):

```python
from vaif.lib.storage import upload_to_signed_url

await upload_to_signed_url(
    "https://signed.example.com/...",
    body_bytes,
    method="PUT",
    headers={"content-type": "image/jpeg"},
)
```

## Errors

All errors derive from `StorageError`:
- `UploadError` — generic failure
- `ChunkUploadError` — a multipart part failed after all retries
- `UploadCancelledError` — `handle.cancel()` was called
- `SignedUrlError` — direct signed-URL upload failure

## Future work (not in MVP)

- Resume support (persist part etags between runs)
- Streaming uploads without buffering chunks in memory
- Server-driven backpressure
