from __future__ import annotations

from ticket_docs.models.checks.exceptions.folder_rules.se_invalid_folder_rules_exception import (
    SEInvalidFolderRulesException,
)


class SEFolderRulesInvalidHeadings(SEInvalidFolderRulesException):
    """Exception raised when an invalid ``headings`` is provided."""
