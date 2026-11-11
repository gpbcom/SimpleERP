from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path

import pytest

from pr_watch.models.configuration.watch_settings import WatchSettings


class TestWrapper:
    def test_bin_pr_watch_runs_the_tool_from_any_folder_with_the_callers_folder(self, tmp_path: Path) -> None:
        if shutil.which("uv") is None:
            pytest.skip("uv is not installed")
        environment = {
            **os.environ,
            "PR_WATCH_STATE_DIR": str(tmp_path / "state"),
            "PR_WATCH_CLAUDE_HOME": str(tmp_path / "claude"),
        }
        result = subprocess.run(
            [str(WatchSettings().skill_dir / "bin" / "pr-watch"), "status"],
            cwd=tmp_path,
            capture_output=True,
            text=True,
            env=environment,
            check=False,
        )
        assert (result.returncode, result.stdout) == (0, "No pull request is watched.\n")
        assert (tmp_path / "state" / "pr-watch.log").exists()

    def test_the_hook_through_bin_pr_watch_answers_within_half_a_second(self, tmp_path: Path) -> None:
        environment = {**os.environ, "PR_WATCH_STATE_DIR": str(tmp_path / "state")}
        started = time.monotonic()
        result = subprocess.run(
            [str(WatchSettings().skill_dir / "bin" / "pr-watch"), "hook-inbox"],
            input='{"session_id": "nobody"}',
            capture_output=True,
            text=True,
            env=environment,
            check=False,
        )
        assert (result.returncode, result.stdout, result.stderr) == (0, "", "")
        assert time.monotonic() - started < 0.5
