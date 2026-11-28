from __future__ import annotations

import pytest
from erp_metering.models.calls.exceptions import SEInvalidReservationException, SEReservationInvalidReservationId
from erp_metering.models.calls.reservation import Reservation
from pydantic import JsonValue, ValidationError


class TestReservation:
    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            Reservation.model_validate({})

    def test_full_valid_construction(self) -> None:
        assert Reservation(reservation_id="  res-1  ").reservation_id == "res-1"

    def test_none_becomes_the_default(self) -> None:
        with pytest.raises(SEReservationInvalidReservationId):
            Reservation.model_validate({"reservation_id": None})

    @pytest.mark.parametrize("value", ["", "   ", True, 12, 1.5, ["res-1"], {"a": 1}])
    def test_rejects_bad_values(self, value: JsonValue) -> None:
        with pytest.raises(SEReservationInvalidReservationId):
            Reservation.model_validate({"reservation_id": value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            Reservation.model_validate({"reservation_id": "res-1", "other": "x"})

    def test_round_trip(self) -> None:
        reservation = Reservation(reservation_id="res-1")
        assert Reservation.model_validate(reservation.model_dump(mode="json")) == reservation
        assert Reservation.model_validate_json(reservation.model_dump_json()) == reservation

    def test_the_field_exception_belongs_to_the_model_hierarchy(self) -> None:
        assert issubclass(SEReservationInvalidReservationId, SEInvalidReservationException)

    def test_assignment_is_refused(self) -> None:
        reservation = Reservation(reservation_id="res-1")
        with pytest.raises(ValidationError):
            reservation.reservation_id = "res-2"
