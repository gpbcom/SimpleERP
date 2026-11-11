from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, List, Optional
from urllib.parse import quote

# First-party imports
from pr_watch.models.configuration.commands_config import CommandsConfig
from pr_watch.models.enums import DispatchAction
from pr_watch.models.events.pr_event import PrEvent
from pr_watch.models.sessions.dispatch_outcome import DispatchOutcome
from pr_watch.models.sessions.live_session import LiveSession
from pr_watch.models.watch.session_ref import SessionRef
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.storage.desktop.command_runner import CommandRunner


class SessionDispatcher:
    """Brings a ticket's events to its own Claude Code session, and never to another one.

    Attributes:
        APP_NAME (str): The name the notifications show.
        VSCODE_URI (str): The link that opens a session in the VS Code extension with a prompt typed.
        HEADLINE_EVENTS (int): The events named in a notification.
        commands (CommandsConfig): The desktop programs.
        runner (CommandRunner): Starts them.
        logger (Logger): Logger instance.

    Notes:
        - A closed session, or one open in VS Code, is opened in VS Code with ``/pr-watch <KEY>`` typed in its
          prompt box. VS Code cannot submit it: **the person presses Enter**, a human gate by design.
        - **A session open in a terminal is only notified**: opening it a second time would make two writers on one
          transcript.
        - The ``vscode://`` link opens in the focused window, so ``code <folder>`` brings the session's folder
          forward first.
        - The outcome fails when any command failed, so that the events are not marked as delivered and the next
          run tries again.
    """

    APP_NAME: ClassVar[str] = "--app-name=Claude PR watch"
    VSCODE_URI: ClassVar[str] = "vscode://anthropic.claude-code/open?session={session}&prompt={prompt}"
    HEADLINE_EVENTS: ClassVar[int] = 3

    def __init__(self, commands: CommandsConfig, runner: CommandRunner, logger: Optional[Logger] = None) -> None:
        """Set the programs.

        Args:
            commands (CommandsConfig): The desktop programs.
            runner (CommandRunner): Starts them.
            logger (Optional[Logger]): Logger instance.
        """
        self.commands = commands
        self.runner = runner
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _notify(self, watch: TicketWatch, body: str) -> Optional[str]:
        """Show a desktop notification.

        Args:
            watch (TicketWatch): The pull request.
            body (str): What to say.

        Returns:
            Optional[str]: Why it failed, ``None`` when it was shown.
        """
        summary = f"{watch.key} · {watch.pull_request.label}"
        return self.runner.failure_of([self.commands.notifier, self.APP_NAME, summary, body])

    def _outcome(self, action: DispatchAction, detail: str, failures: List[Optional[str]]) -> DispatchOutcome:
        """Build the outcome of a dispatch.

        Args:
            action (DispatchAction): What was done.
            detail (str): One line saying it.
            failures (List[Optional[str]]): Why each command failed, ``None`` for the ones that succeeded.

        Returns:
            DispatchOutcome: Successful only when every command succeeded.
        """
        failed = [failure for failure in failures if failure]
        if failed:
            self.logger.warning("%s: %d commands failed.", detail, len(failed))
            return DispatchOutcome(action=action, ok=False, detail=f"{detail} (failed: {'; '.join(failed)})")
        self.logger.info("%s.", detail)
        return DispatchOutcome(action=action, ok=True, detail=detail)

    def _headline(self, events: List[PrEvent]) -> str:
        """Say what the events are about.

        Args:
            events (List[PrEvent]): The events.

        Returns:
            str: The titles of the first ones, and how many more there are.
        """
        shown = events[: self.HEADLINE_EVENTS]
        more = f" (+{len(events) - len(shown)} more)" if len(events) > len(shown) else ""
        return " · ".join(event.detail.title for event in shown) + more

    ############################
    # Publicly Exposed Methods #
    ############################

    def dispatch(self, watch: TicketWatch, live: Optional[LiveSession], events: List[PrEvent]) -> DispatchOutcome:
        """Bring new events to the ticket's session.

        Args:
            watch (TicketWatch): The pull request.
            live (Optional[LiveSession]): The ticket's session when it runs now, ``None`` when it is closed.
            events (List[PrEvent]): The new events.

        Returns:
            DispatchOutcome: What was done, and whether it worked.
        """
        headline = self._headline(events)
        prompt = f"/pr-watch {watch.key}"
        vscode = self.runner.available(self.commands.vscode)
        terminal = self.runner.available(self.commands.terminal)
        self.logger.debug("Dispatching %d events of %s.", len(events), watch.id)
        match (watch.session, live, vscode, terminal):
            case (None, _, _, _):
                body = f"{headline}\nNo Claude session owns {watch.key}: run pr-watch register {watch.key} in it."
                return self._outcome(
                    DispatchAction.NOTIFIED, "no session registered, notified", [self._notify(watch, body)]
                )
            case (SessionRef() as session, LiveSession() as running, _, _) if not running.in_vscode:
                body = f"{headline}\nType {prompt} in its terminal session ({session.short})."
                detail = f"session {session.short} open in a terminal, notified"
                return self._outcome(DispatchAction.NOTIFIED, detail, [self._notify(watch, body)])
            case (SessionRef() as session, _, True, _):
                uri = self.VSCODE_URI.format(session=quote(session.session_id), prompt=quote(prompt))
                failures = [
                    self.runner.failure_of([self.commands.vscode, session.cwd or watch.pull_request.root]),
                    self.runner.failure_of([self.commands.opener, uri]),
                    self._notify(watch, f"{headline}\nPress Enter in its Claude tab: {prompt} is typed."),
                ]
                detail = f"session {session.short} opened in VS Code, {prompt} typed"
                return self._outcome(DispatchAction.REOPENED_VSCODE, detail, failures)
            case (SessionRef() as session, None, False, True):
                command = [self.commands.terminal, "--", self.commands.claude, "--resume", session.session_id, prompt]
                failures = [self.runner.failure_of(command), self._notify(watch, headline)]
                detail = f"session {session.short} resumed in a terminal"
                return self._outcome(DispatchAction.OPENED_TERMINAL, detail, failures)
            case (SessionRef() as session, _, _, _):
                body = f"{headline}\nRun {prompt} in session {session.short}."
                detail = "neither VS Code nor a terminal found, notified"
                return self._outcome(DispatchAction.NOTIFIED, detail, [self._notify(watch, body)])

    def remind(self, watch: TicketWatch, events: List[PrEvent]) -> DispatchOutcome:
        """Remind the events a session has not taken yet.

        Args:
            watch (TicketWatch): The pull request.
            events (List[PrEvent]): The events still waiting.

        Returns:
            DispatchOutcome: The notification, and whether it was shown.
        """
        body = f"Still waiting: {self._headline(events)}\nPress Enter on /pr-watch {watch.key} in its Claude session."
        detail = f"{len(events)} events still waiting, reminded"
        return self._outcome(DispatchAction.NOTIFIED, detail, [self._notify(watch, body)])
