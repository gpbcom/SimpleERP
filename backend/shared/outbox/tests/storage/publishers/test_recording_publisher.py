from __future__ import annotations

import pytest
from erp_models.events.event_envelope import EventEnvelope
from erp_models.ids.company_id import CompanyId
from erp_outbox.storage.publishers.publisher import Publisher
from erp_outbox.storage.publishers.recording_publisher import RecordingPublisher


class TestRecordingPublisher:
    def an_envelope(self, event_type: str = "audit.entry.appended") -> EventEnvelope:
        return EventEnvelope(event_type=event_type, company_id=CompanyId(value="C-12"))

    def test_a_new_publisher_has_published_nothing(self) -> None:
        assert RecordingPublisher().published == []

    def test_envelopes_are_recorded_in_call_order(self) -> None:
        publisher = RecordingPublisher()
        envelopes = [self.an_envelope(f"synthetic.event.{index}") for index in range(3)]

        for envelope in envelopes:
            publisher.publish(envelope)

        assert publisher.published == envelopes

    def test_the_same_envelope_published_twice_is_recorded_twice(self) -> None:
        publisher = RecordingPublisher()
        envelope = self.an_envelope()

        publisher.publish(envelope)
        publisher.publish(envelope)

        assert publisher.published == [envelope, envelope]

    def test_a_recording_publisher_is_a_publisher(self) -> None:
        assert isinstance(RecordingPublisher(), Publisher)

    def test_the_publisher_interface_cannot_be_instantiated(self) -> None:
        with pytest.raises(TypeError):
            Publisher()  # type: ignore[abstract]
