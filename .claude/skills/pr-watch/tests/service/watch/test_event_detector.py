from __future__ import annotations

from datetime import timedelta
from pathlib import Path
from typing import List, Optional

import pytest

from pr_watch.models.checks.check_run import CheckRun
from pr_watch.models.checks.pending_approval import PendingApproval
from pr_watch.models.checks.rebase_probe_result import RebaseProbeResult
from pr_watch.models.checks.stage_deployment import StageDeployment
from pr_watch.models.checks.workflow_run import WorkflowRun
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.enums import ChecksStatus, CommentSource, EventKind, ReviewState
from pr_watch.models.pull_requests.pr_comment import PrComment
from pr_watch.models.pull_requests.pr_review import PrReview
from pr_watch.models.pull_requests.pull_request_branches import PullRequestBranches
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.watch.event_detector import EventDetector
from tests.stand_ins.helpers import HEAD_REF, HEAD_SHA, NOW, PR_URL, a_watch


class TestEventDetector:
    @pytest.fixture
    def detector(self, catalog: WatchCatalog) -> EventDetector:
        return EventDetector(catalog.github, catalog.timing)

    @pytest.fixture
    def watch(self, tmp_path: Path) -> TicketWatch:
        return a_watch(tmp_path)

    def branches(self, mergeable: str = "clean") -> PullRequestBranches:
        return PullRequestBranches(head_ref=HEAD_REF, head_sha=HEAD_SHA, base_ref="develop", mergeable=mergeable)

    def check(self, identifier: int, conclusion: Optional[str], suite: int = 1) -> CheckRun:
        link = f"https://github.com/gpbcom/simple-erp/runs/{identifier}"
        return CheckRun(id=identifier, name=f"job-{identifier}", conclusion=conclusion, link=link, suite_id=suite)

    def run(self, identifier: int, workflow: str, conclusion: Optional[str], suite: int) -> WorkflowRun:
        link = f"https://github.com/gpbcom/simple-erp/actions/runs/{identifier}"
        return WorkflowRun(id=identifier, workflow=workflow, conclusion=conclusion, link=link, suite_id=suite)

    def review(self, identifier: int, state: str, author: str = "octocat", body: str = "") -> PrReview:
        return PrReview(id=identifier, state=state, author=author, body=body, link=f"{PR_URL}#r{identifier}")

    def test_a_conflict_found_by_the_probe_is_an_event_named_by_the_head(
        self, detector: EventDetector, watch: TicketWatch
    ) -> None:
        probe = RebaseProbeResult(
            head_sha=HEAD_SHA, base_sha="b" * 40, conflict_files=["a.py", "b.py"], messages="CONFLICT"
        )
        events = detector.rebase_events(watch, self.branches(), probe, NOW)
        assert [(event.kind, event.id) for event in events] == [
            (EventKind.REBASE_CONFLICT, f"{watch.id}|rebase:{HEAD_SHA[:12]}")
        ]
        assert events[0].detail.title == "conflicts with develop in 2 files"
        assert events[0].detail.excerpt == "a.py\nb.py\n\nCONFLICT"

    @pytest.mark.parametrize(
        ("probe", "mergeable", "expected"),
        [
            (RebaseProbeResult(head_sha=HEAD_SHA, base_sha="b" * 40), "dirty", 0),
            (RebaseProbeResult(error="git fetch exited 128"), "dirty", 1),
            (RebaseProbeResult(error="git fetch exited 128"), "clean", 0),
        ],
    )
    def test_github_says_conflict_only_when_the_probe_could_not_run(
        self, detector: EventDetector, watch: TicketWatch, probe: RebaseProbeResult, mergeable: str, expected: int
    ) -> None:
        assert len(detector.rebase_events(watch, self.branches(mergeable), probe, NOW)) == expected

    def test_failed_checks_make_one_event_per_head_commit(self, detector: EventDetector, watch: TicketWatch) -> None:
        checks = [self.check(1, "failure"), self.check(2, "timed_out"), self.check(3, "success"), self.check(4, None)]
        events = detector.check_events(watch, HEAD_SHA, checks, [], NOW)
        assert [event.id for event in events] == [f"{watch.id}|checks:{HEAD_SHA[:12]}"]
        assert events[0].detail.title == "2 checks failed on 668501e0"
        assert "job-1: failure" in (events[0].detail.excerpt or "")

    def test_a_failed_stage_job_is_not_a_failed_check(self, detector: EventDetector, watch: TicketWatch) -> None:
        checks = [self.check(1, "failure", suite=9)]
        runs = [self.run(5, "stage.yml", "failure", suite=9)]
        assert detector.check_events(watch, HEAD_SHA, checks, runs, NOW) == []
        assert [event.kind for event in detector.stage_events(watch, HEAD_SHA, [], runs, NOW)] == [
            EventKind.STAGE_FAILED
        ]

    def test_a_ci_run_that_failed_before_any_job_is_a_failed_check(
        self, detector: EventDetector, watch: TicketWatch
    ) -> None:
        runs = [self.run(6, "ci.yml", "startup_failure", suite=4)]
        events = detector.check_events(watch, HEAD_SHA, [], runs, NOW)
        assert [event.kind for event in events] == [EventKind.CHECKS_FAILED]

    @pytest.mark.parametrize(
        ("conclusions", "status"),
        [
            (["success", "failure"], ChecksStatus.FAILED),
            (["success", None], ChecksStatus.RUNNING),
            (["success", "skipped"], ChecksStatus.PASSED),
            ([], ChecksStatus.NONE),
        ],
    )
    def test_the_checks_status_sums_up_the_head_commit(
        self, detector: EventDetector, conclusions: List[Optional[str]], status: ChecksStatus
    ) -> None:
        checks = [self.check(index + 1, conclusion) for index, conclusion in enumerate(conclusions)]
        assert detector.checks_status(checks, [])[0] == status

    def test_a_failed_deployment_hides_the_failed_stage_runs(self, detector: EventDetector, watch: TicketWatch) -> None:
        deployments = [
            StageDeployment(environment="dev", deployment_id=31, state="success"),
            StageDeployment(environment="qa", deployment_id=32, state="error"),
        ]
        runs = [self.run(5, "stage.yml", "failure", suite=9)]
        events = detector.stage_events(watch, HEAD_SHA, deployments, runs, NOW)
        assert [event.id for event in events] == [f"{watch.id}|stage:qa:32"]

    def test_a_reviewer_who_approved_after_asking_for_changes_raises_nothing(
        self, detector: EventDetector, watch: TicketWatch
    ) -> None:
        reviews = [
            self.review(1, "CHANGES_REQUESTED", "alice", "Split it."),
            self.review(2, "COMMENTED", "alice", "And this."),
            self.review(3, "CHANGES_REQUESTED", "bob"),
            self.review(4, "APPROVED", "bob"),
        ]
        events = detector.review_events(watch, reviews, NOW)
        assert [(event.id, event.detail.excerpt) for event in events] == [(f"{watch.id}|review:1", "Split it.")]
        assert detector.review_state(reviews) == ReviewState.CHANGES_REQUESTED
        assert detector.review_state(reviews[3:]) == ReviewState.APPROVED
        assert detector.review_state([]) is None

    def test_comments_of_the_pull_request_author_are_not_events(
        self, detector: EventDetector, watch: TicketWatch
    ) -> None:
        comments = [
            PrComment(
                id=11, source=CommentSource.INLINE, author="octocat", body="\nRename this.\nPlease.", link=PR_URL
            ),
            PrComment(id=12, source=CommentSource.CONVERSATION, author="gpbcom", body="Done.", link=PR_URL),
        ]
        events = detector.comment_events(watch, "gpbcom", comments, NOW)
        assert [(event.id, event.detail.title) for event in events] == [
            (f"{watch.id}|comment:inline:11", "octocat commented: Rename this.")
        ]

    def test_a_qa_approval_becomes_an_event_after_its_delay(self, detector: EventDetector, watch: TicketWatch) -> None:
        approvals = [
            PendingApproval(run_id=41, environment="qa", waiting_since=NOW - timedelta(minutes=45)),
            PendingApproval(run_id=42, environment="qa", waiting_since=NOW - timedelta(minutes=5)),
            PendingApproval(run_id=43, environment="dev", waiting_since=NOW - timedelta(hours=5)),
        ]
        events = detector.approval_events(watch, approvals, NOW)
        assert [(event.id, event.detail.title) for event in events] == [
            (f"{watch.id}|qa-waiting:41", "qa approval waits for 45 min")
        ]
        assert events[0].detail.link == "https://github.com/gpbcom/simple-erp/actions/runs/41"
