# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TriggerTriggersParams"]


class TriggerTriggersParams(TypedDict, total=False):
    event: Required[Literal["db.insert", "db.update", "db.delete"]]

    table_name: Required[Annotated[str, PropertyInfo(alias="tableName")]]

    enabled: bool

    filter: Dict[str, object]
