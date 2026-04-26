# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChangeGetChangesResponse"]


class ChangeGetChangesResponse(BaseModel):
    data: List[object]

    ok: Literal[True]
