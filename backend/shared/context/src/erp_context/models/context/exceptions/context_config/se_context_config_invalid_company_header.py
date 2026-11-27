from __future__ import annotations

from erp_context.models.context.exceptions.context_config.se_invalid_context_config_exception import (
    SEInvalidContextConfigException,
)


class SEContextConfigInvalidCompanyHeader(SEInvalidContextConfigException):
    """Exception raised when an invalid ``company_header`` is provided."""
