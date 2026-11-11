from __future__ import annotations

from pr_watch.models.checks.exceptions.se_invalid_pending_approval_exception import SEInvalidPendingApprovalException


class SEPendingApprovalInvalidRunId(SEInvalidPendingApprovalException):
    """Exception raised when an invalid ``run_id`` is provided."""
