# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIKeyAPIKeysParams"]


class APIKeyAPIKeysParams(TypedDict, total=False):
    env_id: Annotated[str, PropertyInfo(alias="envId")]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAt", format="iso8601")]

    name: str

    scopes: List[Literal["crud", "realtime", "functions", "storage"]]
