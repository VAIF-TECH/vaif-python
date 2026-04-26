# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QueryCreateResponse", "Field"]


class Field(BaseModel):
    data_type_id: float = FieldInfo(alias="dataTypeID")

    name: str


class QueryCreateResponse(BaseModel):
    execution_time_ms: float = FieldInfo(alias="executionTimeMs")

    ok: Literal[True]

    row_count: Optional[float] = FieldInfo(alias="rowCount", default=None)

    rows: List[object]

    command: Optional[str] = None

    fields: Optional[List[Field]] = None

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
