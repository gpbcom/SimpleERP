from __future__ import annotations

import logging
from pathlib import Path

import pytest

from tests.builders.evidence_builder import EvidenceBuilder
from tests.builders.fake_gh import FakeGh


@pytest.fixture
def logger() -> logging.Logger:
    return logging.getLogger("ticket_docs.tests")


@pytest.fixture
def tickets(tmp_path: Path) -> Path:
    root = tmp_path / "repo" / "docs" / "tickets"
    root.mkdir(parents=True)
    return root


@pytest.fixture
def evidence(tickets: Path) -> EvidenceBuilder:
    return EvidenceBuilder(tickets)


@pytest.fixture
def gh(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> FakeGh:
    return FakeGh(tmp_path / "fake-gh", monkeypatch)
