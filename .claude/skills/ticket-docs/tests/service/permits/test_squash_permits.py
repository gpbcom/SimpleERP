from __future__ import annotations

import logging
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

from harness_core.git.git_repository import GitRepository
from tests.builders.git_sandbox import GitSandbox
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.models.permits.squash_permit import SquashPermit
from ticket_docs.service.permits.squash_permits import SquashPermits
from ticket_docs.storage.permits.squash_permit_store import SquashPermitStore


class TestSquashPermits:
    def permits(self, tmp_path: Path, logger: logging.Logger) -> SquashPermits:
        rules = FolderRules.load(FolderRules.SKILL_DIR / "conf" / "folder-rules.yaml")
        return SquashPermits(SquashPermitStore(tmp_path / "permits", logger), rules, logger)

    def staged_squash(self, tmp_path: Path) -> GitSandbox:
        sandbox = GitSandbox(tmp_path / "repo")
        base = sandbox.head()
        sandbox.commit("tests/test_a.py")
        sandbox.commit("src/a.py")
        sandbox.git("reset", "-q", "--soft", base)
        return sandbox

    def test_a_permit_records_the_branch_head_and_staged_tree_for_thirty_minutes(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        sandbox = self.staged_squash(tmp_path)
        before = datetime.now(UTC)
        permit = self.permits(tmp_path, logger).grant("GH-1", GitRepository(sandbox.root, logger))
        assert permit is not None
        assert (permit.ticket, permit.branch, permit.head) == ("GH-1", "feature/GH-1-thing", sandbox.head())
        assert permit.tree == sandbox.git("write-tree")
        assert before + timedelta(minutes=29) < permit.expires_at <= datetime.now(UTC) + timedelta(minutes=30)
        assert (tmp_path / "permits" / "GH-1.json").is_file()

    @pytest.mark.parametrize("branch", ["feature/GH-2-other", "develop", "worktree-agent-x"])
    def test_no_permit_is_granted_on_a_branch_that_does_not_carry_the_ticket(
        self, tmp_path: Path, logger: logging.Logger, branch: str
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo", branch=branch)
        assert self.permits(tmp_path, logger).grant("GH-1", GitRepository(sandbox.root, logger)) is None
        assert not (tmp_path / "permits" / "GH-1.json").exists()

    def test_a_matching_permit_is_redeemed_once(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = self.staged_squash(tmp_path)
        permits = self.permits(tmp_path, logger)
        repository = GitRepository(sandbox.root, logger)
        permits.grant("GH-1", repository)
        assert permits.redeem("GH-1", repository) is True
        assert not (tmp_path / "permits" / "GH-1.json").exists()
        assert permits.redeem("GH-1", repository) is False

    @pytest.mark.parametrize("change", ["tree", "head", "branch", "expired", "ticket"])
    def test_a_permit_that_does_not_match_exactly_is_not_redeemed(
        self, tmp_path: Path, logger: logging.Logger, change: str
    ) -> None:
        sandbox = self.staged_squash(tmp_path)
        permits = self.permits(tmp_path, logger)
        repository = GitRepository(sandbox.root, logger)
        permit = permits.grant("GH-1", repository)
        assert permit is not None
        store = SquashPermitStore(tmp_path / "permits", logger)
        match change:
            case "tree":
                sandbox.write("src/b.py")
                sandbox.git("add", "src/b.py")
            case "head":
                store.write(permit.model_copy(update={"head": "c" * 40}))
            case "branch":
                store.write(permit.model_copy(update={"branch": "feature/GH-1-other"}))
            case "expired":
                store.write(permit.model_copy(update={"expires_at": datetime.now(UTC) - timedelta(seconds=1)}))
            case _:
                other = SquashPermit.model_validate({**permit.model_dump(), "ticket": "GH-2"})
                store.path("GH-1").write_text(other.model_dump_json(), encoding="utf-8")
        assert permits.redeem("GH-1", repository) is False
