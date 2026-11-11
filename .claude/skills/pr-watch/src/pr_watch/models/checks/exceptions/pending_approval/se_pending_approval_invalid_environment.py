from __future__ import annotations

from pr_watch.models.checks.exceptions.se_invalid_pending_approval_exception import SEInvalidPendingApprovalException


class SEPendingApprovalInvalidEnvironment(SEInvalidPendingApprovalException):
    """Exception raised when an invalid ``environment`` is provided."""
