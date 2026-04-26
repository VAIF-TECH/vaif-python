# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AuthLoginResponse", "User"]


class User(BaseModel):
    id: str

    email: Optional[str] = None

    metadata: Optional[object] = None

    phone: Optional[str] = None

    provider: Optional[str] = None


class AuthLoginResponse(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")

    expires_in: float = FieldInfo(alias="expiresIn")

    ok: Literal[True]

    user: User
