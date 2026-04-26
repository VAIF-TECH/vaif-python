# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIKeyAPIKeysResponse"]


class APIKeyAPIKeysResponse(BaseModel):
    api_key: str = FieldInfo(alias="apiKey")

    api_key_id: str = FieldInfo(alias="apiKeyId")
