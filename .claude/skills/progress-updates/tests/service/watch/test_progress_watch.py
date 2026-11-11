from __future__ import annotations

import io
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple

import pytest

from progress_updates.models.catalogs.progress_catalog import ProgressCatalog
from progress_updates.models.exceptions import SEWatchIntervalError
from progress_updates.models.tasks.running_task import RunningTask
from progress_updates.service.facts.fact_collector import FactCollector
from progress_updates.service.watch.progress_watch import ProgressWatch
from tests.service.watch.fake_clock import FakeClock
from tests.service.watch.sequence_reader import SequenceReader


class TestProgressWatch:
    @pytest.fixture
    def catalog(self, skill_root: Path) -> ProgressCatalog:
        return ProgressCatalog.load(skill_root / "conf" / "progress-updates.yaml")

    def _task(self, name: str, state: str) -> RunningTask:
        return RunningTask.model_validate({"name": name, "source": "background", "state": state})

    def _watch(
        self,
        catalog: ProgressCatalog,
        reads: List[List[RunningTask]],
        interval_s: int = 120,
        max_ticks: Optional[int] = None,
    ) -> Tuple[ProgressWatch, io.StringIO, FakeClock]:
        out = io.StringIO()
        clock = FakeClock(datetime(2026, 11, 11, 14, 30))
        collector = FactCollector([SequenceReader(reads)], [])
        return ProgressWatch(collector, catalog, clock, out, interval_s, max_ticks), out, clock

    def test_a_running_task_gives_one_event_every_2_minutes(self, catalog: ProgressCatalog) -> None:
        watch, out, clock = self._watch(catalog, [[self._task("b1", "running")]], max_ticks=2)
        assert watch.follow() == 0
        lines = out.getvalue().splitlines()
        assert len(lines) == 2
        assert clock.sleeps == [120, 120]
        assert lines[0].startswith("⏱️ 14:32 · 🔄 1 running")

    def test_an_interval_under_2_minutes_is_refused(self, catalog: ProgressCatalog) -> None:
        with pytest.raises(SEWatchIntervalError):
            self._watch(catalog, [[]], interval_s=60)

    def test_when_the_last_task_ends_a_final_event_is_printed_and_the_watch_stops(
        self, catalog: ProgressCatalog
    ) -> None:
        running, done = [self._task("b1", "running")], [self._task("b1", "done")]
        watch, out, _ = self._watch(catalog, [running, running, done])
        assert watch.follow() == 0
        lines = out.getvalue().splitlines()
        assert len(lines) == 2
        assert lines[-1].startswith("🏁 14:34 · nothing runs any more")

    def test_nothing_running_at_start_gives_one_final_event(self, catalog: ProgressCatalog) -> None:
        watch, out, clock = self._watch(catalog, [[self._task("b1", "done")]])
        assert watch.follow() == 0
        assert out.getvalue().splitlines() == ["🏁 14:30 · nothing runs any more · post the final update"]
        assert clock.sleeps == []

    def test_each_event_is_one_line_naming_the_command_to_run(self, catalog: ProgressCatalog) -> None:
        watch, out, _ = self._watch(
            catalog, [[self._task("a", "running"), self._task("b", "waiting"), self._task("c", "failed")]], max_ticks=1
        )
        watch.follow()
        [line] = out.getvalue().splitlines()
        assert line == "⏱️ 14:32 · 🔄 1 running · ⏳ 1 waiting · ❌ 1 failed · post an update (progress-updates status)"
