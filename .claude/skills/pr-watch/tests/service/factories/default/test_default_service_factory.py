from __future__ import annotations

from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.service.factories.default.default_service_factory import DefaultServiceFactory
from pr_watch.service.inbox.inbox_service import InboxService
from pr_watch.service.report.summary_renderer import SummaryRenderer
from pr_watch.service.sessions.ticket_registration import TicketRegistration
from pr_watch.service.setup.unit_installer import UnitInstaller
from pr_watch.service.watch.watch_job import WatchJob


class TestDefaultServiceFactory:
    def test_every_service_is_wired_to_the_settings(self, settings: WatchSettings, catalog: WatchCatalog) -> None:
        factory = DefaultServiceFactory(settings, catalog)
        assert isinstance(factory.watch_job(), WatchJob)
        assert isinstance(factory.inbox(), InboxService)
        assert isinstance(factory.renderer(), SummaryRenderer)
        assert isinstance(factory.installer(), UnitInstaller)
        registration = factory.registration()
        assert isinstance(registration, TicketRegistration)
        assert registration.caller_cwd == settings.caller_cwd
        assert factory.store.state_dir == settings.state_dir
        with factory.lock():
            assert (settings.state_dir / ".lock").exists()
