# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["BucketUpdateParams"]


class BucketUpdateParams(TypedDict, total=False):
    allowed_mime_types: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="allowedMimeTypes")]

    cors_origins: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="corsOrigins")]

    file_size_limit: Annotated[int, PropertyInfo(alias="fileSizeLimit")]

    public: bool
