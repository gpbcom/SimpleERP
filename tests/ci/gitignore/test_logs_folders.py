from __future__ import annotations

import subprocess
from pathlib import Path

import pytest


class TestLogsFolders:
    ROOT = Path(__file__).resolve().parents[3]

    def is_ignored(self, path: str) -> bool:
        result = subprocess.run(
            ["git", "check-ignore", "-q", path],
            cwd=self.ROOT,
            capture_output=True,
            check=False,
        )
        return result.returncode == 0

    @pytest.mark.parametrize(
        "path",
        [
            "backend/shared/testing/src/erp_testing/logs/log_capture.py",
            "backend/shared/testing/tests/logs/test_log_capture.py",
            "backend/services/demo/src/demo/logs/__init__.py",
            "backend/services/demo/tests/logs/sub/test_x.py",
        ],
    )
    def test_a_logs_package_of_src_or_tests_is_tracked(self, path: str) -> None:
        assert not self.is_ignored(path)

    @pytest.mark.parametrize(
        "path",
        [
            "logs/app.log",
            "backend/services/platform/logs/platform.log",
            "backend/shared/logging/logs/logging.jsonl",
        ],
    )
    def test_a_runtime_log_folder_is_ignored(self, path: str) -> None:
        assert self.is_ignored(path)
