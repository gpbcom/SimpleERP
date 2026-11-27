from __future__ import annotations

from typing import Type

import erp_models.exceptions as exceptions
import pytest
from erp_models.exceptions import SEError, SEException, SEInvalidModelException


class TestSEInvalidModelException:
    def test_the_code_is_the_one_of_the_standard(self) -> None:
        assert SEInvalidModelException.CODE == "INVALID-INPUT-01"

    def test_a_model_exception_is_an_se_exception(self) -> None:
        assert issubclass(SEInvalidModelException, SEException)
        assert SEInvalidModelException.CODE != SEException.CODE

    def test_a_model_exception_is_not_a_layer_error(self) -> None:
        assert not issubclass(SEInvalidModelException, SEError)

    def test_it_is_exported_by_the_package(self) -> None:
        assert "SEInvalidModelException" in exceptions.__all__

    def test_the_message_is_kept(self) -> None:
        assert str(SEInvalidModelException("Invalid port.")) == "Invalid port."

    def test_a_subclass_without_its_own_code_inherits_it(self) -> None:
        child = type("SEInvalidChildException", (SEInvalidModelException,), {})
        assert child.CODE == "INVALID-INPUT-01"
        assert child("x").CODE == "INVALID-INPUT-01"

    def test_a_subclass_can_set_its_own_code(self) -> None:
        child = type("SEInvalidChildException", (SEInvalidModelException,), {"CODE": "OTHER-CODE-01"})
        assert child.CODE == "OTHER-CODE-01"
        assert SEInvalidModelException.CODE == "INVALID-INPUT-01"

    def wrap(self, cause: KeyError) -> None:
        try:
            raise cause
        except KeyError as error:
            raise SEInvalidModelException("Wrapped.") from error

    def test_the_cause_is_kept_by_raise_from(self) -> None:
        cause = KeyError("missing")
        with pytest.raises(SEInvalidModelException) as caught:
            self.wrap(cause)
        assert caught.value.__cause__ is cause

    @pytest.mark.parametrize("forbidden", [ValueError, TypeError, AssertionError])
    def test_it_is_not_a_builtin_that_pydantic_wraps(self, forbidden: Type[Exception]) -> None:
        assert not issubclass(SEInvalidModelException, forbidden)
