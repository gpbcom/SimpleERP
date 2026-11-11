from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Dict


class TicketBuilder:
    """Writes ticket folders: a small complete one, or one copied from the skill's templates."""

    SKILL = Path(__file__).resolve().parents[2]
    REPOSITORY = SKILL.parents[2]
    PROGRESS = """# GH-7 — Progress

**Legend:** ✅ done / PASS · 🔄 in progress · ⬜ to do · ⏳ waiting · ⏸️ paused · ❌ failed

## Status

| Step (PLAN.md) | Status | Started | Finished | Elapsed |
|---|---|---|---|---|
| 0a — Ticket documentation folder | ✅ Done | 2026-11-10 09:00 | 2026-11-10 09:30 | 0h30 |
| 1 — Customer storage (TDD) | 🔄 In progress | 2026-11-10 09:30 | — | 0h10 so far |
| 2 — Final acceptance run and hand-over | ⬜ To do | — | — | — |

**Total time:** 0h40 elapsed · 0h00 waiting / paused · wall-clock 2026-11-10 09:00 → running.

## Stage validation

| Where | Status | Run | Commit | Result | Evidence |
|---|---|---|---|---|---|
| 💻 Local | ⬜ To do | — | — | — | — |
| 🟦 Dev | ⬜ To do | — | — | — | — |
| 🟪 QA | ⬜ To do | — | — | — | — |

## Documentation

| Chapter | Status | What changed |
|---|---|---|
| docs/technical/README.md | ⬜ To do | — |

## Release note

| Item | Status | Detail |
|---|---|---|
| RELEASE-NOTE.md | ⬜ To do | — |
| Changelog fragment | ⬜ To do | — |
| Issue comment `<!-- release-note -->` | ⬜ To do | after the push |

## Pull request

| Step | Status | Detail |
|---|---|---|
| Pull request (GIT-5) | ⬜ To do | — |

## PR review

No round yet.

## Log

### Step 1 — Customer storage (2026-11-10) 🔄
- **Sub-steps:** ✅ tests commit · ⬜ 🔴 red run · ⬜ code · ⬜ 🟢 green run · ⬜ checks

## Acceptance criteria — final verification

| AC | Tests | Command | Commit | 💻 Local | 🟦 Dev | 🟪 QA | Evidence |
|---|---|---|---|---|---|---|---|
| AC1 | T1 | pytest | — | ⬜ | ⬜ | ⬜ | — |
"""
    EXPLAIN = """# GH-7 — Customers: what was done and how to test it

## 1. In short

Customers are stored.

## 2. What changed for users

Nothing yet.

## 3. What changed in the code

### 3.1 API changes

No API change.

## 4. How to test

### 4.1 Prerequisites

None.

### 4.2 Test cases

None.

### 4.3 Automated tests

None.

### 4.4 Last results

| Where | Stage | Date | Commit | Result | Evidence |
|---|---|---|---|---|---|
| Local | — | — | — | Not verified yet | — |

## 5. Acceptance criteria

Not verified yet.

## 6. Limitations, risks and out of scope

### 6.1 Risks and open points

None.

### 6.2 Questions for the issue

None.

### 6.3 Decision log

None.

## 7. References

[PLAN.md](PLAN.md)
"""
    FILES: Dict[str, str] = {
        "TICKET.md": "# GH-7 — Customers\n\n## Acceptance criteria\n\n- AC1: a customer is stored.\n",
        "PLAN.md": (
            "# Plan — GH-7\n\n## Acceptance criteria → unit tests → validation\n\nAC1.\n\n"
            "## Development rules enforced\n\nTEST-7.\n\n## Files modified\n\nSee IMPLEMENTATION.md.\n"
        ),
        "IMPLEMENTATION.md": "# GH-7\n\n## 0. Files modified\n\nNone.\n\n## 1. Implementation choices\n\nNone.\n",
        "TESTS-CATALOG.md": "# GH-7 — Tests catalog\n\nT1 covers AC1.\n",
        "TESTS-NOTICE.md": "# GH-7 — Tests notice\n\nRun pytest.\n",
        "README.md": "# GH-7 — Customers\n\n**Status (2026-11-10):** 🔄 step 1 in progress.\n",
        "tests-evidences/README.md": "# GH-7 — Test evidence\n\n## Index\n\n| Folder | Result |\n|---|---|\n",
    }

    def __init__(self, tickets: Path, key: str = "GH-7") -> None:
        self.tickets = tickets
        self.key = key
        self.folder = tickets / key

    def minimal(self) -> Path:
        (self.folder / "attachments").mkdir(parents=True, exist_ok=True)
        (self.folder / "tests-evidences").mkdir(parents=True, exist_ok=True)
        for name, text in {**self.FILES, "PROGRESS.md": self.PROGRESS, "EXPLAIN.md": self.EXPLAIN}.items():
            self.write(name, text)
        return self.folder

    def from_templates(self) -> Path:
        templates = self.SKILL / "templates"
        repository = self.tickets.parents[1]
        for rule in ("coding-style.md", "git-rules-and-deploy.md", "rule-proposals.md", "testing.md"):
            (repository / ".claude" / "rules").mkdir(parents=True, exist_ok=True)
            (repository / ".claude" / "rules" / rule).write_text("# Rules\n", encoding="utf-8")
        shutil.copy(
            self.REPOSITORY / ".claude" / "rules" / "ticket-documentation.md",
            repository / ".claude" / "rules" / "ticket-documentation.md",
        )
        (repository / "AGENT.md").write_text("# AGENT.md\n", encoding="utf-8")
        (self.folder / "attachments").mkdir(parents=True, exist_ok=True)
        for source in sorted(templates.rglob("*.md")):
            relative = source.relative_to(templates)
            if relative.name in {"STATUS.md", "RUN-README.md", "REQUIREMENTS-AUDIT.md"}:
                continue
            text = source.read_text(encoding="utf-8")
            text = text.replace("<KEY>", self.key).replace("<TITLE>", "Customers").replace("<DATE>", "2026-11-10")
            text = text.replace("<HH:MM>", "09:00").replace("<h>h<mm>", "0h30")
            text = re.sub(r"\[[^\]]*\]\((?:attachments/<file name>|\.\./GH-xxxxx/README\.md)\)", "none", text)
            self.write(str(relative), text)
        self.write("TESTS-NOTICE.md", "# GH-7 — Tests notice\n\nRun pytest.\n")
        return self.folder

    def write(self, name: str, text: str) -> Path:
        path = self.folder / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def edit(self, name: str, old: str, new: str) -> None:
        path = self.folder / name
        text = path.read_text(encoding="utf-8")
        assert old in text, f"{old!r} is not in {name}"
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
