from __future__ import annotations

# Standard library imports
import json
from pathlib import Path
from typing import List

# First-party imports
from tests.harness.tickets.helpers import DONE, make_repo, write_plan

HELM = "T9.05"
PACKS = "T9.06"
DOCS = "T9.07"
LOCK = "uv.lock"
TICKETS = {
    DONE: {"deps": [], "external": [], "area": "backend/services/sales", "size": "S"},
    HELM: {"deps": [DONE], "external": [], "area": "infra/helm", "size": "S"},
    PACKS: {"deps": [], "external": [], "area": "packs/countries", "size": "S"},
    DOCS: {"deps": [], "external": [], "area": "infra/terraform", "size": "S"},
}


def make_file_lock_repo(base: Path) -> Path:
    """Create the repository of ``make_repo`` with a graph of three tickets of three different areas."""
    main = make_repo(base)
    (base / "graph.json").write_text(json.dumps({"tickets": TICKETS}), encoding="utf-8")
    return main


def write_plan_with_files(main: Path, ticket: str, status: str, files: List[str]) -> Path:
    """Write a PLAN.md whose json block holds one task changing ``files``, as plan.py renders it."""
    plan = write_plan(main, ticket, status)
    task = {
        "id": "K01",
        "title": "Change the files",
        "agent": "implementer",
        "depends_on": [],
        "files": files,
        "brief": "Change them.",
        "done_when": "They are changed.",
        "wave": 1,
    }
    block = json.dumps([task], indent=2)
    plan.write_text(plan.read_text(encoding="utf-8") + f"\n```json\n{block}\n```\n", encoding="utf-8")
    return plan
