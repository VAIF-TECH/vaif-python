# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    key: Required[str]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    value: Required[str]

    env_id: Annotated[str, PropertyInfo(alias="envId")]
