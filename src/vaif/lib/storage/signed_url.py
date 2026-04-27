"""Direct upload to a pre-signed URL (e.g. S3 PUT URL)."""

from __future__ import annotations

from typing import Any, Dict, Optional

import httpx

from .errors import SignedUrlError


async def upload_to_signed_url(
    url: str,
    body: bytes,
    *,
    method: str = "PUT",
    headers: Optional[Dict[str, str]] = None,
    fields: Optional[Dict[str, str]] = None,
    http_client: Optional[httpx.AsyncClient] = None,
) -> Dict[str, Any]:
    """Upload ``body`` directly to a presigned URL. Returns ``{"etag": ...}``.

    Set ``fields`` for POST policy uploads — fields are sent as multipart form
    data along with the file under the key ``"file"``.
    """

    owns = http_client is None
    http = http_client or httpx.AsyncClient(timeout=60.0)
    try:
        if method.upper() == "POST" and fields:
            files = {"file": body}
            data = dict(fields)
            res = await http.post(
                url,
                data=data,
                files=files,
                headers=headers or {},
            )
        else:
            res = await http.request(
                method.upper(),
                url,
                content=body,
                headers=headers or {},
            )
        if res.status_code >= 400:
            raise SignedUrlError(
                f"signed URL upload failed: {res.status_code} {res.text[:200]}",
                code="signed_failed",
            )
        etag = res.headers.get("etag")
        return {"etag": etag} if etag else {}
    finally:
        if owns:
            await http.aclose()
