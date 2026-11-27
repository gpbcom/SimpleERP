"""The exception rules of AGENT.md hold on every Python package of the repository."""

from __future__ import annotations

from tests.conventions.exceptions.exception_scanner import ExceptionScanner
from tests.conventions.helpers import ROOT


class TestExceptionConventions:
    def test_every_exception_name_starts_with_se(self) -> None:
        assert not ExceptionScanner(ROOT).misnamed_exceptions()

    def test_every_exception_has_its_own_file_in_an_exceptions_folder(self) -> None:
        assert not ExceptionScanner(ROOT).misplaced_exceptions()

    def test_every_exceptions_package_exports_its_exceptions_in_a_sorted_all(self) -> None:
        assert not ExceptionScanner(ROOT).unexported_exceptions()
