from __future__ import annotations

from harness_core.models.catalogs.exceptions import SEYamlCatalogUnreadable


class SEProgressCatalogUnreadable(SEYamlCatalogUnreadable):
    """Exception raised when the progress updates catalogue cannot be read."""
