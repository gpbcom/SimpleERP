from __future__ import annotations

# Standard library imports
import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional

OPENAPI = "openapi.json"
SERVICE_NAME = "demo"
SERVICE = f"backend/services/{SERVICE_NAME}"
COLLECTION = f"bruno/{SERVICE_NAME}"
PASSWORD = "S3cret-Passw0rd"
TOKEN = "eyJhbGciOiJIUzI1NiJ9.fake-token"
EXAMPLE_EMAIL = "jane.doe@example.com"
HEALTH_FILE = f"{COLLECTION}/requests/default/health.bru"
GET_FILE = f"{COLLECTION}/requests/customers/get_customer.bru"
CREATE_FILE = f"{COLLECTION}/requests/customers/create_customer.bru"
OWNED_FILES = [
    f"{COLLECTION}/bruno.json",
    f"{COLLECTION}/collection.bru",
    HEALTH_FILE,
    GET_FILE,
    CREATE_FILE,
]
SPEC: Dict[str, object] = {
    "openapi": "3.1.0",
    "info": {"title": "Demo", "version": "1.0.0"},
    "paths": {
        "/health": {
            "get": {
                "operationId": "health",
                "summary": "Health",
                "responses": {"200": {"description": "OK"}},
            }
        },
        "/v1/customers/{customer_id}": {
            "get": {
                "operationId": "get_customer",
                "summary": "Get one customer",
                "tags": ["Customers"],
                "security": [{"bearerAuth": []}],
                "parameters": [
                    {"name": "customer_id", "in": "path", "required": True, "schema": {"type": "string"}},
                    {
                        "name": "expand",
                        "in": "query",
                        "required": False,
                        "schema": {"type": "string", "default": "everything"},
                    },
                ],
                "responses": {"200": {"description": "OK"}},
            }
        },
        "/v1/customers": {
            "post": {
                "operationId": "create_customer",
                "summary": "Create a customer",
                "tags": ["Customers"],
                "security": [{"bearerAuth": []}],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"type": "object"},
                            "example": {"email": EXAMPLE_EMAIL, "password": PASSWORD},
                        }
                    },
                },
                "responses": {"201": {"description": "Created"}},
            }
        },
    },
    "components": {
        "securitySchemes": {
            "bearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT", "description": TOKEN}
        }
    },
}


def script_path() -> Path:
    return Path(__file__).resolve().parents[3] / ".github" / "scripts" / "bruno_collection.py"


def spec() -> Dict[str, object]:
    return copy.deepcopy(SPEC)


def paths_of(document: Dict[str, object]) -> Dict[str, Dict[str, object]]:
    paths = document["paths"]
    assert isinstance(paths, dict)
    return paths


def write_service(root: Path, document: Optional[Dict[str, object]] = None) -> None:
    folder = root / SERVICE
    folder.mkdir(parents=True, exist_ok=True)
    (folder / OPENAPI).write_text(json.dumps(document if document is not None else spec(), indent=2), encoding="utf-8")


def run_script(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script_path()), *args],
        capture_output=True,
        text=True,
        check=False,
        cwd=root,
    )


def generate(root: Path) -> subprocess.CompletedProcess[str]:
    return run_script(root, "generate", "--service", SERVICE, "--root", str(root))


def check(root: Path) -> subprocess.CompletedProcess[str]:
    return run_script(root, "check", "--service", SERVICE, "--root", str(root))


def generated_files(root: Path) -> List[str]:
    folder = root / COLLECTION
    return sorted(str(path.relative_to(root)) for path in folder.rglob("*") if path.is_file())


def snapshot(root: Path) -> Dict[str, bytes]:
    return {name: (root / name).read_bytes() for name in generated_files(root)}
