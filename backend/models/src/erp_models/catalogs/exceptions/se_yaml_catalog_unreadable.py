from __future__ import annotations

# First-party imports
from erp_models.catalogs.exceptions.se_invalid_yaml_catalog_exception import SEInvalidYamlCatalogException


class SEYamlCatalogUnreadable(SEInvalidYamlCatalogException):
    """Exception raised when a YamlCatalog file cannot be read."""
