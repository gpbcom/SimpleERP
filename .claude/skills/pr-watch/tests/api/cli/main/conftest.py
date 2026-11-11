from __future__ import annotations

from pathlib import Path

import pytest

from harness_core.testing.github_fake import GithubFake
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.models.events.inbox import Inbox
from pr_watch.models.watch.registry import Registry
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.factories.default.default_service_factory import DefaultServiceFactory
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.state.watch_store import WatchStore
from tests.stand_ins.git_sandbox import GitSandbox
from tests.stand_ins.helpers import a_watch, an_event


@pytest.fixture
def environment(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> WatchSettings:
    """Point the command line's settings at the test's folders, as bin/pr-watch would."""
    clone = GitSandbox(tmp_path).build(conflict=False)
    monkeypatch.setenv("PR_WATCH_STATE_DIR", str(tmp_path / "state"))
    monkeypatch.setenv("PR_WATCH_CLAUDE_HOME", str(tmp_path / "claude"))
    monkeypatch.setenv("PR_WATCH_CALLER_CWD", str(clone))
    monkeypatch.setenv("AI_COST_STATE_DIR", str(tmp_path / "costs"))
    monkeypatch.setenv("GITHUB_TOKEN", "secret-token")
    monkeypatch.delenv("CLAUDE_CODE_SESSION_ID", raising=False)
    return WatchSettings()


@pytest.fixture
def services(environment: WatchSettings, faked_catalog: WatchCatalog, fake: GithubFake) -> DefaultServiceFactory:
    return DefaultServiceFactory(environment, faked_catalog, fake.transport())


@pytest.fixture
def store(environment: WatchSettings) -> WatchStore:
    return WatchStore(environment.state_dir, TextFiles())


@pytest.fixture
def waiting(environment: WatchSettings, store: WatchStore) -> TicketWatch:
    """Watch the sandbox's pull request with one waiting event."""
    watch = a_watch(environment.caller_cwd)
    store.save_registry(Registry(pull_requests={watch.id: watch}))
    store.save_inbox(watch.key, Inbox(events=[an_event(watch)]))
    return watch
