from __future__ import annotations

# First-party imports
from erp_config.models.exceptions.loading.se_app_config_error import SEAppConfigError


class SEAppConfigInvalidError(SEAppConfigError):
    """Raised when validation refuses the configuration data."""
