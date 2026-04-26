# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["SaveCreateParams", "Plan", "PlanStep"]


class SaveCreateParams(TypedDict, total=False):
    name: Required[str]

    org_id: Required[Annotated[str, PropertyInfo(alias="orgId")]]

    plan: Required[Plan]

    task_type: Required[Annotated[str, PropertyInfo(alias="taskType")]]

    description: str

    visibility: Literal["public", "org_private", "unlisted"]


class PlanStep(TypedDict, total=False):
    action: Required[str]

    args: Dict[str, object]


class Plan(TypedDict, total=False):
    intent: Required[str]

    steps: Required[Iterable[PlanStep]]

    version: Required[str]

    warnings: SequenceNotStr[str]
