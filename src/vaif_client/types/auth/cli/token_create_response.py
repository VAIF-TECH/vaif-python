# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TokenCreateResponse", "UnionMember0", "UnionMember1", "UnionMember1User"]


class UnionMember0(BaseModel):
    ok: Literal[False]

    status: Literal["pending"]


class UnionMember1User(BaseModel):
    id: str

    email: str

    name: Optional[str] = None


class UnionMember1(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")

    expires_in: float = FieldInfo(alias="expiresIn")

    ok: Literal[True]

    user: UnionMember1User


TokenCreateResponse: TypeAlias = Union[UnionMember0, UnionMember1]
