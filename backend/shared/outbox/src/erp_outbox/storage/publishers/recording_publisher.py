from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import List, Optional

# First-party imports
from erp_models.events.event_envelope import EventEnvelope

from erp_outbox.storage.publishers.publisher import Publisher


class RecordingPublisher(Publisher):
    """A publisher that keeps every event it is given, in call order.

    Attributes:
        published (List[EventEnvelope]): The envelopes published so far.
        logger (Logger): Logger instance.

    Notes:
        It stands in for the event bus in tests. T0.11 and the services' tests use it.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Create an empty publisher.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.published: List[EventEnvelope] = []
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def publish(self, envelope: EventEnvelope) -> None:
        """Record one event.

        Args:
            envelope (EventEnvelope): The event to record.
        """
        self.published.append(envelope)
        self.logger.debug("Recorded event %s of type %s.", envelope.event_id, envelope.event_type)
