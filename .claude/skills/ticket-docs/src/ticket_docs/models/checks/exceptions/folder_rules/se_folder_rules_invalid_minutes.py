from __future__ import annotations

from ticket_docs.models.checks.exceptions.folder_rules.se_invalid_folder_rules_exception import (
    SEInvalidFolderRulesException,
)


class SEFolderRulesInvalidMinutes(SEInvalidFolderRulesException):
    """Exception raised when an invalid ``squash_permit_minutes`` is provided."""
