from __future__ import annotations

import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from harness_core.shell.shell_command_splitter import ShellCommandSplitter
from tests.builders.git_sandbox import GitSandbox
from ticket_docs.service.hooks.git_invocations import GitInvocations
from ticket_docs.service.hooks.time_reminder import TimeReminder
from ticket_docs.service.paths.tickets_root import TicketsRoot


class TestTimeReminder:
    def reminder(self, command: str, cwd: Path, logger: logging.Logger) -> Optional[str]:
        invocations = GitInvocations(ShellCommandSplitter(logger), logger)
        return TimeReminder(invocations, TicketsRoot(logger), logger).reminder(command, cwd)

    def progress(self, sandbox: GitSandbox, stamp: datetime, status: str = "🔄 In progress") -> Path:
        path = sandbox.root / "docs" / "tickets" / "GH-1" / "PROGRESS.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"## Status\n\n| Step | Status | Started |\n|---|---|---|\n| 1 — x | {status} | {stamp:%Y-%m-%d %H:%M} |\n",
            encoding="utf-8",
        )
        return path

    def test_a_current_progress_needs_no_reminder(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        self.progress(sandbox, datetime.now())
        assert self.reminder("git commit -m 'x'", sandbox.root, logger) is None

    def test_a_stale_clock_reading_asks_for_the_times(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        path = self.progress(sandbox, datetime.now() - timedelta(minutes=40))
        reminder = self.reminder("git add -A && git commit -m 'x'", sandbox.root, logger)
        assert reminder is not None
        assert reminder.startswith("Time tracking of GH-1 is behind after this commit")
        assert "more than 15 minutes ago" in reminder
        assert str(path) in reminder
        assert "date '+%F %H:%M'" in reminder

    def test_no_running_step_asks_for_the_times(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        self.progress(sandbox, datetime.now(), "✅ Done")
        assert "no Status row is 🔄" in str(self.reminder("git commit -m x", sandbox.root, logger))

    def test_other_commands_branches_and_tickets_are_left_alone(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        assert self.reminder("git commit -m x", sandbox.root, logger) is None
        self.progress(sandbox, datetime.now() - timedelta(hours=2))
        assert self.reminder("git status", sandbox.root, logger) is None
        assert self.reminder("echo git commit", sandbox.root, logger) is None
        other = GitSandbox(tmp_path / "other", branch="develop")
        assert self.reminder("git commit -m x", other.root, logger) is None
