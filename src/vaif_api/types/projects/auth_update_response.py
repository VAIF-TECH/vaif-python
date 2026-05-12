# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AuthUpdateResponse", "App"]


class App(BaseModel):
    id: str

    client_id: str = FieldInfo(alias="clientId")

    created_at: Union[str, datetime, None] = FieldInfo(alias="createdAt", default=None)

    enabled: Optional[bool] = None

    provider: str

    redirect_uri: Optional[str] = FieldInfo(alias="redirectUri", default=None)

    updated_at: Union[str, datetime, None] = FieldInfo(alias="updatedAt", default=None)

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


class AuthUpdateResponse(BaseModel):
    app: App
