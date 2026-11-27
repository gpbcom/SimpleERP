"""mypy sees each source folder as a module root, as CI does: a file is never found under two module names (TKT-6)."""

from __future__ import annotations

# Standard library imports
import os
from pathlib import Path
from typing import Dict, List, Tuple

# First-party imports
from tests.harness.checks.helpers import call
from tests.harness.checks.runs.test_checks_python import tree

SOURCES = ("backend/models/src", "backend/shared/lifecycle/src", "sdk/src")


def mypy_run(root: Path) -> Tuple[List[str], Dict[str, str]]:
    """Return the mypy command ``checks.py`` runs on ``root`` and the environment it adds."""
    setup = (
        f"checks.ROOT = Path({str(root)!r}); calls = []\n"
        "checks.run = lambda command, cwd=None, env=None: (calls.append([command, env or {}]) or (0, ''))\n"
        f"c = checks.Checks('T9.03', Path({str(root)!r}))\n"
        "checks.python_checks(c, ['tests/a/test_a.py'])"
    )
    calls = call("calls", setup)
    assert isinstance(calls, list)
    command, env = next(entry for entry in calls if "mypy" in entry[0])
    return command, env


class TestChecksMypyPath:
    def test_mypy_runs_with_every_source_folder_as_a_module_root(self, tmp_path: Path) -> None:
        command, env = mypy_run(tree(tmp_path, *SOURCES))
        roots = env["MYPYPATH"].split(os.pathsep)
        assert set(SOURCES) <= set(roots)
        assert roots == [word for word in command if word.endswith("/src")]

    def test_mypy_still_checks_every_source_folder(self, tmp_path: Path) -> None:
        command, _ = mypy_run(tree(tmp_path, *SOURCES))
        assert set(SOURCES) <= set(command)

    def test_mypy_and_pytest_run_with_every_workspace_member_installed(self, tmp_path: Path) -> None:
        setup = (
            f"checks.ROOT = Path({str(tmp_path)!r}); calls = []\n"
            "checks.run = lambda command, cwd=None, env=None: (calls.append(command) or (0, ''))\n"
            f"c = checks.Checks('T9.03', Path({str(tmp_path)!r}))\n"
            "checks.python_checks(c, ['tests/a/test_a.py'])"
        )
        tree(tmp_path, *SOURCES)
        calls = call("calls", setup)
        assert isinstance(calls, list)
        for tool in ("mypy", "pytest"):
            command = next(c for c in calls if c[2:3] == [tool] or tool in c)
            assert command[:3] == ["uv", "run", "--all-packages"], command
