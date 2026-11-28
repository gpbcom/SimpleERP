from __future__ import annotations

# Standard library imports
from decimal import Decimal
from functools import partial
from http.server import ThreadingHTTPServer
from threading import Lock, Thread
from typing import Dict, List, Optional, Tuple

# Third-party imports
from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.calls.settlement import Settlement

# First-party imports
from backend.shared.metering.tests.stand_in.stand_in_metering_handler import StandInMeteringHandler


class StandInMeteringServer:
    """A real HTTP server on 127.0.0.1 that stands for the metering API, with its budget in memory."""

    def __init__(self, remaining: Decimal = Decimal("0")) -> None:
        self.remaining = remaining
        self.available = True
        self.requests: List[Tuple[str, str]] = []
        self.reservations: Dict[str, PaidCall] = {}
        self.settlements: List[Settlement] = []
        self.released: List[str] = []
        self.lock = Lock()
        self.httpd: Optional[ThreadingHTTPServer] = None
        self.thread: Optional[Thread] = None

    @property
    def url(self) -> str:
        assert self.httpd is not None, "serve() has not been called."
        return f"http://127.0.0.1:{self.httpd.server_address[1]}"

    def serve(self) -> None:
        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), partial(StandInMeteringHandler, self))
        self.thread = Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()

    def close(self) -> None:
        if self.httpd is not None:
            self.httpd.shutdown()
            self.httpd.server_close()
            self.httpd = None
        if self.thread is not None:
            self.thread.join(timeout=5)
            self.thread = None
