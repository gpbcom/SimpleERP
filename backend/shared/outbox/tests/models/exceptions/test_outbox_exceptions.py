from __future__ import annotations

import pytest
from erp_models.exceptions import SEError
from erp_outbox.models import exceptions
from erp_outbox.models.exceptions import SEOutboxError, SEOutboxPublishError, SEOutboxStoreError


class TestOutboxExceptions:
    def test_each_error_is_importable_from_the_package(self) -> None:
        assert exceptions.SEOutboxError is SEOutboxError
        assert exceptions.SEOutboxStoreError is SEOutboxStoreError
        assert exceptions.SEOutboxPublishError is SEOutboxPublishError

    def test_the_base_error_is_a_layer_error_of_erp_models(self) -> None:
        assert issubclass(SEOutboxError, SEError)

    @pytest.mark.parametrize("error_type", [SEOutboxStoreError, SEOutboxPublishError])
    def test_both_errors_are_outbox_errors(self, error_type: type[SEOutboxError]) -> None:
        assert issubclass(error_type, SEOutboxError)
        with pytest.raises(SEOutboxError):
            raise error_type("boom")

    @pytest.mark.parametrize("error_type", [SEOutboxError, SEOutboxStoreError, SEOutboxPublishError])
    def test_an_error_keeps_its_message(self, error_type: type[SEOutboxError]) -> None:
        assert "The outbox table is locked." in str(error_type("The outbox table is locked."))

    @pytest.mark.parametrize("error_type", [SEOutboxStoreError, SEOutboxPublishError])
    def test_raising_an_error_from_a_cause_keeps_the_cause(self, error_type: type[SEOutboxError]) -> None:
        cause = OSError("disk full")
        with pytest.raises(SEOutboxError) as caught:
            raise error_type("Cannot write the event.") from cause
        assert caught.value.__cause__ is cause

    def test_the_package_all_is_sorted_and_lists_exactly_the_three_names(self) -> None:
        assert exceptions.__all__ == sorted(exceptions.__all__)
        assert set(exceptions.__all__) == {"SEOutboxError", "SEOutboxPublishError", "SEOutboxStoreError"}
        assert len(exceptions.__all__) == 3
