from __future__ import annotations

import pytest

from progress_updates.service.rendering.secret_mask import SecretMask


class TestSecretMask:
    @pytest.mark.parametrize(
        "secret",
        [
            "ghp_abcdefghijklmnopqrstuvwxyz0123456789",
            "github_pat_11ABCDEFG0123456789_abcdefghijklmnopqrstuvwxyz",
            "sk-ant-api03-abcdefghijklmnopqrstuvwxyz",
            "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.abcdefghijk",
            "AKIAABCDEFGHIJKLMNOP",
        ],
    )
    def test_known_token_shapes_are_masked(self, secret: str) -> None:
        assert SecretMask().mask(f"before {secret} after") == "before ••• after"

    @pytest.mark.parametrize(
        "text",
        [
            "password=hunter2",
            "token: abc123",
            "Authorization: Bearer abc.def",
            "GITHUB_TOKEN=abc123",
            "db_password: 'hunter2'",
            'api_key="abc123"',
            "--access-key abc123",
        ],
    )
    def test_named_secrets_keep_their_name_and_lose_their_value(self, text: str) -> None:
        masked = SecretMask().mask(text)
        assert "•••" in masked
        assert "hunter2" not in masked
        assert "abc123" not in masked
        assert "abc.def" not in masked

    @pytest.mark.parametrize(
        "secret",
        ["xoxb-1234567890-abcdefghijkl", "-----BEGIN RSA PRIVATE KEY-----", "-----BEGIN OPENSSH PRIVATE KEY-----"],
    )
    def test_other_secret_shapes_are_masked(self, secret: str) -> None:
        assert secret not in SecretMask().mask(f"x {secret} y")

    def test_plain_text_is_unchanged(self) -> None:
        assert SecretMask().mask("43 passed in 0.8 s") == "43 passed in 0.8 s"
