from __future__ import annotations

# Standard library imports
import os
import subprocess
from typing import ClassVar, Dict, List, cast

# Third-party imports
import pytest

# First-party imports
from tests.ci.workflows.helpers import jobs, runs, steps, triggers


class TestGitflowWorkflows:
    WAITED_FOR: ClassVar[List[str]] = ["ci", "gitflow", "stage"]
    MERGE_PERMISSIONS: ClassVar[Dict[str, str]] = {
        "contents": "write",
        "pull-requests": "write",
        "issues": "write",
        "checks": "read",
        "statuses": "read",
    }

    def check(self, head: str, base: str, title: str = "Some change") -> subprocess.CompletedProcess[str]:
        """Run the rules of gitflow.yml under bash, as GitHub runs them."""
        env = {**os.environ, "HEAD": head, "BASE": base, "TITLE": title}
        return subprocess.run(
            ["bash", "-e", "-c", runs("gitflow.yml", "rules")], env=env, capture_output=True, text=True, check=False
        )

    def test_automerge_waits_for_every_workflow_that_checks_a_commit(self) -> None:
        assert triggers("automerge.yml")["workflow_run"]["workflows"] == self.WAITED_FOR

    def test_automerge_may_read_the_checks_and_merge_in_its_job_only(self) -> None:
        assert jobs("automerge.yml")["merge"]["permissions"] == self.MERGE_PERMISSIONS

    def test_automerge_only_merges_labelled_pull_requests_whose_checks_passed(self) -> None:
        script = runs("automerge.yml", "merge")
        assert '.name == "automerge"' in script
        assert '.baseRefName == "develop"' in script
        assert "success|skipped|neutral" in script
        assert "--match-head-commit" in script

    def test_automerge_reads_the_check_runs_of_the_head_commit_through_rest(self) -> None:
        script = runs("automerge.yml", "merge")
        assert "repos/$REPO/commits/$HEAD_SHA/check-runs" in script
        assert "statusCheckRollup" not in script

    def test_a_pull_request_that_changes_ci_is_left_to_a_person(self) -> None:
        script = runs("automerge.yml", "merge")
        assert "repos/$REPO/pulls/$pr/files" in script
        assert "needs-person" in script
        assert script.index("^\\.github/workflows/") < script.rindex("gh pr merge")

    def test_automerge_keeps_the_gitflow_merge_commit(self) -> None:
        script = runs("automerge.yml", "merge")
        assert "--merge" in script
        assert "--squash" not in script
        assert "--rebase" not in script

    def test_gitflow_checks_every_pull_request(self) -> None:
        assert "pull_request" in triggers("gitflow.yml")

    @pytest.mark.parametrize(
        ("head", "base"),
        [
            ("feature/GH-12-customers", "develop"),
            ("bugfix/GH-13-vat", "develop"),
            ("feature/harness-ci", "develop"),
            ("release/0.2.0", "master"),
            ("release/0.2.0", "develop"),
            ("hotfix/0.2.1-GH-14-rounding", "master"),
            ("master", "develop"),
            ("dependabot/uv/ruff-0.14.0", "develop"),
        ],
    )
    def test_a_gitflow_branch_to_its_base_passes(self, head: str, base: str) -> None:
        result = self.check(head, base)
        assert result.returncode == 0, result.stdout
        assert f"GitFlow: {head} -> {base}" in result.stdout

    @pytest.mark.parametrize(
        ("head", "base"),
        [
            ("feature/GH-12-customers", "master"),
            ("bugfix/x", "release/0.2.0"),
            ("master", "release/0.2.0"),
            ("develop", "master"),
            ("wip", "develop"),
            ("dependabot/uv/ruff-0.14.0", "master"),
        ],
    )
    def test_a_branch_outside_gitflow_or_to_the_wrong_base_fails(self, head: str, base: str) -> None:
        result = self.check(head, base)
        assert result.returncode == 1
        assert "::error::" in result.stdout

    @pytest.mark.parametrize(
        ("head", "title", "passes"),
        [
            ("feature/T0.10", "T0.10: Dev cell observability", True),
            ("feature/T10.02", "T10.02 Hosted backups", True),
            ("feature/T0.10", "Dev cell observability", False),
            ("feature/tickets", "T0.10: Dev cell observability", True),
            ("feature/tickets", "Tickets T0.10, T0.12", True),
            ("feature/tickets", "Several tickets", False),
            ("feature/GH-12-customers", "Anything", True),
        ],
    )
    def test_a_tickets_pull_request_is_titled_with_its_id(self, head: str, title: str, passes: bool) -> None:
        assert (self.check(head, "develop", title).returncode == 0) is passes

    def test_the_title_is_read_from_the_environment_never_interpolated(self) -> None:
        env = cast(Dict[str, str], steps("gitflow.yml", "rules")[0]["env"])
        assert env["TITLE"] == "${{ github.event.pull_request.title }}"
        assert "${{" not in runs("gitflow.yml", "rules")
