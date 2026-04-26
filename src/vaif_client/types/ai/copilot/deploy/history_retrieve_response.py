# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["HistoryRetrieveResponse", "Pagination"]


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    limit: float

    offset: float


class HistoryRetrieveResponse(BaseModel):
    deploys: List[object]

    pagination: Pagination
