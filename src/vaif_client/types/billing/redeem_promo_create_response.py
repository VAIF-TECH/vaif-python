# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RedeemPromoCreateResponse"]


class RedeemPromoCreateResponse(BaseModel):
    code: str

    credits_added: float = FieldInfo(alias="creditsAdded")

    ok: Literal[True]
