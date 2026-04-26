# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UptimeRetrieveResponse", "History"]


class History(BaseModel):
    avg_latency: Optional[float] = FieldInfo(alias="avgLatency", default=None)

    date: Union[str, datetime]

    uptime: float


class UptimeRetrieveResponse(BaseModel):
    component_id: str = FieldInfo(alias="componentId")

    days: float

    history: List[History]
