from __future__ import annotations

from erp_platform.storage.catalogs.exceptions.se_error_code_storage_error import SEErrorCodeStorageError


class SEErrorCodeCatalogUnreadableError(SEErrorCodeStorageError):
    """Raised when the error code catalogue cannot be read or is invalid."""
