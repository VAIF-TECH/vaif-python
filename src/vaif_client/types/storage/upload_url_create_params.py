# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UploadURLCreateParams"]


class UploadURLCreateParams(TypedDict, total=False):
    key: Required[str]

    bucket: str

    size_bytes: Annotated[int, PropertyInfo(alias="sizeBytes")]
