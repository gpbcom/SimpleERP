from __future__ import annotations

from erp_testing.models.stand_in.exceptions.answer.se_invalid_stand_in_answer_exception import (
    SEInvalidStandInAnswerException,
)


class SEStandInAnswerInvalidHeaders(SEInvalidStandInAnswerException):
    """Exception raised when an invalid ``headers`` is provided."""
