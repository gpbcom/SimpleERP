from __future__ import annotations

# Standard library imports
from typing import ClassVar, FrozenSet, List, Tuple

# First-party imports
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class ReadmeFieldsCheck(TicketCheck):
    """Checks that every evidence README gives what TEST-8 asks: command, commit, kind, place, result, raw output.

    Attributes:
        FIELDS (Tuple[str, ...]): The README rows TEST-8 needs.
        NOT_RAW (FrozenSet[str]): The files of a run folder that are not raw output.
        logger (Logger): Logger instance.

    Notes:
        The commit must be a full 40-character hash: ``EvidenceRun`` refuses any other, and its error is named.
    """

    FIELDS: ClassVar[Tuple[str, ...]] = ("command", "commit", "kind", "where", "result")
    NOT_RAW: ClassVar[FrozenSet[str]] = frozenset({"README.md", "REPORT.md"})

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the README rows and raw outputs missing from each run folder.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per problem.
        """
        problems: List[str] = []
        unreadable = folder.unreadable()
        runs = {run.folder: run for run in folder.runs()}
        for name in sorted({*unreadable, *runs}):
            label = folder.label(f"tests-evidences/{name}")
            if name in unreadable:
                problems.append(f"{label}: README.md cannot be read: {unreadable[name]} (TEST-8)")
                continue
            run = runs[name]
            problems += [
                f"{label}: README.md has no {field.capitalize()} (TEST-8)"
                for field in self.FIELDS
                if getattr(run, field) is None
            ]
            files = folder.evidence.files(folder.run_folder(name))
            if not [file for file in files if file not in self.NOT_RAW]:
                problems.append(f"{label}: no raw output file next to README.md (TEST-8)")
        self.logger.debug("%s's evidence READMEs have %d problems.", folder.key, len(problems))
        return problems
