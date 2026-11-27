from __future__ import annotations

# Standard library imports
from logging import Logger
from threading import Event, Thread
from typing import Dict, List, Optional, Tuple

# First-party imports
from erp_lifecycle.runnables.runnable import Runnable

# Third-party imports
from pydantic import ValidationError

from erp_testing.models.stand_in.enums import HttpMethod
from erp_testing.models.stand_in.exceptions import (
    SEStandInServerNoEmptyValueError,
    SEStandInServerNotStartedError,
    SEStandInServerUnknownRouteError,
)
from erp_testing.models.stand_in.stand_in_answer import StandInAnswer
from erp_testing.models.stand_in.stand_in_request import StandInRequest
from erp_testing.models.stand_in.stand_in_route import StandInRoute
from erp_testing.stand_in.stand_in_handler import StandInHandler
from erp_testing.stand_in.stand_in_http_server import StandInHttpServer


class StandInServer(Runnable):
    """A real local HTTP server that stands in for a service a test depends on.

    Attributes:
        host (str): The address to bind.
        port (int): The port to bind, ``0`` for a free one.
        routes (Dict[Tuple[HttpMethod, str], StandInRoute]): The registered routes.
        answers (Dict[Tuple[HttpMethod, str], StandInAnswer]): The configured answers.
        requests (List[StandInRequest]): The requests received, in order.
        http_server (Optional[StandInHttpServer]): The bound server, ``None`` until ``initialize``.
        thread (Optional[Thread]): The thread that serves, ``None`` until ``initialize``.
        closed (Event): Set when the server is closed, which ends ``run``.
        logger (Logger): Logger instance.

    Notes:
        - **A route answers the valid empty value of its real model until an answer is set** (TEST-2), so a route
          whose model has a required field is refused unless it answers a list.
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 0, logger: Optional[Logger] = None) -> None:
        """Create the server, not yet bound.

        Args:
            host (str): The address to bind.
            port (int): The port to bind, ``0`` for a free one.
            logger (Optional[Logger]): Logger to use. A logger named after the module is created when it is ``None``.
        """
        super().__init__(logger)
        self.host = host
        self.port = port
        self.routes: Dict[Tuple[HttpMethod, str], StandInRoute] = {}
        self.answers: Dict[Tuple[HttpMethod, str], StandInAnswer] = {}
        self.requests: List[StandInRequest] = []
        self.http_server: Optional[StandInHttpServer] = None
        self.thread: Optional[Thread] = None
        self.closed = Event()

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def url(self) -> str:
        """The base URL with the real port.

        Returns:
            str: The URL, such as ``http://127.0.0.1:41233``.

        Raises:
            SEStandInServerNotStartedError: When ``initialize`` has not run.
        """
        if self.http_server is None:
            self.logger.error("The stand-in server is not started.")
            raise SEStandInServerNotStartedError("The stand-in server is not started.")
        return f"http://{self.host}:{self.http_server.server_address[1]}"

    def route(self, route: StandInRoute) -> None:
        """Register a route.

        Args:
            route (StandInRoute): The route to answer.

        Raises:
            SEStandInServerNoEmptyValueError: When the model has no valid empty value and the route is not a list.
        """
        if not route.many:
            try:
                route.model.model_validate({})
            except ValidationError as error:
                self.logger.error("The model of %s %s has no valid empty value.", route.method.value, route.path)
                raise SEStandInServerNoEmptyValueError(
                    f"No valid empty value: {route.model.__name__}. "  # noqa: E501
                    "Give the route a model whose fields all have defaults, or set many."
                ) from error
        self.routes[(route.method, route.path)] = route
        self.logger.debug("Registered %s %s.", route.method.value, route.path)

    def answer(self, method: HttpMethod, path: str, answer: StandInAnswer) -> None:
        """Set the answer of a registered route, replacing the earlier one.

        Args:
            method (HttpMethod): The HTTP method of the route.
            path (str): The path of the route.
            answer (StandInAnswer): What the route answers.

        Raises:
            SEStandInServerUnknownRouteError: When the route is not registered.
        """
        if (method, path) not in self.routes:
            self.logger.error("Cannot answer the unregistered route %s %s.", method.value, path)
            raise SEStandInServerUnknownRouteError(
                f"Unknown route: {method.value} {path}. "  # noqa: E501
                "Register it with route() first."
            )
        self.answers[(method, path)] = answer
        self.logger.debug("Set the answer of %s %s.", method.value, path)

    def initialize(self) -> None:
        """Bind the server and serve it in a background thread, already serving on return."""
        self.closed.clear()
        self.http_server = StandInHttpServer((self.host, self.port), StandInHandler, self, self.logger)
        self.thread = Thread(target=self.http_server.serve_forever, name="stand-in-server", daemon=True)
        self.thread.start()
        self.logger.info("Serving the stand-in server on port %d.", self.http_server.server_address[1])

    def run(self) -> None:
        """Block until the server is closed."""
        self.logger.debug("Waiting for the stand-in server to close.")
        self.closed.wait()

    def close(self) -> None:
        """Stop serving and free the port, safely before ``initialize`` and twice."""
        http_server, thread = self.http_server, self.thread
        self.http_server = None
        self.thread = None
        if http_server is not None:
            if thread is not None:
                http_server.shutdown()
            http_server.server_close()
            self.logger.info("Closed the stand-in server.")
        if thread is not None:
            thread.join(timeout=5)
        self.closed.set()
