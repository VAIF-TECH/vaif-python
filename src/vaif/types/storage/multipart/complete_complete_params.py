# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CompleteCompleteParams", "Part"]


class CompleteCompleteParams(TypedDict, total=False):
    bucket_id: Required[Annotated[str, PropertyInfo(alias="bucketId")]]

    key: Required[str]

    parts: Required[Iterable[Part]]


class Part(TypedDict, total=False):
    e_tag: Required[Annotated[str, PropertyInfo(alias="ETag")]]

    part_number: Required[Annotated[int, PropertyInfo(alias="PartNumber")]]
