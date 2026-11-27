from __future__ import annotations

from erp_models.errors.catalogs.exceptions.se_invalid_error_catalog_exception import SEInvalidErrorCatalogException


class SEErrorCatalogUnreadable(SEInvalidErrorCatalogException):
    """Exception raised when the error catalogue file cannot be read."""
