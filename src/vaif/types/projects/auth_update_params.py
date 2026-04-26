# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AuthUpdateParams"]


class AuthUpdateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    client_id: Required[Annotated[str, PropertyInfo(alias="clientId")]]

    client_secret: Required[Annotated[str, PropertyInfo(alias="clientSecret")]]

    redirect_uri: Required[Annotated[str, PropertyInfo(alias="redirectUri")]]

    enabled: bool

    scopes: SequenceNotStr[str]
