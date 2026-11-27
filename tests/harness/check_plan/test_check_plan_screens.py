from __future__ import annotations

# Standard library imports
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

# Third-party imports
import pytest
from pydantic import JsonValue

# First-party imports
from tests.harness.check_plan.helpers import APPROVED, a_task, script_path

FRONT_END = "T0.16"
BACK_END = "T0.03"
SCREEN = "docs/specs/02-functional/f06-customers-and-sales/screens/01-lead-to-quote/s-f06-01-pipeline.md"
SCREENS = f"- [🖥️ S-F6-01: Pipeline](../../{SCREEN.removeprefix('docs/')})"
NO_SCREEN = "- ➖ No screen: the shell holds no state of a use case yet."  # noqa: RUF001
GRAPH = "docs/specs/00-vision/roadmap/phases/gantt/ticket-graph.json"
E2E_TEST = "frontend/backoffice/e2e/pipeline.spec.ts"


class TestCheckPlanScreens:
    def ticket_root(self, tmp_path: Path, screens: str = SCREENS) -> Path:
        root = tmp_path / "root"
        graph = {"tickets": {FRONT_END: {"area": "frontend/backoffice"}, BACK_END: {"area": "backend/models"}}}
        (root / GRAPH).parent.mkdir(parents=True)
        (root / GRAPH).write_text(json.dumps(graph), encoding="utf-8")
        for ticket in (FRONT_END, BACK_END):
            text = f"# {ticket}: Sample\n\n## Screens touched\n\n{screens}\n\n## Budgets touched\n\n- None.\n"
            (root / "docs" / "tickets" / ticket).mkdir(parents=True)
            (root / "docs" / "tickets" / ticket / "TICKET.md").write_text(text, encoding="utf-8")
        return root

    def plan(self, root: Path, ticket: str, tasks: List[Dict[str, JsonValue]]) -> subprocess.CompletedProcess[str]:
        text = f"# {ticket}: Plan\n\n{APPROVED}\n\n## Task graph\n\n```json\n{json.dumps(tasks)}\n```\n"
        (root / "docs" / "tickets" / ticket / "PLAN.md").write_text(text, encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(script_path()), ticket, "--root", str(root)],
            capture_output=True,
            text=True,
            check=False,
        )

    def front_end_work(self, test_file: str = E2E_TEST) -> List[Dict[str, JsonValue]]:
        return [
            a_task("K01", "test-writer", 1, files=[test_file]),
            a_task("K02", "frontend-implementer", 2, ["K01"], ["frontend/backoffice/src/views/Pipeline.vue"]),
        ]

    @pytest.mark.parametrize("test_file", [E2E_TEST, "frontend/portals/customer/e2e/pipeline.spec.ts"])
    def test_a_front_end_plan_with_playwright_tests_of_its_screens_passes(self, tmp_path: Path, test_file: str) -> None:
        result = self.plan(self.ticket_root(tmp_path), FRONT_END, self.front_end_work(test_file))
        assert result.stdout == "", result.stdout

    @pytest.mark.parametrize(
        "test_file", ["frontend/backoffice/src/views/Pipeline.spec.ts", "backend/services/customers/tests/e2e/x.py"]
    )
    def test_a_front_end_plan_without_playwright_tests_is_refused(self, tmp_path: Path, test_file: str) -> None:
        result = self.plan(self.ticket_root(tmp_path), FRONT_END, self.front_end_work(test_file))
        assert result.returncode == 1
        assert "TKT-21" in result.stdout
        assert "S-F6-01" in result.stdout

    def test_playwright_tests_written_by_another_agent_do_not_count(self, tmp_path: Path) -> None:
        tasks = [
            a_task("K01", "test-writer", 1),
            a_task("K02", "frontend-implementer", 2, ["K01"], [E2E_TEST]),
        ]
        result = self.plan(self.ticket_root(tmp_path), FRONT_END, tasks)
        assert result.returncode == 1
        assert "test-writer" in result.stdout

    def test_a_front_end_ticket_with_no_screen_needs_no_playwright_task(self, tmp_path: Path) -> None:
        tasks = [a_task("K01", "test-writer", 1), a_task("K02", "frontend-implementer", 2, ["K01"])]
        assert self.plan(self.ticket_root(tmp_path, NO_SCREEN), FRONT_END, tasks).stdout == ""

    def test_a_ticket_that_changes_no_front_end_needs_no_playwright_task(self, tmp_path: Path) -> None:
        tasks = [a_task("K01", "test-writer", 1), a_task("K02", "implementer", 2, ["K01"])]
        assert self.plan(self.ticket_root(tmp_path), BACK_END, tasks).stdout == ""
