# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TaxInfoTaxInfoParams", "Address"]


class TaxInfoTaxInfoParams(TypedDict, total=False):
    address: Address

    business_name: Annotated[Optional[str], PropertyInfo(alias="businessName")]

    tax_id: Annotated[Optional[str], PropertyInfo(alias="taxId")]

    tax_id_type: Annotated[Optional[str], PropertyInfo(alias="taxIdType")]


class Address(TypedDict, total=False):
    city: Optional[str]

    country: Optional[str]

    line1: Optional[str]

    line2: Optional[str]

    postal_code: Annotated[Optional[str], PropertyInfo(alias="postalCode")]

    state: Optional[str]
