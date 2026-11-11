from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.checks.exceptions import (
    SERebaseProbeResultInvalidBaseSha,
    SERebaseProbeResultInvalidConflictFiles,
    SERebaseProbeResultInvalidError,
    SERebaseProbeResultInvalidHeadSha,
    SERebaseProbeResultInvalidMessages,
)
from pr_watch.models.checks.rebase_probe_result import RebaseProbeResult


class TestRebaseProbeResult:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "head_sha": "668501e0d3a1",
        "base_sha": "08a71846",
        "conflict_files": ["src/a.py"],
        "messages": "CONFLICT (content): Merge conflict in src/a.py",
        "error": "git fetch exited 128",
    }

    def test_defaults(self) -> None:
        model = RebaseProbeResult(**self.REQUIRED)
        assert model.head_sha == RebaseProbeResult.model_fields["head_sha"].get_default(call_default_factory=True)
        assert model.base_sha == RebaseProbeResult.model_fields["base_sha"].get_default(call_default_factory=True)
        assert model.conflict_files == RebaseProbeResult.model_fields["conflict_files"].get_default(
            call_default_factory=True
        )
        assert model.messages == RebaseProbeResult.model_fields["messages"].get_default(call_default_factory=True)
        assert model.error == RebaseProbeResult.model_fields["error"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = RebaseProbeResult(**self.FULL)
        assert model.conflict_files == ["src/a.py"]

    @pytest.mark.parametrize("name", ["head_sha", "base_sha", "conflict_files", "messages", "error"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = RebaseProbeResult(**{**self.FULL, name: None})
        assert getattr(model, name) == RebaseProbeResult.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("head_sha", "", SERebaseProbeResultInvalidHeadSha),
            ("head_sha", 1, SERebaseProbeResultInvalidHeadSha),
            ("base_sha", " ", SERebaseProbeResultInvalidBaseSha),
            ("base_sha", 2, SERebaseProbeResultInvalidBaseSha),
            ("conflict_files", "src/a.py", SERebaseProbeResultInvalidConflictFiles),
            ("conflict_files", [""], SERebaseProbeResultInvalidConflictFiles),
            ("messages", 1, SERebaseProbeResultInvalidMessages),
            ("messages", [], SERebaseProbeResultInvalidMessages),
            ("error", "", SERebaseProbeResultInvalidError),
            ("error", 5, SERebaseProbeResultInvalidError),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            RebaseProbeResult(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            RebaseProbeResult(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = RebaseProbeResult(**self.FULL)
        assert RebaseProbeResult.model_validate_json(model.model_dump_json()) == model
