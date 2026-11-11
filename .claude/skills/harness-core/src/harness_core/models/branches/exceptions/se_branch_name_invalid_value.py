from __future__ import annotations

from harness_core.models.branches.exceptions.se_invalid_branch_name_exception import SEInvalidBranchNameException


class SEBranchNameInvalidValue(SEInvalidBranchNameException):
    """Exception raised when an invalid ``value`` is provided."""
