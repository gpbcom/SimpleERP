from __future__ import annotations

from datetime import date

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from release_notes.api.cli.main import main


class TestBuildCommand:
    def test_the_section_is_added_and_the_deleted_fragments_are_printed(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        caller_in_sandbox.write("changelog.d/GH-7.added.md", "Customers can be archived.\n")
        caller_in_sandbox.write("changelog.d/GH-9.fixed.md", "Login works again.\n")
        assert main(["build", "0.1.0"]) == 0
        assert capsys.readouterr().out.splitlines() == [
            f"CHANGELOG.md: added ## [0.1.0] - {date.today().isoformat()}.",
            "changelog.d/GH-7.added.md: deleted.",
            "changelog.d/GH-9.fixed.md: deleted.",
        ]
        assert main(["check", "--branch", "release/0.1.0"]) == 0

    def test_an_existing_version_is_a_failure_the_person_can_fix(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        caller_in_sandbox.write("changelog.d/GH-7.added.md", "Customers can be archived.\n")
        caller_in_sandbox.git("tag", "v0.1.0")
        assert main(["build", "0.1.0"]) == 2
        assert capsys.readouterr().err.startswith("release-notes: ")
