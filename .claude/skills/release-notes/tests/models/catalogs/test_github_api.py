from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import JsonValue, ValidationError

from release_notes.models.catalogs.exceptions import (
    SEGithubApiInvalidApiUrl,
    SEGithubApiInvalidApiVersion,
    SEGithubApiUnreadable,
    SEInvalidGithubApiException,
)
from release_notes.models.catalogs.github_api import GithubApi
from tests.helpers import GITHUB_API_FILE


class TestGithubApi:
    def test_defaults(self) -> None:
        api = GithubApi.load(GITHUB_API_FILE)
        assert api.api_url == "https://api.github.com"
        assert api.api_version == "2022-11-28"

    def test_full_valid_construction(self) -> None:
        api = GithubApi(api_url=" http://localhost:8080/api ", api_version=" 2022-11-28 ")
        assert (api.api_url, api.api_version) == ("http://localhost:8080/api", "2022-11-28")

    @pytest.mark.parametrize("name", ["api_url", "api_version"])
    def test_none_becomes_the_default(self, name: str) -> None:
        with pytest.raises(SEInvalidGithubApiException):
            GithubApi.model_validate({"api_url": "https://api.github.com", "api_version": "2022-11-28", name: None})

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("api_url", "api.github.com", SEGithubApiInvalidApiUrl),
            ("api_url", 3, SEGithubApiInvalidApiUrl),
            ("api_version", "", SEGithubApiInvalidApiVersion),
            ("api_version", 2022, SEGithubApiInvalidApiVersion),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            GithubApi.model_validate({"api_url": "https://api.github.com", "api_version": "2022-11-28", name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            GithubApi.model_validate({"api_url": "https://api.github.com", "api_version": "v", "token": "x"})

    def test_round_trip(self) -> None:
        api = GithubApi.load(GITHUB_API_FILE)
        assert GithubApi.model_validate(api.model_dump()) == api

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEGithubApiUnreadable):
            GithubApi.load(tmp_path / "github-api.yaml")
