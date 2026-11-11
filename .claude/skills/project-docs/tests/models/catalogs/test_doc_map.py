from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest
from pydantic import JsonValue, ValidationError

from project_docs.models.catalogs.doc_map import DocMap
from project_docs.models.catalogs.exceptions import (
    SEDocMapInvalidAlways,
    SEDocMapInvalidChapterPattern,
    SEDocMapInvalidRules,
    SEDocMapRuleInvalidPaths,
    SEDocMapUnreadable,
    SEInvalidDocMapException,
)
from tests.helpers import DOC_MAP_FILE


class TestDocMap:
    def valid(self) -> Dict[str, JsonValue]:
        return {
            "rules": [{"paths": ["conf/*"], "chapters": ["docs/technical/configuration.md"]}],
            "always": ["README.md"],
            "per_service": "docs/technical/services/{service}.md",
            "per_frontend": "docs/technical/frontends/{frontend}.md",
        }

    def test_defaults(self) -> None:
        data = self.valid()
        del data["always"]
        assert DocMap.model_validate(data).always == []

    def test_full_valid_construction(self) -> None:
        doc_map = DocMap.model_validate(self.valid())
        assert doc_map.rules[0].chapters == ["docs/technical/configuration.md"]
        assert doc_map.per_service == "docs/technical/services/{service}.md"

    def test_none_becomes_the_default(self) -> None:
        assert DocMap.model_validate({**self.valid(), "always": None}).always == []

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("rules", None, SEDocMapInvalidRules),
            ("rules", [], SEDocMapInvalidRules),
            ("rules", {"paths": ["x"]}, SEDocMapInvalidRules),
            ("rules", [{"paths": []}], SEDocMapRuleInvalidPaths),
            ("always", "README.md", SEDocMapInvalidAlways),
            ("always", [" "], SEDocMapInvalidAlways),
            ("per_service", "", SEDocMapInvalidChapterPattern),
            ("per_service", "docs/technical/services/x.md", SEDocMapInvalidChapterPattern),
            ("per_frontend", None, SEDocMapInvalidChapterPattern),
            ("per_frontend", "docs/technical/frontends/{service}.md", SEDocMapInvalidChapterPattern),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        data = self.valid()
        data[name] = value
        with pytest.raises(error):
            DocMap.model_validate(data)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            DocMap.model_validate({**self.valid(), "never": []})

    def test_round_trip(self) -> None:
        doc_map = DocMap.model_validate(self.valid())
        assert DocMap.model_validate(doc_map.model_dump()) == doc_map

    def test_the_versioned_doc_map_loads(self) -> None:
        doc_map = DocMap.load(DOC_MAP_FILE)
        assert doc_map.always == ["README.md"]
        assert doc_map.rules[-1].chapters == []

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEDocMapUnreadable):
            DocMap.load(tmp_path / "doc-map.yaml")
        assert issubclass(SEDocMapUnreadable, SEInvalidDocMapException)
