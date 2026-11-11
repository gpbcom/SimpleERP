from __future__ import annotations

from release_notes.models.settings.exceptions.notes_settings.se_invalid_release_notes_settings_exception import (
    SEInvalidReleaseNotesSettingsException,
)


class SEReleaseNotesSettingsInvalidSkillDir(SEInvalidReleaseNotesSettingsException):
    """Exception raised when an invalid ``skill_dir`` is provided."""
