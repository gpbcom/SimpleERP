from __future__ import annotations

# Standard library imports
import json
import os
import re
from datetime import datetime
from logging import Logger, getLogger
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Third-party imports
from pydantic import JsonValue, ValidationError

from harness_core.github.json_payload import JsonPayload

# First-party imports
from pr_watch.models.exceptions import SEPrWatchError
from pr_watch.models.sessions.live_session import LiveSession
from pr_watch.models.sessions.session_candidate import SessionCandidate
from pr_watch.storage.desktop.command_runner import CommandRunner


class SessionDirectory:
    """Finds the Claude Code sessions: the ones running now, and the ones whose title names a ticket.

    Attributes:
        claude_home (Path): Claude Code's folder, with its ``sessions/`` and ``projects/``.
        claude_command (str): The Claude Code command.
        runner (CommandRunner): Runs ``claude agents --json``.
        logger (Logger): Logger instance.

    Notes:
        - ``claude agents --json`` says which sessions run. ``sessions/<pid>.json`` says where each one runs (the
          VS Code extension or a terminal), and stands alone when the command fails.
        - ``sessions/*.json`` is not a documented interface: an entry that cannot be read is left out with a
          warning.
        - A transcript is a candidate owner of a ticket when its **last** title names the ticket.
    """

    def __init__(
        self, claude_home: Path, claude_command: str, runner: CommandRunner, logger: Optional[Logger] = None
    ) -> None:
        """Set where the sessions are described.

        Args:
            claude_home (Path): Claude Code's folder.
            claude_command (str): The Claude Code command.
            runner (CommandRunner): Runs ``claude agents --json``.
            logger (Optional[Logger]): Logger instance.
        """
        self.claude_home = claude_home
        self.claude_command = claude_command
        self.runner = runner
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _alive(self, pid: int) -> bool:
        """Tell whether a process runs.

        Args:
            pid (int): The process.

        Returns:
            bool: ``True`` when it runs, or runs as another user.
        """
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return False
        except PermissionError:
            return True
        return True

    def _session(self, entry: Dict[str, JsonValue], entrypoint: Optional[str]) -> LiveSession:
        """Build a running session from Claude Code's description of it.

        Args:
            entry (Dict[str, JsonValue]): The description.
            entrypoint (Optional[str]): Where it runs, when known.

        Returns:
            LiveSession: The session.
        """
        return LiveSession(
            session_id=entry.get("sessionId"),
            pid=entry.get("pid"),
            cwd=JsonPayload.text(entry, "cwd") or None,
            entrypoint=entrypoint,
            status=JsonPayload.text(entry, "status") or None,
        )

    def _described(self) -> Dict[str, LiveSession]:
        """Read the sessions described in Claude Code's sessions folder whose process still runs.

        Returns:
            Dict[str, LiveSession]: Each session, by identifier.
        """
        sessions: Dict[str, LiveSession] = {}
        for path in sorted((self.claude_home / "sessions").glob("*.json")):
            try:
                entry: JsonValue = json.loads(path.read_text(encoding="utf-8"))
                data = entry if isinstance(entry, dict) else {}
                session = self._session(data, JsonPayload.text(data, "entrypoint") or None)
            except (OSError, ValueError, SEPrWatchError) as error:
                self.logger.warning("The session description %s cannot be read: %s.", path.name, type(error).__name__)
                continue
            if self._alive(session.pid):
                sessions[session.session_id] = session
        return sessions

    def _title(self, transcript: Path) -> Tuple[Optional[str], Optional[str]]:
        """Read the last title and the first folder of a transcript.

        Args:
            transcript (Path): The transcript.

        Returns:
            Tuple[Optional[str], Optional[str]]: The title and the folder, ``None`` when missing.
        """
        title: Optional[str] = None
        cwd: Optional[str] = None
        for line in transcript.read_text(encoding="utf-8", errors="replace").splitlines():
            if '"cwd"' not in line and "-title" not in line:
                continue
            try:
                entry: JsonValue = json.loads(line)
            except ValueError:
                continue
            cwd = cwd or JsonPayload.text(entry, "cwd") or None
            title = JsonPayload.text(entry, "aiTitle") or JsonPayload.text(entry, "customTitle") or title
        return title, cwd

    def _candidate(self, transcript: Path, key: str, pr_url: str) -> Optional[SessionCandidate]:
        """Read a transcript whose title may name a ticket.

        Args:
            transcript (Path): The transcript.
            key (str): The ticket.
            pr_url (str): The link of the ticket's pull request.

        Returns:
            Optional[SessionCandidate]: The session, ``None`` when its last title does not name the ticket.
        """
        text = transcript.read_text(encoding="utf-8", errors="replace")
        if key not in text:
            return None
        title, cwd = self._title(transcript)
        if title is None or not re.search(rf"\b{re.escape(key)}\b", title):
            return None
        return SessionCandidate(
            session_id=transcript.stem,
            title=title,
            cwd=cwd,
            modified_on=datetime.fromtimestamp(transcript.stat().st_mtime).astimezone(),
            mentions_pr=pr_url in text,
        )

    def _rank(self, candidate: SessionCandidate) -> Tuple[bool, datetime]:
        """Give the sort key of a candidate: the ones that hold the link first, then the most recent.

        Args:
            candidate (SessionCandidate): The candidate.

        Returns:
            Tuple[bool, datetime]: Its key, higher first.
        """
        return candidate.mentions_pr, candidate.modified_on

    ############################
    # Publicly Exposed Methods #
    ############################

    def live(self) -> Dict[str, LiveSession]:
        """List the sessions running now.

        Returns:
            Dict[str, LiveSession]: Each session, by identifier.
        """
        described = self._described()
        output = self.runner.output_of([self.claude_command, "agents", "--json"])
        if output is None:
            self.logger.warning("claude agents --json failed: the sessions folder is used alone.")
            return described
        sessions: Dict[str, LiveSession] = {}
        try:
            entries: JsonValue = json.loads(output or "[]")
            for entry in JsonPayload.objects(entries):
                known = described.get(JsonPayload.text(entry, "sessionId"))
                session = self._session(entry, known.entrypoint if known else None)
                sessions[session.session_id] = session
        except (ValueError, ValidationError, SEPrWatchError) as error:
            self.logger.warning("claude agents --json cannot be read: %s.", type(error).__name__)
            return described
        self.logger.debug("%d Claude Code sessions run.", len(sessions))
        return sessions

    def describe(self, session_id: str) -> Optional[LiveSession]:
        """Describe a running session from the sessions folder.

        Args:
            session_id (str): The session.

        Returns:
            Optional[LiveSession]: The session, ``None`` when it is not described there.
        """
        return self._described().get(session_id)

    def candidates(self, key: str, pr_url: str) -> List[SessionCandidate]:
        """Find the sessions whose title names a ticket.

        Args:
            key (str): The ticket.
            pr_url (str): The link of its pull request.

        Returns:
            List[SessionCandidate]: The sessions, the most likely owner first.
        """
        found = [self._candidate(path, key, pr_url) for path in (self.claude_home / "projects").glob("*/*.jsonl")]
        candidates = sorted((candidate for candidate in found if candidate is not None), key=self._rank, reverse=True)
        self.logger.debug("%d sessions name %s.", len(candidates), key)
        return candidates
