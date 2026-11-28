from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

ROOT: Path = Path(__file__).resolve().parents[3]
COMPOSE_DIR: Path = ROOT / "infra" / "compose"
MIB: int = 1048576

STAND_IN_DOCKER: str = """#!/usr/bin/env python3
import json
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
scenario = json.loads((here / "scenario.json").read_text(encoding="utf-8"))
argv = sys.argv[1:]
with (here / "calls.jsonl").open("a", encoding="utf-8") as log:
    log.write(json.dumps({"tool": "docker", "argv": argv}) + "\\n")
stats = scenario.get("stats", {})
if argv[:1] == ["info"]:
    if not scenario.get("docker_running", True):
        sys.stderr.write("Cannot connect to the Docker daemon.\\n")
        sys.exit(1)
    print(scenario["memory_bytes"], scenario["cpus"], scenario["docker_root"])
elif argv[:1] == ["compose"] and "up" in argv:
    sys.exit(int(scenario.get("up_exit", 0)))
elif argv[:1] == ["compose"] and "down" in argv:
    sys.exit(0)
elif argv[:1] == ["compose"] and "ps" in argv and "--quiet" in argv:
    for name in sorted(stats):
        print("id-" + name)
elif argv[:1] == ["stats"]:
    for name in sorted(stats):
        print(name + "\\t" + stats[name])
sys.exit(0)
"""

STAND_IN_DF: str = """#!/usr/bin/env python3
import json
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
scenario = json.loads((here / "scenario.json").read_text(encoding="utf-8"))
with (here / "calls.jsonl").open("a", encoding="utf-8") as log:
    log.write(json.dumps({"tool": "df", "argv": sys.argv[1:]}) + "\\n")
print("Filesystem 1024-blocks Used Available Capacity Mounted on")
print("/dev/sim 0 0 " + str(scenario["disk_free_kib"]) + " 0% /")
"""


def profile_settings() -> Dict[str, str]:
    settings: Dict[str, str] = {}
    text = (COMPOSE_DIR / "laptop-profile.env").read_text(encoding="utf-8")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        settings[key.strip()] = value.strip().strip("\"'")
    return settings


def stand_in_machine(
    folder: Path,
    memory_mib: int = 16384,
    cpus: int = 12,
    disk_free_gib: int = 200,
    docker_running: bool = True,
    up_exit: int = 0,
    stats: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    bin_dir = folder / "bin"
    bin_dir.mkdir(parents=True, exist_ok=True)
    docker_root = folder / "docker-root"
    docker_root.mkdir(parents=True, exist_ok=True)
    for name, source in (("docker", STAND_IN_DOCKER), ("df", STAND_IN_DF)):
        path = bin_dir / name
        path.write_text(source, encoding="utf-8")
        path.chmod(0o755)
    scenario = {
        "memory_bytes": memory_mib * MIB,
        "cpus": cpus,
        "disk_free_kib": disk_free_gib * 1048576,
        "docker_root": str(docker_root),
        "docker_running": docker_running,
        "up_exit": up_exit,
        "stats": stats or {},
    }
    (bin_dir / "scenario.json").write_text(json.dumps(scenario), encoding="utf-8")
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env.get("PATH", "")
    return env


def docker_calls(folder: Path) -> List[List[str]]:
    log = folder / "bin" / "calls.jsonl"
    if not log.exists():
        return []
    entries = [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines() if line.strip()]
    return [entry["argv"] for entry in entries if entry.get("tool") == "docker"]


def run_script(name: str, args: List[str], env: Dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["bash", str(COMPOSE_DIR / name), *args],
        capture_output=True,
        text=True,
        timeout=60,
        cwd=ROOT,
        env=env,
        check=False,
    )
