# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UploadBase64CreateParams"]


class UploadBase64CreateParams(TypedDict, total=False):
    bucket: Required[str]

    data: Required[str]

    path: Required[str]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    content_type: Annotated[str, PropertyInfo(alias="contentType")]
