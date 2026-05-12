# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ContactContactsParams"]


class ContactContactsParams(TypedDict, total=False):
    email: Required[str]

    name: Required[str]

    phone: str

    receive_alerts: Annotated[bool, PropertyInfo(alias="receiveAlerts")]

    receive_invoices: Annotated[bool, PropertyInfo(alias="receiveInvoices")]
