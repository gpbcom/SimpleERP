from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest
from pydantic import JsonValue

from ticket_docs.models.github.exceptions import (
    SEGithubCatalogInvalidEnvironments,
    SEGithubCatalogInvalidProject,
    SEGithubCatalogInvalidText,
    SEGithubCatalogUnreadable,
)
from ticket_docs.models.github.github_catalog import GithubCatalog


class TestGithubCatalog:
    CONF = Path(__file__).resolve().parents[3] / "conf" / "github.yaml"
    VALID: Dict[str, JsonValue] = {
        "owner": "gpbcom",
        "repository": "simple-erp",
        "default_branch": "develop",
        "production_branch": "master",
        "project": {"number": 6, "url": "https://x", "id": "PVT_1", "fields": {"status": {"id": "F1"}}},
        "environments": ["dev", "qa"],
        "evidence_release_prefix": "evidence-",
    }

    def test_defaults(self) -> None:
        catalog = GithubCatalog.model_validate({**self.VALID, "environments": None})
        assert catalog.environments == []

    def test_full_valid_construction(self) -> None:
        catalog = GithubCatalog.load(self.CONF)
        assert catalog.full_name == "gpbcom/simple-erp"
        assert catalog.production_branch == "master"
        assert catalog.project.number == 6
        assert catalog.status_field().options["In progress"] == "63440315"
        assert catalog.release_tag("GH-12") == "evidence-GH-12"

    @pytest.mark.parametrize("name", ["environments"])
    def test_none_becomes_the_default(self, name: str) -> None:
        assert getattr(GithubCatalog.model_validate({**self.VALID, name: None}), name) == []

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("owner", "", SEGithubCatalogInvalidText),
            ("repository", None, SEGithubCatalogInvalidText),
            ("evidence_release_prefix", 3, SEGithubCatalogInvalidText),
            ("environments", "dev", SEGithubCatalogInvalidEnvironments),
            ("environments", ["dev", ""], SEGithubCatalogInvalidEnvironments),
            ("project", "6", SEGithubCatalogInvalidProject),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            GithubCatalog.model_validate({**self.VALID, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            GithubCatalog.model_validate({**self.VALID, "other": 1})

    def test_round_trip(self) -> None:
        catalog = GithubCatalog.model_validate(self.VALID)
        assert GithubCatalog.model_validate(catalog.model_dump()) == catalog

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEGithubCatalogUnreadable):
            GithubCatalog.load(tmp_path / "missing.yaml")

    def test_a_catalog_without_a_status_field_has_no_status_options(self) -> None:
        project: Dict[str, JsonValue] = {"number": 6, "url": "https://x", "id": "PVT_1", "fields": {}}
        catalog = GithubCatalog.model_validate({**self.VALID, "project": project})
        assert catalog.status_field().options == {}
