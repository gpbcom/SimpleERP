"""Generate the Bruno collection of a service from its committed OpenAPI document, and check it is fresh (D406).

Usage:
    python3 .github/scripts/bruno_collection.py generate --service backend/services/<name> [--root <repo root>]
    python3 .github/scripts/bruno_collection.py check --service backend/services/<name> [--root <repo root>]

The collection of a service lives in ``bruno/<name>/``. The generator owns only ``bruno.json``, ``collection.bru``
and ``requests/``: the hand-written tests, the environments and the ``.gitignore`` are never written, compared or
removed. One request file is written per operation of ``<service>/openapi.json``, in the folder of its first tag
(``default`` without a tag). A request holds the method, the URL, ``auth: none``, the parameters as disabled empty
entries and an empty JSON body: no example, default value or security scheme of the document is ever copied, so
that no credential reaches the collection (TEST-1, D426).

The output is deterministic: operations are sorted by path then method, with no timestamp and LF line endings.

``generate`` writes the files and removes the request files that are no longer generated. ``check`` compares in
memory and lists the missing, changed and unexpected files, then exits 1; with no collection it says there is
nothing to check and exits 0. Exit codes: 0 fresh or generated, 1 stale or an unreadable document, 2 bad arguments.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

OPENAPI = "openapi.json"
COLLECTIONS = "bruno"
REQUESTS = "requests"
DEFAULT_FOLDER = "default"
METHODS = ("get", "put", "post", "delete", "options", "head", "patch", "trace")
COMMANDS = ("generate", "check")
USAGE = "usage: bruno_collection.py {generate,check} --service backend/services/<name> [--root <repo root>]"
PATH_PARAMETER = re.compile(r"\{([^{}]+)\}")
NOT_WORD = re.compile(r"[^a-z0-9]+")
SPACES = re.compile(r"\s+")


def slug(text: str) -> str:
    """Turn ``text`` into a lower-case file name made of letters, digits and underscores."""
    return NOT_WORD.sub("_", text.lower()).strip("_")


def bruno_json(name: str) -> str:
    """Write ``bruno.json``, which names the collection."""
    document = {"version": "1", "name": name, "type": "collection", "ignore": ["node_modules", ".git"]}
    return json.dumps(document, indent=2) + "\n"


def collection_bru(service: str) -> str:
    """Write ``collection.bru``, whose docs say the collection is generated and how to regenerate it."""
    command = f"python3 .github/scripts/bruno_collection.py generate --service {service}"
    return (
        "docs {\n"
        "  This collection is generated from the OpenAPI document of the service. Do not edit the requests.\n"
        f"  Regenerate it with: {command}\n"
        "}\n"
    )


def request_name(operation: Dict[str, object], method: str, path: str) -> str:
    """Name a request after its summary, else its operation ID, else its method and path."""
    for key in ("summary", "operationId"):
        value = operation.get(key)
        if isinstance(value, str) and value.strip():
            return SPACES.sub(" ", value).strip()
    return f"{method.upper()} {path}"


def request_file(operation: Dict[str, object], method: str, path: str) -> str:
    """Name a request file after its operation ID, else its method and path."""
    value = operation.get("operationId")
    base = slug(value) if isinstance(value, str) else ""
    return f"{base or slug(f'{method} {path}')}.bru"


def request_folder(operation: Dict[str, object]) -> str:
    """Pick the folder of a request: its first tag, else ``default``."""
    tags = operation.get("tags")
    if isinstance(tags, list) and tags and isinstance(tags[0], str):
        return slug(tags[0]) or DEFAULT_FOLDER
    return DEFAULT_FOLDER


def parameters_of(operation: Dict[str, object], location: str) -> List[str]:
    """List the sorted names of the parameters of ``operation`` that sit in ``location``."""
    names: Set[str] = set()
    parameters = operation.get("parameters")
    if isinstance(parameters, list):
        for parameter in parameters:
            if isinstance(parameter, dict) and parameter.get("in") == location:
                name = parameter.get("name")
                if isinstance(name, str) and name:
                    names.add(name)
    return sorted(names)


def has_json_body(operation: Dict[str, object]) -> bool:
    """Tell whether ``operation`` takes a JSON request body."""
    body = operation.get("requestBody")
    if not isinstance(body, dict):
        return False
    content = body.get("content")
    return isinstance(content, dict) and any(
        isinstance(kind, str) and (kind == "application/json" or kind.endswith("+json")) for kind in content
    )


def request_bru(operation: Dict[str, object], method: str, path: str, seq: int) -> str:
    """Write one request file, with no example, default value or security scheme of the operation."""
    url = "{{baseUrl}}" + PATH_PARAMETER.sub(r"{{\1}}", path)
    json_body = has_json_body(operation)
    lines = [
        "meta {",
        f"  name: {request_name(operation, method, path)}",
        "  type: http",
        f"  seq: {seq}",
        "}",
        "",
        f"{method} {{",
        f"  url: {url}",
        f"  body: {'json' if json_body else 'none'}",
        "  auth: none",
        "}",
    ]
    for location in ("path", "query"):
        names = parameters_of(operation, location)
        if names:
            prefix = "" if location == "path" else "~"
            lines += ["", f"params:{location} {{", *[f"  {prefix}{name}: " for name in names], "}"]
    if json_body:
        lines += ["", "body:json {", "  {}", "}"]
    return "\n".join(lines) + "\n"


def operations_of(document: Dict[str, object]) -> List[Tuple[str, str, Dict[str, object]]]:
    """List the operations of the document as (path, method, operation), sorted by path then method."""
    found: List[Tuple[str, str, Dict[str, object]]] = []
    paths = document.get("paths")
    if not isinstance(paths, dict):
        return found
    for path, item in paths.items():
        if not isinstance(item, dict):
            continue
        for method in METHODS:
            operation = item.get(method)
            if isinstance(operation, dict):
                found.append((str(path), method, operation))
    return sorted(found, key=lambda entry: (entry[0], entry[1]))


def render(name: str, service: str, document: Dict[str, object]) -> Dict[str, str]:
    """Build every generated file of the collection, as a relative path to its content.

    The ``seq`` of a request counts the methods of one path within its folder, so a path always starts at 1.
    """
    files = {"bruno.json": bruno_json(name), "collection.bru": collection_bru(service)}
    counters: Dict[Tuple[str, str], int] = {}
    for path, method, operation in operations_of(document):
        folder = request_folder(operation)
        counters[(folder, path)] = counters.get((folder, path), 0) + 1
        target = f"{REQUESTS}/{folder}/{request_file(operation, method, path)}"
        if target in files:
            target = target.removesuffix(".bru") + f"_{method}.bru"
        files[target] = request_bru(operation, method, path, counters[(folder, path)])
    return files


def read_document(path: Path) -> Optional[Dict[str, object]]:
    """Read the OpenAPI document, or None when it is missing or is not a JSON object."""
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return document if isinstance(document, dict) else None


def existing_requests(collection: Path) -> List[str]:
    """List the files under ``requests/`` of the collection, as relative paths."""
    folder = collection / REQUESTS
    if not folder.is_dir():
        return []
    return sorted(path.relative_to(collection).as_posix() for path in folder.rglob("*") if path.is_file())


def remove_empty_folders(collection: Path) -> None:
    """Remove the empty folders left under ``requests/``, deepest first."""
    folder = collection / REQUESTS
    if not folder.is_dir():
        return
    for path in sorted(folder.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()


def generate(collection: Path, files: Dict[str, str]) -> int:
    """Write the generated files and remove the request files that are no longer generated."""
    for relative in existing_requests(collection):
        if relative not in files:
            (collection / relative).unlink()
    remove_empty_folders(collection)
    for relative, content in files.items():
        target = collection / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
    print(f"Generated {len(files)} files in {collection}.")
    return 0


def check(collection: Path, files: Dict[str, str], command: str) -> int:
    """Compare the collection with the generated files in memory, and list what differs."""
    missing: List[str] = []
    changed: List[str] = []
    for relative, content in files.items():
        target = collection / relative
        if not target.is_file():
            missing.append(relative)
        elif target.read_bytes() != content.encode("utf-8"):
            changed.append(relative)
    unexpected = [relative for relative in existing_requests(collection) if relative not in files]
    if not (missing or changed or unexpected):
        print("The Bruno collection is fresh.")
        return 0
    for title, names in (("Missing", missing), ("Changed", changed), ("Unexpected", unexpected)):
        for relative in names:
            print(f"{title}: {(collection / relative).as_posix()}")
    print(f"The Bruno collection is stale. Run: {command}")
    return 1


def parse_args(argv: List[str]) -> Optional[argparse.Namespace]:
    """Read the command, the service and the root, or None when the arguments are bad."""
    parser = argparse.ArgumentParser(add_help=False, allow_abbrev=False, exit_on_error=False)
    parser.add_argument("command")
    parser.add_argument("--service")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    try:
        args, unknown = parser.parse_known_args(argv)
    except (argparse.ArgumentError, SystemExit):
        return None
    if unknown or args.command not in COMMANDS or not args.service:
        return None
    return args


def main(argv: Optional[List[str]] = None) -> int:
    """Run ``generate`` or ``check`` for one service and return the exit code."""
    parsed = parse_args(sys.argv[1:] if argv is None else argv)
    if parsed is None:
        print(USAGE, file=sys.stderr)
        return 2
    service: str = parsed.service.strip("/")
    root: Path = parsed.root
    name = service.rsplit("/", 1)[-1]
    collection = root / COLLECTIONS / name
    command = f"python3 .github/scripts/bruno_collection.py generate --service {service}"
    if parsed.command == "check" and not collection.is_dir():
        print(f"There is no collection in {COLLECTIONS}/{name}: nothing to check.")
        return 0
    document = read_document(root / service / OPENAPI)
    if document is None:
        print(f"Cannot read {service}/{OPENAPI}: it is missing or is not a JSON object.", file=sys.stderr)
        return 1
    files = render(name, service, document)
    if parsed.command == "generate":
        return generate(collection, files)
    return check(collection, files, command)


if __name__ == "__main__":
    sys.exit(main())
