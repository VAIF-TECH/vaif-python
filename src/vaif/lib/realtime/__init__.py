"""``vaif.lib.realtime`` — WebSocket realtime client.

Public surface mirrors ``@vaif/client/realtime``::

    from vaif.lib.realtime import Realtime

    rt = Realtime(client=vaif)
    await rt.connect()
    ch = rt.channel("room:1")

    @ch.on_broadcast(event="msg")
    async def _(payload):
        print(payload)

    await ch.subscribe()
    await ch.send_broadcast("msg", {"text": "hi"})
    await rt.disconnect()
"""

from .errors import (
    RealtimeError,
    ProtocolError,
    SubscriptionError,
)
from .errors import ConnectionError as ConnectionError  # re-export, shadows builtin
from .channel import Channel
from .client import RealtimeClient as Realtime
from .client import RealtimeClient

__all__ = [
    "Realtime",
    "RealtimeClient",
    "Channel",
    "RealtimeError",
    "ConnectionError",
    "SubscriptionError",
    "ProtocolError",
]
