from __future__ import annotations

from erp_testing.models.synthetic.exceptions.catalog.se_invalid_synthetic_catalog_exception import (
    SEInvalidSyntheticCatalogException,
)


class SESyntheticCatalogInvalidCompanyWords(SEInvalidSyntheticCatalogException):
    """Exception raised when an invalid ``company_words`` is provided."""
