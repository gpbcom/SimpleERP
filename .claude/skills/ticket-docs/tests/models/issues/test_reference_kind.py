from __future__ import annotations

from typing import Dict

import pytest
from pydantic import JsonValue, ValidationError

from ticket_docs.models.issues.exceptions import SEReferenceKindInvalidPaths, SEReferenceKindInvalidPatterns
from ticket_docs.models.issues.reference_kind import ReferenceKind


class TestReferenceKind:
    VALID: Dict[str, JsonValue] = {"paths": ["docs/specs/"], "patterns": {"feature": r"f\d{2}", "page": "[a-z]+"}}

    def test_defaults(self) -> None:
        kind = ReferenceKind.model_validate(self.VALID)
        assert kind.paths == ["docs/specs/"]

    def test_full_valid_construction(self) -> None:
        kind = ReferenceKind.model_validate(self.VALID)
        assert kind.covers("docs/specs/03-technical/t09-install")
        assert not kind.covers(".claude/rules/testing.md")
        assert kind.matches("f01")
        assert kind.matches("updates")
        assert not kind.matches("f1x")
        assert not kind.matches("GIT-6")

    def test_a_file_path_is_covered_when_it_is_named_exactly(self) -> None:
        kind = ReferenceKind.model_validate({"paths": ["AGENT.md", ".claude/"], "patterns": {"file": r"[\w.]+"}})
        assert kind.covers("AGENT.md")
        assert not kind.covers("AGENT.md.bak")
        assert kind.covers(".claude/rules/testing.md")

    @pytest.mark.parametrize("name", ["paths", "patterns"])
    def test_none_becomes_the_default(self, name: str) -> None:
        with pytest.raises((SEReferenceKindInvalidPaths, SEReferenceKindInvalidPatterns)):
            ReferenceKind.model_validate({**self.VALID, name: None})

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("paths", [], SEReferenceKindInvalidPaths),
            ("paths", "docs/specs/", SEReferenceKindInvalidPaths),
            ("paths", [""], SEReferenceKindInvalidPaths),
            ("patterns", {}, SEReferenceKindInvalidPatterns),
            ("patterns", ["f01"], SEReferenceKindInvalidPatterns),
            ("patterns", {"feature": "f(01"}, SEReferenceKindInvalidPatterns),
            ("patterns", {"feature": ""}, SEReferenceKindInvalidPatterns),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            ReferenceKind.model_validate({**self.VALID, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            ReferenceKind.model_validate({**self.VALID, "colour": "blue"})

    def test_round_trip(self) -> None:
        kind = ReferenceKind.model_validate(self.VALID)
        assert ReferenceKind.model_validate(kind.model_dump()) == kind
