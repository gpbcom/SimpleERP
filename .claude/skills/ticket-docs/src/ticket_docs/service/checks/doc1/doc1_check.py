from __future__ import annotations

# Standard library imports
import re
import sys
from logging import Logger
from pathlib import Path
from typing import ClassVar, List, Optional, Pattern

# First-party imports
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder
from ticket_docs.storage.processes.command_runner import CommandRunner


class Doc1Check(TicketCheck):
    """Runs the DOC-1 check script, read from ``.claude/rules/ticket-documentation.md`` so the rule keeps one source.

    Attributes:
        SECTION (str): The heading that starts the DOC-1 rule.
        SCRIPT (Pattern[str]): The script's here-document in the rule.
        rules_file (Path): The ticket documentation rules.
        runner (CommandRunner): Runs the script.
        logger (Logger): Logger instance.

    Notes:
        The script runs in isolated mode (``python3 -I``) from the tickets folder with the ticket's key, exactly as
        the rule says to run it by hand. Each line it prints is a problem.
    """

    SECTION: ClassVar[str] = "## DOC-1"
    SCRIPT: ClassVar[Pattern[str]] = re.compile(r"<<'PY'\n(.*?)\nPY\n", re.S)

    def __init__(self, rules_file: Path, runner: CommandRunner, logger: Optional[Logger] = None) -> None:
        """Set the rules file and the runner.

        Args:
            rules_file (Path): The ticket documentation rules.
            runner (CommandRunner): Runs the script.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.rules_file = rules_file
        self.runner = runner

    ############################
    # Internal Helpers Methods #
    ############################

    def _script(self) -> Optional[str]:
        """Read the DOC-1 check script from the rules file.

        Returns:
            Optional[str]: The Python source, ``None`` when it cannot be found.
        """
        if not self.rules_file.is_file():
            self.logger.warning("The rules file %s does not exist.", self.rules_file)
            return None
        parts = self.rules_file.read_text(encoding="utf-8").split(self.SECTION, 1)
        match = self.SCRIPT.search(parts[1]) if len(parts) > 1 else None
        return match.group(1) if match else None

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """Run the DOC-1 script on the ticket and report what it prints.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per line the script printed, ``DOC-1:`` first.
        """
        script = self._script()
        if script is None:
            return [f"{self.rules_file}: DOC-1 check script not found, run it by hand"]
        outcome = self.runner.run([sys.executable, "-I", "-", folder.key], folder.path.parent, script)
        problems = [f"DOC-1: {line}" for line in outcome.output.strip().splitlines() if line.strip()]
        self.logger.debug("DOC-1 printed %d lines for %s.", len(problems), folder.key)
        return problems
