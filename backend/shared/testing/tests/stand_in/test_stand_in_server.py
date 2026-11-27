from __future__ import annotations

import json
import logging
import threading
import urllib.error
import urllib.request
from typing import Dict, Iterator, List, Optional, Tuple

import pytest
from erp_testing.logs.log_capture import LogCapture
from erp_testing.models.stand_in.enums import HttpMethod
from erp_testing.models.stand_in.exceptions import (
    SEStandInServerNoEmptyValueError,
    SEStandInServerNotStartedError,
    SEStandInServerUnknownRouteError,
)
from erp_testing.models.stand_in.stand_in_answer import StandInAnswer
from erp_testing.models.stand_in.stand_in_request import StandInRequest
from erp_testing.models.stand_in.stand_in_route import StandInRoute
from erp_testing.stand_in.stand_in_server import StandInServer


class TestStandInServer:
    @pytest.fixture
    def server(self) -> Iterator[StandInServer]:
        server = StandInServer()
        server.initialize()
        try:
            yield server
        finally:
            server.close()

    def fetch(
        self,
        server: StandInServer,
        path: str,
        method: str = "GET",
        data: Optional[bytes] = None,
    ) -> Tuple[int, Dict[str, str], bytes]:
        request = urllib.request.Request(server.url + path, data=data, method=method)
        try:
            with urllib.request.urlopen(request, timeout=5) as response:
                return response.status, dict(response.headers), response.read()
        except urllib.error.HTTPError as error:
            return error.code, dict(error.headers), error.read()

    def test_the_url_carries_the_real_port_once_started(self, server: StandInServer) -> None:
        assert server.url.startswith("http://127.0.0.1:")
        assert int(server.url.rsplit(":", 1)[1]) > 0

    def test_the_url_is_refused_before_initialize(self) -> None:
        with pytest.raises(SEStandInServerNotStartedError):
            _ = StandInServer().url

    def test_close_before_initialize_is_safe(self) -> None:
        StandInServer().close()

    def test_close_twice_is_safe(self) -> None:
        server = StandInServer()
        server.initialize()
        server.close()
        server.close()

    def test_close_frees_the_port(self) -> None:
        server = StandInServer()
        server.initialize()
        url = server.url
        server.close()
        with pytest.raises(urllib.error.URLError):
            urllib.request.urlopen(url + "/anything", timeout=2)

    def test_the_server_is_serving_when_initialize_returns(self, server: StandInServer) -> None:
        status, _, _ = self.fetch(server, "/nothing")
        assert status == 404

    @pytest.mark.parametrize("method", list(HttpMethod))
    def test_an_unanswered_route_gives_the_empty_model_for_every_method(
        self, server: StandInServer, method: HttpMethod
    ) -> None:
        server.route(StandInRoute(method=method, path="/things", model=StandInAnswer))
        data = b"{}" if method in {HttpMethod.POST, HttpMethod.PUT, HttpMethod.PATCH} else None
        status, headers, body = self.fetch(server, "/things", method=method.value, data=data)
        assert status == 200
        assert headers["Content-Type"].startswith("application/json")
        assert StandInAnswer.model_validate(json.loads(body)) == StandInAnswer()

    def test_an_unanswered_route_of_many_gives_an_empty_list(self, server: StandInServer) -> None:
        server.route(StandInRoute(method=HttpMethod.GET, path="/things", model=StandInRequest, many=True))
        status, headers, body = self.fetch(server, "/things")
        assert status == 200
        assert headers["Content-Type"].startswith("application/json")
        assert json.loads(body) == []

    def test_a_configured_answer_is_returned_with_status_headers_and_body(self, server: StandInServer) -> None:
        server.route(StandInRoute(method=HttpMethod.GET, path="/things", model=StandInAnswer))
        server.answer(
            HttpMethod.GET,
            "/things",
            StandInAnswer(status=201, body={"a": [1, 2]}, headers={"X-Custom": "yes"}),
        )
        status, headers, body = self.fetch(server, "/things")
        assert status == 201
        assert headers["X-Custom"] == "yes"
        assert json.loads(body) == {"a": [1, 2]}

    def test_a_later_answer_replaces_the_earlier_one(self, server: StandInServer) -> None:
        server.route(StandInRoute(method=HttpMethod.GET, path="/things", model=StandInAnswer))
        server.answer(HttpMethod.GET, "/things", StandInAnswer(status=418, body={"a": 1}))
        server.answer(HttpMethod.GET, "/things", StandInAnswer(status=202, body={"a": 2}))
        status, _, body = self.fetch(server, "/things")
        assert status == 202
        assert json.loads(body) == {"a": 2}

    def test_a_model_with_a_required_field_is_refused_unless_many(self, server: StandInServer) -> None:
        with pytest.raises(SEStandInServerNoEmptyValueError):
            server.route(StandInRoute(method=HttpMethod.GET, path="/requests", model=StandInRequest))

    def test_answering_an_unregistered_route_is_refused(self, server: StandInServer) -> None:
        with pytest.raises(SEStandInServerUnknownRouteError):
            server.answer(HttpMethod.GET, "/missing", StandInAnswer())

    def test_a_route_answers_only_its_own_method(self, server: StandInServer) -> None:
        server.route(StandInRoute(method=HttpMethod.GET, path="/things", model=StandInAnswer))
        status, _, _ = self.fetch(server, "/things", method="DELETE")
        assert status == 404

    def test_an_unknown_path_answers_404_and_logs_a_warning(self) -> None:
        logger = logging.getLogger("test_stand_in_server.unknown_path")
        server = StandInServer(logger=logger)
        server.initialize()
        try:
            with LogCapture("test_stand_in_server.unknown_path") as capture:
                status, _, _ = self.fetch(server, "/unknown")
            assert status == 404
            assert capture.messages(logging.WARNING)
            assert capture.contains("/unknown", logging.WARNING)
        finally:
            server.close()

    def test_every_request_is_recorded_in_order(self, server: StandInServer) -> None:
        server.route(StandInRoute(method=HttpMethod.POST, path="/things", model=StandInAnswer))
        self.fetch(server, "/things?page=2", method="POST", data=b'{"x": 1}')
        self.fetch(server, "/other")
        requests: List[StandInRequest] = server.requests
        assert [(request.method, request.path) for request in requests] == [
            (HttpMethod.POST, "/things?page=2"),
            (HttpMethod.GET, "/other"),
        ]
        assert requests[0].body == '{"x": 1}'

    def test_run_blocks_until_close(self) -> None:
        server = StandInServer()
        server.initialize()
        runner = threading.Thread(target=server.run)
        runner.start()
        runner.join(timeout=0.3)
        assert runner.is_alive()
        server.close()
        runner.join(timeout=5)
        assert not runner.is_alive()
