# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InquireCreateParams", "Requirements"]


class InquireCreateParams(TypedDict, total=False):
    company_name: Required[Annotated[str, PropertyInfo(alias="companyName")]]

    contact_email: Required[Annotated[str, PropertyInfo(alias="contactEmail")]]

    contact_name: Required[Annotated[str, PropertyInfo(alias="contactName")]]

    company_size: Annotated[Literal["1-10", "11-50", "51-200", "201-500", "500+"], PropertyInfo(alias="companySize")]

    contact_phone: Annotated[str, PropertyInfo(alias="contactPhone")]

    current_plan: Annotated[
        Literal["free", "starter", "pro", "agency", "studio_plus"], PropertyInfo(alias="currentPlan")
    ]

    estimated_projects: Annotated[int, PropertyInfo(alias="estimatedProjects")]

    requirements: Requirements

    source: str

    use_case: Annotated[str, PropertyInfo(alias="useCase")]


class Requirements(TypedDict, total=False):
    bedrock_routing: Annotated[bool, PropertyInfo(alias="bedrockRouting")]

    custom_retention: Annotated[bool, PropertyInfo(alias="customRetention")]

    custom_sla: Annotated[bool, PropertyInfo(alias="customSla")]

    dedicated_db: Annotated[bool, PropertyInfo(alias="dedicatedDb")]

    dedicated_support: Annotated[bool, PropertyInfo(alias="dedicatedSupport")]

    hipaa_compliance: Annotated[bool, PropertyInfo(alias="hipaaCompliance")]

    saml: bool

    soc2_compliance: Annotated[bool, PropertyInfo(alias="soc2Compliance")]

    sso: bool

    vertex_routing: Annotated[bool, PropertyInfo(alias="vertexRouting")]
