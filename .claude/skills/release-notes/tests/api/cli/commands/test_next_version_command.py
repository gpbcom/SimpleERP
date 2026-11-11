from __future__ import annotations

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from release_notes.api.cli.main import main


class TestNextVersionCommand:
    def test_the_version_and_its_reason_are_printed(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        caller_in_sandbox.git("tag", "v0.1.0")
        caller_in_sandbox.write("changelog.d/GH-7.fixed.md", "Login works again.\n")
        assert main(["next-version"]) == 0
        assert capsys.readouterr().out.splitlines() == ["0.1.1", "patch bump from v0.1.0: GH-7.fixed.md (patch)."]

    def test_no_fragment_is_a_failure_the_person_can_fix(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["next-version"]) == 2
        captured = capsys.readouterr()
        assert captured.out == ""
        assert "nothing to release" in captured.err
