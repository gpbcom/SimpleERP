from __future__ import annotations

from ai_cost.models.ledger.exceptions.ledger.se_invalid_ledger_exception import SEInvalidLedgerException


class SELedgerInvalidTicket(SEInvalidLedgerException):
    """Exception raised when an invalid ``ticket`` is provided."""
