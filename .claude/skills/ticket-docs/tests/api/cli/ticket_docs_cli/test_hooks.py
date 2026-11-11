from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Tuple

import pytest

from harness_core.terminal.human_confirmation import HumanConfirmation
from harness_core.testing.scripted_confirmation import ScriptedConfirmation
from tests.api.cli.ticket_docs_cli.helpers import call
from tests.builders.git_sandbox import GitSandbox


class TestHooks:
    def hook(self, command: str, cwd: Path) -> str:
        return json.dumps({"session_id": "s", "tool_name": "Bash", "tool_input": {"command": command}, "cwd": str(cwd)})

    def test_the_gate_refuses_as_the_hook_expects(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        code, out, err = call(["git-gate"], tmp_path, self.hook("git push origin develop", sandbox.root))
        answer = json.loads(out)["hookSpecificOutput"]
        assert (code, err) == (0, "")
        assert answer["hookEventName"] == "PreToolUse"
        assert answer["permissionDecision"] == "deny"
        assert answer["permissionDecisionReason"].startswith("GIT-8")

    @pytest.mark.parametrize(
        "payload",
        ["", "not json", "[]", "{}", '{"tool_input": {"command": "git push origin develop"}, "cwd": "/no/such/dir"}'],
    )
    def test_the_gate_never_fails_and_says_nothing_when_it_allows(self, tmp_path: Path, payload: str) -> None:
        assert call(["git-gate"], tmp_path, payload) == (0, "", "")

    def test_the_gate_allows_a_harmless_command(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        assert call(["git-gate"], tmp_path, self.hook("git status", sandbox.root)) == (0, "", "")

    @pytest.mark.parametrize("folder", ["claude-harness/squash-permits", "ai-test-cost"])
    def test_the_file_gate_refuses_a_file_tool_in_a_guard_state_folder(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, folder: str
    ) -> None:
        monkeypatch.setenv("HOME", str(tmp_path / "home"))
        target = tmp_path / "home" / ".local" / "state" / folder / "GH-1.json"
        payload = json.dumps({"tool_name": "Write", "tool_input": {"file_path": str(target)}, "cwd": str(tmp_path)})
        code, out, err = call(["file-gate"], tmp_path, payload)
        answer = json.loads(out)["hookSpecificOutput"]
        assert (code, err) == (0, "")
        assert answer["permissionDecision"] == "deny"
        assert answer["permissionDecisionReason"].startswith("TEST-")

    @pytest.mark.parametrize(
        "payload",
        ["", "{}", '{"tool_input": {"file_path": "src/a.py"}}', '{"tool_input": {"notebook_path": "/repo/n.ipynb"}}'],
    )
    def test_the_file_gate_never_fails_and_says_nothing_when_it_allows(self, tmp_path: Path, payload: str) -> None:
        assert call(["file-gate"], tmp_path, payload) == (0, "", "")

    def test_the_time_reminder_adds_context_after_a_commit(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        progress = sandbox.write(
            "docs/tickets/GH-1/PROGRESS.md",
            f"| 1 — x | 🔄 In progress | {datetime.now() - timedelta(hours=1):%Y-%m-%d %H:%M} |\n",
        )
        code, out, _ = call(["time-reminder"], tmp_path, self.hook("git commit -m x", sandbox.root))
        answer = json.loads(out)["hookSpecificOutput"]
        assert code == 0
        assert answer["hookEventName"] == "PostToolUse"
        assert str(progress) in answer["additionalContext"]

    @pytest.mark.parametrize("payload", ["", "{}", '{"tool_input": {"command": "git commit"}, "cwd": "/no/such"}'])
    def test_the_time_reminder_never_fails(self, tmp_path: Path, payload: str) -> None:
        assert call(["time-reminder"], tmp_path, payload) == (0, "", "")

    def staged_squash(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Tuple[GitSandbox, Path]:
        monkeypatch.setenv("HOME", str(tmp_path / "home"))
        sandbox = GitSandbox(tmp_path / "repo")
        base = sandbox.head()
        sandbox.commit("tests/test_a.py")
        sandbox.commit("src/a.py")
        sandbox.git("reset", "-q", "--soft", base)
        return sandbox, tmp_path / "home" / ".local" / "state" / "claude-harness" / "squash-permits" / "GH-1.json"

    def test_the_human_grants_a_squash_permit_by_typing_the_ticket_back(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        sandbox, permit = self.staged_squash(tmp_path, monkeypatch)
        human = ScriptedConfirmation(True)
        code, out, err = call(["allow-squash", "GH-1"], sandbox.root, confirmation=human)
        assert (code, err) == (0, "")
        assert "GH-1" in human.questions[0]
        assert str(permit) in out
        assert json.loads(permit.read_text(encoding="utf-8"))["tree"] == sandbox.git("write-tree")

    @pytest.mark.parametrize("terminal", [True, False])
    def test_no_permit_without_a_terminal_or_the_code_typed_back(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, terminal: bool
    ) -> None:
        sandbox, permit = self.staged_squash(tmp_path, monkeypatch)
        human = ScriptedConfirmation(False) if terminal else HumanConfirmation(tmp_path / "no-tty")
        code, _, err = call(["allow-squash", "GH-1"], sandbox.root, confirmation=human)
        assert code == 1
        assert err.startswith("ticket-docs:")
        assert not permit.exists()

    def test_no_permit_on_a_branch_of_another_ticket(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        sandbox, permit = self.staged_squash(tmp_path, monkeypatch)
        code, _, _ = call(["allow-squash", "GH-2"], sandbox.root, confirmation=ScriptedConfirmation(True))
        assert code == 1
        assert not permit.with_name("GH-2.json").exists()
