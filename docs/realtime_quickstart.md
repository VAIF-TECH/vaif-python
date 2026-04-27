# Realtime Quickstart

The `vaif.lib.realtime` module provides a WebSocket-based realtime client with
channel subscriptions, broadcasts, presence, and Postgres change feeds. It is
the Python counterpart to `@vaif/client/realtime` (v0.3.0).

## Install

```sh
pip install "vaif[realtime]"
```

The realtime feature requires the optional `websockets` dependency.

## Connect

```python
import asyncio
from vaif import AsyncVaif
from vaif.lib.realtime import Realtime

async def main():
    vaif = AsyncVaif(api_key="...")

    async with Realtime(client=vaif) as rt:
        channel = rt.channel("room:123")
        await channel.subscribe()
        await channel.send_broadcast("hello", {"text": "hi"})

asyncio.run(main())
```

Or without the context manager:

```python
rt = Realtime(client=vaif)
await rt.connect()
# ...
await rt.disconnect()
```

## Broadcasts

```python
@channel.on_broadcast(event="message")
async def on_message(payload):
    print(payload)

await channel.subscribe()
await channel.send_broadcast("message", {"text": "hi"})
```

Use `event="*"` (the default in the decorator) to receive every broadcast event.

## Presence

```python
@channel.on_presence(event="sync")
def on_sync(state):
    print("presence sync", state)

@channel.on_presence(event="join")
def on_join(payload):
    print("joined", payload["joined"])

await channel.subscribe()
await channel.track({"user_id": "abc"})
# later:
await channel.untrack()
```

## Postgres changes

```python
@channel.on_postgres_changes(event="INSERT", schema="public", table="messages")
def on_insert(payload):
    print("new row", payload["new"])
```

The payload shape mirrors the JS SDK:
`{"schema", "table", "eventType", "new", "old", "commit_timestamp"}`.

Filter keys (all optional): `event` (`INSERT|UPDATE|DELETE|*`), `schema`, `table`.

## Reconnect

The client automatically reconnects with exponential backoff (1s → 30s, ±30%
jitter) when the socket drops. Pass `reconnect=False` to disable, or
`max_reconnect_attempts=N` to cap retries. Pending channel subscriptions are
re-sent on reconnect.

## Future work (not in MVP)

- SSE fallback when WebSocket is blocked
- JWT auth-token refresh
- Client-side rate limiting
- Outgoing message queue with size cap
- Presence cleanup on disconnect
