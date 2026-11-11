from __future__ import annotations

import json
from datetime import timedelta
from pathlib import Path
from typing import Dict

import pytest
from pydantic import JsonValue

from pr_watch.models.events.inbox import Inbox
from pr_watch.models.sessions.live_session import LiveSession
from pr_watch.models.state.pr_snapshot import PrSnapshot
from pr_watch.service.report.summary_cells import SummaryCells
from pr_watch.storage.costs.cost_ledger_reader import CostLedgerReader
from tests.stand_ins.helpers import NOW, SESSION_ID, a_watch, an_event


class TestSummaryCells:
    @pytest.fixture
    def cells(self, tmp_path: Path) -> SummaryCells:
        return SummaryCells(CostLedgerReader(tmp_path / "costs"))

    def test_durations_show_days_hours_and_minutes(self, cells: SummaryCells) -> None:
        assert cells.duration(NOW, NOW + timedelta(days=2, hours=3, minutes=5)) == "2d 3h05"
        assert cells.duration(NOW, NOW + timedelta(minutes=59)) == "0h59"
        assert cells.duration(None, NOW) == "—"

    def test_a_cell_holds_one_escaped_line(self, cells: SummaryCells) -> None:
        assert cells.text("a | b\nc", 80) == "a \\| b c"
        assert cells.text("abcdef", 4) == "abc…"

    @pytest.mark.parametrize(
        ("ledger", "shown"),
        [
            ({"ticket": "GH-12", "cap_usd": 20, "spent_usd": 3.5, "blocked": False}, "$3.50 / $20"),
            ({"ticket": "GH-12", "cap_usd": 20, "spent_usd": 17, "blocked": False}, "$17.00 / $20 ⚠️"),
            ({"ticket": "GH-12", "cap_usd": 20, "spent_usd": 20, "blocked": True}, "$20.00 / $20 ⚠️ ⛔"),
        ],
    )
    def test_the_cost_shows_the_spend_against_the_cap(
        self, cells: SummaryCells, tmp_path: Path, ledger: Dict[str, JsonValue], shown: str
    ) -> None:
        (tmp_path / "costs").mkdir()
        (tmp_path / "costs" / "GH-12.json").write_text(json.dumps(ledger), encoding="utf-8")
        assert cells.cost("GH-12") == shown
        assert cells.cost("GH-13") == "—"

    def test_the_status_lists_every_problem(self, cells: SummaryCells) -> None:
        snapshot = PrSnapshot(
            rebase={"conflict_files": ["a.py"]},
            ci={
                "checks": "failed",
                "stages": [{"environment": "qa", "deployment_id": 3, "state": "error"}],
                "review": "CHANGES_REQUESTED",
            },
            error="GitHub answered 503",
            checked_on=NOW,
        )
        assert cells.status(snapshot) == "🔀 🔧 🚧 ✍️ ⚠️"
        assert cells.status(PrSnapshot(checked_on=NOW)) == "🟢"
        assert cells.status(None) == "⚠️ not checked yet"
        assert cells.stages(snapshot) == "🟪 qa ❌"
        assert cells.review(snapshot) == "✍️ changes requested"

    def test_handling_shows_who_must_act(self, cells: SummaryCells, tmp_path: Path) -> None:
        watch = a_watch(tmp_path)
        event = an_event(watch)
        failing = PrSnapshot(ci={"checks": "failed"}, checked_on=NOW)
        assert cells.handling(Inbox(events=[event]), failing, watch) == "⏳ 1 waiting: 🔧"
        taken = Inbox(events=[event.model_copy(update={"acked_on": NOW})])
        assert cells.handling(taken, failing, watch) == "🔄 in the session"
        assert cells.handling(taken, PrSnapshot(checked_on=NOW), watch) == "—"

    def test_the_session_shows_where_it_runs(self, cells: SummaryCells, tmp_path: Path) -> None:
        watch = a_watch(tmp_path)
        live = {SESSION_ID: LiveSession(session_id=SESSION_ID, pid=1, entrypoint="claude-vscode")}
        assert cells.session(watch, live) == "`7a30c2c8` 🟢 VS Code"
        assert cells.session(watch, {}) == "`7a30c2c8`"
        assert cells.session(a_watch(tmp_path, session=False), live) == "🔔 none"
