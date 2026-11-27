from __future__ import annotations

from typing import Type

import erp_models.exceptions as exceptions
import pytest
from erp_models.exceptions import SEError, SEException


class TestSEError:
    def test_the_code_is_the_one_of_the_standard(self) -> None:
        assert SEError.CODE == "SERVICE-FAILURE-01"

    def test_a_layer_error_is_an_se_exception(self) -> None:
        assert issubclass(SEError, SEException)
        assert SEError.CODE != SEException.CODE

    def test_a_layer_error_is_caught_as_an_se_exception(self) -> None:
        with pytest.raises(SEException):
            raise SEError("Failed.")

    def test_it_is_exported_by_the_package(self) -> None:
        assert "SEError" in exceptions.__all__

    def test_the_message_is_kept(self) -> None:
        assert str(SEError("Something failed.")) == "Something failed."

    def test_a_subclass_without_its_own_code_inherits_it(self) -> None:
        child = type("SEChildError", (SEError,), {})
        assert child.CODE == "SERVICE-FAILURE-01"
        assert child("x").CODE == "SERVICE-FAILURE-01"

    def test_a_subclass_can_set_its_own_code(self) -> None:
        child = type("SEChildError", (SEError,), {"CODE": "OTHER-CODE-01"})
        assert child.CODE == "OTHER-CODE-01"
        assert SEError.CODE == "SERVICE-FAILURE-01"

    def wrap(self, cause: KeyError) -> None:
        try:
            raise cause
        except KeyError as error:
            raise SEError("Wrapped.") from error

    def test_the_cause_is_kept_by_raise_from(self) -> None:
        cause = KeyError("missing")
        with pytest.raises(SEError) as caught:
            self.wrap(cause)
        assert caught.value.__cause__ is cause

    @pytest.mark.parametrize("forbidden", [ValueError, TypeError, AssertionError])
    def test_it_is_not_a_builtin_that_pydantic_wraps(self, forbidden: Type[Exception]) -> None:
        assert not issubclass(SEError, forbidden)
