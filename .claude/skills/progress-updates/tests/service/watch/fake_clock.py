from __future__ import annotations

from datetime import datetime, timedelta
from typing import List

from progress_updates.service.watch.clock import Clock


class FakeClock(Clock):
    """A clock that never waits: each sleep moves its time forward and is recorded."""

    def __init__(self, start: datetime) -> None:
        super().__init__()
        self.current = start
        self.sleeps: List[float] = []

    def now(self) -> datetime:
        return self.current

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.current += timedelta(seconds=seconds)
