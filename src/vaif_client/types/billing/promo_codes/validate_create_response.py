# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ValidateCreateResponse"]


class ValidateCreateResponse(BaseModel):
    applicable_plans: Optional[List[str]] = FieldInfo(alias="applicablePlans", default=None)

    code: str

    discount_type: str = FieldInfo(alias="discountType")

    discount_value: float = FieldInfo(alias="discountValue")

    duration: str

    duration_months: Optional[float] = FieldInfo(alias="durationMonths", default=None)

    expires_at: Union[str, datetime, None] = FieldInfo(alias="expiresAt", default=None)

    ok: Literal[True]
