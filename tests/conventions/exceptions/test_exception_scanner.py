"""The exception rules pass a clean tree, and catch each kind of offender."""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar, Dict, Tuple

import pytest

from tests.conventions.exceptions.exception_scanner import ExceptionScanner


class TestExceptionScanner:
    PACKAGE: ClassVar[str] = "backend/models/src/erp_models/customers"
    EXCEPTIONS: ClassVar[str] = f"{PACKAGE}/exceptions"
    BASE: ClassVar[str] = "class SECustomerError(Exception):\n    pass\n"
    DERIVED: ClassVar[str] = "class SECustomerMissingError(SECustomerError):\n    pass\n"
    CLEAN_TREE: ClassVar[Dict[str, str]] = {
        f"{EXCEPTIONS}/__init__.py": '__all__ = ["SECustomerError", "SECustomerMissingError"]\n',
        f"{EXCEPTIONS}/se_customer_error.py": BASE,
        f"{EXCEPTIONS}/se_customer_missing_error.py": DERIVED,
        f"{PACKAGE}/customer.py": "class Customer:\n    pass\n",
    }
    BROKEN_TREES: ClassVar[Dict[str, Tuple[str, Dict[str, str]]]] = {
        "misnamed": (
            "misnamed_exceptions",
            {
                f"{EXCEPTIONS}/__init__.py": (
                    '__all__ = ["CustomerError", "SECustomerError", "SECustomerMissingError"]\n'
                ),
                f"{EXCEPTIONS}/customer_error.py": "class CustomerError(Exception):\n    pass\n",
            },
        ),
        "misnamed_by_inheritance": (
            "misnamed_exceptions",
            {
                f"{EXCEPTIONS}/__init__.py": (
                    '__all__ = ["CustomerGone", "SECustomerError", "SECustomerMissingError"]\n'
                ),
                f"{EXCEPTIONS}/customer_gone.py": "class CustomerGone(SECustomerError):\n    pass\n",
            },
        ),
        "wrong_file_name": (
            "misplaced_exceptions",
            {
                f"{EXCEPTIONS}/__init__.py": (
                    '__all__ = ["SECustomerError", "SECustomerMissingError", "SECustomerOtherError"]\n'
                ),
                f"{EXCEPTIONS}/oops.py": "class SECustomerOtherError(SECustomerError):\n    pass\n",
            },
        ),
        "outside_exceptions": (
            "misplaced_exceptions",
            {f"{PACKAGE}/se_customer_late_error.py": "class SECustomerLateError(Exception):\n    pass\n"},
        ),
        "no_all": ("unexported_exceptions", {f"{EXCEPTIONS}/__init__.py": ""}),
        "unsorted_all": (
            "unexported_exceptions",
            {f"{EXCEPTIONS}/__init__.py": '__all__ = ["SECustomerMissingError", "SECustomerError"]\n'},
        ),
        "missing_from_all": (
            "unexported_exceptions",
            {f"{EXCEPTIONS}/__init__.py": '__all__ = ["SECustomerError"]\n'},
        ),
        "sub_folder_missing_from_all": (
            "unexported_exceptions",
            {
                f"{EXCEPTIONS}/lookups/se_customer_lookup_error.py": (
                    "class SECustomerLookupError(SECustomerError):\n    pass\n"
                ),
            },
        ),
    }
    RULES: ClassVar[Tuple[str, ...]] = ("misnamed_exceptions", "misplaced_exceptions", "unexported_exceptions")

    def write(self, root: Path, files: Dict[str, str]) -> ExceptionScanner:
        for name, text in {**self.CLEAN_TREE, **files}.items():
            (root / name).parent.mkdir(parents=True, exist_ok=True)
            (root / name).write_text(text, encoding="utf-8")
        return ExceptionScanner(root)

    @pytest.mark.parametrize("rule", RULES)
    def test_a_clean_tree_has_no_offender(self, tmp_path: Path, rule: str) -> None:
        assert not getattr(self.write(tmp_path, {}), rule)()

    @pytest.mark.parametrize("case", sorted(BROKEN_TREES))
    def test_each_broken_tree_fails_its_rule_exactly_once(self, tmp_path: Path, case: str) -> None:
        broken_rule, files = self.BROKEN_TREES[case]
        scanner = self.write(tmp_path, files)
        for rule in self.RULES:
            expected = 1 if rule == broken_rule else 0
            assert len(getattr(scanner, rule)()) == expected, (case, rule)

    @pytest.mark.parametrize("rule", RULES)
    def test_a_class_that_is_not_an_exception_is_ignored(self, tmp_path: Path, rule: str) -> None:
        scanner = self.write(tmp_path, {f"{self.PACKAGE}/Thing.py": "class Thing:\n    pass\n"})
        assert not getattr(scanner, rule)()

    def test_an_offender_names_its_file_and_line(self, tmp_path: Path) -> None:
        scanner = self.write(tmp_path, self.BROKEN_TREES["misnamed"][1])
        assert scanner.misnamed_exceptions() == [f"{self.EXCEPTIONS}/customer_error.py:1"]
