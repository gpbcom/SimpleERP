from __future__ import annotations

import pytest

from pr_watch.api.cli.main import main
from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.service.factories.default.default_service_factory import DefaultServiceFactory
from pr_watch.storage.state.watch_store import WatchStore
from tests.stand_ins.helpers import PR_URL, SESSION_ID


class TestSessionCommands:
    @pytest.fixture
    def ticket(self, environment: WatchSettings) -> None:
        folder = environment.caller_cwd / "docs" / "tickets" / "GH-12"
        folder.mkdir(parents=True)
        (folder / "PROGRESS.md").write_text(f"# GH-12\n\n## Pull request\n\n{PR_URL}\n", encoding="utf-8")

    def test_register_watches_for_the_session_it_runs_in(
        self,
        services: DefaultServiceFactory,
        ticket: None,
        store: WatchStore,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", SESSION_ID)
        assert main(["register", "GH-12"], services) == 0
        assert capsys.readouterr().out == f"Watching GH-12:gpbcom/simple-erp#7 ({PR_URL}) for session {SESSION_ID}.\n"
        watch = store.registry().pull_requests["GH-12:gpbcom/simple-erp#7"]
        assert watch.session is not None
        assert watch.session.session_id == SESSION_ID

    def test_register_outside_a_session_needs_a_choice(
        self, services: DefaultServiceFactory, ticket: None, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["register", "GH-12"], services) == 2
        assert "--no-session" in capsys.readouterr().err
        assert main(["register", "GH-12", "--no-session"], services) == 0

    def test_register_without_link_fails_with_a_message(
        self, services: DefaultServiceFactory, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["register", "GH-13", "--session", SESSION_ID], services) == 2
        assert "--link" in capsys.readouterr().err

    def test_backfill_proposes_and_applies_only_on_request(
        self, services: DefaultServiceFactory, ticket: None, store: WatchStore, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["backfill"], services) == 0
        out = capsys.readouterr().out
        assert f"GH-12 {PR_URL}: no session found" in out
        assert "Nothing registered" in out
        assert store.registry().pull_requests == {}
        assert main(["backfill", "--apply"], services) == 0
        assert list(store.registry().pull_requests) == ["GH-12:gpbcom/simple-erp#7"]
