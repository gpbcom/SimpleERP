from __future__ import annotations

from typing import Dict

import pytest
from pydantic import JsonValue, ValidationError

from ticket_docs.models.issues.enums import IssueState
from ticket_docs.models.issues.exceptions import (
    SEGithubIssueInvalidBody,
    SEGithubIssueInvalidLabels,
    SEGithubIssueInvalidNumber,
    SEGithubIssueInvalidParent,
    SEGithubIssueInvalidState,
    SEGithubIssueInvalidSubIssues,
    SEGithubIssueInvalidTitle,
)
from ticket_docs.models.issues.github_issue import GithubIssue


class TestGithubIssue:
    VALID: Dict[str, JsonValue] = {
        "number": 13,
        "id": 6328695016,
        "title": "[INFRA] Accept a short SHA as ref in stage.yml",
        "body": "## Description\n",
        "state": "open",
        "labels": ["type:bug", "INFRA"],
        "parent": 17,
        "sub_issues": 0,
    }

    def test_defaults(self) -> None:
        issue = GithubIssue.model_validate({key: self.VALID[key] for key in ("number", "id", "title", "state")})
        assert (issue.body, issue.labels, issue.parent, issue.sub_issues) == ("", [], None, 0)

    def test_full_valid_construction(self) -> None:
        issue = GithubIssue.model_validate(self.VALID)
        assert (issue.number, issue.state, issue.parent) == (13, IssueState.OPEN, 17)
        assert issue.labels == ["type:bug", "INFRA"]
        assert issue.key == "GH-13"

    def test_labels_given_as_objects_keep_their_names(self) -> None:
        issue = GithubIssue.model_validate({**self.VALID, "labels": [{"name": "INFRA", "color": "c5def5"}]})
        assert issue.labels == ["INFRA"]

    def test_the_title_is_stripped(self) -> None:
        assert GithubIssue.model_validate({**self.VALID, "title": "  CI/CD pipeline "}).title == "CI/CD pipeline"

    @pytest.mark.parametrize("name", ["body", "labels", "parent", "sub_issues"])
    def test_none_becomes_the_default(self, name: str) -> None:
        issue = GithubIssue.model_validate({**self.VALID, name: None})
        assert getattr(issue, name) in ("", [], None, 0)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("number", 0, SEGithubIssueInvalidNumber),
            ("number", True, SEGithubIssueInvalidNumber),
            ("number", "13", SEGithubIssueInvalidNumber),
            ("id", -1, SEGithubIssueInvalidNumber),
            ("title", "", SEGithubIssueInvalidTitle),
            ("title", 3, SEGithubIssueInvalidTitle),
            ("body", 3, SEGithubIssueInvalidBody),
            ("state", "merged", SEGithubIssueInvalidState),
            ("state", None, SEGithubIssueInvalidState),
            ("labels", "INFRA", SEGithubIssueInvalidLabels),
            ("labels", [""], SEGithubIssueInvalidLabels),
            ("labels", [{"color": "x"}], SEGithubIssueInvalidLabels),
            ("parent", 0, SEGithubIssueInvalidParent),
            ("parent", False, SEGithubIssueInvalidParent),
            ("sub_issues", -1, SEGithubIssueInvalidSubIssues),
            ("sub_issues", True, SEGithubIssueInvalidSubIssues),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            GithubIssue.model_validate({**self.VALID, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            GithubIssue.model_validate({**self.VALID, "milestone": None})

    def test_round_trip(self) -> None:
        issue = GithubIssue.model_validate(self.VALID)
        assert GithubIssue.model_validate(issue.model_dump()) == issue
