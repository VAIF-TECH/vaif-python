# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ChangePlanChangePlanResponse"]


class ChangePlanChangePlanResponse(BaseModel):
    effective_date: Union[str, datetime] = FieldInfo(alias="effectiveDate")

    new_interval: str = FieldInfo(alias="newInterval")

    new_plan: str = FieldInfo(alias="newPlan")

    ok: Literal[True]
