"""A stand-in for the gh command line, run as a child process by the fake ``gh`` of ``FakeGh``.

Usage: ``python3 gh_stub.py <state folder> <gh arguments...>``. It appends its arguments to ``calls.jsonl`` and
answers with the first rule of ``rules.json`` whose ``args`` start its arguments: ``stdout``, ``exit`` and the
``files`` it writes under the folder given with ``--dir``.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    state = Path(sys.argv[1])
    arguments = sys.argv[2:]
    with (state / "calls.jsonl").open("a", encoding="utf-8") as calls:
        calls.write(json.dumps(arguments) + "\n")
    rules = json.loads((state / "rules.json").read_text(encoding="utf-8"))
    for rule in rules:
        prefix = rule["args"]
        if arguments[: len(prefix)] != prefix:
            continue
        if rule.get("files") and "--dir" in arguments:
            folder = Path(arguments[arguments.index("--dir") + 1])
            for name, content in rule["files"].items():
                (folder / name).parent.mkdir(parents=True, exist_ok=True)
                (folder / name).write_text(content, encoding="utf-8")
        sys.stdout.write(rule.get("stdout", ""))
        sys.stderr.write(rule.get("stderr", ""))
        return int(rule.get("exit", 0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
