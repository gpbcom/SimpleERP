from __future__ import annotations

from logging import Logger
from typing import Optional

from erp_models.events.event_envelope import EventEnvelope
from erp_outbox.models.exceptions import SEOutboxPublishError
from erp_outbox.storage.publishers.recording_publisher import RecordingPublisher


class RefusingPublisher(RecordingPublisher):
    """A publisher that refuses its first calls, then records like ``RecordingPublisher``."""

    def __init__(self, refusals: int, logger: Optional[Logger] = None) -> None:
        """Create the publisher.

        Args:
            refusals (int): How many calls to refuse before recording.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.refusals = refusals
        self.calls = 0

    def publish(self, envelope: EventEnvelope) -> None:
        """Refuse while refusals are left, otherwise record the event."""
        self.calls += 1
        if self.calls <= self.refusals:
            raise SEOutboxPublishError("The bus refused the event on purpose.")
        super().publish(envelope)
