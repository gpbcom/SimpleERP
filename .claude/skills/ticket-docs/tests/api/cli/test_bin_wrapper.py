from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict

from tests.builders.git_sandbox import GitSandbox


class TestBinWrapper:
    WRAPPER = Path(__file__).resolve().parents[3] / "bin" / "ticket-docs"

    def environment(self) -> Dict[str, str]:
        return {key: value for key, value in os.environ.items() if key != "VIRTUAL_ENV"}

    def test_the_wrapper_answers_the_gate_from_any_folder(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        hook = json.dumps({"tool_input": {"command": "git push origin master"}, "cwd": str(sandbox.root)})
        done = subprocess.run(
            [str(self.WRAPPER), "git-gate"],
            input=hook,
            capture_output=True,
            text=True,
            cwd=tmp_path,
            env=self.environment(),
            timeout=120,
            check=False,
        )
        assert done.returncode == 0, done.stderr
        assert json.loads(done.stdout)["hookSpecificOutput"]["permissionDecision"] == "deny"

    def test_the_wrapper_records_in_the_callers_repository(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        command = [
            str(self.WRAPPER), "record-run", "--ticket", "GH-1", "--kind", "check", "--where", "local",
            "--check", "wrapper", "--what", "The wrapper runs where it is called", "--", sys.executable, "-c", "1",
        ]  # fmt: skip
        done = subprocess.run(
            command, capture_output=True, text=True, cwd=sandbox.root, env=self.environment(), timeout=120, check=False
        )
        assert done.returncode == 0, done.stderr
        assert done.stdout == "✅ PASS (exit 0)\n"
        assert list((sandbox.root / "docs" / "tickets" / "GH-1" / "tests-evidences").iterdir())
