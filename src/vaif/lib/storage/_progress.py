"""Progress event used by upload callbacks."""

from __future__ import annotations

from typing import Optional
from dataclasses import dataclass


@dataclass
class ProgressEvent:
    """Progress notification for an in-flight upload.

    Attributes:
        loaded: Bytes uploaded so far.
        total: Total bytes (0 if unknown).
        percent: 0.0–100.0; 0.0 when total is unknown.
    """

    loaded: int
    total: int
    percent: float
    part_number: Optional[int] = None
