from __future__ import annotations

from erp_context.models.refusals.exceptions.catalogs.se_invalid_refusal_catalog_exception import (
    SEInvalidRefusalCatalogException,
)


class SERefusalCatalogUnreadable(SEInvalidRefusalCatalogException):
    """Exception raised when the refusal catalogue file cannot be read."""
