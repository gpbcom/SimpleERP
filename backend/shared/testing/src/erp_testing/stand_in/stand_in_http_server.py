from __future__ import annotations

# Standard library imports
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from logging import Logger, getLogger
from typing import TYPE_CHECKING, Optional, Tuple, Type

if TYPE_CHECKING:
    from erp_testing.stand_in.stand_in_server import StandInServer


class StandInHttpServer(ThreadingHTTPServer):
    """The HTTP server of a stand-in, which gives its handlers the stand-in that owns the routes.

    Attributes:
        stand_in (StandInServer): The stand-in server whose routes, answers and requests the handlers use.
        logger (Logger): Logger instance.
    """

    daemon_threads = True

    def __init__(
        self,
        address: Tuple[str, int],
        handler: Type[BaseHTTPRequestHandler],
        stand_in: StandInServer,
        logger: Optional[Logger] = None,
    ) -> None:
        """Bind the server.

        Args:
            address (Tuple[str, int]): The host and the port to bind. Port ``0`` picks a free one.
            handler (Type[BaseHTTPRequestHandler]): The class that handles each request.
            stand_in (StandInServer): The stand-in server that owns the routes.
            logger (Optional[Logger]): Logger to use. A logger named after the module is created when it is ``None``.
        """
        self.stand_in = stand_in
        self.logger = logger if logger else getLogger(__name__)
        super().__init__(address, handler)
        self.logger.debug("Bound the stand-in HTTP server on port %d.", self.server_address[1])
