from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.state.exceptions import (
    SEPrSnapshotInvalidBranches,
    SEPrSnapshotInvalidCheckedOn,
    SEPrSnapshotInvalidCi,
    SEPrSnapshotInvalidError,
    SEPrSnapshotInvalidRebase,
)
from pr_watch.models.state.pr_snapshot import PrSnapshot


class TestPrSnapshot:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {"checked_on": "2026-11-10T09:10:00+01:00"}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "branches": {
            "head_ref": "feature/GH-12-add-customers",
            "head_sha": "668501e0d3a1b2c3d4e5f60718293a4b5c6d7e8f",
            "base_ref": "develop",
        },
        "rebase": {"conflict_files": ["src/a.py"]},
        "ci": {"checks": "passed"},
        "error": "GitHub answered 503",
        "checked_on": "2026-11-10T09:10:00+01:00",
    }

    def test_defaults(self) -> None:
        model = PrSnapshot(**self.REQUIRED)
        assert model.branches == PrSnapshot.model_fields["branches"].get_default(call_default_factory=True)
        assert model.rebase == PrSnapshot.model_fields["rebase"].get_default(call_default_factory=True)
        assert model.ci == PrSnapshot.model_fields["ci"].get_default(call_default_factory=True)
        assert model.error == PrSnapshot.model_fields["error"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = PrSnapshot(**self.FULL)
        assert model.ci.checks == "passed"

    @pytest.mark.parametrize("name", ["branches", "rebase", "ci", "error"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = PrSnapshot(**{**self.FULL, name: None})
        assert getattr(model, name) == PrSnapshot.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("branches", "develop", SEPrSnapshotInvalidBranches),
            ("branches", 1, SEPrSnapshotInvalidBranches),
            ("rebase", "clean", SEPrSnapshotInvalidRebase),
            ("rebase", 1, SEPrSnapshotInvalidRebase),
            ("ci", "passed", SEPrSnapshotInvalidCi),
            ("ci", 1, SEPrSnapshotInvalidCi),
            ("error", "", SEPrSnapshotInvalidError),
            ("error", 1, SEPrSnapshotInvalidError),
            ("checked_on", "today", SEPrSnapshotInvalidCheckedOn),
            ("checked_on", None, SEPrSnapshotInvalidCheckedOn),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            PrSnapshot(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PrSnapshot(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = PrSnapshot(**self.FULL)
        assert PrSnapshot.model_validate_json(model.model_dump_json()) == model
