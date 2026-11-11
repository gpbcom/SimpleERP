from __future__ import annotations

from ticket_docs.models.evidence.exceptions.actions_run.se_invalid_actions_run_exception import (
    SEInvalidActionsRunException,
)


class SEActionsRunInvalidText(SEInvalidActionsRunException):
    """Exception raised when an invalid ``head_branch``, ``url`` or ``display_title`` is provided."""
