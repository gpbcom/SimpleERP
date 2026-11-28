from __future__ import annotations

# First-party imports
from erp_metering.models.calls.exceptions.paid_call.se_invalid_paid_call_exception import SEInvalidPaidCallException


class SEPaidCallInvalidConnector(SEInvalidPaidCallException):
    """Exception raised when an invalid ``connector`` is provided."""
