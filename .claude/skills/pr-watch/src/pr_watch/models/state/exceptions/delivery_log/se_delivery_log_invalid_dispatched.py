from __future__ import annotations

from pr_watch.models.state.exceptions.se_invalid_delivery_log_exception import SEInvalidDeliveryLogException


class SEDeliveryLogInvalidDispatched(SEInvalidDeliveryLogException):
    """Exception raised when an invalid ``dispatched`` is provided."""
