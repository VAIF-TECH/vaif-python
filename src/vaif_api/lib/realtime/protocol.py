"""Pydantic models mirroring the realtime wire protocol.

These match the Zod schemas in the JS SDK
(``packages/sdk-js/src/lib/realtime/protocol.ts``). Keep field names in lockstep —
the wire format is shared across SDKs.
"""

from __future__ import annotations

from typing import Any, Dict, List, Union, Literal, Optional

try:
    # Pydantic v2
    from pydantic import BaseModel, Field, ConfigDict
    from pydantic import ValidationError as ValidationError  # noqa: F401 — re-export

    _PYDANTIC_V2 = True
except ImportError:  # pragma: no cover — Pydantic v1 fallback shouldn't hit in practice
    from pydantic import BaseModel, Field  # type: ignore[no-redef]
    from pydantic import ValidationError as ValidationError  # type: ignore[no-redef]  # noqa: F401

    ConfigDict = dict  # type: ignore[assignment,misc]
    _PYDANTIC_V2 = False


JsonObject = Dict[str, Any]


class _Base(BaseModel):
    if _PYDANTIC_V2:
        model_config = ConfigDict(extra="ignore")
    else:  # pragma: no cover

        class Config:
            extra = "ignore"


# ─── Client → Server ────────────────────────────────────────────────────


class Subscribe(_Base):
    type: Literal["subscribe"] = "subscribe"
    channel: str


class Unsubscribe(_Base):
    type: Literal["unsubscribe"] = "unsubscribe"
    channel: str


class Ping(_Base):
    type: Literal["ping"] = "ping"
    ts: Optional[float] = None


class Broadcast(_Base):
    type: Literal["broadcast"] = "broadcast"
    channel: str
    event: str
    payload: Optional[JsonObject] = None


class PresenceTrack(_Base):
    type: Literal["presence_track"] = "presence_track"
    state: Optional[JsonObject] = None


class PresenceUpdate(_Base):
    type: Literal["presence_update"] = "presence_update"
    state: JsonObject


class PresenceUntrack(_Base):
    type: Literal["presence_untrack"] = "presence_untrack"


class PresenceList(_Base):
    type: Literal["presence_list"] = "presence_list"


ClientMessage = Union[
    Subscribe,
    Unsubscribe,
    Ping,
    Broadcast,
    PresenceTrack,
    PresenceUpdate,
    PresenceUntrack,
    PresenceList,
]


# ─── Server → Client ────────────────────────────────────────────────────


class Pong(_Base):
    type: Literal["pong"] = "pong"
    ts: Optional[float] = None


class Subscribed(_Base):
    type: Literal["subscribed"] = "subscribed"
    channel: str


class Unsubscribed(_Base):
    type: Literal["unsubscribed"] = "unsubscribed"
    channel: str


class DbChange(_Base):
    type: Literal["db_change"] = "db_change"
    projectId: str
    schema_name: str = Field(alias="schema")
    table: str
    op: Literal["INSERT", "UPDATE", "DELETE"]
    record: Optional[JsonObject] = None
    old_record: Optional[JsonObject] = None
    ts: str
    partial: Optional[bool] = None

    if _PYDANTIC_V2:
        model_config = ConfigDict(populate_by_name=True, extra="ignore")
    else:  # pragma: no cover

        class Config:
            allow_population_by_field_name = True
            extra = "ignore"


class BroadcastReceived(_Base):
    type: Literal["broadcast"] = "broadcast"
    channel: str
    event: str
    payload: Optional[JsonObject] = None


class PresenceSync(_Base):
    type: Literal["presence_sync"] = "presence_sync"
    channel: Optional[str] = None
    state: Dict[str, List[JsonObject]]


class PresenceJoin(_Base):
    type: Literal["presence_join"] = "presence_join"
    key: str
    current: List[JsonObject]
    joined: List[JsonObject]


class PresenceLeave(_Base):
    type: Literal["presence_leave"] = "presence_leave"
    key: str
    current: List[JsonObject]
    left: List[JsonObject]


class ServerError(_Base):
    type: Literal["error"] = "error"
    code: str
    message: str
    channel: Optional[str] = None


ServerMessage = Union[
    Pong,
    Subscribed,
    Unsubscribed,
    DbChange,
    BroadcastReceived,
    PresenceSync,
    PresenceJoin,
    PresenceLeave,
    ServerError,
]


_SERVER_TYPES: Dict[str, type] = {
    "pong": Pong,
    "subscribed": Subscribed,
    "unsubscribed": Unsubscribed,
    "db_change": DbChange,
    "broadcast": BroadcastReceived,
    "presence_sync": PresenceSync,
    "presence_join": PresenceJoin,
    "presence_leave": PresenceLeave,
    "error": ServerError,
}


def parse_server_message(data: JsonObject) -> ServerMessage:
    """Validate a raw dict into a typed ``ServerMessage``.

    Raises ``pydantic.ValidationError`` for malformed inputs. Callers in the
    Channel/Client layer translate these into ``ProtocolError``.
    """

    msg_type = data.get("type")
    cls = _SERVER_TYPES.get(msg_type)  # type: ignore[arg-type]
    if cls is None:
        raise ValueError(f"unknown server message type: {msg_type!r}")
    if _PYDANTIC_V2:
        return cls.model_validate(data)  # type: ignore[no-any-return]
    return cls.parse_obj(data)  # type: ignore[no-any-return]


def dump_client_message(msg: ClientMessage) -> JsonObject:
    """Serialize a client message to a dict ready for ``json.dumps``."""

    if _PYDANTIC_V2:
        return msg.model_dump(by_alias=True, exclude_none=True)
    return msg.dict(by_alias=True, exclude_none=True)  # type: ignore[no-any-return]
