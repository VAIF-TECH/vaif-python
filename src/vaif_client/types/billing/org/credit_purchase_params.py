# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CreditPurchaseParams"]


class CreditPurchaseParams(TypedDict, total=False):
    package_id: Required[
        Annotated[Literal["credits_10", "credits_25", "credits_50", "credits_100"], PropertyInfo(alias="packageId")]
    ]

    cancel_url: Annotated[str, PropertyInfo(alias="cancelUrl")]

    success_url: Annotated[str, PropertyInfo(alias="successUrl")]
