# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ApplyCreateParams"]


class ApplyCreateParams(TypedDict, total=False):
    plan_id: Required[Annotated[str, PropertyInfo(alias="planId")]]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    allow_apply: Annotated[bool, PropertyInfo(alias="allowApply")]

    env_id: Annotated[str, PropertyInfo(alias="envId")]
