"""``vaif.lib.storage`` — file uploads with multipart + cancellation.

Public usage::

    from vaif.lib.storage import upload

    handle = upload(vaif, bucket="avatars", path="me.jpg",
                    file=open("me.jpg", "rb"), content_type="image/jpeg")
    result = await handle
    print(result["path"], result.get("size"), result.get("etag"))
"""

from .errors import (
    StorageError,
    UploadError,
    ChunkUploadError,
    UploadCancelledError,
    SignedUrlError,
)
from .upload import upload, UploadHandle
from ._progress import ProgressEvent
from .signed_url import upload_to_signed_url

__all__ = [
    "upload",
    "UploadHandle",
    "ProgressEvent",
    "upload_to_signed_url",
    "StorageError",
    "UploadError",
    "ChunkUploadError",
    "UploadCancelledError",
    "SignedUrlError",
]
