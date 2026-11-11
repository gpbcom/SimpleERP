from __future__ import annotations

from pr_watch.models.state.exceptions.se_invalid_delivery_log_exception import SEInvalidDeliveryLogException


class SEDeliveryLogInvalidNotified(SEInvalidDeliveryLogException):
    """Exception raised when an invalid ``notified`` is provided."""
