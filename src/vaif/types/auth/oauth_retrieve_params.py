# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OAuthRetrieveParams"]


class OAuthRetrieveParams(TypedDict, total=False):
    mode: Literal["login", "link"]

    redirect: str
