# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIKeyUpdateResponse", "APIKey"]


class APIKey(BaseModel):
    id: str

    created_at: Union[str, datetime] = FieldInfo(alias="createdAt")

    expires_at: Union[str, datetime, None] = FieldInfo(alias="expiresAt", default=None)

    last_used_at: Union[str, datetime, None] = FieldInfo(alias="lastUsedAt", default=None)

    name: Optional[str] = None

    scopes: Optional[object] = None

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


class APIKeyUpdateResponse(BaseModel):
    api_key: APIKey = FieldInfo(alias="apiKey")

    ok: Literal[True]
