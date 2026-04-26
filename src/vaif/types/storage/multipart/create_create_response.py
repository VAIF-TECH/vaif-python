# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CreateCreateResponse"]


class CreateCreateResponse(BaseModel):
    key: str

    ok: Literal[True]

    upload_id: str = FieldInfo(alias="uploadId")
