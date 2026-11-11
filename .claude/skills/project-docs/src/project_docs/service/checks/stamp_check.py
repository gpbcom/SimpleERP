from __future__ import annotations

# Standard library imports
import re
from datetime import date
from typing import ClassVar, List

# First-party imports
from project_docs.service.checks.document_check import DocumentCheck


class StampCheck(DocumentCheck):
    """Checks that every document carries its ``Last reviewed:`` stamp and no em dash.

    Attributes:
        STAMP_PATTERN (re.Pattern[str]): The stamp line, ``Last reviewed: YYYY-MM-DD (GH-<n>)``.
        EM_DASH (str): The character the writing rules forbid.

    Notes:
        The stamp names the date and the ticket that last changed the document (DOC-2), so a reader knows how
        current it is.
    """

    STAMP_PATTERN: ClassVar[re.Pattern[str]] = re.compile(
        r"^Last reviewed: (?P<date>\d{4}-\d{2}-\d{2}) \(GH-\d+\)\s*$", re.MULTILINE
    )
    EM_DASH: ClassVar[str] = chr(0x2014)

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self) -> List[str]:
        """List the documents without a valid stamp, and every line with an em dash.

        Returns:
            List[str]: One line per problem.
        """
        problems: List[str] = []
        for document in self.files.documents():
            text = self.files.read(document)
            match = self.STAMP_PATTERN.search(text)
            if match is None:
                problems.append(f'{document}: no "Last reviewed: YYYY-MM-DD (GH-<n>)" line.')
            else:
                try:
                    date.fromisoformat(match.group("date"))
                except ValueError:
                    problems.append(f"{document}: invalid date {match.group('date')} in its Last reviewed line.")
            for number, line in enumerate(text.splitlines(), start=1):
                if self.EM_DASH in line:
                    problems.append(f"{document}:{number}: em dash.")
        self.logger.info("The stamp check found %d problems.", len(problems))
        return problems
