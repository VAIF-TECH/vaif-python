# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    app_metadata: Annotated[Dict[str, object], PropertyInfo(alias="appMetadata")]

    banned: bool

    banned_reason: Annotated[str, PropertyInfo(alias="bannedReason")]

    email: str

    metadata: Dict[str, object]

    phone: str
