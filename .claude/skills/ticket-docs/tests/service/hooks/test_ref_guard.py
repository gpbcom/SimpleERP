from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import pytest

from harness_core.git.git_repository import GitRepository
from harness_core.shell.shell_command_splitter import ShellCommandSplitter
from tests.builders.git_sandbox import GitSandbox
from ticket_docs.service.hooks.git_invocations import GitInvocations
from ticket_docs.service.hooks.ref_guard import RefGuard


class TestRefGuard:
    def refusal(self, command: str, sandbox: GitSandbox, logger: logging.Logger) -> Optional[str]:
        guard = RefGuard(logger)
        call = GitInvocations(ShellCommandSplitter(logger), logger).calls(command, sandbox.root)[0]
        return guard.refusal(call, GitRepository(sandbox.root, logger))

    @pytest.fixture
    def sandbox(self, tmp_path: Path) -> GitSandbox:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.commit("docs/a.md")
        return sandbox

    @pytest.mark.parametrize(
        "command",
        [
            "git commit-tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904 -m forged",
            "git update-ref refs/heads/feature/GH-1-thing HEAD",
            "git update-ref -d refs/forged",
            "git update-ref --stdin",
            "git replace aaaa bbbb",
            "git replace -d aaaa",
            "git replace --edit HEAD",
            "git replace --graft HEAD",
            "git hash-object -w README.md",
            "git hash-object --stdin -w",
            "git branch -f feature/GH-1-thing HEAD~1",
            "git branch --force feature/GH-1-thing",
            "git branch -fq feature/GH-1-thing",
            "git branch -C other feature/GH-1-thing",
            "git branch -M other feature/GH-1-thing",
            'git reset --soft "$(git merge-base HEAD origin/develop)"',
            "git reset --hard `cat sha.txt`",
        ],
    )
    def test_a_command_that_writes_commits_or_moves_the_branch_is_refused(
        self, sandbox: GitSandbox, logger: logging.Logger, command: str
    ) -> None:
        reason = self.refusal(command, sandbox, logger)
        assert reason is not None
        assert reason.startswith("TEST-7")

    @pytest.mark.parametrize(
        "command",
        [
            "git commit-tree -h",
            "git update-ref -h",
            "git replace",
            "git replace -l",
            "git replace --list 'a*'",
            "git replace --format=short -l",
            "git hash-object README.md",
            "git hash-object --stdin",
            "git branch -f other HEAD",
            "git branch -D other",
            "git branch --show-current",
            "git branch new-one",
            "git reset",
            "git reset -q -- README.md",
            "git reset README.md",
            "git reset --hard HEAD",
            "git reset --soft HEAD~1",
            "git reset --hard origin/develop",
        ],
    )
    def test_reading_forms_and_moves_within_the_branch_history_are_allowed(
        self, sandbox: GitSandbox, logger: logging.Logger, command: str
    ) -> None:
        assert self.refusal(command, sandbox, logger) is None

    def test_a_reset_onto_a_commit_outside_the_branch_history_is_refused(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        forged = sandbox.git("commit-tree", sandbox.git("write-tree"), "-p", sandbox.head(), "-m", "forged")
        assert str(self.refusal(f"git reset --hard {forged}", sandbox, logger)).startswith("TEST-7")
