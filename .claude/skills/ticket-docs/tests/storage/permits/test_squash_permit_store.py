from __future__ import annotations

import logging
from datetime import UTC, datetime
from pathlib import Path
from typing import Optional

import pytest

from ticket_docs.models.permits.squash_permit import SquashPermit
from ticket_docs.storage.permits.exceptions import SESquashPermitStoreError
from ticket_docs.storage.permits.squash_permit_store import SquashPermitStore


class TestSquashPermitStore:
    def permit(self) -> SquashPermit:
        return SquashPermit(
            ticket="GH-1",
            branch="feature/GH-1-thing",
            head="a" * 40,
            tree="b" * 40,
            expires_at=datetime(2026, 11, 10, 12, 30, tzinfo=UTC),
        )

    def test_a_written_permit_is_read_back_and_deleted(self, tmp_path: Path, logger: logging.Logger) -> None:
        store = SquashPermitStore(tmp_path / "permits", logger)
        path = store.write(self.permit())
        assert path == tmp_path / "permits" / "GH-1.json"
        assert store.read("GH-1") == self.permit()
        store.delete("GH-1")
        assert not path.exists()
        assert store.read("GH-1") is None

    @pytest.mark.parametrize("text", [None, "not json", '{"ticket": "GH-1"}'])
    def test_a_missing_or_unreadable_permit_is_none(
        self, tmp_path: Path, logger: logging.Logger, text: Optional[str]
    ) -> None:
        if text is not None:
            (tmp_path / "GH-1.json").write_text(text, encoding="utf-8")
        assert SquashPermitStore(tmp_path, logger).read("GH-1") is None

    def test_deleting_a_missing_permit_does_nothing(self, tmp_path: Path, logger: logging.Logger) -> None:
        SquashPermitStore(tmp_path, logger).delete("GH-1")

    def test_a_permit_that_cannot_be_written_is_refused(self, tmp_path: Path, logger: logging.Logger) -> None:
        (tmp_path / "file").write_text("x", encoding="utf-8")
        with pytest.raises(SESquashPermitStoreError):
            SquashPermitStore(tmp_path / "file" / "permits", logger).write(self.permit())

    def test_the_default_folder_is_under_the_harness_state(self, tmp_path: Path, logger: logging.Logger) -> None:
        store = SquashPermitStore.default(tmp_path, logger)
        assert store.root == tmp_path / ".local" / "state" / "claude-harness" / "squash-permits"
