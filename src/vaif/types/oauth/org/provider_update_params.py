# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ProviderUpdateParams"]


class ProviderUpdateParams(TypedDict, total=False):
    org_id: Required[Annotated[str, PropertyInfo(alias="orgId")]]

    client_id: Annotated[str, PropertyInfo(alias="clientId")]

    client_secret: Annotated[str, PropertyInfo(alias="clientSecret")]

    enabled: bool

    redirect_uri: Annotated[str, PropertyInfo(alias="redirectUri")]
