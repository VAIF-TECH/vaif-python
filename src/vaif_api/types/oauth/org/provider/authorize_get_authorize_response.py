# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AuthorizeGetAuthorizeResponse"]


class AuthorizeGetAuthorizeResponse(BaseModel):
    authorization_url: str = FieldInfo(alias="authorizationUrl")

    expires_in: float = FieldInfo(alias="expiresIn")

    state: str
