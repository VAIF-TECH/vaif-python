# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["InstallInstallParams"]


class InstallInstallParams(TypedDict, total=False):
    extension_id: Required[Annotated[str, PropertyInfo(alias="extensionId")]]

    config: Dict[str, object]

    env_id: Annotated[str, PropertyInfo(alias="envId")]
