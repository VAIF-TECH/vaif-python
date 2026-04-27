"""Integration tests for the realtime layer using an in-process WS server."""

from __future__ import annotations

import json
import asyncio
from typing import Any, Dict, List

import pytest
import websockets

from vaif.lib.realtime import Realtime


pytestmark = pytest.mark.asyncio


async def _start_server(handler: Any) -> Any:
    return await websockets.serve(handler, "127.0.0.1", 0, ping_interval=None)  # type: ignore[attr-defined]


def _ws_url(server: Any) -> str:
    sock = list(server.sockets)[0]
    host, port = sock.getsockname()[:2]
    return f"ws://{host}:{port}/realtime"


async def test_connect_subscribe_receive_broadcast() -> None:
    received: List[Dict[str, Any]] = []
    incoming: List[Dict[str, Any]] = []

    async def handler(ws: Any) -> None:
        async for raw in ws:
            data = json.loads(raw)
            incoming.append(data)
            if data["type"] == "subscribe":
                await ws.send(
                    json.dumps({"type": "subscribed", "channel": data["channel"]})
                )
                # Send a broadcast targeted at the channel.
                await ws.send(
                    json.dumps(
                        {
                            "type": "broadcast",
                            "channel": data["channel"],
                            "event": "msg",
                            "payload": {"hello": "world"},
                        }
                    )
                )

    server = await _start_server(handler)
    try:
        rt = Realtime(url=_ws_url(server))
        await rt.connect()
        ch = rt.channel("room:1")

        ev = asyncio.Event()

        @ch.on_broadcast(event="msg")
        def _h(payload: Dict[str, Any]) -> None:
            received.append(payload)
            ev.set()

        await ch.subscribe(timeout=2.0)
        await asyncio.wait_for(ev.wait(), timeout=2.0)
        assert received == [{"hello": "world"}]
        assert any(m["type"] == "subscribe" for m in incoming)

        await rt.disconnect()
    finally:
        server.close()
        await server.wait_closed()


async def test_send_broadcast_round_trip() -> None:
    server_received: List[Dict[str, Any]] = []

    async def handler(ws: Any) -> None:
        async for raw in ws:
            data = json.loads(raw)
            server_received.append(data)
            if data["type"] == "subscribe":
                await ws.send(
                    json.dumps({"type": "subscribed", "channel": data["channel"]})
                )

    server = await _start_server(handler)
    try:
        rt = Realtime(url=_ws_url(server))
        await rt.connect()
        ch = rt.channel("room:2")
        await ch.subscribe(timeout=2.0)
        await ch.send_broadcast("hello", {"text": "hi"})
        # Give server a moment to record.
        await asyncio.sleep(0.1)
        broadcasts = [m for m in server_received if m["type"] == "broadcast"]
        assert broadcasts == [
            {
                "type": "broadcast",
                "channel": "room:2",
                "event": "hello",
                "payload": {"text": "hi"},
            }
        ]
        await rt.disconnect()
    finally:
        server.close()
        await server.wait_closed()


async def test_presence_sync_dispatched() -> None:
    received: List[Dict[str, Any]] = []

    async def handler(ws: Any) -> None:
        async for raw in ws:
            data = json.loads(raw)
            if data["type"] == "subscribe":
                await ws.send(
                    json.dumps({"type": "subscribed", "channel": data["channel"]})
                )
                await ws.send(
                    json.dumps(
                        {
                            "type": "presence_sync",
                            "channel": data["channel"],
                            "state": {"abc": [{"user_id": "1"}]},
                        }
                    )
                )

    server = await _start_server(handler)
    try:
        rt = Realtime(url=_ws_url(server))
        await rt.connect()
        ch = rt.channel("room:p")
        ev = asyncio.Event()

        @ch.on_presence(event="sync")
        def _h(state: Dict[str, Any]) -> None:
            received.append(state)
            ev.set()

        await ch.subscribe(timeout=2.0)
        await asyncio.wait_for(ev.wait(), timeout=2.0)
        assert received == [{"abc": [{"user_id": "1"}]}]
        await rt.disconnect()
    finally:
        server.close()
        await server.wait_closed()


async def test_postgres_changes_filter_matches() -> None:
    inserts: List[Dict[str, Any]] = []
    updates: List[Dict[str, Any]] = []

    async def handler(ws: Any) -> None:
        async for raw in ws:
            data = json.loads(raw)
            if data["type"] == "subscribe":
                ch = data["channel"]
                await ws.send(json.dumps({"type": "subscribed", "channel": ch}))
                # Send an INSERT and an UPDATE on table=messages
                for op in ("INSERT", "UPDATE"):
                    await ws.send(
                        json.dumps(
                            {
                                "type": "db_change",
                                "projectId": "p",
                                "schema": "public",
                                "table": "messages",
                                "op": op,
                                "record": {"id": 1},
                                "ts": "2026-04-26T00:00:00Z",
                            }
                        )
                    )

    server = await _start_server(handler)
    try:
        rt = Realtime(url=_ws_url(server))
        await rt.connect()
        ch = rt.channel("db:messages")
        ev_i = asyncio.Event()
        ev_u = asyncio.Event()

        @ch.on_postgres_changes(event="INSERT", table="messages")
        def _i(p: Dict[str, Any]) -> None:
            inserts.append(p)
            ev_i.set()

        @ch.on_postgres_changes(event="UPDATE", table="messages")
        def _u(p: Dict[str, Any]) -> None:
            updates.append(p)
            ev_u.set()

        await ch.subscribe(timeout=2.0)
        await asyncio.wait_for(ev_i.wait(), timeout=2.0)
        await asyncio.wait_for(ev_u.wait(), timeout=2.0)
        assert len(inserts) == 1 and inserts[0]["eventType"] == "INSERT"
        assert len(updates) == 1 and updates[0]["eventType"] == "UPDATE"
        await rt.disconnect()
    finally:
        server.close()
        await server.wait_closed()


async def test_async_context_manager() -> None:
    async def handler(ws: Any) -> None:
        async for raw in ws:
            data = json.loads(raw)
            if data["type"] == "subscribe":
                await ws.send(
                    json.dumps({"type": "subscribed", "channel": data["channel"]})
                )

    server = await _start_server(handler)
    try:
        async with Realtime(url=_ws_url(server)) as rt:
            ch = rt.channel("room:cm")
            await ch.subscribe(timeout=2.0)
            assert rt.is_connected
        assert not rt.is_connected
    finally:
        server.close()
        await server.wait_closed()
