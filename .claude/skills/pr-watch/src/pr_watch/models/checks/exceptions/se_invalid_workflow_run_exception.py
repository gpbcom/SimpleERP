from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidWorkflowRunException(SEPrWatchError):
    """Exception raised when an invalid WorkflowRun is provided."""
