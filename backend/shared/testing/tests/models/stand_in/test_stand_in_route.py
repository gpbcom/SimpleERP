from __future__ import annotations

from typing import Dict, Type

import pytest
from erp_testing.models.stand_in.enums import HttpMethod
from erp_testing.models.stand_in.exceptions import (
    SEStandInRouteInvalidMany,
    SEStandInRouteInvalidMethod,
    SEStandInRouteInvalidModel,
    SEStandInRouteInvalidPath,
)
from erp_testing.models.stand_in.stand_in_answer import StandInAnswer
from erp_testing.models.stand_in.stand_in_route import StandInRoute
from pydantic import ValidationError


class TestStandInRoute:
    def test_defaults(self) -> None:
        route = StandInRoute(method=HttpMethod.GET, path="/customers", model=StandInAnswer)
        assert route.method == HttpMethod.GET
        assert route.path == "/customers"
        assert route.model is StandInAnswer
        assert route.many is False

    def test_full_valid_construction(self) -> None:
        route = StandInRoute(method="POST", path="  /customers/1  ", model=StandInAnswer, many=True)
        assert route.method == HttpMethod.POST
        assert route.path == "/customers/1"
        assert route.model is StandInAnswer
        assert route.many is True

    @pytest.mark.parametrize("name", ["many"])
    def test_none_becomes_the_default(self, name: str) -> None:
        route = StandInRoute.model_validate({"method": "GET", "path": "/a", "model": StandInAnswer, name: None})
        assert route.many is False

    @pytest.mark.parametrize("method", ["GET", "POST", "PUT", "PATCH", "DELETE"])
    def test_every_http_method_is_accepted_as_a_string(self, method: str) -> None:
        route = StandInRoute(method=method, path="/a", model=StandInAnswer)
        assert route.method == HttpMethod(method)

    @pytest.mark.parametrize(
        ("field", "value", "error"),
        [
            ("method", "TRACE", SEStandInRouteInvalidMethod),
            ("method", "get", SEStandInRouteInvalidMethod),
            ("method", None, SEStandInRouteInvalidMethod),
            ("method", 1, SEStandInRouteInvalidMethod),
            ("path", "customers", SEStandInRouteInvalidPath),
            ("path", "", SEStandInRouteInvalidPath),
            ("path", "   ", SEStandInRouteInvalidPath),
            ("path", None, SEStandInRouteInvalidPath),
            ("path", 12, SEStandInRouteInvalidPath),
            ("model", None, SEStandInRouteInvalidModel),
            ("model", "StandInAnswer", SEStandInRouteInvalidModel),
            ("model", dict, SEStandInRouteInvalidModel),
            ("model", StandInAnswer(), SEStandInRouteInvalidModel),
            ("many", "yes", SEStandInRouteInvalidMany),
            ("many", 1, SEStandInRouteInvalidMany),
        ],
    )
    def test_rejects_bad_values(self, field: str, value: object, error: Type[Exception]) -> None:
        data: Dict[str, object] = {"method": "GET", "path": "/a", "model": StandInAnswer}
        data[field] = value
        with pytest.raises(error):
            StandInRoute.model_validate(data)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            StandInRoute.model_validate({"method": "GET", "path": "/a", "model": StandInAnswer, "unknown": 1})

    def test_round_trip(self) -> None:
        route = StandInRoute(method=HttpMethod.PUT, path="/a", model=StandInAnswer, many=True)
        assert StandInRoute.model_validate(route.model_dump()) == route

    def test_assignment_is_refused_because_the_model_is_frozen(self) -> None:
        route = StandInRoute(method=HttpMethod.GET, path="/a", model=StandInAnswer)
        with pytest.raises(ValidationError):
            route.path = "/b"
