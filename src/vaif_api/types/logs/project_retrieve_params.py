# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ProjectRetrieveParams"]


class ProjectRetrieveParams(TypedDict, total=False):
    level: Literal["info", "warn", "error"]

    limit: int
