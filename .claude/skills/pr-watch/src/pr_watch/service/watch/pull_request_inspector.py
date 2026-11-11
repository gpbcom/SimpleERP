from __future__ import annotations

# Standard library imports
from datetime import datetime
from logging import Logger, getLogger
from pathlib import Path
from typing import List, Optional, Tuple

from harness_core.github.github_connection import GithubConnection

# First-party imports
from pr_watch.models.configuration.github_config import GithubConfig
from pr_watch.models.enums import CommentSource, PullRequestStatus, ReviewState
from pr_watch.models.events.pr_event import PrEvent
from pr_watch.models.pull_requests.pr_comment import PrComment
from pr_watch.models.pull_requests.pr_review import PrReview
from pr_watch.models.pull_requests.pull_request_state import PullRequestState
from pr_watch.models.state.ci_summary import CiSummary
from pr_watch.models.state.pr_snapshot import PrSnapshot
from pr_watch.models.state.watch_state import WatchState
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.watch.event_detector import EventDetector
from pr_watch.storage.git.pull_request_clone import PullRequestClone
from pr_watch.storage.github.ci_reader import CiReader
from pr_watch.storage.github.pull_request_reader import PullRequestReader


class PullRequestInspector:
    """Reads everything about one open pull request and finds what its ticket's session must handle.

    Attributes:
        connection (GithubConnection): The HTTP client of the run.
        detector (EventDetector): Turns what was read into events.
        github (GithubConfig): The environments whose deployments are read.
        logger (Logger): Logger instance.

    Notes:
        - **The first read of a comment source only sets its cursor**: comments written before the watch started are
          not replayed. Reviews, line comments and conversation comments each have their own cursor, because their
          identifiers come from different sequences.
        - A review with a text counts as a comment, unless it asks for changes: that one is a ``changes_requested``
          event already.
        - The rebase probe runs in the main working tree of the clone the pull request was registered from.
    """

    def __init__(
        self,
        connection: GithubConnection,
        detector: EventDetector,
        github: GithubConfig,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set what the inspection needs.

        Args:
            connection (GithubConnection): The HTTP client of the run.
            detector (EventDetector): Turns what was read into events.
            github (GithubConfig): The environments whose deployments are read.
            logger (Optional[Logger]): Logger instance.
        """
        self.connection = connection
        self.detector = detector
        self.github = github
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _review_comments(self, reviews: List[PrReview]) -> List[PrComment]:
        """Turn the reviews that carry a text into comments.

        Args:
            reviews (List[PrReview]): The reviews.

        Returns:
            List[PrComment]: One comment per review with a text that does not ask for changes.
        """
        return [
            PrComment(
                id=review.id, source=CommentSource.REVIEW, author=review.author, body=review.body, link=review.link
            )
            for review in reviews
            if review.body.strip() and review.state != ReviewState.CHANGES_REQUESTED
        ]

    def _new_comments(self, watch: TicketWatch, comments: List[PrComment], state: WatchState) -> List[PrComment]:
        """Keep the comments written since the last run, and move each source's cursor.

        Args:
            watch (TicketWatch): The pull request.
            comments (List[PrComment]): Every comment of every source.
            state (WatchState): The watcher's memory, its cursors updated in place.

        Returns:
            List[PrComment]: The comments after the cursor of their source, none on a source's first read.
        """
        fresh: List[PrComment] = []
        for source in CommentSource:
            key = f"{watch.id}|{source.value}"
            items = [comment for comment in comments if comment.source == source]
            latest = max((comment.id for comment in items), default=0)
            if key in state.cursors:
                fresh += [comment for comment in items if comment.id > state.cursors[key]]
                latest = max(latest, state.cursors[key])
            else:
                self.logger.debug(
                    "%s: first read of the %s comments, cursor set to %d.", watch.id, source.value, latest
                )
            state.cursors[key] = latest
        return fresh

    ############################
    # Publicly Exposed Methods #
    ############################

    async def inspect(
        self, watch: TicketWatch, state: WatchState, now: datetime
    ) -> Tuple[PullRequestState, List[PrEvent]]:
        """Read one pull request and find its events.

        Args:
            watch (TicketWatch): The pull request.
            state (WatchState): The watcher's memory, its cursors and snapshot updated in place.
            now (datetime): The time of the run.

        Returns:
            Tuple[PullRequestState, List[PrEvent]]: What GitHub says of the pull request now, and its events. A
            closed pull request has no event.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        repository, number = watch.pull_request.repository, watch.pull_request.number
        pulls = PullRequestReader(self.connection, repository, self.logger)
        ci = CiReader(self.connection, repository, self.logger)
        pull_request = await pulls.pull_request(number)
        if pull_request.status != PullRequestStatus.OPEN:
            self.logger.info("%s is %s.", watch.id, pull_request.status.value)
            return pull_request, []
        branches = pull_request.branches
        checks = await ci.check_runs(branches.head_sha)
        runs = await ci.workflow_runs(branches.head_ref, branches.head_sha)
        deployments = await ci.deployments(branches.head_sha, self.github.environments)
        approvals = await ci.pending_approvals(branches.head_sha)
        reviews = await pulls.reviews(number)
        comments = await pulls.comments(number)
        probe = PullRequestClone(Path(watch.pull_request.root), self.logger).probe(branches.base_ref, branches.head_ref)
        fresh = self._new_comments(watch, self._review_comments(reviews) + comments, state)
        events = (
            self.detector.rebase_events(watch, branches, probe, now)
            + self.detector.check_events(watch, branches.head_sha, checks, runs, now)
            + self.detector.stage_events(watch, branches.head_sha, deployments, runs, now)
            + self.detector.review_events(watch, reviews, now)
            + self.detector.comment_events(watch, pull_request.author, fresh, now)
            + self.detector.approval_events(watch, approvals, now)
        )
        checks_status, checks_link = self.detector.checks_status(checks, runs)
        state.snapshots[watch.id] = PrSnapshot(
            branches=branches,
            rebase=probe,
            ci=CiSummary(
                checks=checks_status,
                checks_link=checks_link,
                stages=deployments,
                review=self.detector.review_state(reviews),
            ),
            checked_on=now,
        )
        if probe.error:
            self.logger.warning("%s: the rebase was not tried: %s.", watch.id, probe.error)
        self.logger.info("Inspected %s: %d events, checks %s.", watch.id, len(events), checks_status.value)
        return pull_request, events
