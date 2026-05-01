# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "TokenCreateResponse",
    "AuthCliTokenPost200Variant0",
    "AuthCliTokenPost200Variant1",
    "AuthCliTokenPost200Variant1User",
]


class AuthCliTokenPost200Variant0(BaseModel):
    """CLI auth token poll: still pending — the user hasn't approved the device yet."""

    ok: Literal[False]

    status: Literal["pending"]


class AuthCliTokenPost200Variant1User(BaseModel):
    id: str

    email: str

    name: Optional[str] = None


class AuthCliTokenPost200Variant1(BaseModel):
    """CLI auth token poll: approved — token issued, login complete."""

    access_token: str = FieldInfo(alias="accessToken")

    expires_in: float = FieldInfo(alias="expiresIn")

    ok: Literal[True]

    user: AuthCliTokenPost200Variant1User


TokenCreateResponse: TypeAlias = Union[AuthCliTokenPost200Variant0, AuthCliTokenPost200Variant1]
