# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AuthForgotPasswordResponse"]


class AuthForgotPasswordResponse(BaseModel):
    message: str

    ok: Literal[True]

    reset_token: Optional[str] = FieldInfo(alias="resetToken", default=None)
