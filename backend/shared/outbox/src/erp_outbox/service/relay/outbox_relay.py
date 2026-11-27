from __future__ import annotations

# Standard library imports
import sqlite3
from logging import Logger
from typing import Optional

# First-party imports
from erp_lifecycle.runnables.runnable import Runnable

from erp_outbox.models.exceptions import SEOutboxPublishError, SEOutboxStoreError
from erp_outbox.storage.outbox_store import OutboxStore
from erp_outbox.storage.publishers.publisher import Publisher


class OutboxRelay(Runnable):
    """Publish every event written to the outbox, at least once.

    Attributes:
        store (OutboxStore[sqlite3.Connection]): Where the events wait to be published.
        publisher (Publisher): The adapter the events are published through.
        connection (Optional[sqlite3.Connection]): The open connection, ``None`` until ``initialize()``.
        published_count (int): The number of events published and marked by ``run()``.
        logger (Logger): Logger instance.

    Notes:
        - **An event is marked as published only after the publisher returned.** A stop between the two leaves it
          pending, so it is published again: delivery is at least once, never lost.
        - **Consumers must tolerate a duplicate**, identified by the ``event_id`` of the envelope.
        - The relay makes one pass and does not loop, retry or wait. The service schedules its passes.
        - A refused publish stops the pass, so that later events never overtake the refused one.
    """

    def __init__(
        self, store: OutboxStore[sqlite3.Connection], publisher: Publisher, logger: Optional[Logger] = None
    ) -> None:
        """Create the relay.

        Args:
            store (OutboxStore[sqlite3.Connection]): Where the events wait to be published.
            publisher (Publisher): The adapter the events are published through.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.store = store
        self.publisher = publisher
        self.connection: Optional[sqlite3.Connection] = None
        self.published_count = 0

    ############################
    # Publicly Exposed Methods #
    ############################

    def initialize(self) -> None:
        """Open the connection and create the outbox table when it is missing.

        Raises:
            SEOutboxStoreError: When the database cannot be opened or prepared.
        """
        self.logger.debug("Opening the outbox connection.")
        try:
            self.connection = self.store.connect()
            self.store.create_table(self.connection)
        except SEOutboxStoreError as error:
            self.logger.error("Failed to initialise the outbox relay: %s.", type(error).__name__)
            raise
        self.logger.debug("Opened the outbox connection.")

    def run(self) -> None:
        """Publish the pending events in write order, in one pass.

        Raises:
            SEOutboxStoreError: When the outbox cannot be read or an event cannot be marked.
        """
        connection = self.connection
        if connection is None:
            self.logger.warning("The outbox relay ran before it was initialised.")
            return
        try:
            pending = self.store.pending(connection)
            self.logger.debug("Found %d pending events.", len(pending))
            for envelope in pending:
                try:
                    self.publisher.publish(envelope)
                except SEOutboxPublishError as error:
                    self.logger.warning(
                        "Publisher refused event %s of type %s: %s. "  # noqa: E501
                        "Stopping the pass with %d events published.",
                        envelope.event_id,
                        envelope.event_type,
                        type(error).__name__,
                        self.published_count,
                    )
                    return
                self.store.mark_published(connection, envelope.event_id)
                self.published_count += 1
        except SEOutboxStoreError as error:
            self.logger.error("Failed to relay the outbox events: %s.", type(error).__name__)
            raise
        self.logger.info("Published %d events from the outbox.", self.published_count)

    def close(self) -> None:
        """Close the connection when it is open, safely after a failed ``initialize()`` and when called twice."""
        connection = self.connection
        self.connection = None
        if connection is not None:
            connection.close()
            self.logger.debug("Closed the outbox connection.")
