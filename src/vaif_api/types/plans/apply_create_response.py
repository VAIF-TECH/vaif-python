# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ApplyCreateResponse"]


class ApplyCreateResponse(BaseModel):
    ok: Literal[True]

    applied_steps: Optional[object] = FieldInfo(alias="appliedSteps", default=None)
