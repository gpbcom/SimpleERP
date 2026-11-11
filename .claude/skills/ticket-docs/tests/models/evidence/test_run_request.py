from __future__ import annotations

from typing import Dict

import pytest
from pydantic import JsonValue

from ticket_docs.models.enums import Expectation, RunKind, RunPlace
from ticket_docs.models.evidence.exceptions import (
    SERunRequestInvalidCheck,
    SERunRequestInvalidCommand,
    SERunRequestInvalidExpectation,
    SERunRequestInvalidKind,
    SERunRequestInvalidRunId,
    SERunRequestInvalidTicket,
    SERunRequestInvalidWhat,
    SERunRequestInvalidWhere,
    SERunRequestNoCommand,
)
from ticket_docs.models.evidence.run_request import RunRequest


class TestRunRequest:
    VALID: Dict[str, JsonValue] = {
        "ticket": "GH-12",
        "kind": "unit",
        "where": "local",
        "check": "tdd-red-storage",
        "what": "The storage tests before the code",
        "command": ["pytest", "-q", "tests/storage"],
    }

    def test_defaults(self) -> None:
        request = RunRequest.model_validate(self.VALID)
        assert (request.expectation, request.run_id) == (Expectation.GREEN, None)

    def test_full_valid_construction(self) -> None:
        request = RunRequest.model_validate(
            {**self.VALID, "command": [], "run_id": "123456", "expectation": "red", "where": "dev", "kind": "e2e"}
        )
        assert (request.kind, request.where, request.expectation) == (RunKind.E2E, RunPlace.DEV, Expectation.RED)
        assert request.run_id == "123456"

    @pytest.mark.parametrize("name", ["expectation", "run_id"])
    def test_none_becomes_the_default(self, name: str) -> None:
        request = RunRequest.model_validate({**self.VALID, name: None})
        assert getattr(request, name) == RunRequest.model_fields[name].get_default()

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("ticket", "ARE-1", SERunRequestInvalidTicket),
            ("kind", "smoke", SERunRequestInvalidKind),
            ("where", "prod", SERunRequestInvalidWhere),
            ("check", "Tdd Red", SERunRequestInvalidCheck),
            ("check", "../escape", SERunRequestInvalidCheck),
            ("what", " ", SERunRequestInvalidWhat),
            ("expectation", "amber", SERunRequestInvalidExpectation),
            ("command", "pytest -q", SERunRequestInvalidCommand),
            ("command", ["pytest", 3], SERunRequestInvalidCommand),
            ("run_id", "12a", SERunRequestInvalidRunId),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            RunRequest.model_validate({**self.VALID, name: value})

    @pytest.mark.parametrize(("command", "run_id"), [([], None), (["pytest"], "12")])
    def test_needs_exactly_one_command_or_run(self, command: JsonValue, run_id: JsonValue) -> None:
        with pytest.raises(SERunRequestNoCommand):
            RunRequest.model_validate({**self.VALID, "command": command, "run_id": run_id})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            RunRequest.model_validate({**self.VALID, "other": 1})

    def test_round_trip(self) -> None:
        request = RunRequest.model_validate(self.VALID)
        assert RunRequest.model_validate(request.model_dump()) == request
