from __future__ import annotations

# Standard library imports
from decimal import Decimal
from pathlib import Path
from typing import AsyncIterator, Callable, Iterator, List

# Third-party imports
import httpx
import pytest
import pytest_asyncio
from erp_metering.models.calls.paid_call import PaidCall
from erp_models.events.event_envelope import EventEnvelope
from erp_models.ids.company_id import CompanyId
from erp_models.money.money import Money
from erp_outbox.storage.sqlite.sqlite_outbox_store import SqliteOutboxStore

# First-party imports
from backend.shared.metering.tests.stand_in.stand_in_metering_server import StandInMeteringServer


@pytest.fixture
def metering_server() -> Iterator[StandInMeteringServer]:
    server = StandInMeteringServer()
    server.serve()
    yield server
    server.close()


@pytest_asyncio.fixture
async def metering_http(metering_server: StandInMeteringServer) -> AsyncIterator[httpx.AsyncClient]:
    client = httpx.AsyncClient(base_url=metering_server.url)
    yield client
    await client.aclose()


@pytest.fixture
def outbox_writer(tmp_path: Path) -> SqliteOutboxStore:
    store = SqliteOutboxStore(tmp_path / "metering.db")
    connection = store.connect()
    store.create_table(connection)
    connection.close()
    return store


@pytest.fixture
def outbox_events(outbox_writer: SqliteOutboxStore) -> Iterator[Callable[[], List[EventEnvelope]]]:
    connection = outbox_writer.connect()
    yield lambda: (lambda events: (connection.rollback(), events)[1])(outbox_writer.pending(connection))
    connection.close()


@pytest.fixture
def paid_call_factory() -> Callable[..., PaidCall]:
    return lambda amount=Decimal("10.00"), legal_duty=False: PaidCall(
        company_id=CompanyId(value="C-TEST-1"),
        module="sales",
        feature="quotes",
        estimated_cost=Money(amount=amount, currency="EUR"),
        legal_duty=legal_duty,
    )
