from __future__ import annotations

from ai_cost.storage.ledgers.exceptions.se_ledger_store_error import SELedgerStoreError


class SELedgerTicketRefusedError(SELedgerStoreError):
    """Raised when a key that is not a ticket would name a ledger file."""
