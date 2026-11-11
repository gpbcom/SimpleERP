from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import JsonValue, ValidationError

from project_docs.models.settings.exceptions import (
    SEInvalidProjectDocsSettingsException,
    SEProjectDocsSettingsInvalidCallerCwd,
    SEProjectDocsSettingsInvalidSkillDir,
)
from project_docs.models.settings.project_docs_settings import ProjectDocsSettings
from tests.helpers import SKILL_DIR


class TestProjectDocsSettings:
    @pytest.fixture(autouse=True)
    def no_variables(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("PROJECT_DOCS_CALLER_CWD", raising=False)
        monkeypatch.delenv("PROJECT_DOCS_SKILL_DIR", raising=False)

    def test_defaults(self) -> None:
        settings = ProjectDocsSettings()
        assert settings.caller_cwd == Path.cwd()
        assert settings.skill_dir == SKILL_DIR
        assert settings.doc_map_file == SKILL_DIR / "conf" / "doc-map.yaml"

    def test_full_valid_construction(self, tmp_path: Path) -> None:
        settings = ProjectDocsSettings(caller_cwd=tmp_path, skill_dir=str(tmp_path / "skill"))
        assert settings.caller_cwd == tmp_path
        assert settings.skill_dir == tmp_path / "skill"

    def test_the_caller_folder_comes_from_its_variable(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        monkeypatch.setenv("PROJECT_DOCS_CALLER_CWD", str(tmp_path))
        assert ProjectDocsSettings().caller_cwd == tmp_path

    @pytest.mark.parametrize("name", ["caller_cwd", "skill_dir"])
    def test_none_becomes_the_default(self, name: str) -> None:
        settings = ProjectDocsSettings.model_validate({name: None})
        assert getattr(settings, name) == getattr(ProjectDocsSettings(), name)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("caller_cwd", "", SEProjectDocsSettingsInvalidCallerCwd),
            ("caller_cwd", 3, SEProjectDocsSettingsInvalidCallerCwd),
            ("skill_dir", " ", SEProjectDocsSettingsInvalidSkillDir),
            ("skill_dir", ["x"], SEProjectDocsSettingsInvalidSkillDir),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            ProjectDocsSettings.model_validate({name: value})
        assert issubclass(error, SEInvalidProjectDocsSettingsException)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            ProjectDocsSettings.model_validate({"state_dir": "/tmp"})

    def test_round_trip(self, tmp_path: Path) -> None:
        settings = ProjectDocsSettings(caller_cwd=tmp_path)
        assert ProjectDocsSettings.model_validate(settings.model_dump()) == settings
