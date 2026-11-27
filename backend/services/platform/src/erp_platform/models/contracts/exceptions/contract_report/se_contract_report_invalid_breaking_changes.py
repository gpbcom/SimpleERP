from __future__ import annotations

from erp_platform.models.contracts.exceptions.contract_report.se_invalid_contract_report_exception import (
    SEInvalidContractReportException,
)


class SEContractReportInvalidBreakingChanges(SEInvalidContractReportException):
    """Exception raised when an invalid ``breaking_changes`` is provided."""
