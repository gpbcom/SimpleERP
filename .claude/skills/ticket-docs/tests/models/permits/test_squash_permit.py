from __future__ import annotations

from datetime import UTC, datetime
from typing import Dict

import pytest
from pydantic import JsonValue

from ticket_docs.models.permits.exceptions import (
    SESquashPermitInvalidBranch,
    SESquashPermitInvalidExpiresAt,
    SESquashPermitInvalidHash,
    SESquashPermitInvalidTicket,
)
from ticket_docs.models.permits.squash_permit import SquashPermit


class TestSquashPermit:
    VALID: Dict[str, JsonValue] = {
        "ticket": "GH-1",
        "branch": "feature/GH-1-thing",
        "head": "a" * 40,
        "tree": "b" * 40,
        "expires_at": "2026-11-10T12:30:00+00:00",
    }

    def test_defaults(self) -> None:
        assert SquashPermit.model_validate(self.VALID).ticket == "GH-1"

    def test_full_valid_construction(self) -> None:
        permit = SquashPermit.model_validate({**self.VALID, "branch": " feature/GH-1-thing ", "head": "A" * 40})
        assert (permit.branch, permit.head, permit.tree) == ("feature/GH-1-thing", "a" * 40, "b" * 40)
        assert permit.expires_at == datetime(2026, 11, 10, 12, 30, tzinfo=UTC)

    @pytest.mark.parametrize(
        ("name", "error"),
        [
            ("ticket", SESquashPermitInvalidTicket),
            ("branch", SESquashPermitInvalidBranch),
            ("head", SESquashPermitInvalidHash),
            ("tree", SESquashPermitInvalidHash),
            ("expires_at", SESquashPermitInvalidExpiresAt),
        ],
    )
    def test_none_becomes_the_default(self, name: str, error: type[Exception]) -> None:
        with pytest.raises(error):
            SquashPermit.model_validate({**self.VALID, name: None})

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("ticket", "GH-x", SESquashPermitInvalidTicket),
            ("ticket", 1, SESquashPermitInvalidTicket),
            ("branch", " ", SESquashPermitInvalidBranch),
            ("head", "abc", SESquashPermitInvalidHash),
            ("tree", "z" * 40, SESquashPermitInvalidHash),
            ("expires_at", "tomorrow", SESquashPermitInvalidExpiresAt),
            ("expires_at", "2026-11-10T12:30:00", SESquashPermitInvalidExpiresAt),
            ("expires_at", 3, SESquashPermitInvalidExpiresAt),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            SquashPermit.model_validate({**self.VALID, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            SquashPermit.model_validate({**self.VALID, "other": 1})

    def test_round_trip(self) -> None:
        permit = SquashPermit.model_validate(self.VALID)
        assert SquashPermit.model_validate_json(permit.model_dump_json()) == permit
