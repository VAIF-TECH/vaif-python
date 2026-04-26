# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ProjectRetrieveResponse"]


class ProjectRetrieveResponse(BaseModel):
    migrations: List[object]

    ok: Literal[True]
