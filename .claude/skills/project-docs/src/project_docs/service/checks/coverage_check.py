from __future__ import annotations

# Standard library imports
from logging import Logger
from typing import ClassVar, Dict, List, Optional

# First-party imports
from project_docs.models.catalogs.doc_map import DocMap
from project_docs.service.checks.document_check import DocumentCheck
from project_docs.storage.files.document_files import DocumentFiles


class CoverageCheck(DocumentCheck):
    """Checks that every service and every front end has its technical chapter.

    Attributes:
        PARENTS (Dict[str, str]): Each folder that holds services or front ends, and the placeholder of its chapter.
        doc_map (DocMap): The chapter patterns.
    """

    PARENTS: ClassVar[Dict[str, str]] = {"services": "{service}", "frontends": "{frontend}"}

    def __init__(self, files: DocumentFiles, doc_map: DocMap, logger: Optional[Logger] = None) -> None:
        """Set the files and the chapter patterns.

        Args:
            files (DocumentFiles): The documentation's files.
            doc_map (DocMap): The chapter patterns.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(files, logger)
        self.doc_map = doc_map

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self) -> List[str]:
        """List the services and front ends without their chapter.

        Returns:
            List[str]: One line per missing chapter.
        """
        patterns = {"services": self.doc_map.per_service, "frontends": self.doc_map.per_frontend}
        problems: List[str] = []
        for parent, placeholder in self.PARENTS.items():
            for name in self.files.folders(parent):
                chapter = patterns[parent].replace(placeholder, name)
                if not self.files.exists(chapter):
                    problems.append(f"{parent}/{name}/: no chapter {chapter}.")
        self.logger.info("The coverage check found %d missing chapters.", len(problems))
        return problems
