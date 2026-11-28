from __future__ import annotations

# First-party imports
from erp_metering.models.calls.exceptions.settlement.se_invalid_settlement_exception import SEInvalidSettlementException


class SESettlementInvalidReservationId(SEInvalidSettlementException):
    """Exception raised when an invalid ``reservation_id`` is provided."""
