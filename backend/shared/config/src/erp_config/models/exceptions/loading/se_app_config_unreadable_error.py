from __future__ import annotations

# First-party imports
from erp_config.models.exceptions.loading.se_app_config_error import SEAppConfigError


class SEAppConfigUnreadableError(SEAppConfigError):
    """Raised when the configuration file is missing, is not YAML or is not a mapping."""
