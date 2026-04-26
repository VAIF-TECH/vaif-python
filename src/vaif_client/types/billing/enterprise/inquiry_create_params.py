# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["InquiryCreateParams"]


class InquiryCreateParams(TypedDict, total=False):
    company: Required[str]

    email: Required[str]

    name: Required[str]

    message: str

    org_id: Annotated[str, PropertyInfo(alias="orgId")]

    phone: str

    team_size: Annotated[Literal["1-10", "11-50", "51-200", "201-1000", "1000+"], PropertyInfo(alias="teamSize")]
