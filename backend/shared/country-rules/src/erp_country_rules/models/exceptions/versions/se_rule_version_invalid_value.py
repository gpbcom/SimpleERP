from __future__ import annotations

# First-party imports
from erp_country_rules.models.exceptions.versions.se_invalid_rule_version_exception import SEInvalidRuleVersionException


class SERuleVersionInvalidValue(SEInvalidRuleVersionException):
    """Exception raised when an invalid ``value`` is provided."""
