from __future__ import annotations

from typing import Dict

import pytest
from pydantic import JsonValue, ValidationError

from release_notes.models.fragments.changelog_fragment import ChangelogFragment
from release_notes.models.fragments.exceptions import (
    SEChangelogFragmentInvalidLines,
    SEChangelogFragmentInvalidTicket,
    SEChangelogFragmentInvalidTypeName,
    SEInvalidChangelogFragmentException,
)


class TestChangelogFragment:
    def valid(self) -> Dict[str, JsonValue]:
        return {"ticket": "GH-12", "type_name": "added", "lines": ["Customers can be archived."]}

    def test_defaults(self) -> None:
        fragment = ChangelogFragment.model_validate(self.valid())
        assert fragment.number == 12
        assert fragment.file_name == "GH-12.added.md"

    def test_full_valid_construction(self) -> None:
        fragment = ChangelogFragment(ticket="GH-3", type_name="removed", lines=[" **Breaking:** No export. ", "Two."])
        assert fragment.lines == ["**Breaking:** No export.", "Two."]
        assert fragment.starts_with("**Breaking:**")
        assert not ChangelogFragment.model_validate(self.valid()).starts_with("**Breaking:**")

    @pytest.mark.parametrize("name", ["ticket", "type_name", "lines"])
    def test_none_becomes_the_default(self, name: str) -> None:
        with pytest.raises(SEInvalidChangelogFragmentException):
            ChangelogFragment.model_validate({**self.valid(), name: None})

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("ticket", "12", SEChangelogFragmentInvalidTicket),
            ("ticket", "GH-x", SEChangelogFragmentInvalidTicket),
            ("type_name", "Added", SEChangelogFragmentInvalidTypeName),
            ("type_name", "", SEChangelogFragmentInvalidTypeName),
            ("lines", [], SEChangelogFragmentInvalidLines),
            ("lines", ["a", "b", "c", "d"], SEChangelogFragmentInvalidLines),
            ("lines", ["a", " "], SEChangelogFragmentInvalidLines),
            ("lines", "a", SEChangelogFragmentInvalidLines),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            ChangelogFragment.model_validate({**self.valid(), name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            ChangelogFragment.model_validate({**self.valid(), "path": "changelog.d/GH-12.added.md"})

    def test_round_trip(self) -> None:
        fragment = ChangelogFragment.model_validate(self.valid())
        assert ChangelogFragment.model_validate(fragment.model_dump()) == fragment
