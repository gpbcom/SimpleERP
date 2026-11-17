from __future__ import annotations

from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.models.tasks.running_task import RunningTask
from progress_updates.service.facts.fact_collector import FactCollector
from tests.service.facts.broken_reader import BrokenReader
from tests.service.facts.fixed_reader import FixedReader


class TestFactCollector:
    def _task(self, name: str, state: str = "running", source: str = "background") -> RunningTask:
        return RunningTask.model_validate({"name": name, "source": source, "state": state})

    def test_declared_tasks_come_first_then_each_reader(self) -> None:
        declared = [self._task("research agent", source="declared")]
        tasks = FactCollector([FixedReader([self._task("b1")])], declared).collect()
        assert [task.name for task in tasks] == ["research agent", "b1"]

    def test_a_task_found_twice_is_reported_once(self) -> None:
        tasks = FactCollector([FixedReader([self._task("b1"), self._task("b1")])], []).collect()
        assert [task.name for task in tasks] == ["b1"]

    def test_a_source_that_fails_is_a_warning_and_the_others_are_still_read(self) -> None:
        tasks = FactCollector([BrokenReader(), FixedReader([self._task("b1")])], []).collect()
        assert [(task.source, task.state) for task in tasks] == [
            (TaskSource.ACTIONS, TaskState.WARNING),
            (TaskSource.BACKGROUND, TaskState.RUNNING),
        ]
        assert tasks[0].detail.startswith("not read:")
