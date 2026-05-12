# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PartURLPartURLResponse"]


class PartURLPartURLResponse(BaseModel):
    ok: Literal[True]

    part_number: float = FieldInfo(alias="partNumber")

    url: str
