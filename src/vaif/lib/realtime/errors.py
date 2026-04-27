"""Realtime-specific exception hierarchy.

These are public — see ``vaif.lib.realtime.__init__`` for re-exports.
"""

from __future__ import annotations

from typing import Optional


class RealtimeError(Exception):
    """Base class for all realtime errors."""

    def __init__(self, message: str, code: Optional[str] = None) -> None:
        super().__init__(message)
        self.message = message
        self.code = code


class ConnectionError(RealtimeError):  # noqa: A001 — public name shadow is intentional
    """Raised for transport / WebSocket connection failures."""


class SubscriptionError(RealtimeError):
    """Raised when a channel cannot subscribe or is rejected by the server."""

    def __init__(
        self, message: str, code: Optional[str] = None, channel: Optional[str] = None
    ) -> None:
        super().__init__(message, code)
        self.channel = channel


class ProtocolError(RealtimeError):
    """Raised when a server message fails Pydantic validation."""
