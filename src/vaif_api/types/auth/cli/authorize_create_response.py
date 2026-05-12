# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["AuthorizeCreateResponse"]


class AuthorizeCreateResponse(BaseModel):
    code: str

    url: str
