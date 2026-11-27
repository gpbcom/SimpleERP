"""Resolve the IDs of SimpleERP's specification pages to their files, and back.

An ID is written as the page titles write it: ``UC-F6-01``, ``S-F6-L01``, ``BR-F6-01``, ``E-F6-01``, ``FL-F6-01``
(feature number not padded), ``REQ-T01-01``, ``S-T01-01``, ``UC-SC01-01`` (padded), ``D438``, ``D9``. Its page file
name starts with the same parts in lower case, the feature number padded to two digits: ``uc-f06-01-<slug>.md``,
``req-t01-01-<slug>.md``, ``d09-<slug>.md``.

Usage, from the repository root: ``python3 .claude/skills/ticket/scripts/spec_ids.py <ID>...`` prints the page of each
ID, or ``unknown`` and exits 1.
"""

from __future__ import annotations

import os
import re
import sys
from functools import cache
from pathlib import Path
from typing import Dict, List, Optional

SPEC_ID = re.compile(r"(?<![\w-])(?:(UC|S|BR|E|FL|REQ|I)-(F\d{1,2}|T\d{2}|SC\d{2})-([A-Z]?\d{2})|D(\d{1,4}))(?![\w-])")
FILE_ID = re.compile(r"^(?:(uc|s|br|e|fl|req|i)-(f\d{2}|t\d{2}|sc\d{2})-([a-z]?\d{2})|d(\d{2,4}))-[^/]*\.md$")
SPECS = Path("docs") / "specs"
SKIPPED = {Path("04-ux") / "mockups"}
SKIPPED_NAMES = {"images", "_templates"}


def canonical(kind: str, owner: str, number: str, decision: str) -> str:
    """Return the ID as the page titles write it, from the parts of an ID or of a file name."""
    if decision:
        return f"D{int(decision)}"
    owner = owner.upper()
    if owner.startswith("F"):
        owner = f"F{int(owner[1:])}"
    return f"{kind.upper()}-{owner}-{number.upper()}"


def normalise(spec_id: str) -> Optional[str]:
    """Return the canonical text of an ID (``UC-F06-01`` gives ``UC-F6-01``), or None when it is not an ID."""
    match = SPEC_ID.fullmatch(spec_id.strip())
    return canonical(*(part or "" for part in match.groups())) if match else None


def id_of(path: Path) -> Optional[str]:
    """Return the ID of a specification page from its file name, or None when the name carries no ID."""
    match = FILE_ID.match(path.name)
    return canonical(*(part or "" for part in match.groups())) if match else None


@cache
def index(root: Path) -> Dict[str, Path]:
    """Map every ID of ``docs/specs/`` to its page, walking the tree once per root and process."""
    specs = root / SPECS
    found: Dict[str, Path] = {}
    for folder, children, files in os.walk(specs):
        relative = Path(folder).relative_to(specs)
        children[:] = sorted(c for c in children if c not in SKIPPED_NAMES and relative / c not in SKIPPED)
        for name in sorted(files):
            spec_id = id_of(Path(name))
            if spec_id and spec_id not in found:
                found[spec_id] = Path(folder) / name
    return found


def resolve(spec_id: str, root: Path) -> Optional[Path]:
    """Return the page of an ID under ``root/docs/specs/``, or None when no page carries it."""
    key = normalise(spec_id)
    return index(root.resolve()).get(key) if key else None


def main(argv: Optional[List[str]] = None) -> int:
    """Print the page of each ID given, relative to the repository root."""
    root = Path(__file__).resolve().parents[4]
    unknown = 0
    for spec_id in sys.argv[1:] if argv is None else argv:
        page = resolve(spec_id, root)
        print(f"{spec_id}: {page.relative_to(root.resolve()).as_posix() if page else 'unknown'}")
        unknown += page is None
    return 1 if unknown else 0


if __name__ == "__main__":
    sys.exit(main())
