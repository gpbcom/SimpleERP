from __future__ import annotations

# Standard library imports
import re
import subprocess
from pathlib import Path
from typing import List, Optional, Pattern, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parents[3]
BRUNO_FOLDER = "bruno"
REQUIRED_COLLECTIONS = ["platform"]
AUTH_MODES = ["basic", "bearer", "apikey", "digest", "oauth2", "awsv4", "ntlm", "wsse"]
AUTH_BLOCKS = {f"auth:{mode}" for mode in AUTH_MODES}
AUTH_STRUCTURAL_KEYS = {
    "grant_type",
    "scope",
    "state",
    "pkce",
    "placement",
    "credentials_placement",
    "token_placement",
    "token_header_prefix",
    "callback_url",
    "authorization_url",
    "access_token_url",
    "refresh_token_url",
    "auto_fetch_token",
    "auto_refresh_token",
    "region",
    "service",
    "profilename",
    "key",
}
SECRET_HEADERS = ["Authorization", "Proxy-Authorization", "Cookie", "X-Api-Key"]
SECRET_NAME_PATTERN = r"password|passwd|secret|token|api[_-]?key|client[_-]?secret|private[_-]?key"
BLOCK_START = re.compile(r"^\s*([A-Za-z][\w:\-]*)\s*([\{\[])\s*$")
ENTRY = re.compile(r"^\s*~?\s*([^\s:]+)\s*:\s*(.*?)\s*$")
HEADER_ENTRY = re.compile(
    r"^\s*~?\s*(" + "|".join(re.escape(name) for name in SECRET_HEADERS) + r")\s*:\s*(.*?)\s*$", re.IGNORECASE
)
SECRET_NAME = re.compile(SECRET_NAME_PATTERN, re.IGNORECASE)
PLACEHOLDER = re.compile(r"\{\{\s*[\w.\-]+\s*\}\}")
SCHEME_WORD = re.compile(r"^(bearer|basic|digest|token)\s+", re.IGNORECASE)
LITERAL_PATTERNS: List[Tuple[str, Pattern[str]]] = [
    ("a bearer token", re.compile(r"Bearer\s+(?!\{\{)[^\s{]+")),
    ("a JWT", re.compile(r"eyJ[\w\-]+\.eyJ[\w\-]+\.")),
    ("a private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("a GitHub token", re.compile(r"ghp_\w+|github_pat_\w+")),
    ("an AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("a URL with a user and a password", re.compile(r"[A-Za-z][\w+.\-]*://[^\s/:@{}]+:[^\s/@{}]+@")),
]


def is_literal(value: str) -> bool:
    """Tell whether a value holds something other than empty or placeholders."""
    remainder = SCHEME_WORD.sub("", value.strip())
    remainder = PLACEHOLDER.sub("", remainder).strip()
    return remainder != ""


def is_env_file(path: Path) -> bool:
    """Tell whether a file is a dotenv file."""
    return path.name == ".env" or path.name.startswith(".env.") or path.name.endswith(".env")


def list_files(root: Path) -> List[Path]:
    """List the files of ``bruno/`` under a root: git's view inside a repository, else a recursive walk."""
    folder = root / BRUNO_FOLDER
    if not folder.is_dir():
        return []
    try:
        top = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"], cwd=root, capture_output=True, text=True, check=True
        ).stdout.strip()
        in_repository = Path(top).resolve() == root.resolve()
    except (subprocess.CalledProcessError, FileNotFoundError):
        in_repository = False
    if in_repository:
        listed = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "--", BRUNO_FOLDER],
            cwd=root,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        paths = [root / name for name in listed]
    else:
        paths = list(folder.rglob("*"))
    return sorted({path for path in paths if path.is_file()})


def scan_line(line: str, block: Optional[str]) -> Optional[str]:
    """Return why a line holds a credential, or None."""
    header = HEADER_ENTRY.match(line)
    if header and is_literal(header.group(2)):
        return f"the {header.group(1)} header has a literal value"
    entry = ENTRY.match(line)
    if entry and block is not None:
        name, value = entry.group(1), entry.group(2)
        if block in AUTH_BLOCKS and name.lower() not in AUTH_STRUCTURAL_KEYS and is_literal(value):
            return f"the {block} block has a literal {name}"
        if (block == "vars" or block.startswith("vars:")) and SECRET_NAME.search(name) and is_literal(value):
            return f"the variable {name} has a literal value"
    for label, pattern in LITERAL_PATTERNS:
        if pattern.search(line):
            return f"the line holds {label}"
    return None


def scan_file(path: Path, root: Path) -> List[str]:
    """Scan one file and return its findings as ``path:line: reason``."""
    relative = path.relative_to(root).as_posix()
    findings: List[str] = []
    if is_env_file(path):
        findings.append(f"{relative}:1: a dotenv file must not be in bruno")
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return findings
    block: Optional[str] = None
    skipping: Set[str] = set()
    for number, line in enumerate(lines, start=1):
        start = BLOCK_START.match(line)
        if start:
            block = start.group(1)
            if start.group(2) == "[":
                skipping.add(block)
            continue
        if line.strip() in ("}", "]"):
            skipping.discard(block or "")
            block = None
            continue
        if block in skipping:
            continue
        reason = scan_line(line, block)
        if reason:
            findings.append(f"{relative}:{number}: {reason}")
    return findings


def scan(root: Path) -> List[str]:
    """Scan every file of ``bruno/`` under a root and return all findings."""
    findings: List[str] = []
    for path in list_files(root):
        findings.extend(scan_file(path, root))
    return findings


def collections(root: Path) -> List[str]:
    """List the collection folders of ``bruno/``, with the required ones."""
    folder = root / BRUNO_FOLDER
    found = {child.name for child in folder.iterdir() if child.is_dir()} if folder.is_dir() else set()
    return sorted(found | set(REQUIRED_COLLECTIONS))


def ignores_env(root: Path, name: str) -> bool:
    """Tell whether a collection's ``.gitignore`` ignores ``.env``."""
    path = root / BRUNO_FOLDER / name / ".gitignore"
    if not path.is_file():
        return False
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]
    return any(line in (".env", "/.env", ".env*", "*.env", "**/.env") for line in lines)
