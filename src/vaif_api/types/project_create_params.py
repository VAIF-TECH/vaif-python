# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProjectCreateParams", "Features"]


class ProjectCreateParams(TypedDict, total=False):
    name: Required[str]

    org_id: Required[Annotated[str, PropertyInfo(alias="orgId")]]

    features: Features

    region_key: Annotated[str, PropertyInfo(alias="regionKey")]

    slug: str


class Features(TypedDict, total=False):
    ai: bool

    analytics: bool

    auth: bool

    database: bool

    functions: bool

    realtime: bool

    scheduling: bool

    storage: bool
