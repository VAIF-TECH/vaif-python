# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AdminListResponse"]


class AdminListResponse(BaseModel):
    is_admin: bool = FieldInfo(alias="isAdmin")

    ok: Literal[True]

    permissions: Optional[List[str]] = None

    role: Optional[str] = None
