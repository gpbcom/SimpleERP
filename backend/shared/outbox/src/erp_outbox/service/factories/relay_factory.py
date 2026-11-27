from __future__ import annotations

# First-party imports
from erp_lifecycle.factories.runnable_factory import RunnableFactory

from erp_outbox.service.relay.outbox_relay import OutboxRelay


class RelayFactory(RunnableFactory[OutboxRelay]):
    """Abstract factory that builds the outbox relay.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        - A concrete factory chooses the store the relay reads from.
    """
