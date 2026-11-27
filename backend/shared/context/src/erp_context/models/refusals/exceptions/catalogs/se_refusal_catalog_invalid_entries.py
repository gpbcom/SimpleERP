from __future__ import annotations

from erp_context.models.refusals.exceptions.catalogs.se_invalid_refusal_catalog_exception import (
    SEInvalidRefusalCatalogException,
)


class SERefusalCatalogInvalidEntries(SEInvalidRefusalCatalogException):
    """Exception raised when an invalid ``entries`` is provided."""
