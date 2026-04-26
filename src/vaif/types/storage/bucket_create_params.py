# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["BucketCreateParams"]


class BucketCreateParams(TypedDict, total=False):
    name: Required[str]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    allowed_mime_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedMimeTypes")]

    cors_origins: Annotated[SequenceNotStr[str], PropertyInfo(alias="corsOrigins")]

    env_id: Annotated[str, PropertyInfo(alias="envId")]

    file_size_limit: Annotated[int, PropertyInfo(alias="fileSizeLimit")]

    public: bool
