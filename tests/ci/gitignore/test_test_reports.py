from __future__ import annotations

import subprocess
from pathlib import Path

import pytest


class TestTestReports:
    ROOT = Path(__file__).resolve().parents[3]

    def is_ignored(self, path: str) -> bool:
        result = subprocess.run(
            ["git", "check-ignore", "-q", "--no-index", path],
            cwd=self.ROOT,
            capture_output=True,
            check=False,
        )
        return result.returncode == 0

    @pytest.mark.parametrize("path", ["reports/lifecycle.xml", "reports/junit/a.xml"])
    def test_a_test_report_at_the_repository_root_is_ignored(self, path: str) -> None:
        assert self.is_ignored(path)

    @pytest.mark.parametrize(
        "path",
        [".claude/scripts/reports/progress.py", ".claude/scripts/reports/statusline.py"],
    )
    def test_the_reports_scripts_of_the_harness_stay_tracked(self, path: str) -> None:
        assert (self.ROOT / path).is_file()
        assert not self.is_ignored(path)
