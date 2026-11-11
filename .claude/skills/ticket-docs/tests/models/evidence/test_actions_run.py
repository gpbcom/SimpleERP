from __future__ import annotations

import json
from datetime import UTC, datetime
from typing import Dict

import pytest
from pydantic import JsonValue

from ticket_docs.models.enums import RunConclusion
from ticket_docs.models.evidence.actions_run import ActionsRun
from ticket_docs.models.evidence.exceptions import (
    SEActionsRunInvalidConclusion,
    SEActionsRunInvalidCreatedAt,
    SEActionsRunInvalidHeadSha,
    SEActionsRunInvalidText,
)


class TestActionsRun:
    GH_JSON: Dict[str, JsonValue] = {
        "conclusion": "success",
        "headSha": "c" * 40,
        "headBranch": "feature/GH-1-thing",
        "url": "https://github.com/gpbcom/simple-erp/actions/runs/42",
        "displayTitle": "stage dev",
        "createdAt": "2026-11-10T09:30:00Z",
    }

    def test_defaults(self) -> None:
        run = ActionsRun.model_validate({**self.GH_JSON, "conclusion": None})
        assert run.conclusion is RunConclusion.PENDING

    def test_full_valid_construction(self) -> None:
        run = ActionsRun.model_validate_json(json.dumps(self.GH_JSON))
        assert run.conclusion is RunConclusion.SUCCESS
        assert run.head_sha == "c" * 40
        assert run.head_branch == "feature/GH-1-thing"
        assert run.created_at == datetime(2026, 11, 10, 9, 30, tzinfo=UTC)
        assert run.succeeded

    @pytest.mark.parametrize("name", ["conclusion"])
    def test_none_becomes_the_default(self, name: str) -> None:
        assert ActionsRun.model_validate({**self.GH_JSON, name: None}).conclusion is RunConclusion.PENDING

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("conclusion", "exploded", SEActionsRunInvalidConclusion),
            ("headSha", "abc", SEActionsRunInvalidHeadSha),
            ("headBranch", "", SEActionsRunInvalidText),
            ("url", 3, SEActionsRunInvalidText),
            ("displayTitle", None, SEActionsRunInvalidText),
            ("createdAt", "yesterday", SEActionsRunInvalidCreatedAt),
            ("createdAt", 12, SEActionsRunInvalidCreatedAt),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            ActionsRun.model_validate({**self.GH_JSON, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            ActionsRun.model_validate({**self.GH_JSON, "status": "completed"})

    def test_round_trip(self) -> None:
        run = ActionsRun.model_validate(self.GH_JSON)
        assert ActionsRun.model_validate(run.model_dump(by_alias=True)) == run

    def test_a_failed_run_did_not_succeed(self) -> None:
        assert not ActionsRun.model_validate({**self.GH_JSON, "conclusion": "failure"}).succeeded
