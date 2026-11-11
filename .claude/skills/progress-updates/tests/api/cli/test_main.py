from __future__ import annotations

import io
import json
from pathlib import Path

import pytest

from progress_updates.api.cli.main import main


class TestMain:
    def test_help_lists_the_three_commands(self, capsys: pytest.CaptureFixture[str]) -> None:
        with pytest.raises(SystemExit) as exit_info:
            main(["--help"])
        assert exit_info.value.code == 0
        help_text = capsys.readouterr().out
        for command in ("status", "watch", "hook"):
            assert command in help_text

    def test_status_prints_an_update_from_the_sources(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        tasks = tmp_path / "tasks"
        tasks.mkdir()
        (tasks / "b1.output").write_text("rendering batch 4\n", encoding="utf-8")
        code = main(
            ["status", "--sources", "background", "--tasks-dir", str(tasks), "--task", "research agent=running:read"]
        )
        out = capsys.readouterr().out
        assert code == 0
        assert "`research agent` (declared)" in out
        assert "`b1` (background)" in out
        assert out.rstrip().splitlines()[-1].startswith("**Summary:**")

    def test_watch_with_nothing_running_prints_the_final_line_at_once(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        tasks = tmp_path / "tasks"
        tasks.mkdir()
        assert main(["watch", "--every", "120", "--sources", "background", "--tasks-dir", str(tasks)]) == 0
        assert "nothing runs any more" in capsys.readouterr().out

    def test_watch_refuses_an_interval_under_2_minutes(self, capsys: pytest.CaptureFixture[str]) -> None:
        assert main(["watch", "--every", "30", "--sources", "background"]) == 2
        assert "120" in capsys.readouterr().err

    def test_the_hook_answers_a_background_command_with_a_reminder(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        payload = {"tool_name": "Bash", "tool_input": {"command": "sleep 300", "run_in_background": True}}
        monkeypatch.setattr("sys.stdin", io.StringIO(json.dumps(payload)))
        assert main(["hook"]) == 0
        answer = json.loads(capsys.readouterr().out)
        assert answer["hookSpecificOutput"]["hookEventName"] == "PostToolUse"
        assert "progress-updates" in answer["hookSpecificOutput"]["additionalContext"]

    def test_the_hook_says_nothing_and_never_fails_on_a_bad_payload(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        monkeypatch.setattr("sys.stdin", io.StringIO("not json"))
        assert main(["hook"]) == 0
        assert capsys.readouterr().out == ""
