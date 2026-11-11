from __future__ import annotations

from pathlib import Path
from typing import ClassVar

from pr_watch.storage.tickets.ticket_folders import TicketFolders


class TestTicketFolders:
    PROGRESS: ClassVar[str] = """# GH-12 progress

## Steps

Blocked by https://github.com/gpbcom/simple-erp/pull/3 for a while.

## Pull request

- https://github.com/gpbcom/simple-erp/pull/7 opened 2026-11-09
- https://github.com/gpbcom/simple-erp/pull/7 again

### Review rounds

- https://github.com/gpbcom/simple-erp/pull/9

## Stage validation

- https://github.com/gpbcom/simple-erp/pull/4
"""

    def test_links_come_from_the_pull_request_section_only(self, tmp_path: Path) -> None:
        (tmp_path / "GH-12").mkdir()
        (tmp_path / "GH-12" / "PROGRESS.md").write_text(self.PROGRESS, encoding="utf-8")
        assert TicketFolders(tmp_path).pull_request_links("GH-12") == [
            "https://github.com/gpbcom/simple-erp/pull/7",
            "https://github.com/gpbcom/simple-erp/pull/9",
        ]

    def test_a_ticket_without_progress_has_no_link(self, tmp_path: Path) -> None:
        assert TicketFolders(tmp_path).pull_request_links("GH-12") == []

    def test_ticket_folders_are_listed_by_number(self, tmp_path: Path) -> None:
        for name in ("GH-10", "GH-9", "pull-request-summary", "notes"):
            (tmp_path / name).mkdir()
        (tmp_path / "GH-11").write_text("not a folder", encoding="utf-8")
        assert TicketFolders(tmp_path).ticket_keys() == ["GH-9", "GH-10"]
        assert TicketFolders(tmp_path / "missing").ticket_keys() == []
