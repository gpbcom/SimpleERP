from __future__ import annotations

from pathlib import Path
from typing import List

import pytest

from pr_watch.models.configuration.commands_config import CommandsConfig
from pr_watch.models.enums import DispatchAction
from pr_watch.models.sessions.live_session import LiveSession
from pr_watch.service.sessions.session_dispatcher import SessionDispatcher
from pr_watch.storage.desktop.command_runner import CommandRunner
from tests.stand_ins.helpers import SESSION_ID, a_watch, an_event, recorded_calls, write_program


class TestSessionDispatcher:
    def programs(self, calls_log: Path) -> List[str]:
        return [call[0] for call in recorded_calls(calls_log)]

    def live(self, entrypoint: str) -> LiveSession:
        return LiveSession(session_id=SESSION_ID, pid=1, cwd="/repo", entrypoint=entrypoint)

    def test_a_closed_session_is_opened_in_vscode_with_the_prompt_typed(
        self, commands: CommandsConfig, calls_log: Path, tmp_path: Path
    ) -> None:
        watch = a_watch(tmp_path)
        outcome = SessionDispatcher(commands, CommandRunner()).dispatch(watch, None, [an_event(watch)])
        assert (outcome.action, outcome.ok) == (DispatchAction.REOPENED_VSCODE, True)
        calls = recorded_calls(calls_log)
        assert [call[0] for call in calls] == ["code", "xdg-open", "notify-send"]
        assert calls[0][1] == str(tmp_path)
        assert calls[1][1] == f"vscode://anthropic.claude-code/open?session={SESSION_ID}&prompt=/pr-watch%20GH-12"

    def test_a_session_open_in_vscode_is_brought_forward(
        self, commands: CommandsConfig, calls_log: Path, tmp_path: Path
    ) -> None:
        watch = a_watch(tmp_path)
        outcome = SessionDispatcher(commands, CommandRunner()).dispatch(
            watch, self.live("claude-vscode"), [an_event(watch)]
        )
        assert outcome.action == DispatchAction.REOPENED_VSCODE

    def test_a_session_open_in_a_terminal_is_only_notified(
        self, commands: CommandsConfig, calls_log: Path, tmp_path: Path
    ) -> None:
        watch = a_watch(tmp_path)
        outcome = SessionDispatcher(commands, CommandRunner()).dispatch(watch, self.live("cli"), [an_event(watch)])
        assert (outcome.action, outcome.ok) == (DispatchAction.NOTIFIED, True)
        assert self.programs(calls_log) == ["notify-send"]

    def test_a_watch_without_session_is_only_notified(
        self, commands: CommandsConfig, calls_log: Path, tmp_path: Path
    ) -> None:
        watch = a_watch(tmp_path, session=False)
        outcome = SessionDispatcher(commands, CommandRunner()).dispatch(watch, None, [an_event(watch)])
        assert outcome.detail == "no session registered, notified"
        assert self.programs(calls_log) == ["notify-send"]

    @pytest.mark.parametrize(
        ("terminal", "action"), [(True, DispatchAction.OPENED_TERMINAL), (False, DispatchAction.NOTIFIED)]
    )
    def test_without_vscode_a_closed_session_is_resumed_in_a_terminal_if_there_is_one(
        self, commands: CommandsConfig, calls_log: Path, tmp_path: Path, terminal: bool, action: DispatchAction
    ) -> None:
        missing = str(tmp_path / "missing")
        changed = commands.model_copy(
            update={"vscode": missing, "terminal": commands.terminal if terminal else missing}
        )
        watch = a_watch(tmp_path)
        outcome = SessionDispatcher(changed, CommandRunner()).dispatch(watch, None, [an_event(watch)])
        assert outcome.action == action
        if terminal:
            assert recorded_calls(calls_log)[0] == [
                "gnome-terminal",
                "--",
                commands.claude,
                "--resume",
                SESSION_ID,
                "/pr-watch GH-12",
            ]

    def test_a_failed_command_fails_the_dispatch(self, commands: CommandsConfig, tmp_path: Path) -> None:
        broken = commands.model_copy(update={"opener": str(write_program(tmp_path / "bin", "broken", "exit 4"))})
        watch = a_watch(tmp_path)
        outcome = SessionDispatcher(broken, CommandRunner()).dispatch(watch, None, [an_event(watch)])
        assert not outcome.ok
        assert "exited 4" in outcome.detail

    def test_a_reminder_names_the_waiting_events(
        self, commands: CommandsConfig, calls_log: Path, tmp_path: Path
    ) -> None:
        watch = a_watch(tmp_path)
        events = [an_event(watch, f"checks:{index}") for index in range(5)]
        outcome = SessionDispatcher(commands, CommandRunner()).remind(watch, events)
        assert outcome.detail == "5 events still waiting, reminded"
        assert "(+2 more)" in recorded_calls(calls_log)[0][-1]
