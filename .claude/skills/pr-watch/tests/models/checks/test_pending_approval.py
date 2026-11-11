from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.checks.exceptions import (
    SEPendingApprovalInvalidEnvironment,
    SEPendingApprovalInvalidRunId,
    SEPendingApprovalInvalidWaitingSince,
)
from pr_watch.models.checks.pending_approval import PendingApproval


class TestPendingApproval:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "run_id": 601,
        "environment": "qa",
        "waiting_since": "2026-11-10T09:00:00+01:00",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "run_id": 601,
        "environment": "qa",
        "waiting_since": "2026-11-10T09:00:00+01:00",
    }

    def test_defaults(self) -> None:
        model = PendingApproval(**self.REQUIRED)
        assert PendingApproval.model_validate(model.model_dump()) == model

    def test_full_valid_construction(self) -> None:
        model = PendingApproval(**self.FULL)
        assert model.environment == "qa"

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("run_id", 0, SEPendingApprovalInvalidRunId),
            ("run_id", None, SEPendingApprovalInvalidRunId),
            ("environment", "", SEPendingApprovalInvalidEnvironment),
            ("environment", None, SEPendingApprovalInvalidEnvironment),
            ("waiting_since", "09:00", SEPendingApprovalInvalidWaitingSince),
            ("waiting_since", None, SEPendingApprovalInvalidWaitingSince),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            PendingApproval(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PendingApproval(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = PendingApproval(**self.FULL)
        assert PendingApproval.model_validate_json(model.model_dump_json()) == model
