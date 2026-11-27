from __future__ import annotations

# First-party imports
from erp_country_rules.models.exceptions.packs.se_invalid_country_pack_exception import SEInvalidCountryPackException


class SECountryPackInvalidCountry(SEInvalidCountryPackException):
    """Exception raised when an invalid ``country`` is provided."""
