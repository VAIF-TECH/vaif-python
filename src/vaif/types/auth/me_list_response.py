# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MeListResponse", "User"]


class User(BaseModel):
    id: str

    created_at: Union[datetime, str] = FieldInfo(alias="createdAt")

    email: str

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)

    email_verified_at: Union[datetime, str, None] = FieldInfo(alias="emailVerifiedAt", default=None)

    name: Optional[str] = None

    phone: Optional[str] = None

    timezone: Optional[str] = None

    updated_at: Union[datetime, str, None] = FieldInfo(alias="updatedAt", default=None)


class MeListResponse(BaseModel):
    ok: Literal[True]

    user: User
