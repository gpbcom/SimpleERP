from __future__ import annotations

# Standard library imports
import json
from decimal import Decimal
from http.server import BaseHTTPRequestHandler
from typing import TYPE_CHECKING, Optional, Tuple
from uuid import uuid4

# Third-party imports
from erp_metering.models.calls.budget_check import BudgetCheck
from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.calls.reservation import Reservation
from erp_metering.models.calls.settlement import Settlement

if TYPE_CHECKING:
    from backend.shared.metering.tests.stand_in.stand_in_metering_server import StandInMeteringServer


class StandInMeteringHandler(BaseHTTPRequestHandler):
    """Answer the four routes of the metering API from the state of a ``StandInMeteringServer``."""

    def __init__(self, owner: StandInMeteringServer, *args: object, **kwargs: object) -> None:
        self.owner = owner
        super().__init__(*args, **kwargs)  # type: ignore[arg-type]

    def log_message(self, format: str, *args: object) -> None:
        return None

    def read_body(self) -> bytes:
        return self.rfile.read(int(self.headers.get("Content-Length", "0")))

    def reply(self, status: int, body: Optional[str] = None) -> None:
        payload = body.encode("utf-8") if body is not None else b""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def route(self, method: str) -> Tuple[Optional[str], Optional[str]]:
        """Record the request and return the route name and the reservation id, if any."""
        with self.owner.lock:
            self.owner.requests.append((method, self.path))
        if not self.owner.available:
            return "unavailable", None
        parts = self.path.strip("/").split("/")
        if method == "POST" and parts == ["v1", "budget-checks"]:
            return "check", None
        if method == "POST" and parts == ["v1", "reservations"]:
            return "reserve", None
        if method == "POST" and len(parts) == 4 and parts[:2] == ["v1", "reservations"] and parts[3] == "settlement":
            return "settle", parts[2]
        if method == "DELETE" and len(parts) == 3 and parts[:2] == ["v1", "reservations"]:
            return "release", parts[2]
        return None, None

    def do_POST(self) -> None:
        body = self.read_body()
        name, reservation_id = self.route("POST")
        if name == "unavailable":
            self.reply(503, json.dumps({"detail": "unavailable"}))
        elif name == "check":
            call = PaidCall.model_validate_json(body)
            within = call.estimated_cost.amount <= self.owner.remaining
            self.reply(200, BudgetCheck(within_budget=within).model_dump_json())
        elif name == "reserve":
            self.reserve(PaidCall.model_validate_json(body))
        elif name == "settle" and reservation_id is not None:
            self.settle(reservation_id, Settlement.model_validate_json(body))
        else:
            self.reply(404, json.dumps({"detail": "not found"}))

    def do_DELETE(self) -> None:
        name, reservation_id = self.route("DELETE")
        if name == "unavailable":
            self.reply(503, json.dumps({"detail": "unavailable"}))
        elif name == "release" and reservation_id is not None:
            with self.owner.lock:
                call = self.owner.reservations.pop(reservation_id, None)
                if call is not None:
                    self.owner.released.append(reservation_id)
                    self.owner.remaining += call.estimated_cost.amount
            self.reply(204 if call is not None else 404)
        else:
            self.reply(404, json.dumps({"detail": "not found"}))

    def reserve(self, call: PaidCall) -> None:
        amount = call.estimated_cost.amount
        reservation_id = uuid4().hex
        with self.owner.lock:
            refused = amount > self.owner.remaining and not call.legal_duty
            if not refused:
                self.owner.remaining -= amount
                self.owner.reservations[reservation_id] = call
        if refused:
            self.reply(409, json.dumps({"detail": "budget exhausted"}))
        else:
            self.reply(201, Reservation(reservation_id=reservation_id).model_dump_json())

    def settle(self, reservation_id: str, settlement: Settlement) -> None:
        with self.owner.lock:
            call = self.owner.reservations.pop(reservation_id, None)
            if call is not None:
                self.owner.settlements.append(settlement)
                actual: Decimal = settlement.actual_cost.amount
                self.owner.remaining += call.estimated_cost.amount - actual
        if call is None:
            self.reply(404, json.dumps({"detail": "unknown reservation"}))
        else:
            self.reply(200, settlement.model_dump_json())
