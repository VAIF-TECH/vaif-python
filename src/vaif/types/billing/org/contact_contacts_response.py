# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ContactContactsResponse"]


class ContactContactsResponse(BaseModel):
    contact_id: str = FieldInfo(alias="contactId")

    ok: Literal[True]
