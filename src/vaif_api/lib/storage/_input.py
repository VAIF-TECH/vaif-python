"""File input adapters — turn a path / bytes / file-like into chunked async iter.

Mirrors the contract of ``packages/sdk-js/src/lib/storage/slicer.ts`` for Python.
"""

from __future__ import annotations

import io
import os
from typing import IO, Any, Union, AsyncIterator
from pathlib import Path

UploadInput = Union[bytes, bytearray, memoryview, str, "os.PathLike[str]", IO[bytes]]


def total_size(file: UploadInput) -> int:
    """Return the byte length of the input, or 0 if not knowable."""

    if isinstance(file, (bytes, bytearray, memoryview)):
        return len(file)
    if isinstance(file, (str, os.PathLike)):
        try:
            return os.path.getsize(os.fspath(file))
        except OSError:
            return 0
    # File-like: try seek/tell.
    if hasattr(file, "seek") and hasattr(file, "tell"):
        try:
            cur = file.tell()
            file.seek(0, io.SEEK_END)
            size = file.tell()
            file.seek(cur, io.SEEK_SET)
            return int(size)
        except (OSError, ValueError):
            return 0
    return 0


async def iter_chunks(
    file: UploadInput, chunk_size: int
) -> AsyncIterator[bytes]:
    """Yield ``bytes`` chunks of size ``chunk_size`` (final may be smaller)."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")

    if isinstance(file, (bytes, bytearray, memoryview)):
        buf = bytes(file)
        for i in range(0, len(buf), chunk_size):
            yield buf[i : i + chunk_size]
        return

    if isinstance(file, (str, os.PathLike)):
        # Open for reading and yield.
        with open(os.fspath(file), "rb") as fh:
            while True:
                chunk = fh.read(chunk_size)
                if not chunk:
                    return
                yield chunk
        return

    # File-like
    fh: Any = file
    if hasattr(fh, "seek"):
        try:
            fh.seek(0)
        except (OSError, ValueError):
            pass
    while True:
        chunk = fh.read(chunk_size)
        if not chunk:
            return
        if isinstance(chunk, memoryview):
            chunk = bytes(chunk)
        yield chunk


async def read_all(file: UploadInput) -> bytes:
    """Materialize the input into a single bytes buffer."""

    if isinstance(file, (bytes, bytearray, memoryview)):
        return bytes(file)
    if isinstance(file, (str, os.PathLike)):
        with open(os.fspath(file), "rb") as fh:
            return fh.read()
    fh: Any = file
    if hasattr(fh, "seek"):
        try:
            fh.seek(0)
        except (OSError, ValueError):
            pass
    return fh.read()
