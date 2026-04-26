# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProjectRetrieveResponse", "Token"]


class Token(BaseModel):
    id: str

    created_at: Union[str, datetime] = FieldInfo(alias="createdAt")

    env_id: str = FieldInfo(alias="envId")

    revoked_at: Union[str, datetime, None] = FieldInfo(alias="revokedAt", default=None)


class ProjectRetrieveResponse(BaseModel):
    tokens: List[Token]
