from __future__ import annotations

import base64
import json
import logging
from datetime import UTC, datetime
from pathlib import Path

import pytest

from tests.builders.fake_gh import FakeGh
from ticket_docs.models.enums import RunConclusion
from ticket_docs.models.issues.enums import IssueState
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

    ISSUE = {
        "number": 13,
        "id": 6328695016,
        "title": "[INFRA] Accept a short SHA as ref in stage.yml",
        "body": "## Description\n",
        "state": "open",
        "labels": ["INFRA"],
        "parent": 17,
        "sub_issues": 0,
    }
    SHA = "b2507e41547ef8017f964d4ee7a6283e6a19e3ef"

    def test_every_issue_is_listed_without_the_pull_requests(self, gh: FakeGh, logger: logging.Logger) -> None:
        feature = {**self.ISSUE, "number": 17, "title": "CI/CD pipeline", "parent": None, "sub_issues": 1}
        gh.answer(["api", "--paginate"], stdout=f"{json.dumps(self.ISSUE)}\n{json.dumps(feature)}\n")
        issues = GhClient(self.REPO, logger=logger).issues()
        assert [(issue.number, issue.state, issue.parent) for issue in issues] == [
            (13, IssueState.OPEN, 17),
            (17, IssueState.OPEN, None),
        ]
        call = gh.calls()[0]
        assert call[:3] == ["api", "--paginate", f"repos/{self.REPO}/issues?state=all&per_page=100"]
        assert call[3] == "--jq"
        assert "select(.pull_request == null)" in call[4]
        assert "parent_issue_url" in call[4]

    def test_one_issue_is_read(self, gh: FakeGh, logger: logging.Logger) -> None:
        gh.answer(["api", f"repos/{self.REPO}/issues/13"], stdout=json.dumps(self.ISSUE))
        assert GhClient(self.REPO, logger=logger).issue(13).title.startswith("[INFRA]")

    def test_an_issue_is_created_labelled_then_linked(self, gh: FakeGh, logger: logging.Logger) -> None:
        gh.answer(["api", "-X", "POST", f"repos/{self.REPO}/issues", "-f"], stdout=json.dumps(self.ISSUE))
        client = GhClient(self.REPO, logger=logger)
        created = client.issue_create("[INFRA] Accept a short SHA", "## Description\n", ["INFRA", "type:bug"])
        client.sub_issue_add(17, created.id)
        client.issue_label(13, ["priority:high"])
        client.issue_update(13, "[INFRA] Accept a SHA", "## Description\nNew.\n")
        calls = gh.calls()
        assert calls[0][:4] == ["api", "-X", "POST", f"repos/{self.REPO}/issues"]
        assert calls[0][4:12] == [
            "-f", "title=[INFRA] Accept a short SHA", "-f", "body=## Description\n",
            "-f", "labels[]=INFRA", "-f", "labels[]=type:bug",
        ]  # fmt: skip
        assert calls[1] == [
            "api",
            "-X",
            "POST",
            f"repos/{self.REPO}/issues/17/sub_issues",
            "-F",
            "sub_issue_id=6328695016",
        ]
        assert calls[2] == ["api", "-X", "POST", f"repos/{self.REPO}/issues/13/labels", "-f", "labels[]=priority:high"]
        assert calls[3] == [
            "api", "-X", "PATCH", f"repos/{self.REPO}/issues/13",
            "-f", "title=[INFRA] Accept a SHA", "-f", "body=## Description\nNew.\n",
        ]  # fmt: skip

    def test_a_file_is_read_at_a_commit(self, gh: FakeGh, logger: logging.Logger) -> None:
        content = base64.b64encode("# GIT-6 \u00e9 the QA run\n".encode()).decode()
        gh.answer(
            ["api", f"repos/{self.REPO}/contents/.claude/rules/git%20rules.md?ref={self.SHA}"],
            stdout=json.dumps({"type": "file", "encoding": "base64", "content": content}),
        )
        text = GhClient(self.REPO, logger=logger).content_at(".claude/rules/git rules.md", self.SHA)
        assert text == "# GIT-6 \u00e9 the QA run\n"

    def test_a_folder_read_at_a_commit_gives_its_entries(self, gh: FakeGh, logger: logging.Logger) -> None:
        entries = [{"name": "README.md", "type": "file"}, {"name": "t09-install.md", "type": "file"}]
        gh.answer(
            ["api", f"repos/{self.REPO}/contents/docs/specs/03-technical?ref={self.SHA}"], stdout=json.dumps(entries)
        )
        text = GhClient(self.REPO, logger=logger).content_at("docs/specs/03-technical", self.SHA)
        assert text == "README.md\nt09-install.md"

    def test_a_path_missing_at_a_commit_has_no_content(self, gh: FakeGh, logger: logging.Logger) -> None:
        gh.answer(["api"], exit_code=1, stderr="gh: Not Found (HTTP 404)")
        assert GhClient(self.REPO, logger=logger).content_at("docs/specs/nothing.md", self.SHA) is None

    def test_another_failure_while_reading_a_file_is_raised(self, gh: FakeGh, logger: logging.Logger) -> None:
        gh.answer(["api"], exit_code=1, stderr="gh: Bad credentials (HTTP 401)")
        with pytest.raises(SEGhCommandFailedError, match="401"):
            GhClient(self.REPO, logger=logger).content_at("docs/specs/README.md", self.SHA)

    def test_the_comments_of_an_issue_are_read_written_and_deleted(self, gh: FakeGh, logger: logging.Logger) -> None:
        lines = [json.dumps({"id": 5, "body": "<!-- issue-check -->\nold"}), json.dumps({"id": 6, "body": "Hi"})]
        gh.answer(["api", "--paginate", f"repos/{self.REPO}/issues/13/comments"], stdout="\n".join(lines) + "\n")
        client = GhClient(self.REPO, logger=logger)
        assert client.comments(13) == {5: "<!-- issue-check -->\nold", 6: "Hi"}
        client.comment_update(5, "<!-- issue-check -->\nnew")
        client.comment_delete(5)
        assert gh.calls()[1:] == [
            ["api", "-X", "PATCH", f"repos/{self.REPO}/issues/comments/5", "-f", "body=<!-- issue-check -->\nnew"],
            ["api", "-X", "DELETE", f"repos/{self.REPO}/issues/comments/5"],
        ]
