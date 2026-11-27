from __future__ import annotations

# Standard library imports
from logging import Logger
from pathlib import Path
from typing import Optional

# First-party imports
from erp_outbox.service.factories.relay_factory import RelayFactory
from erp_outbox.service.relay.outbox_relay import OutboxRelay
from erp_outbox.storage.publishers.publisher import Publisher
from erp_outbox.storage.sqlite.sqlite_outbox_store import SqliteOutboxStore


class SqliteRelayFactory(RelayFactory):
    """Build relays that read the outbox of a SQLite database.

    Attributes:
        database_path (Path): The database file the relays read.
        publisher (Publisher): The adapter every relay publishes through.
        logger (Logger): Logger instance.
    """

    def __init__(self, database_path: Path, publisher: Publisher, logger: Optional[Logger] = None) -> None:
        """Create the factory.

        Args:
            database_path (Path): The database file the relays read.
            publisher (Publisher): The adapter every relay publishes through.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.database_path = database_path
        self.publisher = publisher

    ############################
    # Publicly Exposed Methods #
    ############################

    def create(self) -> OutboxRelay:
        """Build a new relay on its own store.

        Returns:
            OutboxRelay: A new relay, not yet initialised.
        """
        self.logger.debug("Creating an outbox relay on %s.", self.database_path)
        store = SqliteOutboxStore(self.database_path, self.logger)
        return OutboxRelay(store, self.publisher, self.logger)
