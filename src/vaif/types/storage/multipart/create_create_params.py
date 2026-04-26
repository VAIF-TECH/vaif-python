# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CreateCreateParams"]


class CreateCreateParams(TypedDict, total=False):
    bucket_id: Required[Annotated[str, PropertyInfo(alias="bucketId")]]

    key: Required[str]

    content_type: Annotated[str, PropertyInfo(alias="contentType")]
