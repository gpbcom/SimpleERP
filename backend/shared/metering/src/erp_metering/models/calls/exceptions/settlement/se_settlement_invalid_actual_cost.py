from __future__ import annotations

# First-party imports
from erp_metering.models.calls.exceptions.settlement.se_invalid_settlement_exception import SEInvalidSettlementException


class SESettlementInvalidActualCost(SEInvalidSettlementException):
    """Exception raised when an invalid ``actual_cost`` is provided."""
