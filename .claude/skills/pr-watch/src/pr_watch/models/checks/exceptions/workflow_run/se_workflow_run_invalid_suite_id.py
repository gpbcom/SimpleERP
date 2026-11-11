from __future__ import annotations

from pr_watch.models.checks.exceptions.se_invalid_workflow_run_exception import SEInvalidWorkflowRunException


class SEWorkflowRunInvalidSuiteId(SEInvalidWorkflowRunException):
    """Exception raised when an invalid ``suite_id`` is provided."""
