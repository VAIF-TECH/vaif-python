# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UnsubscribeRetrieveResponse"]


class UnsubscribeRetrieveResponse(BaseModel):
    message: str

    ok: Literal[True]
