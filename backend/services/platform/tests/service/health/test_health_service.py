from __future__ import annotations

import logging

import pytest
from erp_platform.models.health.enums import HealthState
from erp_platform.models.health.health_status import HealthStatus
from erp_platform.service.health.health_service import HealthService


class TestHealthService:
    def test_the_check_answers_ok(self) -> None:
        assert HealthService().check() == HealthStatus(status=HealthState.OK)

    def test_two_checks_give_equal_values(self) -> None:
        service = HealthService()

        assert service.check() == service.check()

    def test_the_check_writes_a_log_line_through_the_given_logger(self, caplog: pytest.LogCaptureFixture) -> None:
        logger = logging.getLogger("tests.health_service")

        with caplog.at_level(logging.DEBUG, logger="tests.health_service"):
            HealthService(logger).check()

        records = [record for record in caplog.records if record.name == "tests.health_service"]
        assert records
        assert all(record.levelno in (logging.DEBUG, logging.INFO) for record in records)
