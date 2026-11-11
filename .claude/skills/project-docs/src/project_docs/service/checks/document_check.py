from __future__ import annotations

# Standard library imports
import posixpath
import re
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from typing import ClassVar, List, Optional
from urllib.parse import unquote

# First-party imports
from project_docs.storage.files.document_files import DocumentFiles


class DocumentCheck(ABC):
    """One check of the project documentation, which lists the problems it finds.

    Attributes:
        SCHEME_PATTERN (re.Pattern[str]): A link that starts with a scheme, such as ``https:`` or ``mailto:``.
        files (DocumentFiles): The documentation's files.
        logger (Logger): Logger instance.

    Notes:
        - Each problem is one line for the person: ``<path>[:<line>]: <what is wrong>.``
        - A problem is returned, never raised, so that one run lists them all.
    """

    SCHEME_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")

    def __init__(self, files: DocumentFiles, logger: Optional[Logger] = None) -> None:
        """Set the files.

        Args:
            files (DocumentFiles): The documentation's files.
            logger (Optional[Logger]): Logger instance.
        """
        self.files = files
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _target(self, document: str, link: str) -> Optional[str]:
        """Resolve the target of a relative link.

        Args:
            document (str): The document that holds the link, relative to the repository root.
            link (str): The link's target as written.

        Returns:
            Optional[str]: The target's path relative to the repository root, anchor and query left out, or
            ``None`` for a link to another site or to an anchor of the same document.

        Notes:
            A link that starts with ``/`` is relative to the repository root, as GitHub reads it. A target outside
            the repository starts with ``..``.
        """
        if self.SCHEME_PATTERN.match(link):
            return None
        path = unquote(link.split("#", 1)[0].split("?", 1)[0])
        if not path:
            return None
        if path.startswith("/"):
            return posixpath.normpath(path.lstrip("/"))
        return posixpath.normpath(posixpath.join(posixpath.dirname(document), path))

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def problems(self) -> List[str]:
        """List the problems this check finds.

        Returns:
            List[str]: One line per problem, none when the documentation passes the check.
        """
