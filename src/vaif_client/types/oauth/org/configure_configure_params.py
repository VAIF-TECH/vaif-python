# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ConfigureConfigureParams"]


class ConfigureConfigureParams(TypedDict, total=False):
    client_id: Required[Annotated[str, PropertyInfo(alias="clientId")]]

    client_secret: Required[Annotated[str, PropertyInfo(alias="clientSecret")]]

    provider: Required[Literal["google", "apple", "github"]]

    redirect_uri: Required[Annotated[str, PropertyInfo(alias="redirectUri")]]
