from __future__ import annotations

import logging
from pathlib import Path

from harness_core.git.git_repository import GitRepository
from tests.builders.evidence_builder import EvidenceBuilder
from tests.builders.git_sandbox import GitSandbox
from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.checks.evidence.tdd_check import TddCheck
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_folder import TicketFolder
from ticket_docs.service.paths.code_paths import CodePaths


class TestTddCheck:
    RED = "❌ FAIL 0/2 (exit 1; 2 failures, 0 errors) — expected red (TDD), as expected"
    GREEN = "✅ PASS 2/2 (exit 0; 0 failures, 0 errors)"

    def check(
        self, sandbox: GitSandbox, rules: FolderRules, tables: MarkdownTables, logger: logging.Logger
    ) -> TddCheck:
        return TddCheck(GitRepository(sandbox.root, logger), CodePaths(rules, logger), tables, logger)

    def runs(self, ticket: TicketBuilder, red: str, green: str, red_result: str = RED) -> None:
        builder = EvidenceBuilder(ticket.tickets, "GH-7")
        builder.folder("local-2026-11-10-tdd-red-storage", {"Commit": f"`{red}` on `x`", "Result": red_result})
        builder.folder("local-2026-11-10-unit-storage", {"Commit": f"`{green}` on `x`", "Result": self.GREEN})

    def sandbox(self, tickets: Path) -> GitSandbox:
        return GitSandbox(tickets.parents[1])

    def test_tests_first_then_code_on_top_is_proven(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        tickets: Path,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        sandbox = self.sandbox(tickets)
        red = sandbox.commit("tests/test_storage.py")
        green = sandbox.commit("src/storage.py")
        self.runs(ticket, red, green)
        assert self.check(sandbox, rules, tables, logger).problems(folder) == []

    def test_a_red_run_that_passed_or_touched_code_is_refused(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        tickets: Path,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        sandbox = self.sandbox(tickets)
        sandbox.write("tests/test_storage.py")
        red = sandbox.commit(".claude/skills/tool/src/tool/storage.py")
        self.runs(ticket, red, red, self.GREEN + " — expected red (TDD), UNEXPECTED GREEN")
        assert self.check(sandbox, rules, tables, logger).problems(folder) == [
            "GH-7/tests-evidences/local-2026-11-10-tdd-red-storage: the red run did not fail (TEST-7)",
            f"GH-7/tests-evidences/local-2026-11-10-tdd-red-storage: the red commit {red[:7]} touches production "
            "code: .claude/skills/tool/src/tool/storage.py (TEST-7)",
        ]

    def test_a_green_run_that_does_not_descend_from_the_red_one_is_refused(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        tickets: Path,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        sandbox = self.sandbox(tickets)
        green = sandbox.commit("src/storage.py")
        red = sandbox.commit("tests/test_storage.py")
        self.runs(ticket, red, green)
        assert self.check(sandbox, rules, tables, logger).problems(folder) == [
            f"GH-7/tests-evidences/local-2026-11-10-unit-storage: its commit {green[:7]} does not descend from "
            f"the red run's commit {red[:7]} (TEST-7)"
        ]

    def test_an_unknown_commit_is_looked_for_in_the_history_bundles(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        tickets: Path,
        tmp_path: Path,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        sandbox = self.sandbox(tickets)
        other = GitSandbox(tmp_path / "elsewhere")
        other.git("fetch", "-q", str(sandbox.root), "+develop:refs/remotes/origin/develop")
        other.git("reset", "-q", "--hard", "origin/develop")
        red = other.commit("tests/test_storage.py")
        green = other.commit("src/storage.py")
        self.runs(ticket, red, green)
        missing = self.check(sandbox, rules, tables, logger).problems(folder)
        assert missing == [
            f"GH-7/tests-evidences/local-2026-11-10-tdd-red-storage: commit {red[:7]} is neither in the repository "
            "nor in tests-evidences/history (TEST-7)",
            f"GH-7/tests-evidences/local-2026-11-10-unit-storage: commit {green[:7]} is neither in the repository "
            "nor in tests-evidences/history (TEST-7)",
        ]
        history = ticket.folder / "tests-evidences" / "history"
        GitRepository(other.root, logger).create_bundle(
            history / "pre-squash-20261110-1200.bundle", "origin/develop", "HEAD"
        )
        assert self.check(sandbox, rules, tables, logger).problems(folder) == []
        assert sandbox.git("for-each-ref", "--format=%(refname)", "refs/ticket-history/GH-7") != ""

    def test_invalid_red_runs_are_ignored_and_retries_match_their_green_run(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        tickets: Path,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        sandbox = self.sandbox(tickets)
        red = sandbox.commit("tests/test_storage.py")
        green = sandbox.commit("src/storage.py")
        builder = EvidenceBuilder(ticket.tickets, "GH-7")
        builder.folder("local-2026-11-10-tdd-red-guard", {"Commit": f"`{green}` on `x`", "Result": "⚠️ INVALID: x"})
        builder.folder("local-2026-11-10-tdd-red-guard-2", {"Commit": f"`{red}` on `x`", "Result": self.RED})
        builder.folder("local-2026-11-10-unit-guard", {"Commit": f"`{red}` on `x`", "Result": self.GREEN})
        assert self.check(sandbox, rules, tables, logger).problems(folder) == []

    def test_a_red_run_claimed_in_the_log_needs_its_folder(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        tickets: Path,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        sandbox = self.sandbox(tickets)
        ticket.edit("PROGRESS.md", "⬜ 🔴 red run", "✅ 🔴 red run")
        assert self.check(sandbox, rules, tables, logger).problems(folder) == [
            "GH-7/PROGRESS.md: step 'Step 1 — Customer storage (2026-11-10) 🔄' claims a red run without a link "
            "to its tdd-red folder (TEST-7)"
        ]
        red = sandbox.commit("tests/test_storage.py")
        EvidenceBuilder(ticket.tickets, "GH-7").folder(
            "local-2026-11-10-tdd-red-storage", {"Commit": f"`{red}` on `x`", "Result": self.RED}
        )
        link = "([red](tests-evidences/local-2026-11-10-tdd-red-storage/README.md))"
        ticket.edit("PROGRESS.md", "✅ 🔴 red run", f"✅ 🔴 red run {link}")
        assert self.check(sandbox, rules, tables, logger).problems(folder) == []

    def test_without_a_repository_the_commits_cannot_be_checked(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        self.runs(ticket, "1" * 40, "2" * 40)
        check = TddCheck(None, CodePaths(rules, logger), tables, logger)
        assert check.problems(folder) == [
            "GH-7: the tickets folder is not in a git repository, so the TDD commits cannot be checked (TEST-7)"
        ]
