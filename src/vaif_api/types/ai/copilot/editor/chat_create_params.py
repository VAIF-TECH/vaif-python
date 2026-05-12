# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ChatCreateParams", "File", "SelectedRange"]


class ChatCreateParams(TypedDict, total=False):
    message: Required[str]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    files: Iterable[File]

    selected_file: Annotated[str, PropertyInfo(alias="selectedFile")]

    selected_range: Annotated[SelectedRange, PropertyInfo(alias="selectedRange")]

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]


class File(TypedDict, total=False):
    content: Required[str]

    path: Required[str]


class SelectedRange(TypedDict, total=False):
    end_line: Required[Annotated[float, PropertyInfo(alias="endLine")]]

    start_line: Required[Annotated[float, PropertyInfo(alias="startLine")]]
