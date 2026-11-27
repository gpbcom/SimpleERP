from __future__ import annotations

from erp_models.errors.catalogs.exceptions.se_invalid_error_catalog_exception import SEInvalidErrorCatalogException


class SEErrorCatalogInvalidCodes(SEInvalidErrorCatalogException):
    """Exception raised when an invalid ``codes`` is provided."""
