from __future__ import annotations

from pr_watch.models.checks.exceptions.se_invalid_workflow_run_exception import SEInvalidWorkflowRunException


class SEWorkflowRunInvalidConclusion(SEInvalidWorkflowRunException):
    """Exception raised when an invalid ``conclusion`` is provided."""
