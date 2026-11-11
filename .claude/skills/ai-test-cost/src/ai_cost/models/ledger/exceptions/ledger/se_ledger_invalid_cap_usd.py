from __future__ import annotations

from ai_cost.models.ledger.exceptions.ledger.se_invalid_ledger_exception import SEInvalidLedgerException


class SELedgerInvalidCapUsd(SEInvalidLedgerException):
    """Exception raised when an invalid ``cap_usd`` is provided."""
