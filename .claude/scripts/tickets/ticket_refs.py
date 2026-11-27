#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / ".claude" / "skills" / "ticket" / "scripts"))

from check_ticket import anchors_of
from spec_ids import SPEC_ID, id_of

ROOT = Path(__file__).resolve().parents[3]
SPECS = ROOT / "docs" / "specs"
TECHNICAL = ROOT / "docs" / "technical"
START = "<!-- ticket:specs -->"
END = "<!-- /ticket:specs -->"
LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)")
STATUS_LINE = re.compile(r"^\*\*(Plan|Status):\*\*.*$", re.MULTILINE)


def spec_kind(target: Path, text: str) -> Optional[str]:
    """Return what a link refers to: a specification ID, ``technical``, ``non-functional``, or None.

    A specification page counts when its file name carries an ID (``uc-f06-01-*.md``), or when the link text shows one
    (``UC-F6-01``) and it lies under ``docs/specs/``. Every page of a technical capability
    (``docs/specs/03-technical/``) and of the non-functional requirements (``docs/specs/05-non-functional/``) counts,
    and so does every design page of ``docs/technical/`` but its READMEs.
    """
    if target.suffix != ".md":
        return None
    found = SPEC_ID.search(text)
    if target.is_relative_to(SPECS) and (id_of(target) or found):
        return id_of(target) or (found.group(0) if found else None)
    if target.is_relative_to(SPECS / "03-technical") and target.parent != SPECS / "03-technical":
        return "technical"
    if target.is_relative_to(SPECS / "05-non-functional") and target.name != "README.md":
        return "non-functional"
    if target.is_relative_to(TECHNICAL) and target.name != "README.md":
        return "technical"
    return None


def references(ticket_md: Path) -> Tuple[List[Tuple[str, str]], List[str]]:
    """Return the specification links of TICKET.md as (text, href), and the problems of those links."""
    found: List[Tuple[str, str]] = []
    problems: List[str] = []
    seen = set()
    for text, href in LINK.findall(ticket_md.read_text(encoding="utf-8")):
        if re.match(r"^[a-z]+:", href):
            continue
        path_part, _, anchor = href.partition("#")
        target = (ticket_md.parent / path_part).resolve()
        if spec_kind(target, text) is None:
            continue
        if not target.is_file():
            problems.append(f"the link {href!r} points to a page that does not exist")
            continue
        if anchor and anchor not in anchors_of(target):
            problems.append(f"the link {href!r} points to an anchor that does not exist")
            continue
        if href not in seen:
            seen.add(href)
            found.append((text, href))
    if not found and not problems:
        problems.append(
            "no link to a specification page (a use case, screen, business rule, entity, flow, requirement or "
            "decision of docs/specs/) or a design page of docs/technical/. "
            "Link the specification the ticket builds on, or write it first."
        )
    return found, problems


def section(found: List[Tuple[str, str]]) -> str:
    lines = [
        START,
        "## 📚 Specifications",
        "",
        (
            "The specification and design pages of [TICKET.md](TICKET.md), copied by "
            "`python3 .claude/scripts/tickets/ticket_refs.py sync`."
        ),
        "",
    ]
    lines += [f"- [{text}]({href})" for text, href in found]
    lines.append(END)
    return "\n".join(lines)


def with_section(text: str, block: str) -> str:
    if START in text and END in text:
        return text[: text.index(START)] + block + text[text.index(END) + len(END) :]
    status = STATUS_LINE.search(text)
    if status is None:
        heading = re.search(r"^# .*$", text, re.MULTILINE)
        position = heading.end() if heading else 0
    else:
        position = status.end()
    return text[:position] + "\n\n" + block + "\n\n" + text[position:].lstrip("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Keep the specification references of a ticket's documents.")
    parser.add_argument("command", choices=("sync", "check"))
    parser.add_argument("--ticket", required=True)
    arguments = parser.parse_args()
    if not re.fullmatch(r"T\d{1,2}\.\d{2}", arguments.ticket):
        parser.error(f"Invalid ticket: {arguments.ticket!r}. Must look like T1.07.")
    folder = ROOT / "docs" / "tickets" / arguments.ticket
    ticket_md = folder / "TICKET.md"
    if not ticket_md.is_file():
        print(f"{ticket_md.relative_to(ROOT)}: the file does not exist.")
        return 1
    found, problems = references(ticket_md)
    lines = [f"{ticket_md.relative_to(ROOT)}: {problem}" for problem in problems]
    if found:
        block = section(found)
        for name in ("PLAN.md", "PROGRESS.md"):
            path = folder / name
            if not path.is_file():
                continue
            current = path.read_text(encoding="utf-8")
            wanted = with_section(current, block)
            if wanted == current:
                continue
            if arguments.command == "sync":
                path.write_text(wanted, encoding="utf-8")
            elif START in current:
                lines.append(f"{path.relative_to(ROOT)}: the 📚 Specifications section is out of date. Run sync.")
            else:
                lines.append(f"{path.relative_to(ROOT)}: the 📚 Specifications section is missing. Run sync.")
    for line in lines:
        print(line)
    return 1 if lines else 0


if __name__ == "__main__":
    sys.exit(main())
