from __future__ import annotations

# First-party imports
from erp_country_rules.models.exceptions.errors.se_country_rules_error import SECountryRulesError


class SECountryPackNotFoundError(SECountryRulesError):
    """Raised when a country pack cannot be found."""
