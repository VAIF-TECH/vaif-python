# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DeployCreateParams", "Resource"]


class DeployCreateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    resources: Required[Iterable[Resource]]

    dry_run: Annotated[bool, PropertyInfo(alias="dryRun")]

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]


class Resource(TypedDict, total=False):
    id: Required[str]

    content: Required[str]

    path: Required[str]

    type: Required[Literal["schema", "storage", "functions", "routes", "cron", "auth"]]

    name: str
