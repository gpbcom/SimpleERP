from __future__ import annotations

# Standard library imports
import sqlite3
from logging import Logger, getLogger
from typing import Optional

# Third-party imports
from erp_models.events.event_envelope import EventEnvelope
from erp_outbox.models.exceptions import SEOutboxStoreError
from erp_outbox.storage.outbox_store import OutboxStore

from erp_metering.models.events.usage_event import UsageEvent
from erp_metering.models.metering.exceptions import SEMeteringUsageEventNotWrittenError


class UsageEventWriter:
    """Writes the usage event of a settled paid call through the outbox, so that none is lost.

    Attributes:
        outbox (OutboxStore[sqlite3.Connection]): Where the events wait to be published.
        logger (Logger): Logger instance.

    Notes:
        - The outbox's ``add`` never commits, so each write opens its own connection and transaction through the
          outbox's API, and commits it itself.
        - **A usage event carries a cost, so it is never logged in full**: only its identifiers are.
    """

    def __init__(self, outbox: OutboxStore[sqlite3.Connection], logger: Optional[Logger] = None) -> None:
        """Keep the outbox.

        Args:
            outbox (OutboxStore[sqlite3.Connection]): Where the events wait to be published.
            logger (Optional[Logger]): Logger instance.
        """
        self.outbox = outbox
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _store(self, envelope: EventEnvelope) -> None:
        """Add one envelope to the outbox in its own transaction and commit it.

        Args:
            envelope (EventEnvelope): The event to keep.

        Raises:
            SEOutboxStoreError: When the outbox cannot be opened or written.
            sqlite3.Error: When the commit fails.
        """
        connection = self.outbox.connect()
        try:
            self.outbox.add(connection, envelope)
            connection.commit()
        except (SEOutboxStoreError, sqlite3.Error):
            connection.rollback()
            raise
        finally:
            connection.close()

    ############################
    # Publicly Exposed Methods #
    ############################

    async def write(self, event: UsageEvent) -> None:
        """Write one usage event through the outbox.

        Args:
            event (UsageEvent): The settled call.

        Raises:
            SEMeteringUsageEventNotWrittenError: When the outbox cannot keep the event.
        """
        envelope = EventEnvelope(
            event_type=UsageEvent.EVENT_TYPE,
            company_id=event.call.company_id,
            payload=event.model_dump(mode="json"),
        )
        self.logger.debug("Writing usage event %s.", envelope.event_id.value)
        try:
            self._store(envelope)
        except (SEOutboxStoreError, sqlite3.Error) as error:
            self.logger.error("Cannot write usage event %s: %s.", envelope.event_id.value, type(error).__name__)
            raise SEMeteringUsageEventNotWrittenError(
                f"Cannot write usage event {envelope.event_id.value} through the outbox."
            ) from error
        self.logger.info("Wrote usage event %s through the outbox.", envelope.event_id.value)
