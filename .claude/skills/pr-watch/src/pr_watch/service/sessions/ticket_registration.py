from __future__ import annotations

# Standard library imports
import re
from datetime import datetime
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional, Tuple

# First-party imports
from pr_watch.models.enums import OperationKind
from pr_watch.models.events.operation import Operation
from pr_watch.models.sessions.session_candidate import SessionCandidate
from pr_watch.models.watch.pull_request_ref import PullRequestRef
from pr_watch.models.watch.registry import Registry
from pr_watch.models.watch.session_ref import SessionRef
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.models.watch.watch_history import WatchHistory
from pr_watch.service.exceptions import SENoPullRequestLinkError, SEPullRequestLinkInvalidError
from pr_watch.storage.git.pull_request_clone import PullRequestClone
from pr_watch.storage.sessions.session_directory import SessionDirectory
from pr_watch.storage.state.watch_store import WatchStore
from pr_watch.storage.tickets.ticket_folders import TicketFolders


class TicketRegistration:
    """Links a ticket's pull request to the ticket's Claude Code session.

    Attributes:
        LINK_PATTERN (re.Pattern[str]): A GitHub pull request link.
        TICKETS (Path): Where the ticket folders sit in a repository.
        store (WatchStore): The watcher's files.
        sessions (SessionDirectory): Describes the sessions.
        caller_cwd (Path): The folder the command was typed in, inside the repository.
        logger (Logger): Logger instance.

    Notes:
        - The links come from the "Pull request" section of the ticket's ``PROGRESS.md`` in the **main** working
          tree, so that a ticket worked on in a worktree is found too.
        - Registering again changes the owner session and keeps what the watcher learnt about the pull request.
    """

    LINK_PATTERN: ClassVar[re.Pattern[str]] = re.compile(
        r"^https://github\.com/(?P<repository>[\w.-]+/[\w.-]+)/pull/(?P<number>\d+)/?$"
    )
    TICKETS: ClassVar[Path] = Path("docs") / "tickets"

    def __init__(
        self, store: WatchStore, sessions: SessionDirectory, caller_cwd: Path, logger: Optional[Logger] = None
    ) -> None:
        """Set what the registration needs.

        Args:
            store (WatchStore): The watcher's files.
            sessions (SessionDirectory): Describes the sessions.
            caller_cwd (Path): The folder the command was typed in.
            logger (Optional[Logger]): Logger instance.
        """
        self.store = store
        self.sessions = sessions
        self.caller_cwd = caller_cwd
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _root(self) -> Path:
        """Find the main working tree of the repository the command was typed in.

        Returns:
            Path: The main working tree.

        Raises:
            SEGitCommandFailedError: When the folder is not inside a git working tree.
        """
        return PullRequestClone(self.caller_cwd, self.logger).main_root()

    def _watch(
        self, registry: Registry, key: str, link: str, root: Path, session: Optional[SessionRef], now: datetime
    ) -> TicketWatch:
        """Create the watch of a pull request, or change the owner of a known one.

        Args:
            registry (Registry): The registry, updated in place.
            key (str): The ticket.
            link (str): The pull request's link.
            root (Path): The main working tree of the repository.
            session (Optional[SessionRef]): The owner session, ``None`` for a watch that only notifies.
            now (datetime): The time of the registration.

        Returns:
            TicketWatch: The watch.

        Raises:
            SEPullRequestLinkInvalidError: When the link is not a GitHub pull request link.
        """
        match = self.LINK_PATTERN.match(link.strip())
        if match is None:
            self.logger.error("%s is not a GitHub pull request link.", link)
            raise SEPullRequestLinkInvalidError(
                f"{link} is not a GitHub pull request link. "  # noqa: E501
                "It must look like https://github.com/<owner>/<name>/pull/<number>."
            )
        candidate = TicketWatch(
            key=key,
            pull_request=PullRequestRef(
                repository=match.group("repository"), number=int(match.group("number")), root=str(root)
            ),
            session=session,
            history=WatchHistory(registered_on=now),
        )
        known = registry.pull_requests.get(candidate.id)
        watch = known.model_copy(update={"session": session}) if known else candidate
        registry.pull_requests[watch.id] = watch
        return watch

    ############################
    # Publicly Exposed Methods #
    ############################

    def session_for(self, session_id: str, cwd: Optional[str] = None) -> SessionRef:
        """Describe an owner session, with the folder VS Code must open for it.

        Args:
            session_id (str): The session.
            cwd (Optional[str]): Its folder when known, else the one Claude Code describes, else the caller's.

        Returns:
            SessionRef: The session.
        """
        described = self.sessions.describe(session_id)
        folder = cwd or (described.cwd if described else None) or str(self.caller_cwd)
        return SessionRef(session_id=session_id, cwd=folder)

    def register(self, key: str, links: List[str], session: Optional[SessionRef], now: datetime) -> List[TicketWatch]:
        """Watch a ticket's pull requests on behalf of a session. The caller holds the store's lock.

        Args:
            key (str): The ticket.
            links (List[str]): The links, by default the ones of the ticket's ``PROGRESS.md``.
            session (Optional[SessionRef]): The owner session, ``None`` for a watch that only notifies.
            now (datetime): The time of the registration.

        Returns:
            List[TicketWatch]: The watches.

        Raises:
            SENoPullRequestLinkError: When no link is given and ``PROGRESS.md`` has none.
            SEPullRequestLinkInvalidError: When a link is not a GitHub pull request link.
        """
        root = self._root()
        found = links or TicketFolders(root / self.TICKETS, self.logger).pull_request_links(key)
        if not found:
            self.logger.error("%s has no pull request link to watch.", key)
            raise SENoPullRequestLinkError(
                f"{key} has no pull request link in the Pull request section of its PROGRESS.md. "  # noqa: E501
                "Open the pull request first, or give its link with --link."
            )
        registry = self.store.registry()
        watches = [self._watch(registry, key, link, root, session, now) for link in found]
        self.store.save_registry(registry)
        owner = f"session {session.short}" if session else "no session, notifications only"
        for watch in watches:
            self.store.append_operation(
                Operation(
                    at=now,
                    pr_id=watch.id,
                    kind=OperationKind.REGISTERED,
                    detail=f"watched for {owner}",
                    link=watch.pull_request.url,
                )
            )
        self.logger.info("Registered %d pull requests of %s.", len(watches), key)
        return watches

    def proposals(self) -> List[Tuple[str, str, List[SessionCandidate]]]:
        """Propose a session for every ticket folder whose pull request nobody watches.

        Returns:
            List[Tuple[str, str, List[SessionCandidate]]]: The ticket, the link and the candidate sessions, the most
            likely owner first.
        """
        known = {watch.pull_request.url for watch in self.store.registry().pull_requests.values()}
        tickets = TicketFolders(self._root() / self.TICKETS, self.logger)
        proposals = [
            (key, link, self.sessions.candidates(key, link))
            for key in tickets.ticket_keys()
            for link in tickets.pull_request_links(key)
            if link not in known
        ]
        self.logger.info("Found %d pull requests nobody watches.", len(proposals))
        return proposals
