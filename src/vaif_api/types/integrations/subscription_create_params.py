# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["SubscriptionCreateParams", "Config", "EventFilter"]


class SubscriptionCreateParams(TypedDict, total=False):
    config: Required[Config]

    event_filter: Required[Annotated[EventFilter, PropertyInfo(alias="eventFilter")]]

    name: Required[str]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    type: Required[Literal["webhook", "analytics", "slack", "discord"]]

    env_id: Annotated[str, PropertyInfo(alias="envId")]


class Config(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]

    api_secret: Annotated[str, PropertyInfo(alias="apiSecret")]

    headers: Dict[str, str]

    measurement_id: Annotated[str, PropertyInfo(alias="measurementId")]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    provider: str

    secret: str

    url: str


class EventFilter(TypedDict, total=False):
    allow: SequenceNotStr[str]
