# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChangePlanChangePlanParams"]


class ChangePlanChangePlanParams(TypedDict, total=False):
    plan: Required[Literal["starter", "pro", "agency", "studio_plus"]]

    interval: Literal["monthly", "yearly"]
