"""Storage-specific exceptions."""

from __future__ import annotations

from typing import Optional


class StorageError(Exception):
    """Base class for all storage errors."""

    def __init__(self, message: str, code: Optional[str] = None) -> None:
        super().__init__(message)
        self.message = message
        self.code = code


class UploadError(StorageError):
    """Generic upload failure (one-shot or multipart create/complete)."""


class ChunkUploadError(UploadError):
    """A specific chunk failed after all retries were exhausted."""

    def __init__(
        self,
        message: str,
        code: Optional[str] = None,
        *,
        part_number: Optional[int] = None,
        attempts: int = 0,
    ) -> None:
        super().__init__(message, code)
        self.part_number = part_number
        self.attempts = attempts


class UploadCancelledError(UploadError):
    """Raised when an upload is cancelled via ``handle.cancel()``."""

    def __init__(self, message: str = "upload cancelled") -> None:
        super().__init__(message, code="cancelled")


class SignedUrlError(StorageError):
    """Signed URL upload failure."""
