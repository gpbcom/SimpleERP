from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.watch.exceptions import (
    SERegistryInvalidPullRequests,
)
from pr_watch.models.watch.registry import Registry


class TestRegistry:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {}
    FULL: ClassVar[Dict[str, JsonValue]] = {"pull_requests": {}}

    def test_defaults(self) -> None:
        model = Registry(**self.REQUIRED)
        assert model.pull_requests == Registry.model_fields["pull_requests"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = Registry(**self.FULL)
        assert model.pull_requests == {}

    @pytest.mark.parametrize("name", ["pull_requests"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = Registry(**{**self.FULL, name: None})
        assert getattr(model, name) == Registry.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("pull_requests", [], SERegistryInvalidPullRequests),
            ("pull_requests", "x", SERegistryInvalidPullRequests),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            Registry(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            Registry(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = Registry(**self.FULL)
        assert Registry.model_validate_json(model.model_dump_json()) == model
