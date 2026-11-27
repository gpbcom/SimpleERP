from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[3]
TERRAFORM = ROOT / "infra" / "terraform"
CLOUDS = ["ovhcloud", "scaleway"]
INTERFACE = ["network", "kubernetes-cluster", "storage", "registry", "dns", "helm-release"]
MODULE_FILES = ["versions.tf", "variables.tf", "main.tf", "outputs.tf"]


def committed_files() -> List[Path]:
    """List the files under ``infra/terraform`` that would be committed, tracked or not yet added."""
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard", "infra/terraform"],
        capture_output=True,
        text=True,
        check=True,
        encoding="utf-8",
    )
    return [ROOT / line for line in result.stdout.splitlines() if line.strip() and (ROOT / line).is_file()]


def module_sources(cloud: str) -> List[str]:
    """Return the ``source = "..."`` values of the ``main.tf`` of one root."""
    text = (TERRAFORM / cloud / "main.tf").read_text(encoding="utf-8")
    return re.findall(r'^\s*source\s*=\s*"([^"]*)"', text, flags=re.MULTILINE)
