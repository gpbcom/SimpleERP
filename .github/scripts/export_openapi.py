"""Write the committed OpenAPI document of a service (REQ-T05-01, D406, D419).

Usage:
    uv run --package <service> python .github/scripts/export_openapi.py <service folder>

A service has no command line: its FastAPI application serves its OpenAPI, and this script writes the committed copy.
It finds the one package of ``<service folder>/src/``, changes the working folder to the service folder, imports
``<package>.api.app_factory``, calls ``AppFactory.create()`` and writes ``app.openapi()`` to
``<service folder>/openapi.json``, indented, unescaped, in UTF-8 and ending with a newline.

It prints ``Wrote <service folder>/openapi.json.`` and exits 0. It exits 2 with one line on stderr for a missing
argument, a folder without exactly one package, or a failed import or factory. It never prints the document.
"""

from __future__ import annotations

import importlib
import json
import os
import sys
from pathlib import Path
from typing import List


def fail(message: str) -> int:
    """Print one line on stderr and return the exit code 2."""
    print(message, file=sys.stderr)
    return 2


def find_packages(folder: Path) -> List[str]:
    """List the packages of ``<folder>/src/``."""
    source = folder / "src"
    if not source.is_dir():
        return []
    return sorted(path.name for path in source.iterdir() if path.is_dir() and not path.name.startswith((".", "_")))


def main() -> int:
    """Export the OpenAPI document of the service named on the command line."""
    if len(sys.argv) != 2:
        return fail("Usage: export_openapi.py <service folder>")
    argument = sys.argv[1].rstrip("/") or sys.argv[1]
    folder = Path(argument).resolve()
    packages = find_packages(folder)
    if len(packages) != 1:
        return fail(f"Expected one package under {argument}/src, found {len(packages)}.")
    try:
        os.chdir(folder)
        sys.path.insert(0, os.getcwd())
        module = importlib.import_module(f"{packages[0]}.api.app_factory")
        document = module.AppFactory.create().openapi()
        text = json.dumps(document, indent=2, ensure_ascii=False) + "\n"
    except Exception as error:  # noqa: BLE001
        return fail(f"Cannot export {argument}: {type(error).__name__}: {' '.join(str(error).split())}")
    (folder / "openapi.json").write_text(text, encoding="utf-8", newline="\n")
    print(f"Wrote {argument}/openapi.json.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
