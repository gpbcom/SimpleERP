🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-02 No voice prints

# 📏 BR-F4-02 No voice prints

**Status:** ✅ specified

## Statement

Speakers are named from the platform's participant names, or labelled "Speaker 1, 2..." and renamed by the organiser
during review; SimpleERP never builds or keeps voice prints.

## Why

Voice prints are biometric data. See [D214](../../../06-decisions/f04-meetings/d214-speaker-names.md).

Legal values from the France country pack:
[CR-FR-053 No biometric voice prints](../../../10-country-packs/france/data-protection/cr-fr-053-no-biometric-voice-prints.md).

## Examples

| Case | Result |
|---|---|
| A Teams meeting | Names from Teams |
| An in-person meeting | Speaker 1, 2, 3; the organiser renames Speaker 2 "Durand SA buyer" |

## Applies to

Every F4 use case.

- [UC-F4-23 Handle an outside speaker's objection or erasure](../use-cases/13-outside-people-and-follow-up/uc-f04-23-handle-an-outside-speakers-objection-or-erasure.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F4-01 Every recording is announced](br-f04-01-every-recording-is-announced.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-03 Recordings are deleted once checked](br-f04-03-recordings-are-deleted-once-checked.md)
