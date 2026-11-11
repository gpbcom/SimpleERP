from __future__ import annotations

# Standard library imports
from datetime import datetime, timedelta
from logging import Logger, getLogger
from typing import ClassVar, Dict, FrozenSet, List, Optional, Tuple

# First-party imports
from pr_watch.models.checks.check_run import CheckRun
from pr_watch.models.checks.pending_approval import PendingApproval
from pr_watch.models.checks.rebase_probe_result import RebaseProbeResult
from pr_watch.models.checks.stage_deployment import StageDeployment
from pr_watch.models.checks.workflow_run import WorkflowRun
from pr_watch.models.configuration.github_config import GithubConfig
from pr_watch.models.configuration.timing_config import TimingConfig
from pr_watch.models.enums import (
    CheckConclusion,
    ChecksStatus,
    DeploymentState,
    EventKind,
    MergeableState,
    ReviewState,
)
from pr_watch.models.events.event_detail import EventDetail
from pr_watch.models.events.pr_event import PrEvent
from pr_watch.models.pull_requests.pr_comment import PrComment
from pr_watch.models.pull_requests.pr_review import PrReview
from pr_watch.models.pull_requests.pull_request_branches import PullRequestBranches
from pr_watch.models.watch.ticket_watch import TicketWatch


class EventDetector:
    """Turns what the watcher read about a pull request into the events its ticket's session must handle.

    Attributes:
        FAILED (FrozenSet[CheckConclusion]): The conclusions of a check or run that failed.
        STAGE_FAILED (FrozenSet[DeploymentState]): The states of a deployment that failed.
        DECISIVE (FrozenSet[ReviewState]): The review states that change a reviewer's decision.
        RUN_URL (str): The web link of a workflow run.
        EXCERPT_LENGTH (int): The characters of a text kept in an event.
        SHORT_SHA (int): The characters of a commit kept in an identifier.
        github (GithubConfig): The stage workflow and the qa environment.
        timing (TimingConfig): How long a qa approval may wait.
        logger (Logger): Logger instance.

    Notes:
        - An event's identifier names what makes it unique, so that a run that sees it again adds nothing: the head
          commit for a conflict or failed checks, the deployment, the review, the comment, the waiting run.
        - **A failed job of the stage workflow is a ``stage_failed`` event, never also a ``checks_failed`` one**:
          check runs that share the stage run's check suite are left out of the checks.
        - A deployment that failed hides the failed stage runs of the same commit, which say the same thing.
        - A reviewer's decision is their latest review that approves, asks for changes or was dismissed: a later
          comment-only review does not lift a request for changes.
    """

    FAILED: ClassVar[FrozenSet[CheckConclusion]] = frozenset(
        {CheckConclusion.FAILURE, CheckConclusion.CANCELLED, CheckConclusion.TIMED_OUT, CheckConclusion.STARTUP_FAILURE}
    )
    STAGE_FAILED: ClassVar[FrozenSet[DeploymentState]] = frozenset({DeploymentState.FAILURE, DeploymentState.ERROR})
    DECISIVE: ClassVar[FrozenSet[ReviewState]] = frozenset(
        {ReviewState.APPROVED, ReviewState.CHANGES_REQUESTED, ReviewState.DISMISSED}
    )
    RUN_URL: ClassVar[str] = "https://github.com/{repository}/actions/runs/{run_id}"
    EXCERPT_LENGTH: ClassVar[int] = 1500
    SHORT_SHA: ClassVar[int] = 12

    def __init__(self, github: GithubConfig, timing: TimingConfig, logger: Optional[Logger] = None) -> None:
        """Set the rules.

        Args:
            github (GithubConfig): The stage workflow and the qa environment.
            timing (TimingConfig): How long a qa approval may wait.
            logger (Optional[Logger]): Logger instance.
        """
        self.github = github
        self.timing = timing
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _event(
        self,
        watch: TicketWatch,
        kind: EventKind,
        suffix: str,
        detail: EventDetail,
        now: datetime,
    ) -> PrEvent:
        """Build an event.

        Args:
            watch (TicketWatch): The pull request.
            kind (EventKind): What it needs.
            suffix (str): What makes the event unique on the pull request.
            detail (EventDetail): What the event says.
            now (datetime): When it was seen.

        Returns:
            PrEvent: The event.
        """
        return PrEvent(id=f"{watch.id}|{suffix}", kind=kind, detail=detail, detected_on=now)

    def _failures(self, checks: List[CheckRun], runs: List[WorkflowRun]) -> List[Tuple[str, str, Optional[str]]]:
        """List the failed checks and CI runs of a commit, leaving out the stage workflow.

        Args:
            checks (List[CheckRun]): Its check runs.
            runs (List[WorkflowRun]): Its workflow runs.

        Returns:
            List[Tuple[str, str, Optional[str]]]: The name, the conclusion and the link of each failure.
        """
        stage_suites = {run.suite_id for run in runs if run.workflow == self.github.stage_workflow}
        failed_checks = [
            check
            for check in checks
            if check.conclusion in self.FAILED and (check.suite_id is None or check.suite_id not in stage_suites)
        ]
        covered = {check.suite_id for check in failed_checks}
        failed_runs = [
            run
            for run in runs
            if run.workflow != self.github.stage_workflow
            and run.conclusion in self.FAILED
            and (run.suite_id is None or run.suite_id not in covered)
        ]
        return [(check.name, str(check.conclusion), check.link) for check in failed_checks] + [
            (run.workflow, str(run.conclusion), run.link) for run in failed_runs
        ]

    def _standing(self, reviews: List[PrReview]) -> Dict[str, PrReview]:
        """Find each reviewer's standing decision.

        Args:
            reviews (List[PrReview]): The reviews, oldest first.

        Returns:
            Dict[str, PrReview]: The latest decisive review of each reviewer, by login.
        """
        standing: Dict[str, PrReview] = {}
        for review in sorted(reviews, key=lambda item: item.id):
            if review.state in self.DECISIVE:
                standing[review.author] = review
        return standing

    def _first_line(self, text: str) -> str:
        """Give the first line of a text, cut for a title.

        Args:
            text (str): The text.

        Returns:
            str: Its first non-empty line, at most 100 characters.
        """
        return next((line.strip() for line in text.splitlines() if line.strip()), "")[:100]

    def _minutes(self, since: datetime, now: datetime) -> int:
        """Count the whole minutes between two times.

        Args:
            since (datetime): The start.
            now (datetime): The end.

        Returns:
            int: The minutes.
        """
        return (now - since) // timedelta(minutes=1)

    ############################
    # Publicly Exposed Methods #
    ############################

    def rebase_events(
        self, watch: TicketWatch, branches: PullRequestBranches, probe: RebaseProbeResult, now: datetime
    ) -> List[PrEvent]:
        """Find whether the head no longer merges into the base.

        Args:
            watch (TicketWatch): The pull request.
            branches (PullRequestBranches): Its branches, and what GitHub says of the merge.
            probe (RebaseProbeResult): The merge tried in memory.
            now (datetime): The time of the run.

        Returns:
            List[PrEvent]: A ``rebase_conflict`` event when the probe found conflicts, or when it could not run and
            GitHub says the merge conflicts. Nothing otherwise.
        """
        if probe.conflict_files and probe.head_sha:
            files = "\n".join(probe.conflict_files[:20])
            detail = EventDetail(
                title=f"conflicts with {branches.base_ref} in {len(probe.conflict_files)} files",
                link=watch.pull_request.url,
                excerpt=(files + ("\n\n" + probe.messages if probe.messages else ""))[: self.EXCERPT_LENGTH],
            )
            return [
                self._event(watch, EventKind.REBASE_CONFLICT, f"rebase:{probe.head_sha[: self.SHORT_SHA]}", detail, now)
            ]
        if probe.error and branches.mergeable == MergeableState.DIRTY:
            self.logger.debug("%s: the probe failed and GitHub says the merge conflicts.", watch.id)
            detail = EventDetail(
                title=f"GitHub says it conflicts with {branches.base_ref}",
                link=watch.pull_request.url,
                excerpt=f"The local rebase probe could not run: {probe.error}",
            )
            suffix = f"rebase:{branches.head_sha[: self.SHORT_SHA]}"
            return [self._event(watch, EventKind.REBASE_CONFLICT, suffix, detail, now)]
        return []

    def check_events(
        self, watch: TicketWatch, sha: str, checks: List[CheckRun], runs: List[WorkflowRun], now: datetime
    ) -> List[PrEvent]:
        """Find the failed checks and CI runs of the head commit.

        Args:
            watch (TicketWatch): The pull request.
            sha (str): Its head commit.
            checks (List[CheckRun]): The check runs of the commit.
            runs (List[WorkflowRun]): The workflow runs of the commit.
            now (datetime): The time of the run.

        Returns:
            List[PrEvent]: One ``checks_failed`` event per head commit, listing every failure, or nothing.
        """
        failures = self._failures(checks, runs)
        if not failures:
            return []
        detail = EventDetail(
            title=f"{len(failures)} checks failed on {sha[:8]}",
            link=next((link for _, _, link in failures if link), None),
            excerpt="\n".join(f"- {name}: {conclusion} {link or ''}".rstrip() for name, conclusion, link in failures),
        )
        return [self._event(watch, EventKind.CHECKS_FAILED, f"checks:{sha[: self.SHORT_SHA]}", detail, now)]

    def checks_status(self, checks: List[CheckRun], runs: List[WorkflowRun]) -> Tuple[ChecksStatus, Optional[str]]:
        """Tell what the checks of the head commit say as a whole.

        Args:
            checks (List[CheckRun]): The check runs of the commit.
            runs (List[WorkflowRun]): The workflow runs of the commit.

        Returns:
            Tuple[ChecksStatus, Optional[str]]: The status, and the link of a failure when one failed.
        """
        failures = self._failures(checks, runs)
        if failures:
            return ChecksStatus.FAILED, next((link for _, _, link in failures if link), None)
        if any(check.conclusion is None for check in checks):
            return ChecksStatus.RUNNING, None
        return (ChecksStatus.PASSED if checks else ChecksStatus.NONE), None

    def stage_events(
        self,
        watch: TicketWatch,
        sha: str,
        deployments: List[StageDeployment],
        runs: List[WorkflowRun],
        now: datetime,
    ) -> List[PrEvent]:
        """Find the failed stage deployments and stage runs of the head commit.

        Args:
            watch (TicketWatch): The pull request.
            sha (str): Its head commit.
            deployments (List[StageDeployment]): The latest deployment of the commit to each stage.
            runs (List[WorkflowRun]): The workflow runs of the commit.
            now (datetime): The time of the run.

        Returns:
            List[PrEvent]: One ``stage_failed`` event per failed deployment, or else one per failed stage run.
        """
        events = [
            self._event(
                watch,
                EventKind.STAGE_FAILED,
                f"stage:{deployment.environment}:{deployment.deployment_id}",
                EventDetail(
                    title=f"{deployment.environment} deployment {deployment.state} on {sha[:8]}", link=deployment.link
                ),
                now,
            )
            for deployment in deployments
            if deployment.state in self.STAGE_FAILED
        ]
        if events:
            return events
        return [
            self._event(
                watch,
                EventKind.STAGE_FAILED,
                f"stage-run:{run.id}",
                EventDetail(title=f"{run.workflow} run {run.conclusion} on {sha[:8]}", link=run.link),
                now,
            )
            for run in runs
            if run.workflow == self.github.stage_workflow and run.conclusion in self.FAILED
        ]

    def review_events(self, watch: TicketWatch, reviews: List[PrReview], now: datetime) -> List[PrEvent]:
        """Find the reviewers whose standing decision asks for changes.

        Args:
            watch (TicketWatch): The pull request.
            reviews (List[PrReview]): Its reviews.
            now (datetime): The time of the run.

        Returns:
            List[PrEvent]: One ``changes_requested`` event per such review.
        """
        return [
            self._event(
                watch,
                EventKind.CHANGES_REQUESTED,
                f"review:{review.id}",
                EventDetail(
                    title=f"{review.author} requested changes",
                    link=review.link,
                    excerpt=review.body[: self.EXCERPT_LENGTH] or None,
                ),
                now,
            )
            for review in self._standing(reviews).values()
            if review.state == ReviewState.CHANGES_REQUESTED
        ]

    def review_state(self, reviews: List[PrReview]) -> Optional[ReviewState]:
        """Tell the reviewers' standing decision as a whole.

        Args:
            reviews (List[PrReview]): The reviews.

        Returns:
            Optional[ReviewState]: ``CHANGES_REQUESTED`` when one reviewer asks for changes, ``APPROVED`` when one
            approves and none asks for changes, ``None`` otherwise.
        """
        states = {review.state for review in self._standing(reviews).values()}
        if ReviewState.CHANGES_REQUESTED in states:
            return ReviewState.CHANGES_REQUESTED
        return ReviewState.APPROVED if ReviewState.APPROVED in states else None

    def comment_events(
        self, watch: TicketWatch, author: str, comments: List[PrComment], now: datetime
    ) -> List[PrEvent]:
        """Turn new comments written by someone else than the pull request's author into events.

        Args:
            watch (TicketWatch): The pull request.
            author (str): The pull request's author, whose own comments are replies, not events.
            comments (List[PrComment]): The comments written since the last run.
            now (datetime): The time of the run.

        Returns:
            List[PrEvent]: One ``review_comments`` event per comment.
        """
        return [
            self._event(
                watch,
                EventKind.REVIEW_COMMENTS,
                f"comment:{comment.source}:{comment.id}",
                EventDetail(
                    title=f"{comment.author} commented: {self._first_line(comment.body)}",
                    link=comment.link,
                    excerpt=comment.body[: self.EXCERPT_LENGTH] or None,
                ),
                now,
            )
            for comment in comments
            if comment.author != author
        ]

    def approval_events(self, watch: TicketWatch, approvals: List[PendingApproval], now: datetime) -> List[PrEvent]:
        """Find the qa deployments that have waited for their approval longer than allowed.

        Args:
            watch (TicketWatch): The pull request.
            approvals (List[PendingApproval]): The deployments of the head commit that wait for an approval.
            now (datetime): The time of the run.

        Returns:
            List[PrEvent]: One ``qa_waiting`` event per waiting run.
        """
        limit = now - timedelta(minutes=self.timing.qa_wait_minutes)
        return [
            self._event(
                watch,
                EventKind.QA_WAITING,
                f"qa-waiting:{approval.run_id}",
                EventDetail(
                    title=f"{approval.environment} approval waits for {self._minutes(approval.waiting_since, now)} min",
                    link=self.RUN_URL.format(repository=watch.pull_request.repository, run_id=approval.run_id),
                ),
                now,
            )
            for approval in approvals
            if approval.environment == self.github.qa_environment and approval.waiting_since < limit
        ]
