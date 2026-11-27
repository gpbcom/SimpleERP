from __future__ import annotations

from erp_platform.models.config.exceptions.se_invalid_platform_config_exception import SEInvalidPlatformConfigException


class SEPlatformConfigInvalidErrorCodesPath(SEInvalidPlatformConfigException):
    """Exception raised when an invalid ``error_codes_path`` is provided."""
