# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BillingContactBillingContactsResponse", "Contact"]


class Contact(BaseModel):
    id: str

    created_at: Union[datetime, str] = FieldInfo(alias="createdAt")

    email: str

    label: Optional[str] = None

    org_id: str = FieldInfo(alias="orgId")


class BillingContactBillingContactsResponse(BaseModel):
    contact: Contact

    ok: Literal[True]
