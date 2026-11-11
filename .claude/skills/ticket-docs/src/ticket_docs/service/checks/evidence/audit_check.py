from __future__ import annotations

# Standard library imports
import re
from logging import Logger
from pathlib import Path
from typing import ClassVar, List, Optional, Pattern, Tuple

# First-party imports
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class AuditCheck(TicketCheck):
    """Checks that a handed-over ticket has a complete requirements audit.

    Attributes:
        FOLDER_SUFFIX (str): The end of an audit folder's name.
        REPORT (str): The audit's report file.
        SECTIONS (Tuple[str, ...]): The sections the report keeps from its template.
        CRITERION (Pattern[str]): An acceptance criterion, ``AC<n>``.
        TEMPLATE_SLOT (Pattern[str]): A ``<…>`` slot of a template, HTML tags excepted.
        tables (MarkdownTables): Blanks code and comments.
        logger (Logger): Logger instance.

    Notes:
        The latest audit counts: its report keeps the template's main sections, names every acceptance criterion of
        TICKET.md (in the report or its README) and keeps no template slot.
    """

    FOLDER_SUFFIX: ClassVar[str] = "-requirements-audit"
    REPORT: ClassVar[str] = "REPORT.md"
    SECTIONS: ClassVar[Tuple[str, ...]] = ("Verdict at a glance", "What was run", "Findings", "Limits")
    CRITERION: ClassVar[Pattern[str]] = re.compile(r"\bAC\d+\b")
    TEMPLATE_SLOT: ClassVar[Pattern[str]] = re.compile(
        r"<(?!/?(?:sub|sup|br|details|summary|img|a|b|i|kbd|p|span|div)\b)[^<>\n]{2,120}>"
    )

    def __init__(self, tables: MarkdownTables, logger: Optional[Logger] = None) -> None:
        """Set the text reader.

        Args:
            tables (MarkdownTables): Blanks code and comments.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.tables = tables

    ############################
    # Internal Helpers Methods #
    ############################

    def _audit_order(self, path: Path) -> str:
        """Order the audit folders by their date.

        Args:
            path (Path): An audit folder, ``<where>-<YYYY-MM-DD>-requirements-audit``.

        Returns:
            str: Its name without the place.
        """
        return path.name.split("-", 1)[-1]

    def _criterion_order(self, criterion: str) -> int:
        """Order the acceptance criteria by their number.

        Args:
            criterion (str): A criterion, ``AC<n>``.

        Returns:
            int: Its number.
        """
        return int(criterion[2:])

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List what the latest requirements audit lacks, once the ticket is handed over.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per problem, none before the hand-over.
        """
        if not folder.handed_over():
            return []
        audits = [
            path
            for path in folder.evidence.folders(folder.key)
            if path.name.endswith(self.FOLDER_SUFFIX) and (path / self.REPORT).is_file()
        ]
        if not audits:
            return [
                f"{folder.label('tests-evidences')}: handed over without a requirements audit "
                f"(dev-<date>{self.FOLDER_SUFFIX}/{self.REPORT}, ticket-docs skill)"
            ]
        audit = sorted(audits, key=self._audit_order)[-1]
        report = (audit / self.REPORT).read_text(encoding="utf-8")
        label = folder.label(f"tests-evidences/{audit.name}/{self.REPORT}")
        headings = [heading.lower() for heading in re.findall(r"^#{2,3} (.+)$", report, re.M)]
        problems = [
            f"{label}: section '{section}' missing"
            for section in self.SECTIONS
            if not any(section.lower() in heading for heading in headings)
        ]
        readme = audit / "README.md"
        covered = report + (readme.read_text(encoding="utf-8") if readme.is_file() else "")
        criteria = sorted(set(self.CRITERION.findall(folder.text("TICKET.md") or "")), key=self._criterion_order)
        missing = [ac for ac in criteria if not re.search(rf"\b{ac}\b", covered)]
        if missing:
            problems.append(f"{label}: acceptance criteria of TICKET.md not audited: {', '.join(missing)}")
        slots = sorted(set(self.TEMPLATE_SLOT.findall(self.tables.prose(report))))
        if slots:
            problems.append(f"{label}: template slots left: {', '.join(slots[:5])}")
        self.logger.debug("%s's requirements audit has %d problems.", folder.key, len(problems))
        return problems
