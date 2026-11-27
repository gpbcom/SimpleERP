from __future__ import annotations

# Standard library imports
from http.server import BaseHTTPRequestHandler
from json import dumps
from typing import Dict, Optional

# First-party imports
from erp_testing.models.stand_in.enums import HttpMethod
from erp_testing.models.stand_in.stand_in_answer import StandInAnswer
from erp_testing.models.stand_in.stand_in_request import StandInRequest
from erp_testing.models.stand_in.stand_in_route import StandInRoute
from erp_testing.stand_in.stand_in_http_server import StandInHttpServer


class StandInHandler(BaseHTTPRequestHandler):
    """Answer one request of a stand-in server.

    Notes:
        - Every request is recorded, then answered with the configured answer of its route.
        - **Without a configured answer, a route answers the valid empty value of its real model** (TEST-2).
        - An unknown route answers 404 and a WARNING.
        - The standard library's access log goes to the server's logger instead of stderr.
    """

    ############################
    # Internal Helpers Methods #
    ############################

    def stand_in_server(self) -> StandInHttpServer:
        """Return the HTTP server that owns this handler.

        Returns:
            StandInHttpServer: The server.

        Raises:
            TypeError: When the handler is served by another kind of server.
        """
        if not isinstance(self.server, StandInHttpServer):
            raise TypeError("StandInHandler must be served by a StandInHttpServer.")
        return self.server

    def read_body(self) -> str:
        """Read the request body.

        Returns:
            str: The body, empty when the request has none.
        """
        length = int(self.headers.get("Content-Length") or 0)
        return self.rfile.read(length).decode("utf-8") if length > 0 else ""

    def send_answer(self, status: int, headers: Dict[str, str], body: Optional[str]) -> None:
        """Write one response.

        Args:
            status (int): The HTTP status.
            headers (Dict[str, str]): The response headers.
            body (Optional[str]): The JSON text, or ``None`` for no body.
        """
        payload = body.encode("utf-8") if body is not None else b""
        self.send_response(status)
        names = {name.lower() for name in headers}
        if body is not None and "content-type" not in names:
            self.send_header("Content-Type", "application/json")
        for name, value in headers.items():
            self.send_header(name, value)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def empty_body(self, route: StandInRoute) -> str:
        """Build the valid empty value of a route's real model.

        Args:
            route (StandInRoute): The matched route.

        Returns:
            str: ``[]`` for a list route, else the JSON of the model built with its defaults.
        """
        if route.many:
            return "[]"
        return dumps(route.model().model_dump(mode="json"))

    def handle_method(self, method: HttpMethod) -> None:
        """Record the request, then answer it.

        Args:
            method (HttpMethod): The HTTP method of the request.
        """
        server = self.stand_in_server()
        stand_in = server.stand_in
        request = StandInRequest(
            method=method, path=self.path, headers=dict(self.headers.items()), body=self.read_body()
        )
        stand_in.requests.append(request)
        route = stand_in.routes.get((method, self.path.split("?", 1)[0]))
        if route is None:
            server.logger.warning("No route for %s %s.", method.value, self.path)
            self.send_answer(404, {}, dumps({"detail": "Not found"}))
            return
        answer: Optional[StandInAnswer] = stand_in.answers.get((method, route.path))
        if answer is None:
            server.logger.debug("Answering %s %s with the empty value.", method.value, self.path)
            self.send_answer(200, {}, self.empty_body(route))
            return
        server.logger.debug("Answering %s %s with %d.", method.value, self.path, answer.status)
        self.send_answer(answer.status, answer.headers, None if answer.body is None else dumps(answer.body))

    ############################
    # Publicly Exposed Methods #
    ############################

    def do_GET(self) -> None:  # noqa: N802
        """Answer a GET request."""
        self.handle_method(HttpMethod.GET)

    def do_POST(self) -> None:  # noqa: N802
        """Answer a POST request."""
        self.handle_method(HttpMethod.POST)

    def do_PUT(self) -> None:  # noqa: N802
        """Answer a PUT request."""
        self.handle_method(HttpMethod.PUT)

    def do_PATCH(self) -> None:  # noqa: N802
        """Answer a PATCH request."""
        self.handle_method(HttpMethod.PATCH)

    def do_DELETE(self) -> None:  # noqa: N802
        """Answer a DELETE request."""
        self.handle_method(HttpMethod.DELETE)

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        """Send the access log to the server's logger.

        Args:
            format (str): The ``%`` format of the message.
            *args (object): The values of the format.
        """
        self.stand_in_server().logger.debug(format, *args)
