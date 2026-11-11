from __future__ import annotations

import pytest

from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.service.facts.declared_tasks import DeclaredTasks


class TestDeclaredTasks:
    def test_a_declaration_gives_name_state_detail_and_counts(self) -> None:
        [task] = DeclaredTasks().parse(["research agent=running:12 pages read [12/30]"])
        assert (task.name, task.source, task.state) == ("research agent", TaskSource.DECLARED, TaskState.RUNNING)
        assert (task.detail, task.done, task.total) == ("12 pages read", 12, 30)

    def test_the_detail_is_optional(self) -> None:
        [task] = DeclaredTasks().parse(["workflow=waiting"])
        assert (task.state, task.detail) == (TaskState.WAITING, "")

    @pytest.mark.parametrize("text", ["no equals sign", "x=lost:detail", "=running"])
    def test_a_bad_declaration_becomes_a_warning(self, text: str) -> None:
        [task] = DeclaredTasks().parse([text])
        assert task.state is TaskState.WARNING
        assert task.detail.startswith("bad declaration")
