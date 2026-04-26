# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CancelCancelResponse"]


class CancelCancelResponse(BaseModel):
    cancel_at_period_end: bool = FieldInfo(alias="cancelAtPeriodEnd")

    current_period_end: Union[str, datetime] = FieldInfo(alias="currentPeriodEnd")

    ok: Literal[True]
