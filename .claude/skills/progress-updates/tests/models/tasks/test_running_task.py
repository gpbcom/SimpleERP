from __future__ import annotations

import pytest
from pydantic import JsonValue

from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.models.tasks.exceptions import (
    SERunningTaskDoneAboveTotal,
    SERunningTaskInvalidDetail,
    SERunningTaskInvalidDone,
    SERunningTaskInvalidName,
    SERunningTaskInvalidSource,
    SERunningTaskInvalidState,
    SERunningTaskInvalidTotal,
)
from progress_updates.models.tasks.running_task import RunningTask


class TestRunningTask:
    def _valid(self) -> dict[str, JsonValue]:
        return {
            "name": "K03 mermaid",
            "source": "background",
            "state": "running",
            "detail": "batch 4 of 9",
            "done": 4,
            "total": 9,
        }

    def test_full_valid_construction(self) -> None:
        task = RunningTask.model_validate(self._valid())
        assert task.source is TaskSource.BACKGROUND
        assert task.state is TaskState.RUNNING
        assert (task.done, task.total) == (4, 9)

    def test_defaults(self) -> None:
        task = RunningTask.model_validate({"name": "agent", "source": "declared", "state": "waiting"})
        assert (task.detail, task.done, task.total) == ("", None, None)

    @pytest.mark.parametrize("name", ["detail", "done", "total"])
    def test_none_becomes_the_default(self, name: str) -> None:
        fields = self._valid()
        fields[name] = None
        assert getattr(RunningTask.model_validate(fields), name) in ("", None)

    def test_the_name_and_detail_are_stripped(self) -> None:
        task = RunningTask.model_validate({**self._valid(), "name": "  ci  ", "detail": " ok \n"})
        assert (task.name, task.detail) == ("ci", "ok")

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("name", "", SERunningTaskInvalidName),
            ("name", 3, SERunningTaskInvalidName),
            ("source", "elsewhere", SERunningTaskInvalidSource),
            ("state", "lost", SERunningTaskInvalidState),
            ("detail", 5, SERunningTaskInvalidDetail),
            ("done", -1, SERunningTaskInvalidDone),
            ("done", True, SERunningTaskInvalidDone),
            ("total", 0, SERunningTaskInvalidTotal),
            ("total", "9", SERunningTaskInvalidTotal),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields = self._valid()
        fields[name] = value
        with pytest.raises(error):
            RunningTask.model_validate(fields)

    def test_done_cannot_exceed_the_total(self) -> None:
        with pytest.raises(SERunningTaskDoneAboveTotal):
            RunningTask.model_validate({**self._valid(), "done": 10, "total": 9})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            RunningTask.model_validate({**self._valid(), "other": 1})

    def test_round_trip(self) -> None:
        task = RunningTask.model_validate(self._valid())
        assert RunningTask.model_validate(task.model_dump()) == task
