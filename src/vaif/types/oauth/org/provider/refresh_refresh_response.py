# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["RefreshRefreshResponse", "Tokens"]


class Tokens(BaseModel):
    access_token: Optional[str] = FieldInfo(alias="accessToken", default=None)

    expires_in: Optional[float] = FieldInfo(alias="expiresIn", default=None)

    refresh_token: Optional[str] = FieldInfo(alias="refreshToken", default=None)

    scope: Optional[str] = None

    token_type: Optional[str] = FieldInfo(alias="tokenType", default=None)


class RefreshRefreshResponse(BaseModel):
    ok: Literal[True]

    tokens: Tokens
