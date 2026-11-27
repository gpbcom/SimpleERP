from __future__ import annotations

# Standard library imports
import subprocess
import sys
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.harness.check_ticket.helpers import (
    FRONT_END_TICKET,
    LIST_SCREEN,
    build_root,
    link,
    script_path,
    set_screens,
    write_graph,
)

NO_SCREEN_LINE = "- The ticket touches no screen."


class TestCheckTicketFrontEnd:
    def root_with_area(self, tmp_path: Path, area: str, screens: str) -> Path:
        root = build_root(tmp_path, FRONT_END_TICKET)
        write_graph(root, FRONT_END_TICKET, area)
        set_screens(root, screens, FRONT_END_TICKET)
        return root

    def run_script(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(script_path()), FRONT_END_TICKET, "--root", str(root)],
            capture_output=True,
            text=True,
            check=False,
        )

    @pytest.mark.parametrize("area", ["frontend/backoffice", "backend/services/customers, frontend/portals/customer"])
    def test_a_front_end_ticket_that_lists_no_screen_is_refused(self, tmp_path: Path, area: str) -> None:
        result = self.run_script(self.root_with_area(tmp_path, area, NO_SCREEN_LINE))
        assert result.returncode == 1
        assert "TKT-21" in result.stdout

    def test_a_front_end_ticket_that_links_its_screen_pages_passes(self, tmp_path: Path) -> None:
        screens = f"- [🗂️ S-F6-L01: Customer records]({link(LIST_SCREEN)})"
        result = self.run_script(self.root_with_area(tmp_path, "frontend/backoffice", screens))
        assert result.stdout == "", result.stdout

    def test_a_front_end_ticket_may_say_why_it_builds_no_screen(self, tmp_path: Path) -> None:
        screens = "- ➖ No screen: the shell holds no state of a use case yet."  # noqa: RUF001
        result = self.run_script(self.root_with_area(tmp_path, "frontend/backoffice", screens))
        assert result.stdout == "", result.stdout

    def test_a_screen_link_must_show_its_screen_id(self, tmp_path: Path) -> None:
        screens = f"- [🗂️ Customer records]({link(LIST_SCREEN)})"
        result = self.run_script(self.root_with_area(tmp_path, "frontend/backoffice", screens))
        assert result.returncode == 1
        assert "S-F6-L01" in result.stdout

    @pytest.mark.parametrize("area", ["backend/services/customers", "infra/helm", "docs/frontend/notes"])
    def test_a_ticket_that_changes_no_front_end_needs_no_screen(self, tmp_path: Path, area: str) -> None:
        result = self.run_script(self.root_with_area(tmp_path, area, NO_SCREEN_LINE))
        assert result.stdout == "", result.stdout
