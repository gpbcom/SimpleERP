from __future__ import annotations

from pathlib import Path

import pytest

from pr_watch.api.cli.main import main
from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.models.enums import OperationKind
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.factories.default.default_service_factory import DefaultServiceFactory
from pr_watch.storage.state.watch_store import WatchStore


class TestInboxCommands:
    def page(self, watch: TicketWatch) -> Path:
        return Path(watch.pull_request.root) / "docs" / "tickets" / "pull-request-summary" / "README.md"

    def test_show_prints_the_waiting_events(
        self, services: DefaultServiceFactory, waiting: TicketWatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["show", "GH-12"], services) == 0
        assert capsys.readouterr().out.startswith("- [checks_failed] 2 checks failed on 668501e0")
        assert main(["show", "GH-99"], services) == 0
        assert capsys.readouterr().out == "No event of GH-99 is waiting.\n"

    def test_ack_then_log_reach_the_summary_page(
        self,
        services: DefaultServiceFactory,
        waiting: TicketWatch,
        store: WatchStore,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        assert main(["ack", "GH-12"], services) == 0
        assert capsys.readouterr().out == "1 events taken.\n"
        assert store.inbox("GH-12").pending == []
        assert main(["log", "GH-12", "fixed", "unit test fixed", "--link", "https://x/commit/1"], services) == 0
        assert [operation.kind for operation in store.operations()] == [OperationKind.ACKED, OperationKind.FIXED]
        assert "unit test fixed" in self.page(waiting).read_text(encoding="utf-8")

    def test_logging_on_an_unwatched_ticket_fails_with_a_message(
        self,
        services: DefaultServiceFactory,
        waiting: TicketWatch,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        assert main(["log", "GH-99", "note", "x"], services) == 2
        assert "pr-watch register GH-99" in capsys.readouterr().err

    def test_a_kind_a_session_may_not_log_is_refused(
        self, environment: WatchSettings, services: DefaultServiceFactory
    ) -> None:
        with pytest.raises(SystemExit):
            main(["log", "GH-12", "merged", "x"], services)
