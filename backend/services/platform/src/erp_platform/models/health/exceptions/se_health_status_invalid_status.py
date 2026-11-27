from __future__ import annotations

from erp_platform.models.health.exceptions.se_invalid_health_status_exception import SEInvalidHealthStatusException


class SEHealthStatusInvalidStatus(SEInvalidHealthStatusException):
    """Exception raised when an invalid ``status`` is provided."""
