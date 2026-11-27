from __future__ import annotations

from erp_models.errors.catalogs.exceptions.se_invalid_error_catalog_exception import SEInvalidErrorCatalogException


class SEErrorCatalogUnknownCode(SEInvalidErrorCatalogException):
    """Exception raised when a code is not in the error catalogue."""
