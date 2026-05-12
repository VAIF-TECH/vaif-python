# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserUpdateResponse", "User"]


class User(BaseModel):
    id: str

    banned: Optional[bool] = None

    banned_at: Union[str, datetime, None] = FieldInfo(alias="bannedAt", default=None)

    banned_reason: Optional[str] = FieldInfo(alias="bannedReason", default=None)

    email: Optional[str] = None

    phone: Optional[str] = None

    provider: Optional[str] = None

    updated_at: Union[str, datetime, None] = FieldInfo(alias="updatedAt", default=None)

    app_metadata: Optional[object] = FieldInfo(alias="appMetadata", default=None)

    metadata: Optional[object] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class UserUpdateResponse(BaseModel):
    user: User
