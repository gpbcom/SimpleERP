from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import JsonValue

from release_notes.models.catalogs.exceptions import (
    SEGithubCoordinatesInvalidOwner,
    SEGithubCoordinatesInvalidRepository,
    SEGithubCoordinatesUnreadable,
    SEInvalidGithubCoordinatesException,
)
from release_notes.models.catalogs.github_coordinates import GithubCoordinates
from tests.helpers import GITHUB_FILE


class TestGithubCoordinates:
    def test_defaults(self) -> None:
        coordinates = GithubCoordinates.load(GITHUB_FILE)
        assert (coordinates.owner, coordinates.repository) == ("gpbcom", "simple-erp")

    def test_full_valid_construction(self) -> None:
        coordinates = GithubCoordinates(owner=" gpbcom ", repository="simple-erp")
        assert coordinates.issue_link(12) == "https://github.com/gpbcom/simple-erp/issues/12"
        assert coordinates.issues_path(12) == "/repos/gpbcom/simple-erp/issues/12"

    @pytest.mark.parametrize("name", ["owner", "repository"])
    def test_none_becomes_the_default(self, name: str) -> None:
        with pytest.raises(SEInvalidGithubCoordinatesException):
            GithubCoordinates.model_validate({"owner": "gpbcom", "repository": "simple-erp", name: None})

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("owner", "", SEGithubCoordinatesInvalidOwner),
            ("owner", "gp/bcom", SEGithubCoordinatesInvalidOwner),
            ("repository", "simple erp", SEGithubCoordinatesInvalidRepository),
            ("repository", 1, SEGithubCoordinatesInvalidRepository),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            GithubCoordinates.model_validate({"owner": "gpbcom", "repository": "simple-erp", name: value})

    def test_rejects_unknown_keys(self) -> None:
        coordinates = GithubCoordinates.model_validate({"owner": "o", "repository": "r", "project": {"number": 6}})
        assert "project" not in coordinates.model_dump()

    def test_round_trip(self) -> None:
        coordinates = GithubCoordinates(owner="o", repository="r")
        assert GithubCoordinates.model_validate(coordinates.model_dump()) == coordinates

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEGithubCoordinatesUnreadable):
            GithubCoordinates.load(tmp_path / "github.yaml")
