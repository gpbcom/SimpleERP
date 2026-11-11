from __future__ import annotations

# Standard library imports
from datetime import datetime
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Optional

# First-party imports
from pr_watch.models.enums import ChecksStatus, DeploymentState, EventKind, OperationKind, ReviewState
from pr_watch.models.events.inbox import Inbox
from pr_watch.models.events.operation import Operation
from pr_watch.models.sessions.live_session import LiveSession
from pr_watch.models.state.pr_snapshot import PrSnapshot
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.storage.costs.cost_ledger_reader import CostLedgerReader


class SummaryCells:
    """Writes the cells of the summary page's tables.

    Attributes:
        EMPTY (str): The mark of an empty or unknown cell.
        OPERATION_ICONS (Dict[OperationKind, str]): The icon of each operation, as the page's legend lists them.
        EVENT_ICONS (Dict[EventKind, str]): The icon of each event kind.
        CHECKS (Dict[ChecksStatus, str]): How the checks of a head commit show.
        STAGES (Dict[str, str]): The icon of each known environment.
        DEPLOYMENTS (Dict[DeploymentState, str]): The icon of each deployment state.
        REVIEWS (Dict[ReviewState, str]): How the reviewers' decision shows.
        COST_WARNING_SHARE (float): The share of the cap from which a cost is flagged.
        TIME_FORMAT (str): How a time shows.
        costs (CostLedgerReader): Reads what a ticket's AI tests cost.
        logger (Logger): Logger instance.

    Notes:
        A table cell holds one line: a text is flattened and its pipes escaped.
    """

    EMPTY: ClassVar[str] = "\u2014"
    OPERATION_ICONS: ClassVar[Dict[OperationKind, str]] = {
        OperationKind.REGISTERED: "📝",
        OperationKind.DETECTED: "🔎",
        OperationKind.REOPENED: "📨",
        OperationKind.NOTIFIED: "🔔",
        OperationKind.ACKED: "🔄",
        OperationKind.REBASED: "🔁",
        OperationKind.FIXED: "🛠️",
        OperationKind.WAITING_PUSH: "⏳",
        OperationKind.PUSHED: "🚀",
        OperationKind.QA_STARTED: "🟪",
        OperationKind.MERGED: "✅",
        OperationKind.CLOSED: "🚫",
        OperationKind.WARNING: "⚠️",
        OperationKind.NOTE: "💬",
    }
    EVENT_ICONS: ClassVar[Dict[EventKind, str]] = {
        EventKind.REBASE_CONFLICT: "🔀",
        EventKind.CHECKS_FAILED: "🔧",
        EventKind.STAGE_FAILED: "🚧",
        EventKind.CHANGES_REQUESTED: "✍️",
        EventKind.REVIEW_COMMENTS: "💬",
        EventKind.QA_WAITING: "🟪",
    }
    CHECKS: ClassVar[Dict[ChecksStatus, str]] = {
        ChecksStatus.PASSED: "✅",
        ChecksStatus.FAILED: "❌",
        ChecksStatus.RUNNING: "🔄 running",
        ChecksStatus.NONE: EMPTY,
    }
    STAGES: ClassVar[Dict[str, str]] = {"dev": "🟦", "qa": "🟪"}
    DEPLOYMENTS: ClassVar[Dict[DeploymentState, str]] = {
        DeploymentState.SUCCESS: "✅",
        DeploymentState.FAILURE: "❌",
        DeploymentState.ERROR: "❌",
        DeploymentState.INACTIVE: "⬜",
        DeploymentState.IN_PROGRESS: "🔄",
        DeploymentState.QUEUED: "🔄",
        DeploymentState.PENDING: "🔄",
    }
    REVIEWS: ClassVar[Dict[ReviewState, str]] = {
        ReviewState.APPROVED: "✅ approved",
        ReviewState.CHANGES_REQUESTED: "✍️ changes requested",
    }
    COST_WARNING_SHARE: ClassVar[float] = 0.8
    TIME_FORMAT: ClassVar[str] = "%Y-%m-%d %H:%M"

    def __init__(self, costs: CostLedgerReader, logger: Optional[Logger] = None) -> None:
        """Set where the costs come from.

        Args:
            costs (CostLedgerReader): Reads what a ticket's AI tests cost.
            logger (Optional[Logger]): Logger instance.
        """
        self.costs = costs
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def time(self, moment: Optional[datetime]) -> str:
        """Show a time.

        Args:
            moment (Optional[datetime]): The time.

        Returns:
            str: ``YYYY-MM-DD HH:MM`` in local time, the empty mark when unknown.
        """
        return moment.astimezone().strftime(self.TIME_FORMAT) if moment else self.EMPTY

    def duration(self, start: Optional[datetime], end: Optional[datetime]) -> str:
        """Show the time between two moments.

        Args:
            start (Optional[datetime]): The start.
            end (Optional[datetime]): The end.

        Returns:
            str: ``<d>d <h>h<mm>`` or ``<h>h<mm>``, the empty mark when a moment is unknown.
        """
        if start is None or end is None:
            return self.EMPTY
        minutes = max(0, int((end - start).total_seconds() // 60))
        days, rest = divmod(minutes, 24 * 60)
        text = f"{rest // 60}h{rest % 60:02d}"
        return f"{days}d {text}" if days else text

    def text(self, value: str, length: int) -> str:
        """Make a text safe for a table cell.

        Args:
            value (str): The text.
            length (int): The characters kept.

        Returns:
            str: The text on one line, its pipes escaped, cut to the length.
        """
        flat = " ".join(value.split()).replace("|", "\\|")
        return flat if len(flat) <= length else flat[: length - 1] + "…"

    def pull_request(self, watch: TicketWatch) -> str:
        """Link a pull request.

        Args:
            watch (TicketWatch): The pull request.

        Returns:
            str: ``[#<n>](<link>)``.
        """
        return f"[#{watch.pull_request.number}]({watch.pull_request.url})"

    def ticket(self, key: str) -> str:
        """Link a ticket's folder, relative to the summary page.

        Args:
            key (str): The ticket.

        Returns:
            str: ``[KEY](../KEY/PROGRESS.md)``.
        """
        return f"[{key}](../{key}/PROGRESS.md)"

    def cost(self, key: str) -> str:
        """Show what a ticket's AI tests cost.

        Args:
            key (str): The ticket.

        Returns:
            str: ``$<spent> / $<cap>``, flagged from 80 % of the cap and when the cap stopped the tests, the empty mark
            without a ledger.
        """
        ledger = self.costs.read(key)
        if ledger is None:
            return self.EMPTY
        warning = " ⚠️" if ledger.cap_usd and ledger.spent_usd >= self.COST_WARNING_SHARE * ledger.cap_usd else ""
        blocked = " ⛔" if ledger.blocked else ""
        return f"${ledger.spent_usd:.2f} / ${ledger.cap_usd:.0f}{warning}{blocked}"

    def problems(self, snapshot: PrSnapshot) -> List[str]:
        """List the problems of a pull request.

        Args:
            snapshot (PrSnapshot): What the last run saw.

        Returns:
            List[str]: The icon of each problem, none when the pull request is green.
        """
        icons = []
        if snapshot.rebase is not None and snapshot.rebase.conflict_files:
            icons.append(self.EVENT_ICONS[EventKind.REBASE_CONFLICT])
        if snapshot.ci.checks == ChecksStatus.FAILED:
            icons.append(self.EVENT_ICONS[EventKind.CHECKS_FAILED])
        if any(stage.state in {DeploymentState.FAILURE, DeploymentState.ERROR} for stage in snapshot.ci.stages):
            icons.append(self.EVENT_ICONS[EventKind.STAGE_FAILED])
        if snapshot.ci.review == ReviewState.CHANGES_REQUESTED:
            icons.append(self.EVENT_ICONS[EventKind.CHANGES_REQUESTED])
        if snapshot.error or (snapshot.rebase is not None and snapshot.rebase.error):
            icons.append("⚠️")
        return icons

    def status(self, snapshot: Optional[PrSnapshot]) -> str:
        """Show the status of a pull request.

        Args:
            snapshot (Optional[PrSnapshot]): What the last run saw.

        Returns:
            str: Its problems, 🟢 when there is none.
        """
        if snapshot is None:
            return "⚠️ not checked yet"
        return " ".join(self.problems(snapshot)) or "🟢"

    def checks(self, snapshot: Optional[PrSnapshot]) -> str:
        """Show the checks of the head commit.

        Args:
            snapshot (Optional[PrSnapshot]): What the last run saw.

        Returns:
            str: ✅, ❌ with a link to a failure, 🔄 or the empty mark.
        """
        if snapshot is None:
            return self.EMPTY
        shown = self.CHECKS[snapshot.ci.checks]
        return f"[{shown}]({snapshot.ci.checks_link})" if snapshot.ci.checks_link else shown

    def stages(self, snapshot: Optional[PrSnapshot]) -> str:
        """Show the latest deployment of the head commit to each stage.

        Args:
            snapshot (Optional[PrSnapshot]): What the last run saw.

        Returns:
            str: One entry per stage, such as ``🟦 [dev](link) ✅``, the empty mark when none.
        """
        if snapshot is None or not snapshot.ci.stages:
            return self.EMPTY
        entries = []
        for stage in snapshot.ci.stages:
            name = f"[{stage.environment}]({stage.link})" if stage.link else stage.environment
            state = self.DEPLOYMENTS[stage.state] if stage.state else "❔"
            entries.append(f"{self.STAGES.get(stage.environment, '⬛')} {name} {state}")
        return "<br>".join(entries)

    def review(self, snapshot: Optional[PrSnapshot]) -> str:
        """Show the reviewers' decision.

        Args:
            snapshot (Optional[PrSnapshot]): What the last run saw.

        Returns:
            str: Approved, changes requested, or the empty mark.
        """
        if snapshot is None or snapshot.ci.review is None:
            return self.EMPTY
        return self.REVIEWS.get(snapshot.ci.review, self.EMPTY)

    def handling(self, inbox: Optional[Inbox], snapshot: Optional[PrSnapshot], watch: TicketWatch) -> str:
        """Show who must act on a pull request.

        Args:
            inbox (Optional[Inbox]): Its ticket's events.
            snapshot (Optional[PrSnapshot]): What the last run saw.
            watch (TicketWatch): The pull request.

        Returns:
            str: ⏳ when events wait for the person, 🔄 when the session took them and a problem remains, else
            the empty mark.
        """
        events = [event for event in (inbox.events if inbox else []) if event.pr_id == watch.id]
        pending = [event for event in events if event.is_pending]
        if pending:
            return f"⏳ {len(pending)} waiting: {' '.join(self.EVENT_ICONS[event.kind] for event in pending)}"
        if events and (snapshot is None or self.problems(snapshot)):
            return "🔄 in the session"
        return self.EMPTY

    def session(self, watch: TicketWatch, live: Dict[str, LiveSession]) -> str:
        """Show the ticket's session.

        Args:
            watch (TicketWatch): The pull request.
            live (Dict[str, LiveSession]): The sessions running now.

        Returns:
            str: Its short identifier and where it runs, ``🔔 none`` for a watch that only notifies.
        """
        if watch.session is None:
            return "🔔 none"
        running = live.get(watch.session.session_id)
        where = "" if running is None else (" 🟢 VS Code" if running.in_vscode else " 🟢 terminal")
        return f"`{watch.session.short}`{where}"

    def operation(self, operation: Optional[Operation]) -> str:
        """Show an operation in one cell.

        Args:
            operation (Optional[Operation]): The operation.

        Returns:
            str: Its time, icon and detail, the empty mark when there is none.
        """
        if operation is None:
            return self.EMPTY
        return f"{self.time(operation.at)} {self.OPERATION_ICONS[operation.kind]} {self.text(operation.detail, 80)}"

    def rows(self, rows: List[str], columns: int) -> str:
        """Join table rows, with one placeholder row when there is none.

        Args:
            rows (List[str]): The rows.
            columns (int): The columns of the table.

        Returns:
            str: The rows.
        """
        return "\n".join(rows) if rows else "| " + " | ".join([self.EMPTY] + ["" for _ in range(columns - 1)]) + " |"
