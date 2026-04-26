# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProviderUpdateResponse", "Connection"]


class Connection(BaseModel):
    id: str

    client_id: str = FieldInfo(alias="clientId")

    enabled: bool

    provider: str

    redirect_uri: str = FieldInfo(alias="redirectUri")


class ProviderUpdateResponse(BaseModel):
    connection: Connection

    ok: Literal[True]
