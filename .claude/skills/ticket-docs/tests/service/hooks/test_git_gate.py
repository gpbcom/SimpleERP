from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import pytest

from harness_core.git.git_repository import GitRepository
from harness_core.shell.shell_command_splitter import ShellCommandSplitter
from tests.builders.evidence_builder import EvidenceBuilder
from tests.builders.git_sandbox import GitSandbox
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.hooks.git_gate import GitGate
from ticket_docs.service.hooks.git_invocations import GitInvocations
from ticket_docs.service.paths.code_paths import CodePaths
from ticket_docs.service.paths.tickets_root import TicketsRoot
from ticket_docs.service.permits.squash_permits import SquashPermits
from ticket_docs.storage.permits.squash_permit_store import SquashPermitStore


class TestGitGate:
    RED = "❌ FAIL 0/1 (exit 1; 1 failures, 0 errors) — expected red (TDD), as expected"
    GREEN = "✅ PASS 1/1 (exit 0; 0 failures, 0 errors)"

    def refusal(self, command: str, cwd: Path, logger: logging.Logger) -> Optional[str]:
        rules = FolderRules.load(FolderRules.SKILL_DIR / "conf" / "folder-rules.yaml")
        catalog = GithubCatalog.load(GithubCatalog.SKILL_DIR / "conf" / "github.yaml")
        splitter = ShellCommandSplitter(logger)
        gate = GitGate(GitInvocations(splitter, logger), CodePaths(rules, logger), TicketsRoot(logger), catalog, logger)
        return gate.refusal(command, cwd)

    def evidence(self, sandbox: GitSandbox, name: str, commit: str, result: str, date: str) -> None:
        builder = EvidenceBuilder(sandbox.root / "docs" / "tickets", "GH-1")
        builder.folder(name, {"Commit": f"`{commit}` on `feature/GH-1-thing`", "Result": result, "Date": date})

    @pytest.mark.parametrize(
        "command",
        [
            "git push origin develop",
            "git push origin master",
            "git push -u origin HEAD:develop",
            "git push origin +feature/GH-1-thing:refs/heads/master",
            "git push --all origin",
            "git push --mirror origin",
            "git -C . push origin develop --force-with-lease",
            "cd . && git push origin develop",
        ],
    )
    def test_a_push_to_master_or_develop_is_refused(self, tmp_path: Path, logger: logging.Logger, command: str) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        reason = self.refusal(command, sandbox.root, logger)
        assert reason is not None
        assert reason.startswith("GIT-8")

    @pytest.mark.parametrize(
        "command",
        [
            "git push origin feature/GH-1-thing",
            "git push -u origin HEAD",
            "git push",
            "git push origin v1.0.0",
            "git push origin refs/tags/v1.0.0",
            "git push origin --tags",
            "echo git push origin develop",
            "git status && git log develop",
        ],
    )
    def test_other_pushes_and_commands_are_allowed(self, tmp_path: Path, logger: logging.Logger, command: str) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        assert self.refusal(command, sandbox.root, logger) is None

    @pytest.mark.parametrize("branch", ["develop", "master"])
    def test_a_bare_push_or_a_commit_on_a_protected_branch_is_refused(
        self, tmp_path: Path, logger: logging.Logger, branch: str
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo", branch="develop")
        if branch == "master":
            sandbox.git("switch", "-q", "-c", "master")
        assert str(self.refusal("git push", sandbox.root, logger)).startswith("GIT-8")
        assert self.refusal("git push origin --tags", sandbox.root, logger) is None
        reason = self.refusal("git commit -m 'x'", sandbox.root, logger)
        assert reason is not None
        assert reason.startswith("GIT-8")
        assert branch in reason

    def test_production_code_with_new_tests_in_one_commit_is_refused(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.write("src/a.py")
        sandbox.write("tests/test_a.py")
        sandbox.git("add", "src/a.py", "tests/test_a.py")
        reason = self.refusal("git commit -m 'feat'", sandbox.root, logger)
        assert reason is not None
        assert reason.startswith("TEST-7")
        assert "tests/test_a.py" in reason

    @pytest.fixture(autouse=True)
    def home(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
        home = tmp_path / "home"
        monkeypatch.setenv("HOME", str(home))
        return home

    def permit_file(self, home: Path) -> Path:
        return home / ".local" / "state" / "claude-harness" / "squash-permits" / "GH-1.json"

    def squashed(self, tmp_path: Path, logger: logging.Logger, extra: str = "") -> GitSandbox:
        sandbox = GitSandbox(tmp_path / "repo")
        base = sandbox.head()
        sandbox.commit("tests/test_a.py", message="test")
        sandbox.commit("src/a.py", message="feat")
        sandbox.git("reset", "-q", "--soft", base)
        rules = FolderRules.load(FolderRules.SKILL_DIR / "conf" / "folder-rules.yaml")
        permits = SquashPermits(SquashPermitStore.default(Path.home(), logger), rules, logger)
        permits.grant("GH-1", GitRepository(sandbox.root, logger))
        if extra:
            sandbox.write(extra)
            sandbox.git("add", extra)
        return sandbox

    def test_a_squash_with_a_matching_permit_is_allowed_once(
        self, tmp_path: Path, logger: logging.Logger, home: Path
    ) -> None:
        sandbox = self.squashed(tmp_path, logger)
        assert self.permit_file(home).is_file()
        assert self.refusal("git commit -m 'squash'", sandbox.root, logger) is None
        assert not self.permit_file(home).exists()
        assert str(self.refusal("git commit -m 'squash'", sandbox.root, logger)).startswith("TEST-7")

    def test_a_squash_that_differs_from_its_permit_is_refused(
        self, tmp_path: Path, logger: logging.Logger, home: Path
    ) -> None:
        sandbox = self.squashed(tmp_path, logger, extra="src/b.py")
        reason = self.refusal("git commit -m 'squash'", sandbox.root, logger)
        assert str(reason).startswith("TEST-7")
        assert self.permit_file(home).is_file()

    def test_a_squash_without_a_permit_is_refused(self, tmp_path: Path, logger: logging.Logger, home: Path) -> None:
        sandbox = self.squashed(tmp_path, logger)
        self.permit_file(home).unlink()
        reason = self.refusal("git commit -m 'squash'", sandbox.root, logger)
        assert str(reason).startswith("TEST-7")
        assert "allow-squash" in str(reason)

    @pytest.mark.parametrize(
        "command",
        [
            "ticket-docs allow-squash GH-1",
            ".claude/skills/.venv/bin/ticket-docs allow-squash GH-1",
            "/repo/bin/ticket-docs allow-squash GH-1",
            "uv run ticket-docs allow-squash GH-1",
            "python -m ticket_docs allow-squash GH-1",
            "bash -c 'ticket-docs allow-squash GH-1'",
            "env -u X ticket-docs allow-squash GH-1",
            "cd /tmp && ticket-docs allow-squash GH-1 < answer.txt",
            "echo '{}' > ~/.local/state/claude-harness/squash-permits/GH-1.json",
            "cp permit.json ~/.local/state/claude-harness/squash-permits/GH-1.json",
            "tee $HOME/.local/state/claude-harness/squash-permits/GH-1.json < permit.json",
            "python3 -c \"open('/home/u/.local/state/claude-harness/squash-permits/GH-1.json', 'w')\"",
            "git commit -m 'explain ticket-docs allow-squash'",
            "git -c alias.x='!ticket-docs allow-squash GH-1' x",
            "python3 -c \"import subprocess; subprocess.run(['ticket-docs', 'allow-squash', 'GH-1'])\"",
            "cat ~/.local/state/ai-test-cost/GH-1.json",
            "echo '{}' > $HOME/.local/state/ai-test-cost/GH-1.json",
        ],
    )
    def test_a_claude_session_neither_grants_nor_writes_a_squash_permit(
        self, tmp_path: Path, logger: logging.Logger, command: str
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        assert str(self.refusal(command, sandbox.root, logger)).startswith("TEST-7")

    @pytest.mark.parametrize(
        "command",
        [
            "ticket-docs check GH-1",
            "git commit -m 'grant the squash permit'",
            "echo allow squash",
            "cd .claude/skills/ai-test-cost && ls",
        ],
    )
    def test_commands_that_only_mention_the_permit_pass(
        self, tmp_path: Path, logger: logging.Logger, command: str
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        assert self.refusal(command, sandbox.root, logger) is None

    @pytest.mark.parametrize(
        "command",
        [
            "git commit -i -m 'squash'",
            "git commit --include -m 'squash'",
            "git commit -o -m 'squash'",
            "git commit --only -m 'squash'",
            "git commit --interactive",
            "git commit -p -m 'squash'",
            "git commit --patch -m 'squash'",
            "git commit -qpm 'squash'",
            "git commit -vi -m 'squash'",
            "git commit --pathspec-from-file=list.txt -m 'squash'",
            "git commit --pathspec-from-file list.txt -m 'squash'",
            "git rm -q --cached README.md && git commit -m 'squash'",
            "git apply fix.diff && git commit -m 'squash'",
            "git read-tree HEAD; git commit -m 'squash'",
            "git restore --staged README.md && git commit -m 'squash'",
            "git mv README.md READ.md && git commit -m 'squash'",
            "git checkout -- README.md && git commit -m 'squash'",
            "git switch -q other && git commit -m 'squash'",
            "git stash && git commit -m 'squash'",
            "git reset -q && git commit -m 'squash'",
            "git update-index --add src/b.py && git commit -m 'squash'",
            "git merge other && git commit -m 'squash'",
            "git cherry-pick abc && git commit -m 'squash'",
            "git revert abc && git commit -m 'squash'",
            "git commit -m 'squash' && git reset -q",
        ],
    )
    def test_a_squash_with_another_way_to_change_what_is_committed_is_not_exempted(
        self, tmp_path: Path, logger: logging.Logger, command: str
    ) -> None:
        sandbox = self.squashed(tmp_path, logger)
        assert str(self.refusal(command, sandbox.root, logger)).startswith("TEST-7")

    @pytest.mark.parametrize(
        "command",
        [
            "git status && git commit -m 'squash'",
            "git log -1 && git diff --cached --stat && git commit -m 'squash'",
            "git commit -q -m 'squash'",
            "git commit -m 'squash -p --only'",
            "git commit -mpatch",
        ],
    )
    def test_a_squash_with_read_only_commands_around_it_is_still_exempted(
        self, tmp_path: Path, logger: logging.Logger, command: str
    ) -> None:
        sandbox = self.squashed(tmp_path, logger)
        assert self.refusal(command, sandbox.root, logger) is None

    def test_production_code_without_a_red_run_is_refused(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.write("src/a.py")
        sandbox.git("add", "src/a.py")
        reason = self.refusal("git commit -m 'feat'", sandbox.root, logger)
        assert reason is not None
        assert reason.startswith("TEST-7")
        assert "red run" in reason

    def test_production_code_after_a_red_run_on_this_branch_is_allowed(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        tests = sandbox.commit("tests/test_a.py")
        self.evidence(sandbox, "local-2026-11-10-unit-old", tests, self.GREEN, "2026-11-10 09:00")
        self.evidence(sandbox, "local-2026-11-10-tdd-red-a", tests, self.RED, "2026-11-10 10:00")
        sandbox.write("src/a.py")
        sandbox.write("tests/test_a.py", "x = 2\n")
        sandbox.git("add", "src/a.py", "tests/test_a.py")
        assert self.refusal("git commit -m 'feat'", sandbox.root, logger) is None

    @pytest.mark.parametrize(
        ("red_result", "red_date", "red_on_branch"),
        [
            (RED, "2026-11-10 08:00", True),
            ("⚠️ INVALID: no html", "2026-11-10 10:00", True),
            (RED, "2026-11-10 10:00", False),
        ],
    )
    def test_a_red_run_older_than_the_last_green_invalid_or_elsewhere_does_not_count(
        self, tmp_path: Path, logger: logging.Logger, red_result: str, red_date: str, red_on_branch: bool
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        tests = sandbox.commit("tests/test_a.py")
        red = tests if red_on_branch else "f" * 40
        self.evidence(sandbox, "local-2026-11-10-unit-old", tests, self.GREEN, "2026-11-10 09:00")
        self.evidence(sandbox, "local-2026-11-10-tdd-red-a", red, red_result, red_date)
        sandbox.write("src/a.py")
        sandbox.git("add", "src/a.py")
        assert str(self.refusal("git commit -m 'feat'", sandbox.root, logger)).startswith("TEST-7")

    @pytest.mark.parametrize(
        "command", ["git add -A && git commit -m 'x'", "git commit -am 'x'", "git commit src/a.py"]
    )
    def test_files_about_to_be_added_count_as_committed(
        self, tmp_path: Path, logger: logging.Logger, command: str
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.commit("src/a.py")
        sandbox.write("src/a.py", "x = 2\n")
        assert str(self.refusal(command, sandbox.root, logger)).startswith("TEST-7")

    @pytest.mark.parametrize("branch", ["worktree-agent-x", "release/1.0.0"])
    def test_branches_without_ticket_work_are_not_held_to_test_7(
        self, tmp_path: Path, logger: logging.Logger, branch: str
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo", branch=branch)
        sandbox.write("src/a.py")
        sandbox.git("add", "src/a.py")
        assert self.refusal("git commit -m 'x'", sandbox.root, logger) is None

    def test_tests_and_docs_alone_are_allowed(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.write("tests/test_a.py")
        sandbox.write("README.md", "docs\n")
        sandbox.git("add", "tests/test_a.py", "README.md")
        assert self.refusal("git commit -m 'test'", sandbox.root, logger) is None

    def test_a_folder_outside_any_repository_is_left_alone(self, tmp_path: Path, logger: logging.Logger) -> None:
        assert self.refusal("git push origin develop", tmp_path, logger) is None

    def docs_staged_code_unstaged(self, tmp_path: Path) -> GitSandbox:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.commit("src/a.py")
        sandbox.write("src/a.py", "x = 2\n")
        sandbox.write("docs/notes.md", "notes\n")
        sandbox.git("add", "docs/notes.md")
        return sandbox

    @pytest.mark.parametrize(
        "command",
        [
            "git commit --inc -m 'docs'",
            "git commit --includ -m 'docs'",
            "git commit --interact",
            "git commit --onl -m 'docs'",
            "git commit --pat -m 'docs'",
            "git commit --al -m 'docs'",
            "git commit --bogus -m 'docs'",
            "git commit --pathspec-f=list.txt -m 'docs'",
        ],
    )
    def test_an_abbreviated_ambiguous_or_unknown_long_option_counts_the_working_tree(
        self, tmp_path: Path, logger: logging.Logger, command: str
    ) -> None:
        sandbox = self.docs_staged_code_unstaged(tmp_path)
        assert str(self.refusal(command, sandbox.root, logger)).startswith("TEST-7")

    @pytest.mark.parametrize(
        "command",
        [
            "git commit -m 'docs'",
            "git commit --mess 'docs'",
            "git commit --no-verify -m 'docs'",
            "git commit --message='docs' --quiet",
        ],
    )
    def test_a_commit_of_the_index_alone_leaves_unstaged_code_out(
        self, tmp_path: Path, logger: logging.Logger, command: str
    ) -> None:
        sandbox = self.docs_staged_code_unstaged(tmp_path)
        assert self.refusal(command, sandbox.root, logger) is None

    @pytest.mark.parametrize(
        "command",
        [
            "git restore --staged docs/other.md && git commit -m 'docs'",
            "git rm -q --cached docs/notes.md && git commit -m 'docs'",
            "git update-index --add docs/notes.md && git commit -m 'docs'",
            "git mv docs/notes.md docs/n.md && git commit -m 'docs'",
        ],
    )
    def test_an_index_writer_on_the_line_counts_every_working_tree_change(
        self, tmp_path: Path, logger: logging.Logger, command: str
    ) -> None:
        sandbox = self.docs_staged_code_unstaged(tmp_path)
        assert str(self.refusal(command, sandbox.root, logger)).startswith("TEST-7")

    def test_the_paths_an_index_writer_names_count_as_committed(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.commit("src/a.py")
        sandbox.write("tests/test_b.py")
        sandbox.git("add", "tests/test_b.py")
        reason = self.refusal("git rm -q --cached src/a.py && git commit -m 'x'", sandbox.root, logger)
        assert str(reason).startswith("TEST-7")

    @pytest.mark.parametrize(
        "writer", ["apply fix.diff", "read-tree HEAD", "stash", "reset -q", "merge other", "checkout other"]
    )
    def test_an_index_writer_whose_effect_cannot_be_computed_must_run_apart(
        self, tmp_path: Path, logger: logging.Logger, writer: str
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.write("docs/notes.md", "notes\n")
        sandbox.git("add", "docs/notes.md")
        reason = self.refusal(f"git {writer} && git commit -m 'docs'", sandbox.root, logger)
        assert str(reason).startswith("TEST-7")
        assert "separate" in str(reason)

    @pytest.mark.parametrize(("branch", "refused"), [("feature/GH-1-thing", True), ("develop", False)])
    def test_commands_that_write_commits_or_refs_are_refused_on_a_ticket_branch(
        self, tmp_path: Path, logger: logging.Logger, branch: str, refused: bool
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo", branch=branch)
        for command in ["git commit-tree HEAD^{tree} -m forged", "git update-ref refs/heads/x HEAD"]:
            reason = self.refusal(command, sandbox.root, logger)
            assert (reason is not None and reason.startswith("TEST-7")) == refused
