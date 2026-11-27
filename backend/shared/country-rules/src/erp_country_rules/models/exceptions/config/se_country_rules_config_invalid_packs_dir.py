from __future__ import annotations

# First-party imports
from erp_country_rules.models.exceptions.config.se_invalid_country_rules_config_exception import (
    SEInvalidCountryRulesConfigException,
)


class SECountryRulesConfigInvalidPacksDir(SEInvalidCountryRulesConfigException):
    """Exception raised when an invalid ``packs_dir`` is provided."""
