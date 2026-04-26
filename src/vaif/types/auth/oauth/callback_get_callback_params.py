# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CallbackGetCallbackParams"]


class CallbackGetCallbackParams(TypedDict, total=False):
    code: str

    error: str

    error_description: str

    state: str
