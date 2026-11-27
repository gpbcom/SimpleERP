from __future__ import annotations

from erp_models.catalogs.exceptions import SEYamlCatalogUnreadable


class SESampleCatalogUnreadable(SEYamlCatalogUnreadable):
    """Raised when the sample catalogue cannot be read."""
