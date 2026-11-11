from __future__ import annotations

from ticket_docs.models.evidence.exceptions.command_outcome.se_invalid_command_outcome_exception import (
    SEInvalidCommandOutcomeException,
)


class SECommandOutcomeInvalidOutput(SEInvalidCommandOutcomeException):
    """Exception raised when an invalid ``output`` is provided."""
