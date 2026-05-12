# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OrgRetrieveResponse", "Connection"]


class Connection(BaseModel):
    id: str

    client_id: str = FieldInfo(alias="clientId")

    created_at: Union[str, datetime] = FieldInfo(alias="createdAt")

    enabled: bool

    provider: str

    redirect_uri: str = FieldInfo(alias="redirectUri")


class OrgRetrieveResponse(BaseModel):
    connections: List[Connection]
