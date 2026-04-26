# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["AuthSignupParams"]


class AuthSignupParams(TypedDict, total=False):
    email: str

    metadata: Dict[str, object]

    password: str

    phone: str
