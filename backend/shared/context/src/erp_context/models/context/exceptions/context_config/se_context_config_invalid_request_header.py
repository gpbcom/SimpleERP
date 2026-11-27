from __future__ import annotations

from erp_context.models.context.exceptions.context_config.se_invalid_context_config_exception import (
    SEInvalidContextConfigException,
)


class SEContextConfigInvalidRequestHeader(SEInvalidContextConfigException):
    """Exception raised when an invalid ``request_header`` is provided."""
