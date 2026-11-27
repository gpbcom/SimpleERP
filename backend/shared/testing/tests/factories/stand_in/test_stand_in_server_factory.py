from __future__ import annotations

import logging

import pytest
from erp_lifecycle.factories.runnable_factory import RunnableFactory
from erp_testing.factories.stand_in.stand_in_server_factory import StandInServerFactory
from erp_testing.models.stand_in.exceptions import SEStandInServerNotStartedError
from erp_testing.stand_in.stand_in_server import StandInServer


class TestStandInServerFactory:
    def test_the_factory_is_a_runnable_factory(self) -> None:
        assert isinstance(StandInServerFactory(), RunnableFactory)

    def test_create_builds_a_stand_in_server_with_the_given_logger(self) -> None:
        logger = logging.getLogger("test_stand_in_server_factory")
        server = StandInServerFactory(host="127.0.0.1", port=0, logger=logger).create()
        assert isinstance(server, StandInServer)
        assert server.logger is logger

    def test_create_builds_a_server_that_serves_on_the_given_host(self) -> None:
        server = StandInServerFactory(host="127.0.0.1", port=0).create()
        server.initialize()
        try:
            assert server.url.startswith("http://127.0.0.1:")
        finally:
            server.close()

    def test_create_builds_a_new_server_each_time(self) -> None:
        factory = StandInServerFactory()
        assert factory.create() is not factory.create()

    def test_a_server_built_by_the_factory_is_not_started(self) -> None:
        with pytest.raises(SEStandInServerNotStartedError):
            _ = StandInServerFactory().create().url
