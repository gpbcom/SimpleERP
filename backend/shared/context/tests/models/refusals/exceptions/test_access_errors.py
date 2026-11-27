from __future__ import annotations

from typing import Type

import pytest
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import (
    SEAccessDeniedError,
    SEAccessError,
    SEAccessNoCompanyError,
    SEAccessNoUserError,
)
from erp_models.exceptions import SEException


class TestAccessErrors:
    @pytest.mark.parametrize(
        "error",
        [SEAccessNoCompanyError, SEAccessNoUserError, SEAccessDeniedError],
    )
    def test_each_access_error_is_an_access_error(self, error: Type[SEAccessError]) -> None:
        assert issubclass(error, SEAccessError)

    def test_the_layer_base_is_an_se_exception(self) -> None:
        assert issubclass(SEAccessError, SEException)

    @pytest.mark.parametrize("reason", list(RefusalReason))
    def test_the_base_keeps_its_reason_and_message(self, reason: RefusalReason) -> None:
        error = SEAccessError(reason, "Refused.")

        assert error.reason is reason
        assert str(error) == "Refused."

    @pytest.mark.parametrize(
        ("error", "reason"),
        [
            (SEAccessNoCompanyError, RefusalReason.NO_COMPANY),
            (SEAccessNoUserError, RefusalReason.NO_USER),
            (SEAccessDeniedError, RefusalReason.POLICY_DENIED),
            (SEAccessDeniedError, RefusalReason.OTHER_COMPANY),
            (SEAccessDeniedError, RefusalReason.NO_POLICY),
        ],
    )
    def test_a_subclass_keeps_its_reason(self, error: Type[SEAccessError], reason: RefusalReason) -> None:
        raised = error(reason, "Refused.")

        assert raised.reason is reason
        with pytest.raises(error):
            raise raised

    def test_a_subclass_is_caught_as_the_base(self) -> None:
        with pytest.raises(SEAccessError) as caught:
            raise SEAccessNoUserError(RefusalReason.NO_USER, "No user.")

        assert caught.value.reason is RefusalReason.NO_USER
