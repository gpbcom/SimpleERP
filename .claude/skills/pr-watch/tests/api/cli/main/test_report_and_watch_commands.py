from __future__ import annotations

from pathlib import Path

import pytest

from harness_core.testing.github_fake import GithubFake
from pr_watch.api.cli.main import main
from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.factories.default.default_service_factory import DefaultServiceFactory
from tests.stand_ins.helpers import SESSION_ID, check_run_payload, open_pull_request_routes


class TestReportAndWatchCommands:
    def test_status_and_render(
        self, services: DefaultServiceFactory, waiting: TicketWatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["status"], services) == 0
        assert capsys.readouterr().out == f"{waiting.id} open session={SESSION_ID} waiting=1\n"
        assert main(["render"], services) == 0
        page = Path(waiting.pull_request.root) / "docs" / "tickets" / "pull-request-summary" / "README.md"
        assert capsys.readouterr().out == f"Wrote {page}.\n"

    def test_status_with_nothing_watched(
        self, services: DefaultServiceFactory, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["status"], services) == 0
        assert capsys.readouterr().out == "No pull request is watched.\n"

    def test_once_runs_the_watcher(
        self,
        services: DefaultServiceFactory,
        waiting: TicketWatch,
        fake: GithubFake,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        fake.routes.update(open_pull_request_routes(checks=[check_run_payload(1, "unit", "failure")]))
        assert main(["once"], services) == 0
        assert capsys.readouterr().out == "Checked 1 open pull requests: 1 events found.\n"

    def test_once_without_token_fails_with_a_message(
        self,
        services: DefaultServiceFactory,
        waiting: TicketWatch,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        monkeypatch.delenv("GITHUB_TOKEN")
        monkeypatch.setenv("PATH", str(tmp_path / "empty"))
        assert main(["once"], services) == 2
        assert "GITHUB_TOKEN" in capsys.readouterr().err

    def test_install_units_writes_them_where_asked(
        self,
        environment: WatchSettings,
        services: DefaultServiceFactory,
        tmp_path: Path,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        assert main(["install-units", "--target", str(tmp_path / "units")], services) == 0
        assert sorted(path.name for path in (tmp_path / "units").iterdir()) == [
            "claude-pr-watch.service",
            "claude-pr-watch.timer",
        ]
        assert "systemctl --user enable --now claude-pr-watch.timer" in capsys.readouterr().out
