from __future__ import annotations

from typing import Dict

import pytest
from pydantic import JsonValue, ValidationError

from project_docs.models.catalogs.doc_map_rule import DocMapRule
from project_docs.models.catalogs.exceptions import (
    SEDocMapRuleInvalidChapters,
    SEDocMapRuleInvalidPaths,
    SEInvalidDocMapRuleException,
)
from project_docs.models.exceptions import SEProjectDocsError


class TestDocMapRule:
    def test_defaults(self) -> None:
        assert DocMapRule(paths=["conf/*"]).chapters == []

    def test_full_valid_construction(self) -> None:
        rule = DocMapRule(paths=[" services/{service}/* "], chapters=["docs/technical/services/{service}.md"])
        assert rule.paths == ["services/{service}/*"]
        assert rule.chapters == ["docs/technical/services/{service}.md"]

    def test_none_becomes_the_default(self) -> None:
        assert DocMapRule(paths=["README.md"], chapters=None).chapters == []

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("paths", None, SEDocMapRuleInvalidPaths),
            ("paths", [], SEDocMapRuleInvalidPaths),
            ("paths", "conf/*", SEDocMapRuleInvalidPaths),
            ("paths", ["conf/*", " "], SEDocMapRuleInvalidPaths),
            ("paths", [3], SEDocMapRuleInvalidPaths),
            ("chapters", "README.md", SEDocMapRuleInvalidChapters),
            ("chapters", [""], SEDocMapRuleInvalidChapters),
            ("chapters", [True], SEDocMapRuleInvalidChapters),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        data: Dict[str, JsonValue] = {"paths": ["conf/*"], "chapters": ["docs/technical/configuration.md"]}
        data[name] = value
        with pytest.raises(error):
            DocMapRule.model_validate(data)
        assert issubclass(error, SEInvalidDocMapRuleException)
        assert issubclass(error, SEProjectDocsError)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            DocMapRule.model_validate({"paths": ["conf/*"], "chapter": []})

    def test_round_trip(self) -> None:
        rule = DocMapRule(paths=["conf/*"], chapters=["docs/technical/configuration.md"])
        assert DocMapRule.model_validate(rule.model_dump()) == rule
