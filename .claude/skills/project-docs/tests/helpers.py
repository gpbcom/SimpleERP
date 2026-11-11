"""A complete documentation set for the sandboxes, and the paths the tests share."""

from __future__ import annotations

from pathlib import Path
from typing import Dict

SKILL_DIR = Path(__file__).resolve().parents[1]
DOC_MAP_FILE = SKILL_DIR / "conf" / "doc-map.yaml"
REPOSITORY_ROOT = SKILL_DIR.parents[2]
STAMP = "Last reviewed: 2026-11-10 (GH-1)"
EM_DASH = chr(0x2014)
FEATURE_BRANCH = "feature/GH-7-add-customers"


def documentation() -> Dict[str, str]:
    """A README and the two documentation folders, every chapter linked, stamped and free of em dashes."""
    return {
        "README.md": (
            "# simple-erp\n\nRead the [functional](docs/functional/README.md) and the "
            f"[technical](docs/technical/README.md#chapters) documentation.\n\n{STAMP}\n"
        ),
        "docs/functional/README.md": (
            "# Functional documentation\n\n| Chapter | Holds |\n|---|---|\n"
            f"| [Capabilities](capabilities.md) | What users can do |\n\n{STAMP}\n"
        ),
        "docs/functional/capabilities.md": (
            f"# Capabilities\n\nNone yet. See the [README](../../README.md).\n\n{STAMP}\n"
        ),
        "docs/technical/README.md": (
            "# Technical documentation\n\n## Chapters\n\n| Chapter | Holds |\n|---|---|\n"
            "| [Architecture](architecture.md) | The layers |\n| [API](./api.md) | The entry points |\n"
            f"| [Development process](development-process.md) | How a ticket is done |\n\n{STAMP}\n"
        ),
        "docs/technical/architecture.md": (
            "# Architecture\n\n```mermaid\nflowchart LR\n    api --> service\n```\n\n"
            f"An example link in code: `[x](missing.md)`.\n\n{STAMP}\n"
        ),
        "docs/technical/api.md": f"# API\n\nSee [the architecture](architecture.md#layers).\n\n{STAMP}\n",
        "docs/technical/development-process.md": f"# Development process\n\nTickets.\n\n{STAMP}\n",
    }
