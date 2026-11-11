from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from contextlib import AbstractContextManager

# First-party imports
from pr_watch.service.inbox.inbox_service import InboxService
from pr_watch.service.report.summary_renderer import SummaryRenderer
from pr_watch.service.sessions.ticket_registration import TicketRegistration
from pr_watch.service.setup.unit_installer import UnitInstaller
from pr_watch.service.watch.watch_job import WatchJob


class ServiceFactory(ABC):
    """Builds the watcher's services and its run, wired to their storage.

    Notes:
        The command line only knows this factory: it never builds a store, a reader or a runner itself, so that the
        layers stay api, then service, then storage.
    """

    @abstractmethod
    def __init__(self) -> None:
        """Set what the services are built from."""

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def lock(self) -> AbstractContextManager[None]:
        """Give the lock of the watcher's state, held by every command that changes it."""

    @abstractmethod
    def watch_job(self) -> WatchJob:
        """Build one run of the watcher."""

    @abstractmethod
    def registration(self) -> TicketRegistration:
        """Build the registration of a ticket's pull request."""

    @abstractmethod
    def inbox(self) -> InboxService:
        """Build what a session does with its events."""

    @abstractmethod
    def renderer(self) -> SummaryRenderer:
        """Build the writer of the summary pages."""

    @abstractmethod
    def installer(self) -> UnitInstaller:
        """Build the installer of the systemd units."""
