from __future__ import annotations

from typing import Type

import erp_models.exceptions as exceptions
import pytest
from erp_models.exceptions import SEException


class TestSEException:
    def test_the_code_is_the_one_of_the_standard(self) -> None:
        assert SEException.CODE == "UNEXPECTED-ERROR-01"

    def test_it_is_an_exception(self) -> None:
        assert issubclass(SEException, Exception)

    def test_it_is_exported_by_the_package(self) -> None:
        assert "SEException" in exceptions.__all__

    def test_the_message_is_kept(self) -> None:
        assert str(SEException("Something failed.")) == "Something failed."

    def test_a_subclass_without_its_own_code_inherits_it(self) -> None:
        child = type("SEChild", (SEException,), {})
        assert child.CODE == "UNEXPECTED-ERROR-01"
        assert child("x").CODE == "UNEXPECTED-ERROR-01"

    def test_a_subclass_can_set_its_own_code(self) -> None:
        child = type("SEChild", (SEException,), {"CODE": "OTHER-CODE-01"})
        assert child.CODE == "OTHER-CODE-01"
        assert SEException.CODE == "UNEXPECTED-ERROR-01"

    def wrap(self, cause: KeyError) -> None:
        try:
            raise cause
        except KeyError as error:
            raise SEException("Wrapped.") from error

    def test_the_cause_is_kept_by_raise_from(self) -> None:
        cause = KeyError("missing")
        with pytest.raises(SEException) as caught:
            self.wrap(cause)
        assert caught.value.__cause__ is cause

    @pytest.mark.parametrize("forbidden", [ValueError, TypeError, AssertionError])
    def test_it_is_not_a_builtin_that_pydantic_wraps(self, forbidden: Type[Exception]) -> None:
        assert not issubclass(SEException, forbidden)
