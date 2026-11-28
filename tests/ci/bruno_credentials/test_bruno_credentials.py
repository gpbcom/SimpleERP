from __future__ import annotations

# Standard library imports
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.ci.bruno_credentials.helpers import REPO_ROOT, collections, ignores_env, scan


def plant(root: Path, name: str, text: str) -> None:
    path = root / "bruno" / "platform" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class TestBrunoCredentials:
    @pytest.mark.parametrize(
        ("name", "text"),
        [
            (".env", "TOKEN=fake\n"),
            ("auth.bru", "auth:basic {\n  username: alice\n  password: not-a-real-one\n}\n"),
            ("auth.bru", "auth:bearer {\n  token: fake-token-value\n}\n"),
            ("auth.bru", "auth:apikey {\n  key: X-Api-Key\n  value: fake-value\n}\n"),
            ("auth.bru", "auth:digest {\n  username: alice\n  password: fake\n}\n"),
            ("auth.bru", "auth:oauth2 {\n  grant_type: client_credentials\n  client_secret: fake\n}\n"),
            ("auth.bru", "auth:awsv4 {\n  accessKeyId: fake\n  secretAccessKey: fake\n}\n"),
            ("auth.bru", "auth:ntlm {\n  username: a\n  password: fake\n}\n"),
            ("auth.bru", "auth:wsse {\n  username: a\n  password: fake\n}\n"),
            ("get.bru", "headers {\n  Authorization: fake-credential\n}\n"),
            ("get.bru", "headers {\n  Proxy-Authorization: fake-credential\n}\n"),
            ("get.bru", "headers {\n  Cookie: session=fake\n}\n"),
            ("get.bru", "headers {\n  x-api-key: fake\n}\n"),
            ("env.bru", "vars {\n  password: fake\n}\n"),
            ("env.bru", "vars:pre-request {\n  api_key: fake\n}\n"),
            ("env.bru", "vars:post-response {\n  client-secret: fake\n}\n"),
            ("env.bru", "vars {\n  refreshToken: fake\n}\n"),
            ("get.bru", "docs {\n  Send Bearer fakevalue here\n}\n"),
            ("get.bru", "docs {\n  eyJhbGciOiJub25lIn0.eyJzdWIiOiJ4In0.sig\n}\n"),
            ("get.bru", "docs {\n  -----BEGIN RSA PRIVATE KEY-----\n}\n"),
            ("get.bru", "docs {\n  ghp_abcdefghijklmnop\n}\n"),
            ("get.bru", "docs {\n  github_pat_abcdefghijklmnop\n}\n"),
            ("get.bru", "docs {\n  AKIAABCDEFGHIJKLMNOP\n}\n"),
            ("get.bru", "get {\n  url: https://alice:hunter2@example.test/v1\n}\n"),
        ],
    )
    def test_a_planted_credential_is_flagged(self, tmp_path: Path, name: str, text: str) -> None:
        plant(tmp_path, name, text)
        findings = scan(tmp_path)
        assert len(findings) >= 1
        assert findings[0].startswith(f"bruno/platform/{name}:")

    @pytest.mark.parametrize(
        ("name", "text"),
        [
            ("auth.bru", "auth:bearer {\n  token: {{token}}\n}\n"),
            ("auth.bru", "auth:basic {\n  username: {{process.env.USER_NAME}}\n  password: {{process.env.PASS}}\n}\n"),
            ("auth.bru", "auth:bearer {\n  token:\n}\n"),
            ("get.bru", "headers {\n  Authorization: Bearer {{token}}\n  Accept: application/json\n}\n"),
            ("get.bru", "headers {\n  X-Api-Key: {{process.env.API_KEY}}\n}\n"),
            ("env.bru", "vars {\n  baseUrl: http://localhost:8000\n  password: {{process.env.PASS}}\n}\n"),
            ("env.bru", "vars:secret [\n  password,\n  token\n]\n"),
            ("get.bru", "get {\n  url: {{user}}:{{pass}}@{{host}}/v1\n}\n"),
            (".gitignore", ".env\n"),
        ],
    )
    def test_placeholders_and_empty_values_are_not_flagged(self, tmp_path: Path, name: str, text: str) -> None:
        plant(tmp_path, name, text)
        assert scan(tmp_path) == []

    def test_a_folder_without_bruno_has_no_finding(self, tmp_path: Path) -> None:
        assert scan(tmp_path) == []

    def test_the_finding_names_the_file_and_the_line(self, tmp_path: Path) -> None:
        plant(tmp_path, "env.bru", "vars {\n  host: x\n  password: fake\n}\n")
        assert scan(tmp_path) == ["bruno/platform/env.bru:3: the variable password has a literal value"]

    def test_the_committed_bruno_folder_holds_no_credential(self) -> None:
        findings = scan(REPO_ROOT)
        assert findings == [], "Credentials found in bruno:\n" + "\n".join(findings)

    @pytest.mark.parametrize("name", collections(REPO_ROOT))
    def test_each_collection_ignores_its_env_file(self, name: str) -> None:
        assert ignores_env(REPO_ROOT, name), f"bruno/{name}/.gitignore must ignore .env."

    def test_a_gitignore_that_does_not_ignore_env_is_refused(self, tmp_path: Path) -> None:
        plant(tmp_path, ".gitignore", "*.log\n")
        assert ignores_env(tmp_path, "platform") is False
