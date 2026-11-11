from __future__ import annotations

import time
from datetime import timedelta
from pathlib import Path
from typing import Iterator

import pytest

from pr_watch.models.configuration.commands_config import CommandsConfig
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.models.enums import OperationKind, PullRequestStatus
from pr_watch.models.events.inbox import Inbox
from pr_watch.models.events.operation import Operation
from pr_watch.models.state.pr_snapshot import PrSnapshot
from pr_watch.models.state.unwatched_pull_request import UnwatchedPullRequest
from pr_watch.models.state.watch_state import WatchState
from pr_watch.models.watch.registry import Registry
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.report.summary_cells import SummaryCells
from pr_watch.service.report.summary_renderer import SummaryRenderer
from pr_watch.storage.costs.cost_ledger_reader import CostLedgerReader
from pr_watch.storage.desktop.command_runner import CommandRunner
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.sessions.session_directory import SessionDirectory
from pr_watch.storage.state.watch_store import WatchStore
from tests.stand_ins.helpers import HEAD_REF, HEAD_SHA, NOW, REPOSITORY, a_watch, an_event


class TestSummaryRenderer:
    @pytest.fixture(autouse=True)
    def utc(self, monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
        monkeypatch.setenv("TZ", "UTC")
        time.tzset()
        yield
        monkeypatch.undo()
        time.tzset()

    @pytest.fixture
    def store(self, tmp_path: Path) -> WatchStore:
        return WatchStore(tmp_path / "state", TextFiles())

    @pytest.fixture
    def renderer(
        self, store: WatchStore, catalog: WatchCatalog, commands: CommandsConfig, tmp_path: Path
    ) -> SummaryRenderer:
        sessions = SessionDirectory(tmp_path / "claude", commands.claude, CommandRunner())
        cells = SummaryCells(CostLedgerReader(tmp_path / "costs"))
        return SummaryRenderer(store, TextFiles(), cells, WatchSettings().template_file, catalog.timing, sessions)

    def closed(self, watch: TicketWatch, status: PullRequestStatus) -> TicketWatch:
        history = watch.history.model_copy(update={"status": status, "closed_on": NOW + timedelta(hours=5)})
        return watch.model_copy(update={"history": history})

    def test_each_repository_gets_its_own_page(
        self, renderer: SummaryRenderer, store: WatchStore, tmp_path: Path
    ) -> None:
        open_watch = a_watch(tmp_path / "repo")
        merged = self.closed(a_watch(tmp_path / "repo", number=5, key="GH-10"), PullRequestStatus.MERGED)
        closed = self.closed(a_watch(tmp_path / "repo", number=6, key="GH-11"), PullRequestStatus.CLOSED)
        elsewhere = a_watch(tmp_path / "other", number=9, key="GH-30")
        registry = Registry(pull_requests={watch.id: watch for watch in (open_watch, merged, closed, elsewhere)})
        store.save_inbox("GH-12", Inbox(events=[an_event(open_watch)]))
        store.append_operation(Operation(at=NOW, pr_id=merged.id, kind=OperationKind.DETECTED, detail="old failure"))
        store.append_operation(
            Operation(at=NOW, pr_id=open_watch.id, kind=OperationKind.FIXED, detail="a | b", link="https://x/1")
        )
        state = WatchState(
            last_checked=NOW,
            snapshots={
                open_watch.id: PrSnapshot(
                    branches={"head_ref": HEAD_REF, "head_sha": HEAD_SHA, "base_ref": "develop"},
                    ci={"checks": "failed", "checks_link": "https://x/runs/1"},
                    checked_on=NOW,
                )
            },
            unwatched={
                f"{REPOSITORY}#8": UnwatchedPullRequest(
                    repository=REPOSITORY, number=8, title="[GH-13] Invoices", ticket="GH-13", updated_on=NOW
                )
            },
        )
        pages = renderer.render(registry, state, {})
        assert pages == [tmp_path / "other" / SummaryRenderer.PAGE, tmp_path / "repo" / SummaryRenderer.PAGE]
        page = pages[1].read_text(encoding="utf-8")
        assert "**Last checked:** 2026-11-10 08:00 · **Next check:** 2026-11-10 08:10" in page
        assert "**Watched:** 1 open · 1 merged · 1 closed" in page
        assert "**Now:** 🟢 0 · 🔀 0 · 🔧 1 · 🚧 0 · ✍️ 0 · ⚠️ 0 · ⏳ 1 events waiting" in page
        assert (
            f"| 🔧 | [GH-12](../GH-12/PROGRESS.md) | [#7](https://github.com/{REPOSITORY}/pull/7) | `{HEAD_REF}` "
            "| [❌](https://x/runs/1) | — | — | ⏳ 1 waiting: 🔧 | — | `7a30c2c8` | 2026-11-09 06:00 "
            "| 2026-11-10 08:00 🛠️ a \\| b |"
        ) in page
        assert f"| [{REPOSITORY}#8](https://github.com/{REPOSITORY}/pull/8) | GH-13 | [GH-13] Invoices |" in page
        assert "| [GH-10](../GH-10/PROGRESS.md) | [#5]" in page
        assert "| 2026-11-10 13:00 | 1d 7h00 | 1 | — |" in page
        assert "GH-30" not in page
        assert "GH-12" not in pages[0].read_text(encoding="utf-8")

    def test_a_refresh_reads_the_stored_state(
        self, renderer: SummaryRenderer, store: WatchStore, tmp_path: Path
    ) -> None:
        watch = a_watch(tmp_path / "repo")
        store.save_registry(Registry(pull_requests={watch.id: watch}))
        pages = renderer.refresh()
        assert "| ⚠️ not checked yet | [GH-12]" in pages[0].read_text(encoding="utf-8")
