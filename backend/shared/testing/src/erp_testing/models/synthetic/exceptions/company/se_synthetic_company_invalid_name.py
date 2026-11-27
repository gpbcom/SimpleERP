from __future__ import annotations

from erp_testing.models.synthetic.exceptions.company.se_invalid_synthetic_company_exception import (
    SEInvalidSyntheticCompanyException,
)


class SESyntheticCompanyInvalidName(SEInvalidSyntheticCompanyException):
    """Exception raised when an invalid ``name`` is provided."""
