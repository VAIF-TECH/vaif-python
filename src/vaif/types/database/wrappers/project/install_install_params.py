# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["InstallInstallParams"]


class InstallInstallParams(TypedDict, total=False):
    config: Required[Dict[str, object]]

    wrapper_id: Required[Annotated[str, PropertyInfo(alias="wrapperId")]]

    enabled_tables: Annotated[SequenceNotStr[str], PropertyInfo(alias="enabledTables")]

    env_id: Annotated[str, PropertyInfo(alias="envId")]
