from __future__ import annotations

from project_docs.models.settings.exceptions.project_docs_settings.se_invalid_project_docs_settings_exception import (
    SEInvalidProjectDocsSettingsException,
)


class SEProjectDocsSettingsInvalidSkillDir(SEInvalidProjectDocsSettingsException):
    """Exception raised when an invalid ``skill_dir`` is provided."""
