from __future__ import annotations

from erp_platform.models.contracts.exceptions.contract_change.se_invalid_contract_change_exception import (
    SEInvalidContractChangeException,
)


class SEContractChangeInvalidKind(SEInvalidContractChangeException):
    """Exception raised when an invalid ``kind`` is provided."""
