# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DatabaseDedicatedParams"]


class DatabaseDedicatedParams(TypedDict, total=False):
    tier: Required[Literal["micro", "small", "medium", "large", "xl", "2xl", "custom"]]

    custom_ram_gb: Annotated[float, PropertyInfo(alias="customRamGb")]

    custom_storage_gb: Annotated[int, PropertyInfo(alias="customStorageGb")]

    custom_vcpus: Annotated[int, PropertyInfo(alias="customVcpus")]

    postgres_version: Annotated[str, PropertyInfo(alias="postgresVersion")]

    region: str
