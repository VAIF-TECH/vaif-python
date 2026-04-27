"""Storage tests using httpx.MockTransport."""

from __future__ import annotations

import io
import json
import asyncio
from typing import Any, Dict, List

import httpx
import pytest

from vaif.lib.storage import (
    upload,
    UploadCancelledError,
)


pytestmark = pytest.mark.asyncio


def _mock_client(handler: Any) -> httpx.AsyncClient:
    return httpx.AsyncClient(transport=httpx.MockTransport(handler))


async def test_oneshot_small_upload() -> None:
    seen: List[httpx.Request] = []

    def handler(req: httpx.Request) -> httpx.Response:
        seen.append(req)
        assert req.url.path == "/storage/upload"
        assert req.headers["x-bucket"] == "avatars"
        assert req.headers["x-path"] == "me.png"
        return httpx.Response(
            200, json={"path": "me.png", "size": len(req.content), "etag": "et-1"}
        )

    http = _mock_client(handler)
    try:
        body = b"hello world" * 10  # ~110 bytes, well under 5MB
        handle = upload(
            client=None,
            bucket="avatars",
            path="me.png",
            file=body,
            base_url="https://api.example.com",
            api_key="sk-test",
            http_client=http,
            content_type="image/png",
        )
        result = await handle
        assert result["path"] == "me.png"
        assert result["etag"] == "et-1"
        assert seen[0].headers["authorization"] == "Bearer sk-test"
    finally:
        await http.aclose()


async def test_oneshot_with_progress_callback() -> None:
    progress: List[float] = []

    def handler(req: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"path": "x.bin", "size": 100, "etag": "e"})

    http = _mock_client(handler)
    try:
        async def cb(p: Any) -> None:
            progress.append(p.percent)

        handle = upload(
            client=None,
            bucket="b",
            path="x.bin",
            file=b"x" * 100,
            base_url="https://api.example.com",
            http_client=http,
            on_progress=cb,
        )
        await handle
        assert progress == [100.0]
    finally:
        await http.aclose()


async def test_multipart_three_chunks() -> None:
    """A 12 MB file with chunk_size=5MB should produce 3 parts."""

    parts_uploaded: List[int] = []
    completed_parts: Dict[str, Any] = {}

    def handler(req: httpx.Request) -> httpx.Response:
        path = req.url.path
        if path == "/storage/multipart/create":
            return httpx.Response(200, json={"uploadId": "u1", "key": "k"})
        if path.endswith("/part-url"):
            body = json.loads(req.content)
            return httpx.Response(
                200,
                json={
                    "url": f"https://signed.example.com/u1/{body['partNumber']}",
                    "partNumber": body["partNumber"],
                },
            )
        if path.startswith("/u1/"):
            # The signed PUT URL.
            part_no = int(path.split("/")[-1])
            parts_uploaded.append(part_no)
            return httpx.Response(200, headers={"etag": f"etag-{part_no}"})
        if path.endswith("/complete"):
            data = json.loads(req.content)
            completed_parts.update(data)
            return httpx.Response(
                200,
                json={
                    "path": data["path"],
                    "size": sum(p["size"] for p in data["parts"]),
                    "etag": "final",
                },
            )
        return httpx.Response(404)

    http = _mock_client(handler)
    try:
        body = b"\xab" * (12 * 1024 * 1024)  # 12 MB
        result = await upload(
            client=None,
            bucket="b",
            path="big.bin",
            file=body,
            base_url="https://api.example.com",
            chunk_size=5 * 1024 * 1024,
            multipart_threshold=5 * 1024 * 1024,
            concurrency=3,
            http_client=http,
        )
        assert sorted(parts_uploaded) == [1, 2, 3]
        assert result["etag"] == "final"
        assert len(completed_parts["parts"]) == 3
        sizes = sorted(p["size"] for p in completed_parts["parts"])
        # 5MB + 5MB + 2MB
        assert sizes == [2 * 1024 * 1024, 5 * 1024 * 1024, 5 * 1024 * 1024]
    finally:
        await http.aclose()


