from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.sessions.exceptions import (
    SESessionCandidateInvalidCwd,
    SESessionCandidateInvalidMentionsPr,
    SESessionCandidateInvalidModifiedOn,
    SESessionCandidateInvalidSessionId,
    SESessionCandidateInvalidTitle,
)
from pr_watch.models.sessions.session_candidate import SessionCandidate


class TestSessionCandidate:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "session_id": "7a30c2c8-75fe-4e6a-8475-dc3d38910314",
        "title": "GH-12 add customers",
        "modified_on": "2026-11-10T08:00:00+01:00",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "session_id": "7a30c2c8-75fe-4e6a-8475-dc3d38910314",
        "title": "GH-12 add customers",
        "cwd": "/home/me/simple-erp",
        "modified_on": "2026-11-10T08:00:00+01:00",
        "mentions_pr": True,
    }

    def test_defaults(self) -> None:
        model = SessionCandidate(**self.REQUIRED)
        assert model.cwd == SessionCandidate.model_fields["cwd"].get_default(call_default_factory=True)
        assert model.mentions_pr == SessionCandidate.model_fields["mentions_pr"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = SessionCandidate(**self.FULL)
        assert model.mentions_pr

    @pytest.mark.parametrize("name", ["cwd", "mentions_pr"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = SessionCandidate(**{**self.FULL, name: None})
        assert getattr(model, name) == SessionCandidate.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("session_id", "", SESessionCandidateInvalidSessionId),
            ("session_id", None, SESessionCandidateInvalidSessionId),
            ("title", "", SESessionCandidateInvalidTitle),
            ("title", None, SESessionCandidateInvalidTitle),
            ("cwd", "", SESessionCandidateInvalidCwd),
            ("cwd", 1, SESessionCandidateInvalidCwd),
            ("modified_on", "x", SESessionCandidateInvalidModifiedOn),
            ("modified_on", None, SESessionCandidateInvalidModifiedOn),
            ("mentions_pr", "yes", SESessionCandidateInvalidMentionsPr),
            ("mentions_pr", 1, SESessionCandidateInvalidMentionsPr),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            SessionCandidate(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            SessionCandidate(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = SessionCandidate(**self.FULL)
        assert SessionCandidate.model_validate_json(model.model_dump_json()) == model
