from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod

# First-party imports
from project_docs.service.documentation.documentation_service import DocumentationService


class ServiceFactory(ABC):
    """Builds the services the ``project-docs`` commands call."""

    @abstractmethod
    def __init__(self) -> None:
        """Set what the services are built with."""

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def documentation(self) -> DocumentationService:
        """Build the documentation service of the caller's repository.

        Returns:
            DocumentationService: The service.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
        """
