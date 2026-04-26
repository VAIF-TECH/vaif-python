# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UsageAlertUsageAlertsParams"]


class UsageAlertUsageAlertsParams(TypedDict, total=False):
    metric: Required[
        Literal["ai_credits", "api_requests", "storage", "realtime_connections", "function_invocations", "bandwidth"]
    ]

    threshold: Required[float]

    notify_email: Annotated[bool, PropertyInfo(alias="notifyEmail")]
