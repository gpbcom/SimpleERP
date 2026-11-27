from __future__ import annotations

from erp_models.base.exceptions.se_invalid_opaque_id_exception import SEInvalidOpaqueIdException


class SEOpaqueIdInvalidValue(SEInvalidOpaqueIdException):
    """Exception raised when an invalid ``value`` is provided."""
