from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional


class FakePostgresBinaries:
    """Writes fake PostgreSQL executables, as shell scripts with given exit codes, under a root folder."""

    NAMES = ("initdb", "pg_ctl", "pg_isready", "psql")

    def __init__(self, root: Path) -> None:
        self.root = root

    def write(self, bin_dir: Path, exit_codes: Optional[Dict[str, int]] = None, skip: Optional[str] = None) -> Path:
        """Write the four fake binaries into ``bin_dir``, leaving out ``skip``, and return the folder."""
        codes = exit_codes or {}
        bin_dir.mkdir(parents=True, exist_ok=True)
        for name in self.NAMES:
            if name == skip:
                continue
            path = bin_dir / name
            path.write_text(f"#!/bin/sh\nexit {codes.get(name, 0)}\n", encoding="utf-8")
            path.chmod(0o755)
        return bin_dir

    def write_version(self, version: int, exit_codes: Optional[Dict[str, int]] = None) -> Path:
        """Write the fake binaries into ``<root>/<version>/bin`` and return that folder."""
        return self.write(self.root / str(version) / "bin", exit_codes)
