# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RedeemPromoCreateParams"]


class RedeemPromoCreateParams(TypedDict, total=False):
    code: Required[str]

    org_id: Required[Annotated[str, PropertyInfo(alias="orgId")]]