async def test_cancel_mid_upload() -> None:
    started_event = asyncio.Event()

    async def handler(req: httpx.Request) -> httpx.Response:
        path = req.url.path
        if path == "/storage/multipart/create":
            return httpx.Response(200, json={"uploadId": "u1", "key": "k"})
        if path.endswith("/part-url"):
            started_event.set()
            # Block long enough for cancel to fire.
            await asyncio.sleep(0.5)
            body = json.loads(req.content)
            return httpx.Response(
                200,
                json={
                    "url": f"https://signed.example.com/u1/{body['partNumber']}",
                    "partNumber": body["partNumber"],
                },
            )
        if path.startswith("/u1/"):
            return httpx.Response(200, headers={"etag": "e"})
        if path.endswith("/abort"):
            return httpx.Response(200, json={"aborted": True})
        if path.endswith("/complete"):
            return httpx.Response(200, json={"path": "x"})
        return httpx.Response(404)

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    try:
        body = b"\x00" * (10 * 1024 * 1024)
        handle = upload(
            client=None,
            bucket="b",
            path="big.bin",
            file=body,
            base_url="https://api.example.com",
            chunk_size=5 * 1024 * 1024,
            multipart_threshold=5 * 1024 * 1024,
            http_client=http,
        )
        # Wait until at least one part is being uploaded, then cancel.
        await asyncio.wait_for(started_event.wait(), timeout=2.0)
        await handle.cancel()
        # After cancel the handle's task should be done (and not have produced a result).
        assert handle.done
        with pytest.raises((UploadCancelledError, asyncio.CancelledError, Exception)):
            await handle
    finally:
        await http.aclose()


async def test_upload_from_file_like() -> None:
    def handler(req: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200, json={"path": "x", "size": len(req.content), "etag": "e"}
        )

    http = _mock_client(handler)
    try:
        buf = io.BytesIO(b"abc" * 100)
        result = await upload(
            client=None,
            bucket="b",
            path="x",
            file=buf,
            base_url="https://api.example.com",
            http_client=http,
        )
        assert result["size"] == 300
    finally:
        await http.aclose()


async def test_upload_picks_up_client_attributes() -> None:
    """Passing a fake ``client`` object should pull base_url + api_key from it."""

    class FakeClient:
        base_url = "https://api.example.com/"
        api_key = "fake-key"

    seen: List[httpx.Request] = []

    def handler(req: httpx.Request) -> httpx.Response:
        seen.append(req)
        return httpx.Response(200, json={"path": "x", "size": 3, "etag": "e"})

    http = _mock_client(handler)
    try:
        await upload(
            FakeClient(),
            bucket="b",
            path="x",
            file=b"abc",
            http_client=http,
        )
        assert seen[0].headers["authorization"] == "Bearer fake-key"
        assert seen[0].url.host == "api.example.com"
    finally:
        await http.aclose()


async def test_upload_error_on_4xx() -> None:
    from vaif.lib.storage import UploadError

    def handler(req: httpx.Request) -> httpx.Response:
        return httpx.Response(403, text="forbidden")

    http = _mock_client(handler)
    try:
        with pytest.raises(UploadError):
            await upload(
                client=None,
                bucket="b",
                path="x",
                file=b"hello",
                base_url="https://api.example.com",
                http_client=http,
            )
    finally:
        await http.aclose()


async def test_signed_url_helper() -> None:
    from vaif.lib.storage import upload_to_signed_url

    def handler(req: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers={"etag": "abc"})

    http = _mock_client(handler)
    try:
        result = await upload_to_signed_url(
            "https://signed.example.com/x",
            b"hello",
            http_client=http,
        )
        assert result == {"etag": "abc"}
    finally:
        await http.aclose()
