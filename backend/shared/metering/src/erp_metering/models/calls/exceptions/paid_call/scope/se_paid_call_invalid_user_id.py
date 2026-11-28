from __future__ import annotations

# First-party imports
from erp_metering.models.calls.exceptions.paid_call.se_invalid_paid_call_exception import SEInvalidPaidCallException


class SEPaidCallInvalidUserId(SEInvalidPaidCallException):
    """Exception raised when an invalid ``user_id`` is provided."""
