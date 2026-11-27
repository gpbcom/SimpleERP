from __future__ import annotations

from erp_platform.models.config.exceptions.se_invalid_platform_config_exception import SEInvalidPlatformConfigException


class SEPlatformConfigInvalidPublicPaths(SEInvalidPlatformConfigException):
    """Exception raised when an invalid ``public_paths`` is provided."""
