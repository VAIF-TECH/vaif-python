# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FunctionUpdateParams"]


class FunctionUpdateParams(TypedDict, total=False):
    description: Optional[str]

    enabled: bool

    entrypoint: str

    name: str

    schedule: Optional[str]

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMs")]
