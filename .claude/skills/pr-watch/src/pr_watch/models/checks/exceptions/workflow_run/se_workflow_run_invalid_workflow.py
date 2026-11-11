from __future__ import annotations

from pr_watch.models.checks.exceptions.se_invalid_workflow_run_exception import SEInvalidWorkflowRunException


class SEWorkflowRunInvalidWorkflow(SEInvalidWorkflowRunException):
    """Exception raised when an invalid ``workflow`` is provided."""
