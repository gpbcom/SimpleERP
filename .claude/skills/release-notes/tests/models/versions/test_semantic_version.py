from __future__ import annotations

import pytest
from pydantic import JsonValue, ValidationError

from release_notes.models.enums import VersionBump
from release_notes.models.versions.exceptions import SEInvalidSemanticVersionException, SESemanticVersionInvalidPart
from release_notes.models.versions.semantic_version import SemanticVersion


class TestSemanticVersion:
    def test_defaults(self) -> None:
        assert str(SemanticVersion()) == "0.0.0"

    def test_full_valid_construction(self) -> None:
        version = SemanticVersion(major=1, minor=4, patch=2)
        assert str(version) == "1.4.2"
        assert SemanticVersion.parse(" 1.4.2 ") == version

    @pytest.mark.parametrize("name", ["major", "minor", "patch"])
    def test_none_becomes_the_default(self, name: str) -> None:
        assert getattr(SemanticVersion.model_validate({name: None}), name) == 0

    @pytest.mark.parametrize(("name", "value"), [("major", -1), ("minor", True), ("patch", "1"), ("patch", 1.5)])
    def test_rejects_bad_values(self, name: str, value: JsonValue) -> None:
        with pytest.raises(SESemanticVersionInvalidPart):
            SemanticVersion.model_validate({name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            SemanticVersion.model_validate({"build": 1})

    def test_round_trip(self) -> None:
        version = SemanticVersion(major=2)
        assert SemanticVersion.model_validate(version.model_dump()) == version

    @pytest.mark.parametrize("text", ["1.4", "v1.4.2", "1.4.2-rc1", "01.4.2", ""])
    def test_only_x_y_z_parses(self, text: str) -> None:
        with pytest.raises(SEInvalidSemanticVersionException):
            SemanticVersion.parse(text)

    @pytest.mark.parametrize(
        ("bump", "expected"),
        [(VersionBump.MAJOR, "2.0.0"), (VersionBump.MINOR, "1.5.0"), (VersionBump.PATCH, "1.4.3")],
    )
    def test_a_bump_resets_the_lower_parts(self, bump: VersionBump, expected: str) -> None:
        assert str(SemanticVersion.parse("1.4.2").bumped(bump)) == expected

    def test_versions_order_by_their_numbers(self) -> None:
        versions = [SemanticVersion.parse(text) for text in ["0.10.0", "0.9.1", "1.0.0", "0.9.0"]]
        assert [str(version) for version in sorted(versions, key=lambda version: version.key)] == [
            "0.9.0",
            "0.9.1",
            "0.10.0",
            "1.0.0",
        ]
