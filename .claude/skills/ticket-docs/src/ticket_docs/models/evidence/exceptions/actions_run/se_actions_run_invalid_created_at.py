from __future__ import annotations

from ticket_docs.models.evidence.exceptions.actions_run.se_invalid_actions_run_exception import (
    SEInvalidActionsRunException,
)


class SEActionsRunInvalidCreatedAt(SEInvalidActionsRunException):
    """Exception raised when an invalid ``created_at`` is provided."""
