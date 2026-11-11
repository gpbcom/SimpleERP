from __future__ import annotations

from ai_cost.service.ledgers.exceptions.se_ledger_service_error import SELedgerServiceError


class SELedgerReadFailedError(SELedgerServiceError):
    """Raised when a ticket's ledger cannot be read."""
