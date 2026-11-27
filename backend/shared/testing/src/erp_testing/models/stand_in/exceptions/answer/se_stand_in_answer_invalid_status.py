from __future__ import annotations

from erp_testing.models.stand_in.exceptions.answer.se_invalid_stand_in_answer_exception import (
    SEInvalidStandInAnswerException,
)


class SEStandInAnswerInvalidStatus(SEInvalidStandInAnswerException):
    """Exception raised when an invalid ``status`` is provided."""
