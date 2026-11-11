from __future__ import annotations

# Standard library imports
from contextlib import AbstractContextManager
from logging import Logger, getLogger
from typing import Optional

# Third-party imports
import httpx

from harness_core.github.github_token import GithubToken

# First-party imports
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.service.factories.service_factory import ServiceFactory
from pr_watch.service.inbox.inbox_service import InboxService
from pr_watch.service.report.summary_cells import SummaryCells
from pr_watch.service.report.summary_renderer import SummaryRenderer
from pr_watch.service.sessions.session_dispatcher import SessionDispatcher
from pr_watch.service.sessions.ticket_registration import TicketRegistration
from pr_watch.service.setup.unit_installer import UnitInstaller
from pr_watch.service.watch.event_delivery import EventDelivery
from pr_watch.service.watch.event_detector import EventDetector
from pr_watch.service.watch.watch_job import WatchJob
from pr_watch.storage.costs.cost_ledger_reader import CostLedgerReader
from pr_watch.storage.desktop.command_runner import CommandRunner
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.sessions.session_directory import SessionDirectory
from pr_watch.storage.state.watch_store import WatchStore


class DefaultServiceFactory(ServiceFactory):
    """Builds the watcher's services on the real files, programs and GitHub.

    Attributes:
        settings (WatchSettings): Where the watcher reads and writes.
        catalog (WatchCatalog): The watcher's configuration.
        transport (Optional[httpx.AsyncBaseTransport]): The HTTP transport, a stand-in in tests.
        files (TextFiles): Reads and writes the text files.
        store (WatchStore): The watcher's files.
        runner (CommandRunner): Starts the desktop programs.
        sessions (SessionDirectory): Finds the Claude Code sessions.
        logger (Logger): Logger instance.
    """

    def __init__(
        self,
        settings: WatchSettings,
        catalog: WatchCatalog,
        transport: Optional[httpx.AsyncBaseTransport] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set what the services are built from.

        Args:
            settings (WatchSettings): Where the watcher reads and writes.
            catalog (WatchCatalog): The watcher's configuration.
            transport (Optional[httpx.AsyncBaseTransport]): The HTTP transport, a stand-in in tests.
            logger (Optional[Logger]): Logger instance.
        """
        self.settings = settings
        self.catalog = catalog
        self.transport = transport
        self.logger = logger if logger else getLogger(__name__)
        self.files = TextFiles(self.logger)
        self.store = WatchStore(settings.state_dir, self.files, self.logger)
        self.runner = CommandRunner(self.logger)
        self.sessions = SessionDirectory(settings.claude_home, catalog.commands.claude, self.runner, self.logger)

    ############################
    # Publicly Exposed Methods #
    ############################

    def lock(self) -> AbstractContextManager[None]:
        """Give the lock of the watcher's state.

        Returns:
            AbstractContextManager[None]: The lock, held inside a ``with`` block.
        """
        return self.store.lock()

    def watch_job(self) -> WatchJob:
        """Build one run of the watcher.

        Returns:
            WatchJob: The run.
        """
        dispatcher = SessionDispatcher(self.catalog.commands, self.runner, self.logger)
        return WatchJob(
            self.catalog,
            self.store,
            GithubToken(self.logger),
            EventDetector(self.catalog.github, self.catalog.timing, self.logger),
            EventDelivery(self.store, dispatcher, self.catalog.timing, self.logger),
            self.sessions,
            self.renderer(),
            self.transport,
            self.logger,
        )

    def registration(self) -> TicketRegistration:
        """Build the registration of a ticket's pull request.

        Returns:
            TicketRegistration: The registration, run from the caller's folder.
        """
        return TicketRegistration(self.store, self.sessions, self.settings.caller_cwd, self.logger)

    def inbox(self) -> InboxService:
        """Build what a session does with its events.

        Returns:
            InboxService: The service.
        """
        return InboxService(self.store, self.logger)

    def renderer(self) -> SummaryRenderer:
        """Build the writer of the summary pages.

        Returns:
            SummaryRenderer: The writer, its costs read from the ai-test-cost ledgers.
        """
        cells = SummaryCells(CostLedgerReader(self.settings.cost_state_dir, self.logger), self.logger)
        return SummaryRenderer(
            self.store, self.files, cells, self.settings.template_file, self.catalog.timing, self.sessions, self.logger
        )

    def installer(self) -> UnitInstaller:
        """Build the installer of the systemd units.

        Returns:
            UnitInstaller: The installer of this skill's units.
        """
        return UnitInstaller(self.settings.units_dir, self.settings.skill_dir, self.files, self.logger)
