from __future__ import annotations

# First-party imports
from erp_config.models.exceptions.loading.se_app_config_error import SEAppConfigError


class SEAppConfigUnknownOverrideError(SEAppConfigError):
    """Raised when an environment variable names a path the configuration file does not hold."""
