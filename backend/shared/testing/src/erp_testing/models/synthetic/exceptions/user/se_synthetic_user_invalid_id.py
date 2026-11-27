from __future__ import annotations

from erp_testing.models.synthetic.exceptions.user.se_invalid_synthetic_user_exception import (
    SEInvalidSyntheticUserException,
)


class SESyntheticUserInvalidId(SEInvalidSyntheticUserException):
    """Exception raised when an invalid ``id`` is provided."""
