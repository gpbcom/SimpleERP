from __future__ import annotations

from erp_models.catalogs.exceptions import SEYamlCatalogUnreadable

# First-party imports
from erp_country_rules.models.exceptions.packs.se_invalid_country_pack_exception import SEInvalidCountryPackException


class SECountryPackUnreadable(SEInvalidCountryPackException, SEYamlCatalogUnreadable):
    """Exception raised when a country pack file cannot be read."""
