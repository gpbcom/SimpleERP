from __future__ import annotations

# First-party imports
from erp_country_rules.models.exceptions.errors.se_country_rules_error import SECountryRulesError


class SECountryRuleNotInForceError(SECountryRulesError):
    """Raised when a country rule has no version in force on the requested date."""
