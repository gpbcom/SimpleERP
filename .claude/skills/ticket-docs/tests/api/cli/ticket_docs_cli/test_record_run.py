from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from tests.api.cli.ticket_docs_cli.helpers import call
from tests.builders.git_sandbox import GitSandbox


class TestRecordRun:
    OPTIONS = ["--ticket", "GH-1", "--kind", "check", "--where", "local", "--check", "lint", "--what", "Lint passes"]

    def test_a_command_is_recorded_and_its_verdict_printed(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        code, out, err = call(["record-run", *self.OPTIONS, "--", sys.executable, "-c", "print('ok')"], sandbox.root)
        assert (code, out, err) == (0, "✅ PASS (exit 0)\n", "")
        folder = (
            sandbox.root / "docs" / "tickets" / "GH-1" / "tests-evidences" / f"local-{datetime.now():%Y-%m-%d}-lint"
        )
        assert (folder / "README.md").is_file()

    def test_the_commands_exit_code_is_kept(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        command = [sys.executable, "-c", "raise SystemExit(5)"]
        code, out, _ = call(["record-run", *self.OPTIONS, "--expect", "red", "--", *command], sandbox.root)
        assert code == 5
        assert out == "❌ FAIL (exit 5) — expected red (TDD), as expected\n"

    def test_a_bad_request_is_a_usage_error(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        options = [*self.OPTIONS]
        options[1] = "ARE-1"
        code, out, err = call(["record-run", *options, "--", "true"], sandbox.root)
        assert (code, out) == (2, "")
        assert "Invalid ticket" in err
        code, _, err = call(["record-run", *self.OPTIONS], sandbox.root)
        assert code == 2
        assert "--run-id" in err

    def test_a_folder_outside_a_repository_is_refused(self, tmp_path: Path) -> None:
        code, _, err = call(["record-run", *self.OPTIONS, "--", "true"], tmp_path)
        assert code == 2
        assert "git" in err
