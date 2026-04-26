# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RegionRegionParams"]


class RegionRegionParams(TypedDict, total=False):
    region_key: Required[Annotated[str, PropertyInfo(alias="regionKey")]]

    tenancy_type: Required[
        Annotated[Literal["shared", "dedicated_db", "dedicated_stack"], PropertyInfo(alias="tenancyType")]
    ]
