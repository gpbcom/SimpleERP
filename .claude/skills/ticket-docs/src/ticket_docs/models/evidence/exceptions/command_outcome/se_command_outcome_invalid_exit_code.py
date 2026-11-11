from __future__ import annotations

from ticket_docs.models.evidence.exceptions.command_outcome.se_invalid_command_outcome_exception import (
    SEInvalidCommandOutcomeException,
)


class SECommandOutcomeInvalidExitCode(SEInvalidCommandOutcomeException):
    """Exception raised when an invalid ``exit_code`` is provided."""
