from __future__ import annotations

# First-party imports
from erp_config.models.exceptions.loading.se_app_config_error import SEAppConfigError


class SEAppConfigMissingDefaultError(SEAppConfigError):
    """Raised when a field of the model is not written in the configuration file."""
