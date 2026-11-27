from __future__ import annotations

# Standard library imports
import json
from pathlib import Path
from typing import Dict, List, Tuple

TICKET_ID = "T0.03"
FRONT_END_TICKET = "T0.16"
PHASES = "docs/specs/00-vision/roadmap/phases"
ROADMAP_LINK = "../../specs/00-vision/roadmap/phases/01-p0-foundations.md"
F06 = "docs/specs/02-functional/f06-customers-and-sales"
T01 = "docs/specs/03-technical/t01-companies-and-data-isolation"
USE_CASE = f"{F06}/use-cases/01-lead-to-quote/uc-f06-01-capture-and-qualify-a-lead.md"
RULE = f"{F06}/business-rules/br-f06-01-acceptance-is-proven.md"
ENTITY = f"{F06}/data/e-f06-01-customer-record.md"
FLOW = f"{F06}/flows/fl-f06-01-lead-to-quote.md"
SCREEN = f"{F06}/screens/01-lead-to-quote/s-f06-01-pipeline.md"
LIST_SCREEN = f"{F06}/screens/00-lists/s-f06-l01-customer-records.md"
REQUIREMENT = f"{T01}/requirements/req-t01-01-company-stores.md"
DECISION = "docs/specs/06-decisions/technical/d438-repository-layout.md"
OLD_DECISION = "docs/specs/06-decisions/foundations/d09-licence-agpl.md"
SECTOR_USE_CASE = "docs/specs/08-sectors/sc01-construction/use-cases/01-win-the-work/uc-sc01-01-open-a-site.md"
BUDGET = "docs/specs/05-non-functional/performance.md"
DESIGN = "docs/technical/delivery/ci-cd-and-stages.md"
MOCKUP = "docs/specs/04-ux/mockups/src/f06-customers-and-sales/states/uc-f06-77-only-a-mock-up.md"
BUDGETS_LINK = "../../specs/05-non-functional/performance.md#measures"
SCREEN_LINE = f"- [🖥️ S-F6-01: Pipeline](../../{SCREEN.removeprefix('docs/')})"
EM_DASH = "—"
HEADINGS: Tuple[str, ...] = (
    "Roadmap",
    "What it delivers",
    "Features, use cases and business rules",
    "Technical pages it builds on",
    "Screens touched",
    "Budgets touched",
    "Acceptance criteria",
    "Out of scope",
)
PAGES: Dict[str, str] = {
    USE_CASE: "# 📝 UC-F6-01 Capture and qualify a lead\n\n## Steps\n",
    RULE: "# 📏 BR-F6-01 Acceptance is proven\n\n## Rule\n",
    ENTITY: "# 🗃️ E-F6-01 Customer record\n\n## Fields\n",
    FLOW: "# 🔀 FL-F6-01 Lead to quote\n\n## Flowchart\n",
    SCREEN: "# 🖥️ S-F6-01 Pipeline\n\n## States\n",
    LIST_SCREEN: "# 🗂️ S-F6-L01 Customer records\n",
    REQUIREMENT: "# 📌 REQ-T01-01 A database, bucket and vector collection per company\n",
    DECISION: "# 📜 D438 Repository layout\n",
    OLD_DECISION: "# 📜 D9 Licence\n",
    SECTOR_USE_CASE: "# 📝 UC-SC01-01 Open a site\n",
    BUDGET: "# ⚡ Performance\n\n## Requirement\n\n## Measures\n",
    DESIGN: "# 🚚 CI/CD and stages\n\n## CI\n",
    MOCKUP: "# A mock-up page that carries an ID but is no specification\n",
    f"{PHASES}/01-p0-foundations.md": (
        '# 🛣️ P0: Foundations\n\n<a id="epics"></a>\n\n## Epics\n\n<a id="s01"></a>\n\n## Sprint S01\n\n'
        f"| {TICKET_ID} | Convention tests |\n| {FRONT_END_TICKET} | Back office shell |\n"
    ),
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def script_path() -> Path:
    return repo_root() / ".claude" / "skills" / "ticket" / "scripts" / "check_ticket.py"


def template_path() -> Path:
    return repo_root() / ".claude" / "skills" / "ticket" / "templates" / "TICKET.md"


def ticket_file(root: Path, ticket_id: str = TICKET_ID) -> Path:
    return root / "docs" / "tickets" / ticket_id / "TICKET.md"


def link(path: str) -> str:
    return f"../../{path.removeprefix('docs/')}"


def valid_ticket_text(ticket_id: str = TICKET_ID) -> str:
    lines: List[str] = [
        f"# {ticket_id}: Convention tests and linters",
        "",
        "**Status:** 🟡 Planned",
        "",
        "## Roadmap",
        "",
        f"- **Ticket:** [{ticket_id}]({ROADMAP_LINK}#s01) in [🛣️ P0: Foundations]({ROADMAP_LINK})",
        f"- **Phase:** [🛣️ P0: Foundations]({ROADMAP_LINK})",
        f"- **Sprint:** [S01]({ROADMAP_LINK}#s01), 7 to 18 December 2026",
        f"- **Epic:** [E0.1]({ROADMAP_LINK}#epics): Mono-repo",
        "",
        "## What it delivers",
        "",
        f"- Tests that enforce the rules, as [🏗️ CI/CD and stages]({link(DESIGN)}#ci).",
        "",
        "## Features, use cases and business rules",
        "",
        f"- [📝 UC-F6-01: Capture and qualify a lead]({link(USE_CASE)}#steps)",
        f"- [📏 BR-F6-01: Acceptance is proven]({link(RULE)})",
        f"- [🗃️ E-F6-01: Customer record]({link(ENTITY)})",
        f"- [🔀 FL-F6-01: Lead to quote]({link(FLOW)}#flowchart)",
        f"- [📜 D438: Repository layout]({link(DECISION)}), and the licence of D9.",
        f"- [📝 UC-SC01-01: Open a site]({link(SECTOR_USE_CASE)})",
        "",
        "## Technical pages it builds on",
        "",
        f"- [🏗️ CI/CD and stages]({link(DESIGN)}#ci): the pipeline.",
        f"- [📌 REQ-T01-01: Company stores]({link(REQUIREMENT)}): one store per company.",
        "",
        "## Screens touched",
        "",
        SCREEN_LINE,
        "",
        "## Budgets touched",
        "",
        f"- [⏱️ Performance]({BUDGETS_LINK})",
        "",
        "## Acceptance criteria",
        "",
        "1. **Given** a broken sample, **when** the tests run, **then** each rule fails once. (BR-F6-01, UC-F6-01)",
        "",
        "## Out of scope",
        "",
        "- Nothing else.",
        "",
    ]
    return "\n".join(lines)


def build_root(tmp_path: Path, ticket_id: str = TICKET_ID) -> Path:
    """Build a repository root with a small specification tree shaped like SimpleERP's, and a valid ticket."""
    root = tmp_path / "root"
    for relative, text in PAGES.items():
        page = root / relative
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(text, encoding="utf-8")
    target = ticket_file(root, ticket_id)
    target.parent.mkdir(parents=True)
    target.write_text(valid_ticket_text(ticket_id), encoding="utf-8")
    return root


def write_graph(root: Path, ticket_id: str, area: str) -> None:
    graph = root / PHASES / "gantt" / "ticket-graph.json"
    graph.parent.mkdir(parents=True, exist_ok=True)
    graph.write_text(json.dumps({"tickets": {ticket_id: {"area": area}}}), encoding="utf-8")


def rewrite(root: Path, old: str, new: str, ticket_id: str = TICKET_ID) -> None:
    target = ticket_file(root, ticket_id)
    text = target.read_text(encoding="utf-8")
    assert old in text, old
    target.write_text(text.replace(old, new), encoding="utf-8")


def set_screens(root: Path, screens: str, ticket_id: str = TICKET_ID) -> None:
    rewrite(root, f"## Screens touched\n\n{SCREEN_LINE}\n", f"## Screens touched\n\n{screens}\n", ticket_id)


def swap_headings(root: Path, first: str, second: str) -> None:
    rewrite(root, f"## {first}\n", "## @@swap@@\n")
    rewrite(root, f"## {second}\n", f"## {first}\n")
    rewrite(root, "## @@swap@@\n", f"## {second}\n")


def apply_fault(root: Path, fault: str) -> str:
    """Break the valid ticket in one way and return the value the message must quote."""
    match fault:
        case "unknown_use_case":
            rewrite(root, "[📝 UC-F6-01: Capture", "[📝 UC-F6-99: Capture")
            rewrite(root, "uc-f06-01-capture", "uc-f06-99-capture")
            return "UC-F6-99"
        case "unknown_rule":
            rewrite(root, "(BR-F6-01, UC-F6-01)", "(BR-F6-99, UC-F6-01)")
            return "BR-F6-99"
        case "unknown_requirement":
            rewrite(root, "one store per company.", "one store per company, as REQ-T01-99 says.")
            return "REQ-T01-99"
        case "unknown_decision":
            rewrite(root, "the licence of D9.", "the licence of D999.")
            return "D999"
        case "mock_up_is_no_specification":
            rewrite(root, "the licence of D9.", "the licence of D9, and UC-F6-77.")
            return "UC-F6-77"
        case "link_without_id":
            rewrite(root, "[📝 UC-F6-01: Capture and qualify a lead]", "[📝 Capture and qualify a lead]")
            return "UC-F6-01"
        case "padded_id_in_link_text":
            rewrite(root, "[📏 BR-F6-01: Acceptance", "[📏 BR-F06-01: Acceptance")
            return "BR-F6-01"
        case "missing_file":
            rewrite(root, "br-f06-01-acceptance-is-proven.md", "br-f06-01-nothing-here.md")
            return "br-f06-01-nothing-here.md"
        case "missing_anchor":
            rewrite(root, "performance.md#measures", "performance.md#no-such-anchor")
            return "no-such-anchor"
        case "bad_status":
            rewrite(root, "🟡 Planned", "Planned soon")
            return "Planned soon"
        case "missing_phase":
            rewrite(root, "- **Phase:**", "- **Stage:**")
            return "Phase"
        case "roadmap_elsewhere":
            rewrite(root, f"[{TICKET_ID}]({ROADMAP_LINK}#s01)", f"[{TICKET_ID}]({BUDGETS_LINK})")
            return "docs/specs/00-vision/roadmap/phases/"
        case "screen_elsewhere":
            set_screens(root, f"- [📝 UC-F6-01: Capture and qualify a lead]({link(USE_CASE)})")
            return "uc-f06-01-capture-and-qualify-a-lead.md"
        case "budget_elsewhere":
            rewrite(root, BUDGETS_LINK, f"{link(DESIGN)}#ci")
            return "ci-cd-and-stages.md"
        case "technical_elsewhere":
            rewrite(root, f"- [🏗️ CI/CD and stages]({link(DESIGN)}#ci): the pipeline.", f"- [⏱️ Speed]({BUDGETS_LINK}).")
            return "performance.md"
        case "empty_budgets":
            rewrite(root, f"- [⏱️ Performance]({BUDGETS_LINK})\n", "")
            return "Budgets touched"
        case "no_given":
            rewrite(root, "**Given**", "Given")
            return "1"
        case "placeholder":
            rewrite(root, "- Nothing else.", "- {{ID}}")
            return "{{ID}}"
        case "em_dash":
            rewrite(root, "- Nothing else.", f"- Nothing else {EM_DASH} really.")
            return ""
        case _:
            raise ValueError(fault)
