from __future__ import annotations

from typing import Dict, Optional

import pytest
from erp_config.models.exceptions import SEConfigSectionInvalidKey
from pydantic import JsonValue, ValidationError

from backend.shared.config.tests.models.config_section.sample_mail_section import SampleMailSection


class TestConfigSection:
    def test_defaults(self) -> None:
        section = SampleMailSection()
        assert section.sender == "erp@example.org"
        assert section.password_key is None

    def test_full_valid_construction(self) -> None:
        section = SampleMailSection(sender="a@b.org", password_key="mail/smtp-password")
        assert section.sender == "a@b.org"
        assert section.password_key == "mail/smtp-password"

    @pytest.mark.parametrize("name", ["password_key"])
    def test_none_becomes_the_default(self, name: str) -> None:
        section = SampleMailSection.model_validate({name: None})
        assert getattr(section, name) is None

    @pytest.mark.parametrize("name", ["mail/smtp-password", "a", "A1.b_c-d/e"])
    def test_a_valid_vault_entry_name_is_accepted(self, name: str) -> None:
        assert SampleMailSection(password_key=name).password_key == name

    @pytest.mark.parametrize("value", ["", "   ", "has space", "pass:word", "a" * 129, 42, True])
    def test_rejects_bad_values(self, value: JsonValue) -> None:
        with pytest.raises(SEConfigSectionInvalidKey):
            SampleMailSection.model_validate({"password_key": value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            SampleMailSection.model_validate({"unknown": 1})

    def test_round_trip(self) -> None:
        section = SampleMailSection(sender="a@b.org", password_key="mail/smtp-password")
        data: Dict[str, Optional[str]] = section.model_dump()
        assert SampleMailSection.model_validate(data) == section
        assert SampleMailSection.model_validate_json(section.model_dump_json()) == section

    def test_assignment_is_refused_because_the_model_is_frozen(self) -> None:
        section = SampleMailSection()
        with pytest.raises(ValidationError):
            section.sender = "other@example.org"

    def test_repr_and_str_mask_the_vault_entry_name(self) -> None:
        section = SampleMailSection(sender="a@b.org", password_key="mail/smtp-password")
        for text in (repr(section), str(section)):
            assert "***" in text
            assert "mail/smtp-password" not in text
            assert "a@b.org" in text
