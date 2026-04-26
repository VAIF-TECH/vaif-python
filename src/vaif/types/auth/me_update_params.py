# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MeUpdateParams"]


class MeUpdateParams(TypedDict, total=False):
    avatar_url: Annotated[Optional[str], PropertyInfo(alias="avatarUrl")]

    name: str

    phone: Optional[str]

    timezone: str
