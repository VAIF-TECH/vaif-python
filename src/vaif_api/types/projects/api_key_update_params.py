# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIKeyUpdateParams"]


class APIKeyUpdateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(alias="expiresAt", format="iso8601")]

    name: str

    scopes: List[Literal["crud", "realtime", "functions", "storage", "mongodb"]]
