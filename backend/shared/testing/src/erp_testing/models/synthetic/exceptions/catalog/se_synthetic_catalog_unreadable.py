from __future__ import annotations

from erp_testing.models.synthetic.exceptions.catalog.se_invalid_synthetic_catalog_exception import (
    SEInvalidSyntheticCatalogException,
)


class SESyntheticCatalogUnreadable(SEInvalidSyntheticCatalogException):
    """Exception raised when the synthetic catalogue file cannot be read."""
