from __future__ import annotations

# Standard library imports
from pathlib import PurePosixPath
from typing import List, Optional, Set

# First-party imports
from harness_core.markdown.markdown_text import MarkdownText
from project_docs.service.checks.document_check import DocumentCheck


class IndexCheck(DocumentCheck):
    """Checks that each documentation folder's ``README.md`` links every chapter of the folder.

    Notes:
        - A chapter's index is the nearest ``README.md`` above it inside its documentation folder, so a sub-folder
          may have its own index, which its parent's index links in turn.
        - A link counts by its resolved target, whatever its text, anchor or ``./`` prefix.
    """

    ############################
    # Internal Helpers Methods #
    ############################

    def _index(self, document: str, folder: str) -> Optional[str]:
        """Find the index that must link a document.

        Args:
            document (str): The document, relative to the repository root.
            folder (str): Its documentation folder, such as ``docs/technical``.

        Returns:
            Optional[str]: The index, or ``None`` for the folder's own ``README.md``.
        """
        parent = PurePosixPath(document).parent
        if PurePosixPath(document).name == self.files.README:
            if parent.as_posix() == folder:
                return None
            parent = parent.parent
        while parent.as_posix() != folder and not self.files.exists((parent / self.files.README).as_posix()):
            parent = parent.parent
        return (parent / self.files.README).as_posix()

    def _linked(self, index: str) -> Set[str]:
        """List what an index links.

        Args:
            index (str): The index, relative to the repository root.

        Returns:
            Set[str]: The resolved targets of its relative links.
        """
        targets = (self._target(index, link) for _, link in MarkdownText.links(self.files.read(index)))
        return {target for target in targets if target is not None}

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self) -> List[str]:
        """List the chapters their index does not link, and the missing folder indexes.

        Returns:
            List[str]: One line per problem.
        """
        problems: List[str] = []
        documents = self.files.documents()
        for folder in self.files.FOLDERS:
            readme = f"{folder}/{self.files.README}"
            if not self.files.exists(readme):
                problems.append(f"{readme}: missing.")
            for document in [item for item in documents if item.startswith(f"{folder}/")]:
                index = self._index(document, folder)
                if index is not None and document not in self._linked(index):
                    problems.append(f"{document}: not linked from {index}.")
        self.logger.info("The index check found %d problems.", len(problems))
        return problems
