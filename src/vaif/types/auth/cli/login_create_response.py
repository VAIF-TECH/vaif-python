# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["LoginCreateResponse", "User"]


class User(BaseModel):
    id: str

    email: str

    name: Optional[str] = None


class LoginCreateResponse(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")

    expires_in: float = FieldInfo(alias="expiresIn")

    ok: Literal[True]

    refresh_token: str = FieldInfo(alias="refreshToken")

    user: User
