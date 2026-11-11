from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from pr_watch.storage.desktop.command_runner import CommandRunner
from pr_watch.storage.sessions.session_directory import SessionDirectory
from tests.stand_ins.helpers import PR_URL, SESSION_ID, write_program


class TestSessionDirectory:
    @pytest.fixture
    def home(self, tmp_path: Path) -> Path:
        sessions = tmp_path / "claude" / "sessions"
        sessions.mkdir(parents=True)
        alive = {"pid": os.getpid(), "sessionId": SESSION_ID, "cwd": "/repo", "entrypoint": "claude-vscode"}
        dead = {"pid": 999_999_999, "sessionId": "dead", "cwd": "/repo", "entrypoint": "cli"}
        (sessions / "1.json").write_text(json.dumps(alive), encoding="utf-8")
        (sessions / "2.json").write_text(json.dumps(dead), encoding="utf-8")
        (sessions / "3.json").write_text("{not json", encoding="utf-8")
        return tmp_path / "claude"

    def directory(self, home: Path, claude: Path) -> SessionDirectory:
        return SessionDirectory(home, str(claude), CommandRunner())

    def test_live_sessions_come_from_claude_agents_with_where_they_run(self, home: Path, tmp_path: Path) -> None:
        agents = json.dumps([{"sessionId": SESSION_ID, "pid": os.getpid(), "cwd": "/repo", "status": "busy"}])
        claude = write_program(tmp_path / "bin", "claude", f"printf '%s' '{agents}'")
        live = self.directory(home, claude).live()
        assert list(live) == [SESSION_ID]
        assert live[SESSION_ID].in_vscode
        assert live[SESSION_ID].status == "busy"

    def test_the_sessions_folder_stands_alone_when_claude_agents_fails(self, home: Path, tmp_path: Path) -> None:
        claude = write_program(tmp_path / "bin", "claude", "exit 1")
        assert list(self.directory(home, claude).live()) == [SESSION_ID]

    def test_a_session_is_described_only_while_its_process_runs(self, home: Path, tmp_path: Path) -> None:
        directory = self.directory(home, tmp_path / "missing")
        described = directory.describe(SESSION_ID)
        assert described is not None
        assert described.cwd == "/repo"
        assert directory.describe("dead") is None

    def test_candidates_are_the_transcripts_whose_last_title_names_the_ticket(self, home: Path, tmp_path: Path) -> None:
        project = home / "projects" / "-repo"
        project.mkdir(parents=True)
        lines = [
            {"type": "user", "cwd": "/repo", "message": "GH-12"},
            {"type": "ai-title", "aiTitle": "GH-12 add customers"},
        ]
        (project / "aaa.jsonl").write_text("\n".join(json.dumps(line) for line in lines), encoding="utf-8")
        with_link = [*lines, {"type": "user", "cwd": "/repo", "message": PR_URL}]
        (project / "bbb.jsonl").write_text("\n".join(json.dumps(line) for line in with_link), encoding="utf-8")
        renamed = [*lines, {"type": "custom-title", "customTitle": "something else"}]
        (project / "ccc.jsonl").write_text("\n".join(json.dumps(line) for line in renamed), encoding="utf-8")
        found = self.directory(home, tmp_path / "missing").candidates("GH-12", PR_URL)
        assert [(item.session_id, item.mentions_pr, item.cwd) for item in found] == [
            ("bbb", True, "/repo"),
            ("aaa", False, "/repo"),
        ]
