from __future__ import annotations

import asyncio
from pathlib import Path

import pytest

from harness_core.github.exceptions import SEGithubTokenMissingError
from harness_core.testing.github_fake import GithubFake
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.models.enums import EventKind, OperationKind, PullRequestStatus
from pr_watch.models.events.inbox import Inbox
from pr_watch.models.watch.registry import Registry
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.factories.default.default_service_factory import DefaultServiceFactory
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.state.watch_store import WatchStore
from tests.stand_ins.git_sandbox import GitSandbox
from tests.stand_ins.helpers import (
    API,
    a_watch,
    an_event,
    check_run_payload,
    open_pull_request_routes,
    pull_request_payload,
    recorded_calls,
)


class TestWatchJob:
    @pytest.fixture(autouse=True)
    def token(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("GITHUB_TOKEN", "secret-token")

    @pytest.fixture
    def factory(self, settings: WatchSettings, faked_catalog: WatchCatalog, fake: GithubFake) -> DefaultServiceFactory:
        return DefaultServiceFactory(settings, faked_catalog, fake.transport())

    @pytest.fixture
    def store(self, settings: WatchSettings) -> WatchStore:
        return WatchStore(settings.state_dir, TextFiles())

    @pytest.fixture
    def watch(self, store: WatchStore, tmp_path: Path) -> TicketWatch:
        watch = a_watch(GitSandbox(tmp_path).build(conflict=False))
        store.save_registry(Registry(pull_requests={watch.id: watch}))
        return watch

    def opened(self, calls_log: Path) -> int:
        return sum(1 for call in recorded_calls(calls_log) if call[0] == "xdg-open")

    def test_a_run_files_the_events_reopens_the_session_and_writes_the_page(
        self, factory: DefaultServiceFactory, store: WatchStore, watch: TicketWatch, fake: GithubFake, calls_log: Path
    ) -> None:
        fake.routes.update(open_pull_request_routes(checks=[check_run_payload(1, "unit", "failure")]))
        job = factory.watch_job()
        asyncio.run(job.execute())
        assert (job.checked, job.found) == (1, 1)
        assert [event.kind for event in store.inbox("GH-12").events] == [EventKind.CHECKS_FAILED]
        assert self.opened(calls_log) == 1
        assert store.state().snapshots[watch.id].rebase is not None
        assert store.registry().pull_requests[watch.id].history.opened_on is not None
        page = (Path(watch.pull_request.root) / "docs" / "tickets" / "pull-request-summary" / "README.md").read_text(
            encoding="utf-8"
        )
        assert "| 🔧 | [GH-12]" in page
        asyncio.run(factory.watch_job().execute())
        assert len(store.inbox("GH-12").events) == 1
        assert self.opened(calls_log) == 1

    def test_a_merged_pull_request_leaves_the_watch_list_and_closes_its_events(
        self, factory: DefaultServiceFactory, store: WatchStore, watch: TicketWatch, fake: GithubFake
    ) -> None:
        store.save_inbox(watch.key, Inbox(events=[an_event(watch)]))
        fake.routes.update(open_pull_request_routes())
        fake.routes[f"{API}/pulls/7"] = pull_request_payload(state="closed", merged=True)
        asyncio.run(factory.watch_job().execute())
        closed = store.registry().pull_requests[watch.id]
        assert closed.history.status == PullRequestStatus.MERGED
        assert store.inbox(watch.key).pending == []
        merged = [operation for operation in store.operations() if operation.kind == OperationKind.MERGED]
        assert [operation.detail for operation in merged] == ["merged as 9f1c2b3a"]

    def test_a_pull_request_github_cannot_read_is_warned_about_once(
        self, factory: DefaultServiceFactory, store: WatchStore, watch: TicketWatch, fake: GithubFake
    ) -> None:
        fake.routes.update(open_pull_request_routes())
        fake.failures[f"{API}/pulls/7"] = 503
        asyncio.run(factory.watch_job().execute())
        asyncio.run(factory.watch_job().execute())
        warnings = [operation for operation in store.operations() if operation.kind == OperationKind.WARNING]
        assert len(warnings) == 1
        assert "503" in (store.state().snapshots[watch.id].error or "")
        assert store.state().last_checked is not None

    def test_a_run_without_token_stops_before_reading_anything(
        self, factory: DefaultServiceFactory, fake: GithubFake, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        monkeypatch.delenv("GITHUB_TOKEN")
        monkeypatch.setenv("PATH", str(tmp_path / "empty"))
        with pytest.raises(SEGithubTokenMissingError):
            asyncio.run(factory.watch_job().execute())
        assert fake.requests == []
