from __future__ import annotations

from erp_models.ids.exceptions.se_invalid_company_id_exception import SEInvalidCompanyIdException


class SECompanyIdInvalidValue(SEInvalidCompanyIdException):
    """Exception raised when an invalid ``value`` is provided."""
