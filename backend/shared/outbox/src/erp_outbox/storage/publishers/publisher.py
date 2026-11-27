from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod

# First-party imports
from erp_models.events.event_envelope import EventEnvelope


class Publisher(ABC):
    """The outbound adapter the relay publishes events through.

    Notes:
        The event bus is chosen in P2, so the relay depends on this interface only.
    """

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def publish(self, envelope: EventEnvelope) -> None:
        """Publish one event to the bus.

        Args:
            envelope (EventEnvelope): The event to publish.

        Raises:
            SEOutboxPublishError: When the bus refuses the event.

        Notes:
            - **Return only once the bus has taken the event**, because the relay then marks it as published.
        """
