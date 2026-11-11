from __future__ import annotations

from pathlib import Path

import pytest

from harness_core.testing.fake_program import FakeProgram
from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.models.exceptions import SESourceUnreadableError
from progress_updates.storage.processes.process_reader import ProcessReader


class TestProcessReader:
    def _ps(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, body: str) -> None:
        bin_dir = tmp_path / "bin"
        FakeProgram(bin_dir).write("ps", body)
        monkeypatch.setenv("PATH", f"{bin_dir}:/usr/bin:/bin")

    def test_only_processes_working_in_the_repository_are_reported(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        root = tmp_path / "repo"
        self._ps(
            tmp_path,
            monkeypatch,
            "cat <<'OUT'\n"
            f"  101   480 python3 -I {root}/tools/check_mermaid.py {root}/docs/specs\n"
            "  102  9000 /usr/lib/firefox/firefox\n"
            f"  103    30 {root}/.claude/skills/.venv/bin/progress-updates watch --every 120\n"
            "OUT",
        )
        [task] = ProcessReader(root, 160).tasks()
        assert (task.source, task.state) == (TaskSource.PROCESS, TaskState.RUNNING)
        assert "check_mermaid.py" in task.name
        assert task.detail == "pid 101 · running for 8 min"

    def test_ps_failing_cannot_be_read(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        self._ps(tmp_path, monkeypatch, "exit 3")
        with pytest.raises(SESourceUnreadableError):
            ProcessReader(tmp_path, 160).tasks()
