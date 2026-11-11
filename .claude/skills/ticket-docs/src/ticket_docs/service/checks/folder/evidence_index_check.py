from __future__ import annotations

# Standard library imports
from typing import ClassVar, List

# First-party imports
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class EvidenceIndexCheck(TicketCheck):
    """Checks that every evidence folder has its README and a row in ``tests-evidences/README.md``.

    Attributes:
        INDEX (str): The ticket's evidence index.
        HISTORY (str): The folder of the history bundles, which is not a run.
        logger (Logger): Logger instance.
    """

    INDEX: ClassVar[str] = "tests-evidences/README.md"
    HISTORY: ClassVar[str] = "history"

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the evidence folders without a README or an index row.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per problem, none when the folder has no index yet.
        """
        index = folder.text(self.INDEX)
        evidence = folder.evidence.evidence_dir(folder.key)
        if index is None or not evidence.is_dir():
            return []
        problems: List[str] = []
        for run in sorted(path for path in evidence.iterdir() if path.is_dir() and path.name != self.HISTORY):
            if not (run / "README.md").is_file():
                problems.append(f"{folder.label(f'tests-evidences/{run.name}')}: README.md missing")
            if f"({run.name}/" not in index:
                problems.append(f"{folder.label(self.INDEX)}: {run.name} not in the index")
        self.logger.debug("%s's evidence index misses %d entries.", folder.key, len(problems))
        return problems
