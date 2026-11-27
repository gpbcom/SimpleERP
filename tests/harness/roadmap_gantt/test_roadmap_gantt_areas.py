from __future__ import annotations

# Standard library imports
import json
import subprocess
import sys
from pathlib import Path
from typing import Set

# Third-party imports
import pytest

ROOT = Path(__file__).resolve().parents[3]
REPORTS = ROOT / ".claude" / "scripts" / "reports"
CODE = (
    "import sys; sys.path.insert(0, {reports!r}); import roadmap_gantt as r; import json; "
    "print(json.dumps(sorted(r.{call})))"
)
KNOWN = {
    "T1.01": {"area": "backend/services/customers"},
    "T1.02": {"area": "frontend/backoffice"},
    "T1.03": {"area": "frontend/portals/supplier"},
}


class TestRoadmapGanttAreas:
    def evaluate(self, call: str) -> Set[str]:
        code = CODE.format(reports=str(REPORTS), call=call)
        output = subprocess.run(
            [sys.executable, "-c", code], cwd=ROOT, capture_output=True, text=True, check=True
        ).stdout
        return set(json.loads(output))

    @pytest.mark.parametrize(
        ("text", "expected"),
        [
            ("backend/models", {"backend/models"}),
            ("backend/shared/erp-logging", {"backend/shared/erp-logging"}),
            ("backend/services/customers/src", {"backend/services/customers"}),
            ("frontend/backoffice/e2e", {"frontend/backoffice"}),
            ("frontend/portals/customer", {"frontend/portals/customer"}),
            ("frontend/packages/ui", {"frontend/packages/ui"}),
            ("frontend/mobile", {"frontend/mobile"}),
            ("plugins/shopify", {"plugins/shopify"}),
            ("sdk", {"sdk"}),
            ("infra/helm, infra/terraform", {"infra/helm", "infra/terraform"}),
            ("packs/countries", {"packs/countries"}),
            ("tests/conventions", {"tests/conventions"}),
            ("`.claude/`, `.github/`", {".claude", ".github"}),
            ("docs/technical", {"docs"}),
        ],
    )
    def test_a_layout_folder_is_its_own_area(self, text: str, expected: Set[str]) -> None:
        assert self.evaluate(f"areas({text!r}, {{}})") == expected

    @pytest.mark.parametrize(
        "old",
        ["backend/apps/gateway", "backend/libs/x", "rust/erp-core", "services/gateway", "frontends/x", "qa/e2e"],
    )
    def test_a_folder_outside_the_layout_locks_every_area(self, old: str) -> None:
        assert self.evaluate(f"areas({old!r}, {{}})") == {"*"}

    @pytest.mark.parametrize(
        ("text", "expected"),
        [
            ("customers", {"backend/services/customers"}),
            ("the Backoffice and the customers service", {"frontend/backoffice", "backend/services/customers"}),
            ("supplier portal", {"frontend/portals/supplier"}),
            ("any service or app", {"*"}),
        ],
    )
    def test_a_service_or_front_end_the_graph_names_is_known_by_its_bare_name(
        self, text: str, expected: Set[str]
    ) -> None:
        call = f"areas({text!r}, r.known_folders({KNOWN!r}))"
        assert self.evaluate(call) == expected

    def test_the_phase_colours_cycle_past_the_palette(self) -> None:
        call = (
            "PHASE_COLOURS[0:0] + [r.phase_colour(0) == r.phase_colour(len(r.PHASE_COLOURS)), "
            "len(set(map(r.phase_colour, range(11))))]"
        )
        assert self.evaluate(call) == {True, 11}
