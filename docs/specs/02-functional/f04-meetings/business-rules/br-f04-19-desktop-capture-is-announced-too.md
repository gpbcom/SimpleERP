🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-19 Desktop capture is announced too

# 📏 BR-F4-19 Desktop capture is announced too

**Status:** ✅ specified

## Statement

Recording from the desktop app without a bot is allowed only after the user confirms everyone in the call was told;
simple-ERP posts the recording notice in the call's chat when the platform allows it; anyone can ask to stop (BR-F4-01).

## Why

Bot-less capture must not become secret recording. See
[D233](../../../06-decisions/f04-meetings/d233-desktop-capture-announced.md).

Legal values from the France country pack:
[CR-FR-059 Recordings are announced](../../../10-country-packs/france/ai-and-recording/cr-fr-059-recordings-are-announced.md).

## Examples

| Case | Result |
|---|---|
| A Webex call, desktop capture | Confirm, then notice in the Webex chat, then recording |
| A platform with no chat API | Confirmation only, and the user tells people aloud |

## Applies to

- [UC-F4-10](../use-cases/07-prepare-and-capture-anywhere/uc-f04-10-capture-from-the-desktop-a-file-or-dictation.md)

## Exceptions

None.

## Configurable

Administrators can turn desktop capture off.

## Open questions

None.

---

⬅️ [BR-F4-18 HR meetings stay with HR and the employee](br-f04-18-hr-meetings-are-recorded-for-hr-and-the-employee.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F4-20 Scores come with their evidence](br-f04-20-scores-come-with-their-evidence.md)
