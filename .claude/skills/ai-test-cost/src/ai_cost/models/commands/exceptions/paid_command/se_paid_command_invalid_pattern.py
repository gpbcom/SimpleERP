from __future__ import annotations

from ai_cost.models.commands.exceptions.paid_command.se_invalid_paid_command_exception import (
    SEInvalidPaidCommandException,
)


class SEPaidCommandInvalidPattern(SEInvalidPaidCommandException):
    """Exception raised when an invalid ``pattern`` is provided."""
