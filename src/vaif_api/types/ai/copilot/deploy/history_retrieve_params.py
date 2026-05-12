# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["HistoryRetrieveParams"]


class HistoryRetrieveParams(TypedDict, total=False):
    limit: int

    offset: int

    status: Literal["success", "failed", "partial_failure", "rolled_back", "in_progress"]
