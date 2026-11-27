from __future__ import annotations

from typing import Dict, Type

import pytest
from erp_testing.models.stand_in.enums import HttpMethod
from erp_testing.models.stand_in.exceptions import (
    SEStandInRequestInvalidBody,
    SEStandInRequestInvalidHeaders,
    SEStandInRequestInvalidMethod,
    SEStandInRequestInvalidPath,
)
from erp_testing.models.stand_in.stand_in_request import StandInRequest
from pydantic import ValidationError


class TestStandInRequest:
    def test_defaults(self) -> None:
        request = StandInRequest(method=HttpMethod.GET, path="/customers")
        assert request.method == HttpMethod.GET
        assert request.path == "/customers"
        assert request.headers == {}
        assert request.body == ""

    def test_full_valid_construction(self) -> None:
        request = StandInRequest(
            method="POST", path="/customers?page=2", headers={"content-type": "application/json"}, body='{"a": 1}'
        )
        assert request.method == HttpMethod.POST
        assert request.path == "/customers?page=2"
        assert request.headers == {"content-type": "application/json"}
        assert request.body == '{"a": 1}'

    @pytest.mark.parametrize(("name", "expected"), [("headers", {}), ("body", "")])
    def test_none_becomes_the_default(self, name: str, expected: object) -> None:
        request = StandInRequest.model_validate({"method": "GET", "path": "/a", name: None})
        assert getattr(request, name) == expected

    @pytest.mark.parametrize(
        ("field", "value", "error"),
        [
            ("method", "TRACE", SEStandInRequestInvalidMethod),
            ("method", None, SEStandInRequestInvalidMethod),
            ("method", 1, SEStandInRequestInvalidMethod),
            ("path", "customers", SEStandInRequestInvalidPath),
            ("path", "", SEStandInRequestInvalidPath),
            ("path", None, SEStandInRequestInvalidPath),
            ("path", 5, SEStandInRequestInvalidPath),
            ("headers", "a: b", SEStandInRequestInvalidHeaders),
            ("headers", {"a": 1}, SEStandInRequestInvalidHeaders),
            ("headers", {1: "a"}, SEStandInRequestInvalidHeaders),
            ("body", 12, SEStandInRequestInvalidBody),
            ("body", b"raw", SEStandInRequestInvalidBody),
            ("body", {"a": 1}, SEStandInRequestInvalidBody),
        ],
    )
    def test_rejects_bad_values(self, field: str, value: object, error: Type[Exception]) -> None:
        data: Dict[str, object] = {"method": "GET", "path": "/a"}
        data[field] = value
        with pytest.raises(error):
            StandInRequest.model_validate(data)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            StandInRequest.model_validate({"method": "GET", "path": "/a", "unknown": 1})

    def test_round_trip(self) -> None:
        request = StandInRequest(method=HttpMethod.PATCH, path="/a?b=1", headers={"x": "y"}, body="text")
        assert StandInRequest.model_validate(request.model_dump()) == request
        assert StandInRequest.model_validate_json(request.model_dump_json()) == request

    def test_assignment_is_refused_because_the_model_is_frozen(self) -> None:
        request = StandInRequest(method=HttpMethod.GET, path="/a")
        with pytest.raises(ValidationError):
            request.body = "x"
