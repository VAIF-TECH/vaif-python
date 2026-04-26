# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProjectRetrieveResponse", "Incident"]


class Incident(BaseModel):
    id: str

    created_at: Union[str, datetime] = FieldInfo(alias="createdAt")

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    status: str

    message: Optional[str] = None

    type: Optional[str] = None

    updated_at: Union[str, datetime, None] = FieldInfo(alias="updatedAt", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ProjectRetrieveResponse(BaseModel):
    incidents: List[Incident]
