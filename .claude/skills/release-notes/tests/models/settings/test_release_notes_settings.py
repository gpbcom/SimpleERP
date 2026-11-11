from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import JsonValue, ValidationError

from release_notes.models.settings.exceptions import (
    SEInvalidReleaseNotesSettingsException,
    SEReleaseNotesSettingsInvalidCallerCwd,
    SEReleaseNotesSettingsInvalidSkillDir,
)
from release_notes.models.settings.release_notes_settings import ReleaseNotesSettings
from tests.helpers import GITHUB_API_FILE, GITHUB_FILE, SKILL_DIR, TEMPLATES, TYPES_FILE


class TestReleaseNotesSettings:
    @pytest.fixture(autouse=True)
    def no_variables(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("RELEASE_NOTES_CALLER_CWD", raising=False)
        monkeypatch.delenv("RELEASE_NOTES_SKILL_DIR", raising=False)

    def test_defaults(self) -> None:
        settings = ReleaseNotesSettings()
        assert settings.caller_cwd == Path.cwd()
        assert settings.skill_dir == SKILL_DIR
        assert settings.changelog_types_file == TYPES_FILE
        assert settings.github_api_file == GITHUB_API_FILE
        assert settings.github_file == GITHUB_FILE
        assert settings.release_note_template == TEMPLATES / "RELEASE-NOTE.md"

    def test_full_valid_construction(self, tmp_path: Path) -> None:
        settings = ReleaseNotesSettings(caller_cwd=tmp_path, skill_dir=str(tmp_path / "skill"))
        assert settings.caller_cwd == tmp_path
        assert settings.github_file == tmp_path / "ticket-docs" / "conf" / "github.yaml"

    def test_the_caller_folder_comes_from_its_variable(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        monkeypatch.setenv("RELEASE_NOTES_CALLER_CWD", str(tmp_path))
        assert ReleaseNotesSettings().caller_cwd == tmp_path

    @pytest.mark.parametrize("name", ["caller_cwd", "skill_dir"])
    def test_none_becomes_the_default(self, name: str) -> None:
        settings = ReleaseNotesSettings.model_validate({name: None})
        assert getattr(settings, name) == getattr(ReleaseNotesSettings(), name)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("caller_cwd", "", SEReleaseNotesSettingsInvalidCallerCwd),
            ("caller_cwd", 3, SEReleaseNotesSettingsInvalidCallerCwd),
            ("skill_dir", " ", SEReleaseNotesSettingsInvalidSkillDir),
            ("skill_dir", ["x"], SEReleaseNotesSettingsInvalidSkillDir),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            ReleaseNotesSettings.model_validate({name: value})
        assert issubclass(error, SEInvalidReleaseNotesSettingsException)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            ReleaseNotesSettings.model_validate({"token": "x"})

    def test_round_trip(self, tmp_path: Path) -> None:
        settings = ReleaseNotesSettings(caller_cwd=tmp_path)
        assert ReleaseNotesSettings.model_validate(settings.model_dump()) == settings
