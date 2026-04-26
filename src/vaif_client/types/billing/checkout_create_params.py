# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CheckoutCreateParams"]


class CheckoutCreateParams(TypedDict, total=False):
    org_id: Required[Annotated[str, PropertyInfo(alias="orgId")]]

    plan: Required[Literal["starter", "pro", "agency", "studio_plus"]]

    cancel_url: Annotated[str, PropertyInfo(alias="cancelUrl")]

    interval: Literal["monthly", "yearly"]

    promo_code: Annotated[str, PropertyInfo(alias="promoCode")]

    success_url: Annotated[str, PropertyInfo(alias="successUrl")]
