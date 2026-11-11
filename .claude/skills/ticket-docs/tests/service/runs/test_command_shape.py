from __future__ import annotations

import logging
from pathlib import Path
from typing import List

import pytest

from ticket_docs.service.runs.command_shape import CommandShape


class TestCommandShape:
    @pytest.mark.parametrize(
        ("command", "pytest_run"),
        [
            (["pytest", "-q"], True),
            (["../.venv/bin/pytest", "-q", "tests"], True),
            (["uv", "run", "pytest", "tests"], True),
            (["uv", "run", "--frozen", "pytest"], True),
            (["python", "-m", "pytest"], True),
            (["python3", "-I", "-m", "pytest", "-x"], True),
            (["/usr/bin/python3.13", "-m", "pytest"], True),
            (["env", "-u", "VIRTUAL_ENV", "PYTHONPATH=src", "pytest"], True),
            (["ruff", "check", "pytest"], False),
            (["python", "-m", "mypy", "pytest"], False),
            (["uv", "run", "ruff", "pytest"], False),
            (["echo", "pytest"], False),
            ([], False),
        ],
    )
    def test_a_pytest_run_is_recognised(self, logger: logging.Logger, command: List[str], pytest_run: bool) -> None:
        assert CommandShape(logger).is_pytest(command) is pytest_run

    @pytest.mark.parametrize(
        ("command", "playwright_run"),
        [
            (["npx", "playwright", "test"], True),
            (["npx", "playwright", "test", "--grep", "@smoke"], True),
            (["/usr/local/bin/npx", "playwright", "test"], True),
            (["npx", "playwright", "show-report"], False),
            (["npm", "test"], False),
        ],
    )
    def test_a_playwright_run_is_recognised(
        self, logger: logging.Logger, command: List[str], playwright_run: bool
    ) -> None:
        assert CommandShape(logger).is_playwright(command) is playwright_run

    def test_a_pytest_run_gets_its_reports_in_the_folder(self, logger: logging.Logger, tmp_path: Path) -> None:
        shape = CommandShape(logger)
        assert shape.with_reports(["pytest", "-q"], tmp_path) == [
            "pytest",
            "-q",
            f"--junitxml={tmp_path}/report.xml",
            f"--html={tmp_path}/report.html",
            "--self-contained-html",
        ]
        assert shape.with_reports(["ruff", "check"], tmp_path) == ["ruff", "check"]

    def test_the_shown_command_names_its_folder_and_hides_the_evidence_path(
        self, logger: logging.Logger, tmp_path: Path
    ) -> None:
        command = ["pytest", "-k", "a and b", f"--junitxml={tmp_path}/report.xml"]
        shown = CommandShape(logger).display(command, tmp_path, ".claude/skills/x")
        assert shown == "cd .claude/skills/x && pytest -k 'a and b' --junitxml=<this folder>/report.xml"
