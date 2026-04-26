# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UsageAlertUsageAlertsResponse"]


class UsageAlertUsageAlertsResponse(BaseModel):
    alert_id: str = FieldInfo(alias="alertId")

    ok: Literal[True]
