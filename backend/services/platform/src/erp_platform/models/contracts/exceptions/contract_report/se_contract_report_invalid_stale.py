from __future__ import annotations

from erp_platform.models.contracts.exceptions.contract_report.se_invalid_contract_report_exception import (
    SEInvalidContractReportException,
)


class SEContractReportInvalidStale(SEInvalidContractReportException):
    """Exception raised when an invalid ``stale`` is provided."""
