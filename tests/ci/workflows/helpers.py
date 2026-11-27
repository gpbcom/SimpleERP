from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import Dict, List, Union, cast

# Third-party imports
import yaml
from pydantic import JsonValue

ROOT = Path(__file__).resolve().parents[3]
WORKFLOWS = ROOT / ".github" / "workflows"
SCRIPTS = ROOT / ".github" / "scripts"
Workflow = Dict[Union[str, bool], JsonValue]
Step = Dict[str, JsonValue]


def workflow_paths() -> List[Path]:
    return sorted(WORKFLOWS.glob("*.yml"))


def workflow(name: str) -> Workflow:
    data = yaml.safe_load((WORKFLOWS / name).read_text(encoding="utf-8"))
    assert isinstance(data, dict), name
    return cast(Workflow, data)


def triggers(name: str) -> Dict[str, Dict[str, JsonValue]]:
    """Return the ``on:`` block, which YAML 1.1 reads as the key ``True``."""
    data = workflow(name)
    return cast(Dict[str, Dict[str, JsonValue]], data.get("on", data.get(True)))


def jobs(name: str) -> Dict[str, Dict[str, JsonValue]]:
    return cast(Dict[str, Dict[str, JsonValue]], workflow(name)["jobs"])


def steps(name: str, job: str) -> List[Step]:
    return cast(List[Step], jobs(name)[job].get("steps", []))


def runs(name: str, job: str) -> str:
    return "\n".join(str(step.get("run", "")) for step in steps(name, job))


def step_using(name: str, job: str, action: str) -> Step:
    for step in steps(name, job):
        if str(step.get("uses", "")).startswith(action + "@"):
            return step
    raise AssertionError(f"No step of {name} {job} uses {action}.")


def with_of(step: Step) -> Dict[str, JsonValue]:
    return cast(Dict[str, JsonValue], step.get("with", {}))


def every_uses(name: str) -> List[str]:
    """Return every ``uses:`` of a workflow, of its steps and of its jobs that call a reusable workflow."""
    found: List[str] = []
    for job, body in jobs(name).items():
        if "uses" in body:
            found.append(str(body["uses"]))
        found += [str(step["uses"]) for step in steps(name, job) if "uses" in step]
    return found
