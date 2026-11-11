from __future__ import annotations

# Standard library imports
import re
from logging import Logger
from typing import List, Optional

# First-party imports
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class RequiredFilesCheck(TicketCheck):
    """Checks that the folder holds every required file, and each file its template's headings.

    Attributes:
        rules (FolderRules): The required files and headings.
        logger (Logger): Logger instance.

    Notes:
        The hand-over files, such as RELEASE-NOTE.md, are required once the hand-over row of PROGRESS.md is done.
        A file that is not required, such as STATUS.md, is checked for its headings only when it exists.
    """

    def __init__(self, rules: FolderRules, logger: Optional[Logger] = None) -> None:
        """Set the rules.

        Args:
            rules (FolderRules): The required files and headings.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.rules = rules

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the missing files and headings.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per missing file or heading.
        """
        required = list(self.rules.required_files)
        if folder.handed_over():
            required += self.rules.handover_files
        problems = [f"{folder.label(name)}: missing" for name in required if not (folder.path / name).exists()]
        for name, headings in self.rules.headings.items():
            text = folder.text(name)
            if text is None:
                continue
            problems += [
                f"{folder.label(name)}: heading '{heading}' missing"
                for heading in headings
                if not re.search(rf"^{re.escape(heading)}", text, re.M)
            ]
        self.logger.debug("%s misses %d files or headings.", folder.key, len(problems))
        return problems
