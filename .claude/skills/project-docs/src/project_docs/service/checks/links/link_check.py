from __future__ import annotations

# Standard library imports
from typing import List

# First-party imports
from harness_core.markdown.markdown_text import MarkdownText
from project_docs.service.checks.document_check import DocumentCheck


class LinkCheck(DocumentCheck):
    """Checks that every relative link of the documentation leads to a file or folder of the repository.

    Notes:
        - Anchors are ignored: a link to ``api.md#routes`` passes when ``api.md`` exists.
        - Links to other sites, and links written inside code, are not checked.
    """

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self) -> List[str]:
        """List the broken relative links.

        Returns:
            List[str]: One line per broken link, with its document and line.
        """
        problems: List[str] = []
        for document in self.files.documents():
            for line, link in MarkdownText.links(self.files.read(document)):
                target = self._target(document, link)
                if target is not None and (target.startswith("..") or not self.files.exists(target)):
                    problems.append(f"{document}:{line}: broken link to {link}.")
        self.logger.info("The link check found %d broken links.", len(problems))
        return problems
