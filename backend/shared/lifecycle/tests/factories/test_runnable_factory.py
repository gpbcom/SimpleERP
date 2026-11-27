from __future__ import annotations

from logging import getLogger

import pytest
from erp_lifecycle.factories.runnable_factory import RunnableFactory

from backend.shared.lifecycle.tests.factories.stand_in_runnable import StandInRunnable
from backend.shared.lifecycle.tests.factories.stand_in_runnable_factory import StandInRunnableFactory


class TestRunnableFactory:
    """Tests of the abstract factory base of the runnables."""

    def test_the_concrete_factory_builds_a_runnable_carrying_its_inputs(self) -> None:
        """The factory's inputs reach the runnable it builds."""
        logger = getLogger("stand_in")
        runnable = StandInRunnableFactory("invoices", logger).create()
        assert isinstance(runnable, StandInRunnable)
        assert runnable.name == "invoices"
        assert runnable.logger is logger

    def test_each_create_returns_a_new_instance(self) -> None:
        """Two calls to ``create`` never share a runnable."""
        factory = StandInRunnableFactory("invoices")
        assert factory.create() is not factory.create()

    def test_the_built_runnable_runs_its_whole_lifecycle_through_execute(self) -> None:
        """``execute`` calls ``initialize``, ``run`` and ``close`` in order."""
        runnable = StandInRunnableFactory("invoices").create()
        runnable.execute()
        assert runnable.calls == ["initialize", "run", "close"]

    def test_the_abstract_factory_cannot_be_instantiated(self) -> None:
        """``RunnableFactory`` itself has an abstract ``create``."""
        with pytest.raises(TypeError):
            RunnableFactory()  # type: ignore[abstract]

    def test_a_subclass_without_create_cannot_be_instantiated(self) -> None:
        """A factory that does not define ``create`` is refused."""
        incomplete = type("IncompleteFactory", (RunnableFactory,), {})
        with pytest.raises(TypeError):
            incomplete()

    def test_the_logger_defaults_to_a_logger_and_a_given_one_is_kept(self) -> None:
        """Without a logger the factory makes one, and a given logger is kept."""
        logger = getLogger("given")
        assert StandInRunnableFactory("a", logger).logger is logger
        assert RunnableFactory.__init__(StandInRunnableFactory("a"), None) is None
        assert StandInRunnableFactory("a").logger is not None
