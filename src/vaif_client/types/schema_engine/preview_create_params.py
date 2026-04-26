# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "PreviewCreateParams",
    "Definition",
    "DefinitionTable",
    "DefinitionTableColumn",
    "DefinitionTableColumnReferences",
    "DefinitionTableIndex",
    "DefinitionTableUnique",
]


class PreviewCreateParams(TypedDict, total=False):
    definition: Required[Definition]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    allow_destructive: Annotated[bool, PropertyInfo(alias="allowDestructive")]

    env_id: Annotated[str, PropertyInfo(alias="envId")]


class DefinitionTableColumnReferences(TypedDict, total=False):
    table: Required[str]

    column: str

    on_delete: Annotated[
        Literal["CASCADE", "RESTRICT", "SET NULL", "SET DEFAULT", "NO ACTION"], PropertyInfo(alias="onDelete")
    ]

    on_update: Annotated[
        Literal["CASCADE", "RESTRICT", "SET NULL", "SET DEFAULT", "NO ACTION"], PropertyInfo(alias="onUpdate")
    ]


class DefinitionTableColumn(TypedDict, total=False):
    name: Required[str]

    type: Required[
        Literal[
            "uuid",
            "text",
            "varchar",
            "string",
            "int",
            "integer",
            "bigint",
            "boolean",
            "bool",
            "jsonb",
            "json",
            "timestamptz",
            "timestamp",
            "date",
            "numeric",
            "decimal",
            "float",
            "double",
            "text[]",
            "integer[]",
        ]
    ]

    default: Union[str, float, bool]

    nullable: bool

    primary_key: Annotated[bool, PropertyInfo(alias="primaryKey")]

    references: DefinitionTableColumnReferences

    unique: bool


class DefinitionTableIndex(TypedDict, total=False):
    columns: Required[SequenceNotStr[str]]

    name: Required[str]

    unique: bool


class DefinitionTableUnique(TypedDict, total=False):
    columns: Required[SequenceNotStr[str]]

    name: Required[str]


class DefinitionTable(TypedDict, total=False):
    columns: Required[Iterable[DefinitionTableColumn]]

    name: Required[str]

    indexes: Iterable[DefinitionTableIndex]

    unique: Iterable[DefinitionTableUnique]


class Definition(TypedDict, total=False):
    schema_version: Required[Annotated[Literal["1.0"], PropertyInfo(alias="schemaVersion")]]

    tables: Required[Iterable[DefinitionTable]]
