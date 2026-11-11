from __future__ import annotations

import json
import logging
import zipfile
from pathlib import Path

import pytest

from harness_core.git.git_repository import GitRepository
from tests.builders.fake_gh import FakeGh
from tests.builders.git_sandbox import GitSandbox
from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.github.evidence_archiver import EvidenceArchiver
from ticket_docs.service.github.exceptions import SETicketFolderMissingError
from ticket_docs.storage.github.gh_client import GhClient
from ticket_docs.storage.tickets.ticket_repository import TicketRepository


class TestEvidenceArchiver:
    REPO = "gpbcom/simple-erp"

    def archiver(self, sandbox: GitSandbox, tmp_path: Path, logger: logging.Logger, dry_run: bool) -> EvidenceArchiver:
        catalog = GithubCatalog.load(GithubCatalog.SKILL_DIR / "conf" / "github.yaml")
        return EvidenceArchiver(
            TicketRepository(sandbox.root / "docs" / "tickets", logger),
            GhClient(self.REPO, dry_run=dry_run, logger=logger),
            catalog,
            GitRepository(sandbox.root, logger),
            tmp_path / "scratch",
            logger,
        )

    def sandbox(self, tmp_path: Path) -> GitSandbox:
        sandbox = GitSandbox(tmp_path / "repo")
        TicketBuilder(sandbox.root / "docs" / "tickets").minimal()
        return sandbox

    def test_the_first_archive_creates_the_pre_release_uploads_and_comments(
        self, tmp_path: Path, logger: logging.Logger, gh: FakeGh
    ) -> None:
        sandbox = self.sandbox(tmp_path)
        gh.answer(["release", "view", "evidence-GH-7"], exit_code=1, stderr="release not found")
        archiver = self.archiver(sandbox, tmp_path, logger, dry_run=False)
        url = archiver.archive("GH-7")
        calls = gh.calls()
        zipped = Path(calls[2][3])
        assert zipped.parent == tmp_path / "scratch"
        assert zipped.name.startswith("GH-7-")
        assert zipped.suffix == ".zip"
        with zipfile.ZipFile(zipped) as archive:
            assert "GH-7/PROGRESS.md" in archive.namelist()
        assert url == f"https://github.com/{self.REPO}/releases/download/evidence-GH-7/{zipped.name}"
        assert calls[1] == [
            "release", "create", "evidence-GH-7", "--repo", self.REPO, "--prerelease", "--target", sandbox.head(),
            "--title", "Evidence GH-7", "--notes", "Test evidence and ticket folder of GH-7 (TEST-9). Not a release.",
        ]  # fmt: skip
        assert calls[2] == ["release", "upload", "evidence-GH-7", str(zipped), "--repo", self.REPO]
        assert "--clobber" not in calls[2]
        assert calls[-1] == [
            "issue", "comment", "7", "--repo", self.REPO, "--body", f"Ticket folder archived: {url} (TEST-9).",
        ]  # fmt: skip

    def test_a_later_archive_adds_an_asset_to_the_existing_pre_release(
        self, tmp_path: Path, logger: logging.Logger, gh: FakeGh
    ) -> None:
        sandbox = self.sandbox(tmp_path)
        asset = {"name": "GH-7-x.zip", "url": "https://x/old.zip", "createdAt": "2026-11-09T09:00:00Z"}
        gh.answer(
            ["release", "view", "evidence-GH-7"], stdout=json.dumps({"tagName": "evidence-GH-7", "assets": [asset]})
        )
        self.archiver(sandbox, tmp_path, logger, dry_run=False).archive("GH-7")
        verbs = [call[:2] for call in gh.calls()]
        assert ["release", "create"] not in verbs
        assert ["release", "upload"] in verbs
        assert ["issue", "comment"] in verbs

    def test_a_dry_run_only_lists_the_commands(self, tmp_path: Path, logger: logging.Logger, gh: FakeGh) -> None:
        sandbox = self.sandbox(tmp_path)
        archiver = self.archiver(sandbox, tmp_path, logger, dry_run=True)
        archiver.archive("GH-7")
        assert gh.calls() == []
        planned = archiver.gh.planned
        assert planned[0].startswith("gh release view evidence-GH-7")
        assert planned[1].startswith("gh release create evidence-GH-7")
        assert planned[2].startswith("gh release upload evidence-GH-7")
        assert planned[-1].startswith("gh issue comment 7")

    def test_a_ticket_without_a_folder_is_refused(self, tmp_path: Path, logger: logging.Logger, gh: FakeGh) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        with pytest.raises(SETicketFolderMissingError):
            self.archiver(sandbox, tmp_path, logger, dry_run=False).archive("GH-7")
        assert gh.calls() == []
