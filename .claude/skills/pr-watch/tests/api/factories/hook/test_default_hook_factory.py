from __future__ import annotations

import io
import json
import sys
from pathlib import Path

import pytest

from pr_watch.api.cli.hook_main import main
from pr_watch.api.cli.hooks.hook_command import HookCommand
from pr_watch.api.factories.hook.default_hook_factory import DefaultHookFactory
from pr_watch.models.events.inbox import Inbox
from pr_watch.models.watch.registry import Registry
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.state.watch_store import WatchStore
from tests.stand_ins.helpers import SESSION_ID, a_watch, an_event


class TestDefaultHookFactory:
    def test_the_hook_reads_the_state_folder_it_is_given(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        watch = a_watch(tmp_path)
        store = WatchStore(tmp_path / "state", TextFiles())
        store.save_registry(Registry(pull_requests={watch.id: watch}))
        store.save_inbox(watch.key, Inbox(events=[an_event(watch)]))
        monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps({"session_id": SESSION_ID})))
        hook = DefaultHookFactory(tmp_path / "state").hook()
        assert isinstance(hook, HookCommand)
        hook.execute()
        assert hook.exit_code == 0
        assert "/pr-watch GH-12" in json.loads(capsys.readouterr().out)["hookSpecificOutput"]["additionalContext"]

    def test_the_light_entry_point_reads_the_state_folder_of_the_settings(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        watch = a_watch(tmp_path)
        store = WatchStore(tmp_path / "state", TextFiles())
        store.save_registry(Registry(pull_requests={watch.id: watch}))
        store.save_inbox(watch.key, Inbox(events=[an_event(watch)]))
        monkeypatch.setenv("PR_WATCH_STATE_DIR", str(tmp_path / "state"))
        monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps({"session_id": SESSION_ID})))
        assert main() == 0
        assert "/pr-watch GH-12" in capsys.readouterr().out
