from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Dict

import pytest
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.events.event_envelope import EventEnvelope
from erp_models.events.exceptions import (
    SEEventEnvelopeInvalidCompanyId,
    SEEventEnvelopeInvalidEventId,
    SEEventEnvelopeInvalidEventType,
    SEEventEnvelopeInvalidOccurredAt,
    SEEventEnvelopeInvalidPayload,
    SEInvalidEventEnvelopeException,
)
from erp_models.ids.company_id import CompanyId
from erp_models.ids.record_id import RecordId
from erp_models.times.utc_timestamp import UtcTimestamp
from pydantic import JsonValue, ValidationError


class TestEventEnvelope:
    def test_defaults(self) -> None:
        before = datetime.now(UTC)

        envelope = EventEnvelope(event_type="audit.entry.appended", company_id=CompanyId(value="C-12"))

        assert isinstance(envelope.event_id, RecordId)
        assert envelope.event_id.value
        assert before <= envelope.occurred_at.instant <= datetime.now(UTC) + timedelta(seconds=1)
        assert envelope.occurred_at.instant.utcoffset() == timedelta(0)
        assert envelope.payload == {}

    def test_it_is_a_frozen_model_of_erp_models(self) -> None:
        assert issubclass(EventEnvelope, FrozenErpModel)

    def test_full_valid_construction(self) -> None:
        envelope = EventEnvelope(
            event_id=RecordId(value="E-1"),
            event_type="  audit.entry.appended  ",
            company_id=CompanyId(value="C-12"),
            occurred_at=UtcTimestamp(instant=datetime(2026, 1, 2, 3, 4, 5, tzinfo=UTC)),
            payload={"entry": "A-1", "count": 2, "nested": {"ok": True}},
        )

        assert envelope.event_id == RecordId(value="E-1")
        assert envelope.event_type == "audit.entry.appended"
        assert envelope.company_id == CompanyId(value="C-12")
        assert envelope.occurred_at.instant == datetime(2026, 1, 2, 3, 4, 5, tzinfo=UTC)
        assert envelope.payload == {"entry": "A-1", "count": 2, "nested": {"ok": True}}

    @pytest.mark.parametrize("name", ["event_id", "occurred_at", "payload"])
    def test_none_becomes_the_default(self, name: str) -> None:
        envelope = EventEnvelope.model_validate(
            {"event_type": "audit.entry.appended", "company_id": {"value": "C-12"}, name: None}
        )

        assert getattr(envelope, name) is not None

    def test_two_default_ids_differ(self) -> None:
        first = EventEnvelope(event_type="audit.entry.appended", company_id=CompanyId(value="C-12"))
        second = EventEnvelope(event_type="audit.entry.appended", company_id=CompanyId(value="C-12"))

        assert first.event_id != second.event_id

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("event_id", 12, SEEventEnvelopeInvalidEventId),
            ("event_id", True, SEEventEnvelopeInvalidEventId),
            ("event_id", "", SEEventEnvelopeInvalidEventId),
            ("event_id", {"value": "  "}, SEEventEnvelopeInvalidEventId),
            ("event_type", "", SEEventEnvelopeInvalidEventType),
            ("event_type", "   ", SEEventEnvelopeInvalidEventType),
            ("event_type", 12, SEEventEnvelopeInvalidEventType),
            ("event_type", True, SEEventEnvelopeInvalidEventType),
            ("event_type", None, SEEventEnvelopeInvalidEventType),
            ("company_id", 12, SEEventEnvelopeInvalidCompanyId),
            ("company_id", True, SEEventEnvelopeInvalidCompanyId),
            ("company_id", "", SEEventEnvelopeInvalidCompanyId),
            ("company_id", {"value": "  "}, SEEventEnvelopeInvalidCompanyId),
            ("occurred_at", 12, SEEventEnvelopeInvalidOccurredAt),
            ("occurred_at", True, SEEventEnvelopeInvalidOccurredAt),
            ("occurred_at", {"instant": "not a time"}, SEEventEnvelopeInvalidOccurredAt),
            ("occurred_at", {"instant": "2026-01-02T03:04:05"}, SEEventEnvelopeInvalidOccurredAt),
            ("payload", "abc", SEEventEnvelopeInvalidPayload),
            ("payload", [1, 2], SEEventEnvelopeInvalidPayload),
            ("payload", 12, SEEventEnvelopeInvalidPayload),
            ("payload", True, SEEventEnvelopeInvalidPayload),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        data: Dict[str, JsonValue] = {"event_type": "audit.entry.appended", "company_id": {"value": "C-12"}}
        data[name] = value

        with pytest.raises(error):
            EventEnvelope.model_validate(data)

    @pytest.mark.parametrize(
        "error",
        [
            SEEventEnvelopeInvalidEventId,
            SEEventEnvelopeInvalidEventType,
            SEEventEnvelopeInvalidCompanyId,
            SEEventEnvelopeInvalidOccurredAt,
            SEEventEnvelopeInvalidPayload,
        ],
    )
    def test_every_field_exception_is_an_envelope_exception(self, error: type[Exception]) -> None:
        assert issubclass(error, SEInvalidEventEnvelopeException)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            EventEnvelope.model_validate(
                {"event_type": "audit.entry.appended", "company_id": {"value": "C-12"}, "unknown": 1}
            )

    def test_assigning_a_field_of_a_built_envelope_is_refused(self) -> None:
        envelope = EventEnvelope(event_type="audit.entry.appended", company_id=CompanyId(value="C-12"))

        with pytest.raises(ValidationError):
            envelope.event_type = "other.type"  # type: ignore[misc]

    def test_round_trip(self) -> None:
        envelope = EventEnvelope(
            event_id=RecordId(value="E-1"),
            event_type="audit.entry.appended",
            company_id=CompanyId(value="C-12"),
            occurred_at=UtcTimestamp(instant=datetime(2026, 1, 2, 3, 4, 5, tzinfo=UTC)),
            payload={"entry": "A-1", "items": [1, 2]},
        )

        assert EventEnvelope.model_validate_json(envelope.model_dump_json()) == envelope
