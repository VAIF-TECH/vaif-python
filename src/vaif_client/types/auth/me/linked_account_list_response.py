# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["LinkedAccountListResponse", "Account"]


class Account(BaseModel):
    id: str

    provider: str

    last_used_at: Union[datetime, str, None] = FieldInfo(alias="lastUsedAt", default=None)

    linked_at: Union[datetime, str, None] = FieldInfo(alias="linkedAt", default=None)

    provider_data: Optional[object] = FieldInfo(alias="providerData", default=None)

    provider_email: Optional[str] = FieldInfo(alias="providerEmail", default=None)


class LinkedAccountListResponse(BaseModel):
    accounts: List[Account]
