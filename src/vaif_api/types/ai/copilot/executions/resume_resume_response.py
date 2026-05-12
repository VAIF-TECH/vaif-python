# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ResumeResumeResponse"]


class ResumeResumeResponse(BaseModel):
    execution_id: str = FieldInfo(alias="executionId")

    message: str

    ok: Literal[True]

    from_checkpoint: Optional[str] = FieldInfo(alias="fromCheckpoint", default=None)
