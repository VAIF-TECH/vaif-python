"""Pydantic round-trip tests for the realtime wire protocol."""

from __future__ import annotations

import pytest

from vaif.lib.realtime.protocol import (
    Broadcast,
    Subscribe,
    BroadcastReceived,
    DbChange,
    PresenceSync,
    ServerError,
    parse_server_message,
    dump_client_message,
)


def test_subscribe_dumps_to_wire_dict() -> None:
    msg = Subscribe(channel="room:1")
    assert dump_client_message(msg) == {"type": "subscribe", "channel": "room:1"}


def test_broadcast_with_payload() -> None:
    msg = Broadcast(channel="room:1", event="msg", payload={"text": "hi"})
    assert dump_client_message(msg) == {
        "type": "broadcast",
        "channel": "room:1",
        "event": "msg",
        "payload": {"text": "hi"},
    }


def test_parse_broadcast_received() -> None:
    msg = parse_server_message(
        {"type": "broadcast", "channel": "room:1", "event": "msg", "payload": {"a": 1}}
    )
    assert isinstance(msg, BroadcastReceived)
    assert msg.event == "msg"
    assert msg.payload == {"a": 1}


def test_parse_db_change_uses_schema_alias() -> None:
    msg = parse_server_message(
        {
            "type": "db_change",
            "projectId": "p",
            "schema": "public",
            "table": "messages",
            "op": "INSERT",
            "record": {"id": 1},
            "ts": "2026-04-26T00:00:00Z",
        }
    )
    assert isinstance(msg, DbChange)
    assert msg.schema_name == "public"
    assert msg.op == "INSERT"


def test_parse_presence_sync() -> None:
    msg = parse_server_message(
        {"type": "presence_sync", "channel": "room:1", "state": {"abc": [{"u": 1}]}}
    )
    assert isinstance(msg, PresenceSync)
    assert msg.state == {"abc": [{"u": 1}]}


def test_parse_error() -> None:
    msg = parse_server_message(
        {"type": "error", "code": "x", "message": "bad", "channel": "c"}
    )
    assert isinstance(msg, ServerError)
    assert msg.code == "x"


def test_parse_unknown_type_raises() -> None:
    with pytest.raises(ValueError):
        parse_server_message({"type": "nope"})
