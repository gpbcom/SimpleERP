from __future__ import annotations

# First-party imports
from erp_country_rules.models.exceptions.rules.se_invalid_country_rule_exception import SEInvalidCountryRuleException


class SECountryRuleOverlappingVersions(SEInvalidCountryRuleException):
    """Exception raised when the versions of a country rule overlap."""
