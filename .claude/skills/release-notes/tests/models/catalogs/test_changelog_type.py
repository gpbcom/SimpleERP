from __future__ import annotations

from typing import Dict

import pytest
from pydantic import JsonValue, ValidationError

from release_notes.models.catalogs.changelog_type import ChangelogType
from release_notes.models.catalogs.exceptions import (
    SEChangelogTypeInvalidBump,
    SEChangelogTypeInvalidHeading,
    SEChangelogTypeInvalidName,
    SEInvalidChangelogTypeException,
)
from release_notes.models.enums import VersionBump
from release_notes.models.exceptions import SEReleaseNotesError


class TestChangelogType:
    def valid(self) -> Dict[str, JsonValue]:
        return {"name": "added", "heading": "Added", "bump": "minor"}

    def test_defaults(self) -> None:
        assert ChangelogType.model_validate(self.valid()).bump == VersionBump.MINOR

    def test_full_valid_construction(self) -> None:
        kind = ChangelogType(name=" fixed ", heading=" Fixed ", bump=VersionBump.PATCH)
        assert (kind.name, kind.heading, kind.bump) == ("fixed", "Fixed", VersionBump.PATCH)

    @pytest.mark.parametrize("name", ["name", "heading", "bump"])
    def test_none_becomes_the_default(self, name: str) -> None:
        with pytest.raises(SEInvalidChangelogTypeException):
            ChangelogType.model_validate({**self.valid(), name: None})

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("name", "Added", SEChangelogTypeInvalidName),
            ("name", "add ed", SEChangelogTypeInvalidName),
            ("name", 3, SEChangelogTypeInvalidName),
            ("heading", " ", SEChangelogTypeInvalidHeading),
            ("heading", ["Added"], SEChangelogTypeInvalidHeading),
            ("bump", "huge", SEChangelogTypeInvalidBump),
            ("bump", True, SEChangelogTypeInvalidBump),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            ChangelogType.model_validate({**self.valid(), name: value})
        assert issubclass(error, SEReleaseNotesError)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            ChangelogType.model_validate({**self.valid(), "order": 1})

    def test_round_trip(self) -> None:
        kind = ChangelogType.model_validate(self.valid())
        assert ChangelogType.model_validate(kind.model_dump()) == kind
