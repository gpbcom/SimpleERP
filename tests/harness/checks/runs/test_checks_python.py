from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import List

# Third-party imports
import pytest

# First-party imports
from tests.harness.checks.helpers import call

SERVICE_FILE = "backend/services/sales/src/erp_sales/service/quotes/quote_service.py"


def python_run(root: Path, changed: List[str]) -> List[List[str]]:
    setup = (
        f"checks.ROOT = Path({str(root)!r}); commands = []\n"
        "checks.run = lambda command, cwd=None, env=None: (commands.append(command) or (0, ''))\n"
        f"c = checks.Checks('T9.03', Path({str(root)!r}))\n"
        f"checks.python_checks(c, {changed!r})"
    )
    value = call("[commands, c.not_applicable]", setup)
    assert isinstance(value, list)
    return value


def tree(root: Path, *folders: str) -> Path:
    (root / "tests" / "a").mkdir(parents=True)
    (root / "tests" / "a" / "test_a.py").write_text("", encoding="utf-8")
    for folder in folders:
        (root / folder).mkdir(parents=True, exist_ok=True)
    (root / SERVICE_FILE).parent.mkdir(parents=True, exist_ok=True)
    (root / SERVICE_FILE).write_text("", encoding="utf-8")
    return root


def pytest_folders(commands: List[List[str]]) -> List[str]:
    return [command[3] for command in commands if command[2] == "pytest"]


class TestChecksPython:
    def test_pytest_runs_the_repository_tests_on_two_workers_as_ci_does(self, tmp_path: Path) -> None:
        commands, _ = python_run(tree(tmp_path), ["tests/a/test_a.py"])
        assert ["uv", "run", "pytest", "tests", "-q", "-n", "2"] in commands

    def test_mypy_is_skipped_with_its_reason_when_no_source_folder_exists(self, tmp_path: Path) -> None:
        root = tmp_path / "empty"
        (root / "tests" / "a").mkdir(parents=True)
        (root / "tests" / "a" / "test_a.py").write_text("", encoding="utf-8")
        commands, skipped = python_run(root, ["tests/a/test_a.py"])
        assert not any("mypy" in command for command in commands)
        assert any(entry.startswith("mypy: not run") for entry in skipped)

    def test_mypy_reads_every_package_source_folder(self, tmp_path: Path) -> None:
        folders = (
            "backend/models/src",
            "backend/shared/lifecycle/src",
            "backend/services/sales/src",
            "plugins/shopify/src",
            "sdk/src",
        )
        commands, skipped = python_run(tree(tmp_path, *folders), ["tests/a/test_a.py"])
        mypy = next(command for command in commands if "mypy" in command)
        assert set(folders) <= set(mypy)
        assert skipped == []

    def test_a_service_change_runs_the_service_s_own_tests_one_folder_at_a_time(self, tmp_path: Path) -> None:
        root = tree(tmp_path, "backend/services/sales/tests", "backend/services/stock/tests")
        commands, _ = python_run(root, [SERVICE_FILE])
        assert pytest_folders(commands) == ["tests", "backend/services/sales/tests"]

    @pytest.mark.parametrize(
        "shared", ["backend/models/src/erp_models/sales/quote.py", "backend/shared/lifecycle/src/erp_lifecycle/x.py"]
    )
    def test_a_shared_change_runs_the_tests_of_every_package(self, tmp_path: Path, shared: str) -> None:
        root = tree(tmp_path, "backend/models/tests", "backend/services/sales/tests", "plugins/shopify/tests")
        (root / shared).parent.mkdir(parents=True, exist_ok=True)
        (root / shared).write_text("", encoding="utf-8")
        commands, _ = python_run(root, [shared])
        assert pytest_folders(commands) == [
            "tests",
            "backend/models/tests",
            "backend/services/sales/tests",
            "plugins/shopify/tests",
        ]

    def test_a_package_without_a_tests_folder_runs_only_the_repository_tests(self, tmp_path: Path) -> None:
        commands, _ = python_run(tree(tmp_path), [SERVICE_FILE])
        assert pytest_folders(commands) == ["tests"]
