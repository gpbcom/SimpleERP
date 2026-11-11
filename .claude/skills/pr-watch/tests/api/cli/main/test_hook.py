from __future__ import annotations

import io
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import pytest

from pr_watch.api.cli.main import main
from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.factories.default.default_service_factory import DefaultServiceFactory
from tests.stand_ins.helpers import SESSION_ID


class TestHook:
    def hook(
        self,
        services: DefaultServiceFactory,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
        stdin: str,
    ) -> str:
        monkeypatch.setattr(sys, "stdin", io.StringIO(stdin))
        assert main(["hook-inbox"], services) == 0
        return capsys.readouterr().out

    def test_the_owner_gets_its_waiting_events_as_context(
        self,
        services: DefaultServiceFactory,
        waiting: TicketWatch,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        answer = json.loads(self.hook(services, monkeypatch, capsys, json.dumps({"session_id": SESSION_ID})))
        assert answer["hookSpecificOutput"]["hookEventName"] == "UserPromptSubmit"
        assert "/pr-watch GH-12" in answer["hookSpecificOutput"]["additionalContext"]

    @pytest.mark.parametrize("stdin", [json.dumps({"session_id": "another"}), "{not json", "[]", ""])
    def test_anything_else_prints_nothing_and_exits_zero(
        self,
        services: DefaultServiceFactory,
        waiting: TicketWatch,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
        stdin: str,
    ) -> None:
        assert self.hook(services, monkeypatch, capsys, stdin) == ""

    def test_unreadable_settings_still_exit_zero(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        monkeypatch.setenv("PR_WATCH_STATE_DIR", "")
        monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps({"session_id": SESSION_ID})))
        assert main(["hook-inbox"]) == 0
        assert capsys.readouterr().out == ""

    def test_the_light_console_script_answers_within_half_a_second(
        self, environment: WatchSettings, waiting: TicketWatch
    ) -> None:
        script = Path(sys.executable).parent / "pr-watch-hook"
        started = time.monotonic()
        result = subprocess.run(
            [str(script)],
            input=json.dumps({"session_id": SESSION_ID, "prompt": "go"}),
            capture_output=True,
            text=True,
            env=dict(os.environ),
            check=False,
        )
        elapsed = time.monotonic() - started
        assert result.returncode == 0
        assert json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"].startswith("PR watcher")
        assert result.stderr == ""
        assert elapsed < 0.5
