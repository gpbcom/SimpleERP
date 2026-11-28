from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import ClassVar, Dict, List

# Third-party imports
import pytest
from pydantic import JsonValue

# First-party imports
from tests.ci.release.helpers import (
    GITHUB_TOKEN,
    HEAD_SHA,
    MERGE_SHA,
    RELEASE_TOKEN,
    argv,
    calls_to,
    check_run,
    commit_status,
    run_automerge,
    scenario,
)
from tests.ci.workflows.helpers import jobs


class TestAutomerge:
    GREEN: ClassVar[Dict[str, str]] = {"result": "success", "rules": "success", "typescript": "skipped"}
    SCAN: ClassVar[str] = "images / scan-dependencies"

    def ticket_with_runs(self, runs: List[Dict[str, JsonValue]]) -> Dict[str, JsonValue]:
        case = scenario("feature/tickets", "develop", ["backend/services/sales/x.py"], self.GREEN)
        case["check_runs"] = [check_run(1, "result", "success"), *runs]
        return case

    def test_a_release_is_merged_into_master_tagged_released_and_brought_back_to_develop(self, tmp_path: Path) -> None:
        calls = run_automerge(tmp_path, scenario("release/0.1.0", "master", [".github/workflows/ci.yml"], self.GREEN))
        [merge] = calls_to(calls, "pr", "merge")
        assert merge["token"] == RELEASE_TOKEN
        assert "Release v0.1.0: merge release/0.1.0 into master (#12)" in argv(merge)
        assert f"--match-head-commit {HEAD_SHA}" in argv(merge)
        [release] = calls_to(calls, "release", "create")
        assert argv(release).startswith(f"release create v0.1.0 -R gpbcom/SimpleERP --target {MERGE_SHA}")
        assert release["token"] == RELEASE_TOKEN
        [back] = calls_to(calls, "pr", "create")
        assert "--base develop --head release/0.1.0 --label automerge" in argv(back)
        assert back["token"] == RELEASE_TOKEN
        assert calls.index(merge) < calls.index(release) < calls.index(back)
        assert not [call for call in calls if "DELETE" in argv(call)]

    def test_a_release_branch_deleted_by_github_on_merge_is_recreated_for_the_way_back(self, tmp_path: Path) -> None:
        case = scenario("release/0.1.0", "master", [], self.GREEN)
        case["branch_gone"] = True
        calls = run_automerge(tmp_path, case)
        [recreate] = [call for call in calls if "git/refs" in argv(call) and "POST" in argv(call)]
        assert f"ref=refs/heads/release/0.1.0 -f sha={HEAD_SHA}" in argv(recreate)
        assert recreate["token"] == RELEASE_TOKEN
        [back] = calls_to(calls, "pr", "create")
        assert calls.index(recreate) < calls.index(back)

    def test_a_release_branch_still_there_is_left_as_it_is(self, tmp_path: Path) -> None:
        calls = run_automerge(tmp_path, scenario("release/0.1.0", "master", [], self.GREEN))
        assert not [call for call in calls if "git/refs" in argv(call) and "POST" in argv(call)]

    def test_no_release_reaches_master_without_the_release_token(self, tmp_path: Path) -> None:
        calls = run_automerge(tmp_path, scenario("release/0.1.0", "master", [], self.GREEN), release_token="")
        assert not calls_to(calls, "pr", "merge")
        assert any("needs-person" in argv(call) for call in calls)
        assert any("RELEASE_TOKEN is missing" in argv(call) for call in calls)

    def test_only_a_release_or_a_hotfix_goes_to_master(self, tmp_path: Path) -> None:
        calls = run_automerge(tmp_path, scenario("feature/x", "master", [], self.GREEN))
        assert not calls_to(calls, "pr", "merge")

    def test_a_red_check_holds_the_release(self, tmp_path: Path) -> None:
        checks = {**self.GREEN, "python / repository": "failure"}
        calls = run_automerge(tmp_path, scenario("release/0.1.0", "master", [], checks))
        assert not calls_to(calls, "pr", "merge")

    def test_a_ticket_is_merged_into_develop_and_its_branch_deleted(self, tmp_path: Path) -> None:
        calls = run_automerge(
            tmp_path, scenario("feature/tickets", "develop", ["backend/services/sales/x.py"], self.GREEN)
        )
        [merge] = calls_to(calls, "pr", "merge")
        assert merge["token"] == GITHUB_TOKEN
        assert "T0.10: merge feature/tickets into develop (#12)" in argv(merge)
        [delete] = [call for call in calls if "DELETE" in argv(call)]
        assert argv(delete).endswith("repos/gpbcom/SimpleERP/git/refs/heads/feature/tickets --silent")
        assert calls.index(merge) < calls.index(delete)

    def test_a_branch_that_moved_after_the_merge_is_kept(self, tmp_path: Path) -> None:
        case = scenario("feature/tickets", "develop", ["backend/services/sales/x.py"], self.GREEN, ref_sha="c" * 40)
        calls = run_automerge(tmp_path, case)
        assert calls_to(calls, "pr", "merge")
        assert not [call for call in calls if "DELETE" in argv(call)]

    def test_the_way_back_of_a_release_is_merged_into_develop_then_its_branch_deleted(self, tmp_path: Path) -> None:
        case = scenario(
            "release/0.1.0", "develop", ["CHANGELOG.md"], self.GREEN, title="Release v0.1.0: back to develop"
        )
        calls = run_automerge(tmp_path, case)
        [merge] = calls_to(calls, "pr", "merge")
        assert merge["token"] == RELEASE_TOKEN
        assert "Release v0.1.0: merge release/0.1.0 into develop (#12)" in argv(merge)
        assert [call for call in calls if "DELETE" in argv(call)]

    def test_a_change_to_ci_bound_for_develop_is_left_to_a_person(self, tmp_path: Path) -> None:
        calls = run_automerge(tmp_path, scenario("feature/ci", "develop", [".github/workflows/ci.yml"], self.GREEN))
        assert not calls_to(calls, "pr", "merge")
        assert any("needs-person" in argv(call) for call in calls)

    def test_the_last_run_of_the_commit_merges_even_when_it_is_a_push(self) -> None:
        condition = str(jobs("automerge.yml")["merge"]["if"])
        assert "github.event.workflow_run.conclusion == 'success'" in condition
        assert "workflow_run.event" not in condition

    def test_no_pull_request_at_this_commit_does_nothing(self, tmp_path: Path) -> None:
        case = scenario("feature/x", "develop", [], self.GREEN)
        case["prs"] = []
        calls = run_automerge(tmp_path, case)
        assert not calls_to(calls, "pr", "merge")

    def test_a_release_is_published_under_the_product_name(self, tmp_path: Path) -> None:
        calls = run_automerge(tmp_path, scenario("release/0.1.0", "master", [], self.GREEN))
        [release] = calls_to(calls, "release", "create")
        assert "--title SimpleERP v0.1.0" in argv(release)

    def test_a_hotfix_takes_the_version_at_the_start_of_its_name(self, tmp_path: Path) -> None:
        calls = run_automerge(tmp_path, scenario("hotfix/0.2.1-GH-14-rounding", "master", [], self.GREEN))
        [merge] = calls_to(calls, "pr", "merge")
        assert "Release v0.2.1: merge hotfix/0.2.1-GH-14-rounding into master (#12)" in argv(merge)
        [release] = calls_to(calls, "release", "create")
        assert argv(release).startswith("release create v0.2.1 ")

    def test_a_hotfix_without_a_version_is_left_to_a_person(self, tmp_path: Path) -> None:
        calls = run_automerge(tmp_path, scenario("hotfix/rounding", "master", [], self.GREEN))
        assert not calls_to(calls, "pr", "merge")
        assert any("no version x.y.z" in argv(call) for call in calls)

    def test_a_check_that_failed_then_passed_on_a_new_run_of_the_commit_merges(self, tmp_path: Path) -> None:
        runs = [check_run(9, self.SCAN, "success"), check_run(2, self.SCAN, "failure")]
        calls = run_automerge(tmp_path, self.ticket_with_runs(runs))
        assert calls_to(calls, "pr", "merge")

    def test_a_check_whose_latest_run_failed_after_a_pass_holds_the_merge(self, tmp_path: Path) -> None:
        runs = [check_run(2, self.SCAN, "success"), check_run(9, self.SCAN, "failure")]
        calls = run_automerge(tmp_path, self.ticket_with_runs(runs))
        assert not calls_to(calls, "pr", "merge")

    @pytest.mark.parametrize("status", ["queued", "in_progress"])
    def test_a_check_whose_latest_run_is_still_going_keeps_the_pull_request_waiting(
        self, tmp_path: Path, status: str
    ) -> None:
        runs = [check_run(2, self.SCAN, "success"), check_run(9, self.SCAN, None, status=status)]
        calls = run_automerge(tmp_path, self.ticket_with_runs(runs))
        assert not calls_to(calls, "pr", "merge")

    def test_checks_of_the_same_name_from_two_apps_are_judged_apart(self, tmp_path: Path) -> None:
        runs = [check_run(9, self.SCAN, "failure", app_id=7), check_run(10, self.SCAN, "success", app_id=8)]
        calls = run_automerge(tmp_path, self.ticket_with_runs(runs))
        assert not calls_to(calls, "pr", "merge")

    @pytest.mark.parametrize(
        ("states", "merged"),
        [
            (["failure", "success"], True),
            (["error", "success"], True),
            (["success", "failure"], False),
            (["success", "error"], False),
            (["failure", "pending"], False),
        ],
    )
    def test_a_commit_status_is_judged_by_its_latest_state(
        self, tmp_path: Path, states: List[str], merged: bool
    ) -> None:
        case = self.ticket_with_runs([])
        case["statuses"] = [commit_status(i, "scan", state) for i, state in reversed(list(enumerate(states, 1)))]
        calls = run_automerge(tmp_path, case)
        assert bool(calls_to(calls, "pr", "merge")) is merged

    def test_every_run_of_the_head_commit_is_read_on_every_page(self, tmp_path: Path) -> None:
        calls = run_automerge(tmp_path, self.ticket_with_runs([]))
        [check_runs] = [call for call in calls if "/check-runs" in argv(call)]
        assert "filter=all" in argv(check_runs)
        assert "--paginate" in argv(check_runs)
        [statuses] = [call for call in calls if f"commits/{HEAD_SHA}/statuses" in argv(call)]
        assert "--paginate" in argv(statuses)
