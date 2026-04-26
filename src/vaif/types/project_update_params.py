# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    default_environment: Annotated[
        Literal["development", "staging", "production"], PropertyInfo(alias="defaultEnvironment")
    ]

    description: Optional[str]

    features: Dict[str, bool]

    name: str

    timezone: str
