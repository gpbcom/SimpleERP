from __future__ import annotations

import json
import logging
from datetime import UTC, datetime
from pathlib import Path

import pytest

from tests.builders.fake_gh import FakeGh
from ticket_docs.models.enums import RunConclusion
from ticket_docs.storage.github.exceptions import SEGhAnswerUnreadableError, SEGhCommandFailedError
from ticket_docs.storage.github.gh_client import GhClient


class TestGhClient:
    REPO = "gpbcom/simple-erp"
    RUN = json.dumps(
        {
            "conclusion": "failure",
            "headSha": "d" * 40,
            "headBranch": "feature/GH-1-x",
            "url": "https://github.com/gpbcom/simple-erp/actions/runs/7",
            "displayTitle": "stage qa",
            "createdAt": "2026-11-10T08:00:00Z",
        }
    )

    def test_an_actions_run_is_read(self, gh: FakeGh, logger: logging.Logger) -> None:
        gh.answer(["run", "view", "7", "--repo", self.REPO, "--json"], stdout=self.RUN)
        run = GhClient(self.REPO, logger=logger).run_view("7")
        assert (run.conclusion, run.head_sha) == (RunConclusion.FAILURE, "d" * 40)
        assert gh.calls() == [
            [
                "run",
                "view",
                "7",
                "--repo",
                self.REPO,
                "--json",
                "conclusion,headSha,headBranch,url,displayTitle,createdAt",
            ]
        ]

    def test_artifacts_and_log_are_fetched(self, gh: FakeGh, tmp_path: Path, logger: logging.Logger) -> None:
        gh.answer(["run", "download", "7"], files={"report/index.html": "<html/>"})
        gh.answer(["run", "view", "7", "--repo", self.REPO, "--log"], stdout="job\tstep\tline\n")
        client = GhClient(self.REPO, logger=logger)
        client.run_download("7", tmp_path / "artifacts")
        assert (tmp_path / "artifacts" / "report" / "index.html").is_file()
        assert client.run_log("7") == "job\tstep\tline\n"

    def test_a_failed_call_raises_with_what_gh_said(self, gh: FakeGh, logger: logging.Logger) -> None:
        gh.answer(["run", "view"], exit_code=1, stderr="run 8 not found")
        with pytest.raises(SEGhCommandFailedError, match="not found"):
            GhClient(self.REPO, logger=logger).run_log("8")

    def test_an_answer_that_is_not_json_is_refused(self, gh: FakeGh, logger: logging.Logger) -> None:
        gh.answer(["run", "view"], stdout="<html>")
        with pytest.raises(SEGhAnswerUnreadableError):
            GhClient(self.REPO, logger=logger).run_view("7")

    def test_a_release_and_its_assets_are_read(self, gh: FakeGh, logger: logging.Logger) -> None:
        assets = {
            "assets": [
                {"name": "GH-1-20261110-0900.zip", "url": "https://x/1.zip", "createdAt": "2026-11-10T09:00:00Z"},
                {"name": "GH-1-20261110-1000.zip", "url": "https://x/2.zip", "createdAt": "2026-11-10T10:00:00Z"},
            ]
        }
        gh.answer(["release", "view", "evidence-GH-1"], stdout=json.dumps(assets))
        client = GhClient(self.REPO, logger=logger)
        assert client.release_exists("evidence-GH-1")
        assert client.release_asset_times("evidence-GH-1") == [
            datetime(2026, 11, 10, 9, tzinfo=UTC),
            datetime(2026, 11, 10, 10, tzinfo=UTC),
        ]
        assert client.release_asset_url("evidence-GH-1", "GH-1-20261110-1000.zip") == "https://x/2.zip"
        assert client.release_asset_url("evidence-GH-1", "other.zip") is None

    def test_a_missing_release_has_no_assets(self, gh: FakeGh, logger: logging.Logger) -> None:
        gh.answer(["release", "view"], exit_code=1, stderr="release not found")
        client = GhClient(self.REPO, logger=logger)
        assert not client.release_exists("evidence-GH-2")
        assert client.release_asset_times("evidence-GH-2") is None

    def test_writes_go_to_github_with_the_repository(self, gh: FakeGh, tmp_path: Path, logger: logging.Logger) -> None:
        client = GhClient(self.REPO, logger=logger)
        client.release_create("evidence-GH-1", "e" * 40, "Evidence GH-1", "Not a release.")
        client.release_upload("evidence-GH-1", tmp_path / "GH-1.zip")
        client.issue_comment(1, "Archived.")
        assert gh.calls() == [
            [
                "release", "create", "evidence-GH-1", "--repo", self.REPO, "--prerelease",
                "--target", "e" * 40, "--title", "Evidence GH-1", "--notes", "Not a release.",
            ],
            ["release", "upload", "evidence-GH-1", str(tmp_path / "GH-1.zip"), "--repo", self.REPO],
            ["issue", "comment", "1", "--repo", self.REPO, "--body", "Archived."],
        ]  # fmt: skip

    def test_graphql_passes_numbers_and_text_apart(self, gh: FakeGh, logger: logging.Logger) -> None:
        gh.answer(["api", "graphql"], stdout='{"data": {"ok": true}}')
        answer = GhClient(self.REPO, logger=logger).graphql("query { ok }", {"owner": "gpbcom", "number": 1})
        assert answer == {"data": {"ok": True}}
        assert gh.calls() == [["api", "graphql", "-f", "query=query { ok }", "-f", "owner=gpbcom", "-F", "number=1"]]

    def test_a_dry_run_asks_nothing_and_lists_the_commands(self, gh: FakeGh, logger: logging.Logger) -> None:
        client = GhClient(self.REPO, dry_run=True, logger=logger)
        assert not client.release_exists("evidence-GH-1")
        client.issue_comment(1, "Ticket folder archived.")
        assert client.release_asset_url("evidence-GH-1", "a.zip") is None
        assert gh.calls() == []
        assert client.planned == [
            f"gh release view evidence-GH-1 --repo {self.REPO} --json tagName,assets",
            f"gh issue comment 1 --repo {self.REPO} --body 'Ticket folder archived.'",
            f"gh release view evidence-GH-1 --repo {self.REPO} --json tagName,assets",
        ]
