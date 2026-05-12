# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ExecuteCreateParams"]


class ExecuteCreateParams(TypedDict, total=False):
    plan_id: Required[Annotated[str, PropertyInfo(alias="planId")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]

    dry_run: Annotated[bool, PropertyInfo(alias="dryRun")]

    step_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="stepIds")]
