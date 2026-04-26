# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["QueryQueryParams"]


class QueryQueryParams(TypedDict, total=False):
    table: Required[str]

    wrapper_id: Required[Annotated[str, PropertyInfo(alias="wrapperId")]]

    filters: Dict[str, object]

    limit: float

    offset: float
