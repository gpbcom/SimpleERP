from __future__ import annotations

import os
import subprocess

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from project_docs.api.cli.main import main
from tests.helpers import REPOSITORY_ROOT, SKILL_DIR


class TestCheckCommand:
    def test_a_complete_documentation_prints_nothing(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["check"]) == 0
        assert capsys.readouterr().out == ""

    def test_each_problem_is_printed_on_its_own_line_and_exits_1(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        caller_in_sandbox.write("docs/technical/operations.md", "# Operations\n")
        assert main(["check"]) == 1
        assert capsys.readouterr().out.splitlines() == [
            "docs/technical/operations.md: not linked from docs/technical/README.md.",
            'docs/technical/operations.md: no "Last reviewed: YYYY-MM-DD (GH-<n>)" line.',
        ]

    def test_the_ticket_check_uses_the_base(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        caller_in_sandbox.commit("conf", {"conf/app.yaml": "a: 1\n"})
        assert main(["check", "--ticket", "GH-7", "--base", "develop"]) == 1
        assert capsys.readouterr().out.startswith("docs/technical/configuration.md: concerned by conf/app.yaml")

    def test_a_bad_ticket_key_is_a_failure_the_person_can_fix(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["check", "--ticket", "seven", "--base", "develop"]) == 2
        assert capsys.readouterr().err.startswith("project-docs: ")

    def test_the_repository_documentation_is_complete(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        monkeypatch.setenv("PROJECT_DOCS_CALLER_CWD", str(REPOSITORY_ROOT))
        monkeypatch.setenv("PATH", "/usr/bin:/bin")
        assert main(["check"]) == 0
        assert capsys.readouterr().out == ""

    def test_the_bin_wrapper_checks_the_folder_it_is_called_from(self, sandbox: GitSandbox) -> None:
        sandbox.write("docs/technical/operations.md", "# Operations\n\nLast reviewed: 2026-11-10 (GH-1)\n")
        environment = {key: value for key, value in os.environ.items() if key != "PROJECT_DOCS_CALLER_CWD"}
        result = subprocess.run(
            [str(SKILL_DIR / "bin" / "project-docs"), "check"],
            cwd=sandbox.root / "docs",
            capture_output=True,
            text=True,
            env=environment,
            check=False,
            timeout=110,
        )
        assert result.returncode == 1
        assert result.stdout == "docs/technical/operations.md: not linked from docs/technical/README.md.\n"
