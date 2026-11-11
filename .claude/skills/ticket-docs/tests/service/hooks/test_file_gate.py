from __future__ import annotations

import logging
from pathlib import Path

import pytest

from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.hooks.file_gate import FileGate


class TestFileGate:
    @pytest.fixture
    def home(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
        home = tmp_path / "home"
        (home / ".local" / "state" / "ai-test-cost").mkdir(parents=True)
        (home / ".local" / "state" / "claude-harness" / "logs").mkdir(parents=True)
        monkeypatch.setenv("HOME", str(home))
        return home

    def gate(self, logger: logging.Logger) -> FileGate:
        return FileGate(FolderRules.load(FolderRules.SKILL_DIR / "conf" / "folder-rules.yaml"), logger)

    @pytest.mark.parametrize(
        "path",
        [
            "~/.local/state/claude-harness/squash-permits/GH-1.json",
            "{home}/.local/state/ai-test-cost/GH-1.json",
            "{home}/.local/state/claude-harness/logs/../squash-permits/GH-1.json",
            "ai-test-cost/GH-1.json",
            "{tmp}/link/GH-1.json",
            "~/.local/state/claude-harness/squash-permits",
        ],
    )
    def test_a_file_in_a_guard_state_folder_is_refused(
        self, tmp_path: Path, home: Path, logger: logging.Logger, path: str
    ) -> None:
        (tmp_path / "link").symlink_to(home / ".local" / "state" / "ai-test-cost")
        cwd = home / ".local" / "state"
        reason = self.gate(logger).refusal(path.format(home=home, tmp=tmp_path), cwd)
        assert reason is not None
        assert reason.startswith("TEST-")

    @pytest.mark.parametrize(
        "path",
        [
            "{home}/.local/state/claude-harness/logs/ticket-docs.log",
            "~/.local/state/ai-test-cost-other/x.json",
            "src/a.py",
            "/repo/.claude/skills/ai-test-cost/conf/settings.yaml",
        ],
    )
    def test_any_other_file_is_allowed(self, tmp_path: Path, home: Path, logger: logging.Logger, path: str) -> None:
        assert self.gate(logger).refusal(path.format(home=home), tmp_path) is None
