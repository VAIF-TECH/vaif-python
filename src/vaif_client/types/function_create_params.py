# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FunctionCreateParams"]


class FunctionCreateParams(TypedDict, total=False):
    name: Required[str]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    description: str

    entrypoint: str

    env_id: Annotated[str, PropertyInfo(alias="envId")]

    runtime: str

    schedule: str

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMs")]
