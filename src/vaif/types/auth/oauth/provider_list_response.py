# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProviderListResponse", "Provider"]


class Provider(BaseModel):
    name: str

    provider: str

    allow_linking: Optional[bool] = FieldInfo(alias="allowLinking", default=None)

    allow_signup: Optional[bool] = FieldInfo(alias="allowSignup", default=None)


class ProviderListResponse(BaseModel):
    providers: List[Provider]
