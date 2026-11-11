from __future__ import annotations

import os
import subprocess

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from release_notes.api.cli.main import main
from tests.helpers import REPOSITORY_ROOT, SKILL_DIR, release_note


class TestCheckCommand:
    def test_a_ticket_branch_with_its_fragment_prints_nothing(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        caller_in_sandbox.write("changelog.d/GH-7.added.md", "Customers can be archived.\n")
        assert main(["check"]) == 0
        assert capsys.readouterr().out == ""

    def test_each_problem_is_printed_and_exits_1(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["check", "--branch", "release/0.1.0"]) == 1
        assert capsys.readouterr().out == "CHANGELOG.md: no section ## [0.1.0] - YYYY-MM-DD.\n"

    def test_the_ticket_release_note_is_checked_too(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        caller_in_sandbox.write("changelog.d/GH-7.added.md", "Customers can be archived.\n")
        assert main(["check", "--ticket", "GH-7"]) == 1
        assert capsys.readouterr().out == "docs/tickets/GH-7/RELEASE-NOTE.md: missing.\n"
        caller_in_sandbox.write("docs/tickets/GH-7/RELEASE-NOTE.md", release_note())
        assert main(["check", "--ticket", "GH-7"]) == 0

    def test_a_bad_ticket_key_is_a_failure_the_person_can_fix(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["check", "--ticket", "seven"]) == 2
        assert capsys.readouterr().err.startswith("release-notes: ")

    def test_the_repository_changelog_is_valid(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        monkeypatch.setenv("RELEASE_NOTES_CALLER_CWD", str(REPOSITORY_ROOT))
        assert main(["check", "--branch", "develop"]) == 0
        assert capsys.readouterr().out == ""

    def test_the_bin_wrapper_checks_the_folder_it_is_called_from(self, sandbox: GitSandbox) -> None:
        environment = {key: value for key, value in os.environ.items() if key != "RELEASE_NOTES_CALLER_CWD"}
        result = subprocess.run(
            [str(SKILL_DIR / "bin" / "release-notes"), "check"],
            cwd=sandbox.root / "changelog.d",
            capture_output=True,
            text=True,
            env=environment,
            check=False,
            timeout=110,
        )
        assert result.returncode == 1
        assert result.stdout == "changelog.d/: no fragment GH-7.<type>.md for GH-7.\n"
