from __future__ import annotations

# First-party imports
from erp_country_rules.models.exceptions.rules.se_invalid_country_rule_exception import SEInvalidCountryRuleException


class SECountryRuleInvalidVersions(SEInvalidCountryRuleException):
    """Exception raised when an invalid ``versions`` is provided."""
