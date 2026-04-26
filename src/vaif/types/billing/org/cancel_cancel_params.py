# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CancelCancelParams"]


class CancelCancelParams(TypedDict, total=False):
    cancel_immediately: Annotated[bool, PropertyInfo(alias="cancelImmediately")]
