from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from typing import List

# First-party imports
from erp_models.events.event_envelope import EventEnvelope
from erp_models.ids.record_id import RecordId


class OutboxStore[ConnectionT](ABC):
    """Where a service keeps the events it has to publish, until they are published.

    Notes:
        - **The change and its event share the caller's transaction.** ``add`` never commits or rolls back, so a
          rollback drops the change and its event, and a commit keeps both.
        - ``mark_published`` is the one method that commits, because publishing is a separate step from the change.
        - The class is generic over the connection type of the database it stores into.
    """

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def connect(self) -> ConnectionT:
        """Open a connection to the database.

        Returns:
            ConnectionT: A new connection, which the caller closes.
        """

    @abstractmethod
    def create_table(self, connection: ConnectionT) -> None:
        """Create the outbox table when it does not exist yet.

        Args:
            connection (ConnectionT): The connection to create it with.
        """

    @abstractmethod
    def add(self, connection: ConnectionT, envelope: EventEnvelope) -> None:
        """Write one event inside the caller's open transaction, without committing or rolling back.

        Args:
            connection (ConnectionT): The connection of the caller's transaction.
            envelope (EventEnvelope): The event to keep.
        """

    @abstractmethod
    def pending(self, connection: ConnectionT) -> List[EventEnvelope]:
        """Read the events not published yet.

        Args:
            connection (ConnectionT): The connection to read with.

        Returns:
            List[EventEnvelope]: The unpublished events, in write order.
        """

    @abstractmethod
    def mark_published(self, connection: ConnectionT, event_id: RecordId) -> None:
        """Mark one event as published and commit.

        Args:
            connection (ConnectionT): The connection to write with.
            event_id (RecordId): The identifier of the event.
        """
