# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CreditPurchaseResponse"]


class CreditPurchaseResponse(BaseModel):
    checkout_url: Optional[str] = FieldInfo(alias="checkoutUrl", default=None)

    ok: Literal[True]
