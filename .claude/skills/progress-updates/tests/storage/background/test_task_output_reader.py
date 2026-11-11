from __future__ import annotations

import os
import time
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.models.exceptions import SESourceUnreadableError
from progress_updates.storage.background.task_output_reader import TaskOutputReader


class TestTaskOutputReader:
    def _write(self, folder: Path, name: str, text: str, age_s: int = 0) -> Path:
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{name}.output"
        path.write_text(text, encoding="utf-8")
        stamp = time.time() - age_s
        os.utime(path, (stamp, stamp))
        return path

    def test_a_command_without_an_exit_line_is_running_with_its_last_line(self, tmp_path: Path) -> None:
        self._write(tmp_path, "b1", "specs-links: ✅ PASS\nspecs-mermaid: rendering batch 4\n\n")
        [task] = TaskOutputReader(tmp_path, 160).tasks()
        assert (task.name, task.source, task.state) == ("b1", TaskSource.BACKGROUND, TaskState.RUNNING)
        assert task.detail == "specs-mermaid: rendering batch 4"

    @pytest.mark.parametrize(("code", "state"), [(0, TaskState.DONE), (1, TaskState.FAILED), (137, TaskState.FAILED)])
    def test_the_exit_line_gives_done_or_failed(self, tmp_path: Path, code: int, state: TaskState) -> None:
        self._write(tmp_path, "b2", f"9 passed\n\n[exited with code {code}]\n")
        [task] = TaskOutputReader(tmp_path, 160).tasks()
        assert task.state is state
        assert task.detail == "9 passed"

    def test_finished_tasks_older_than_since_are_left_out_but_running_ones_stay(self, tmp_path: Path) -> None:
        self._write(tmp_path, "old", "ok\n[exited with code 0]\n", age_s=3600)
        self._write(tmp_path, "slow", "still going\n", age_s=3600)
        tasks = TaskOutputReader(tmp_path, 160, since=datetime.now() - timedelta(minutes=10)).tasks()
        assert [task.name for task in tasks] == ["slow"]

    def test_subagent_transcripts_are_left_to_the_declared_tasks(self, tmp_path: Path) -> None:
        self._write(tmp_path, "agent", '{"type": "assistant"}\n{"type": "user"}\n')
        assert TaskOutputReader(tmp_path, 160).tasks() == []

    def test_a_long_last_line_is_cut(self, tmp_path: Path) -> None:
        self._write(tmp_path, "b3", "x" * 500 + "\n")
        [task] = TaskOutputReader(tmp_path, 40).tasks()
        assert len(task.detail) <= 40
        assert task.detail.endswith("…")

    @pytest.mark.parametrize(
        "line",
        [
            "⏱️ 14:43 · 🔄 3 running · post an update (progress-updates status)",
            "🏁 14:39 · nothing runs any more · post the final update",
        ],
    )
    def test_the_watch_s_own_monitor_output_is_not_a_task(self, tmp_path: Path, line: str) -> None:
        self._write(tmp_path, "monitor", f"{line}\n")
        assert TaskOutputReader(tmp_path, 160).tasks() == []

    def test_a_command_quoting_a_watch_line_is_still_a_task(self, tmp_path: Path) -> None:
        self._write(tmp_path, "quoting", "⏱️ 14:43 · post an update (progress-updates status)\nstep 2 of 5\n")
        [task] = TaskOutputReader(tmp_path, 160).tasks()
        assert (task.state, task.detail) == (TaskState.RUNNING, "step 2 of 5")

    def test_a_task_stopped_by_hand_is_a_warning_not_running(self, tmp_path: Path) -> None:
        self._write(tmp_path, "stopped", "batch 2\n[killed]\n")
        [task] = TaskOutputReader(tmp_path, 160).tasks()
        assert (task.state, task.detail) == (TaskState.WARNING, "stopped: batch 2")

    @pytest.mark.parametrize(
        ("last", "state"),
        [("❌ FAIL (exit 1)", TaskState.FAILED), ("⚠️ invalid", TaskState.WARNING), ("✅ PASS 9/9", TaskState.DONE)],
    )
    def test_an_exit_0_keeps_the_verdict_of_its_last_line(self, tmp_path: Path, last: str, state: TaskState) -> None:
        self._write(tmp_path, "recorded", f"{last}\n\n[exited with code 0]\n")
        assert TaskOutputReader(tmp_path, 160).tasks()[0].state is state

    def test_a_missing_folder_cannot_be_read(self, tmp_path: Path) -> None:
        with pytest.raises(SESourceUnreadableError):
            TaskOutputReader(tmp_path / "missing", 160).tasks()
