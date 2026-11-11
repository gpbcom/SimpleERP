from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.configuration.exceptions import (
    SEGithubConfigInvalidApiUrl,
    SEGithubConfigInvalidApiVersion,
    SEGithubConfigInvalidEnvironments,
    SEGithubConfigInvalidQaEnvironment,
    SEGithubConfigInvalidStageWorkflow,
)
from pr_watch.models.configuration.github_config import GithubConfig


class TestGithubConfig:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "api_url": "https://api.github.com",
        "api_version": "2022-11-28",
        "stage_workflow": "stage.yml",
        "environments": ["dev", "qa"],
        "qa_environment": "qa",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "api_url": "https://api.github.com",
        "api_version": "2022-11-28",
        "stage_workflow": "stage.yml",
        "environments": ["dev", "qa"],
        "qa_environment": "qa",
    }

    def test_defaults(self) -> None:
        model = GithubConfig(**self.REQUIRED)
        assert GithubConfig.model_validate(model.model_dump()) == model

    def test_full_valid_construction(self) -> None:
        model = GithubConfig(**self.FULL)
        assert model.environments == ["dev", "qa"]

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("api_url", "api.github.com", SEGithubConfigInvalidApiUrl),
            ("api_url", None, SEGithubConfigInvalidApiUrl),
            ("api_version", "", SEGithubConfigInvalidApiVersion),
            ("api_version", 3, SEGithubConfigInvalidApiVersion),
            ("stage_workflow", " ", SEGithubConfigInvalidStageWorkflow),
            ("stage_workflow", None, SEGithubConfigInvalidStageWorkflow),
            ("environments", "dev", SEGithubConfigInvalidEnvironments),
            ("environments", [""], SEGithubConfigInvalidEnvironments),
            ("qa_environment", "", SEGithubConfigInvalidQaEnvironment),
            ("qa_environment", 1, SEGithubConfigInvalidQaEnvironment),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            GithubConfig(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            GithubConfig(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = GithubConfig(**self.FULL)
        assert GithubConfig.model_validate_json(model.model_dump_json()) == model
