🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-18 Outside results are marked

# 📏 BR-F3-18 Outside results are marked

**Status:** ✅ specified

## Statement

Results from an outside tool carry the tool's name and an "outside source" badge, apart from ERP data; the AI assistant
never mixes them into ERP figures. Saving them into records goes through the confirmation card (BR-F3-07 to BR-F3-10).

## Why

Users must know what the ERP vouches for. See
[D170](../../../06-decisions/f03-assistant/d170-outside-results-marked.md).

## Examples

| Case | Result |
|---|---|
| A company's details from an outside register | Shown with "Outside source: Register" |
| "Save this address to Durand" | A confirmation card, then signed through the AI assistant |

## Applies to

- [UC-F3-06](../use-cases/06-use-an-outside-tool/uc-f03-06-use-an-outside-tool-through-the-assistant.md)
- [UC-F3-15 Defend against instructions hidden in content](../use-cases/11-trust-the-answers/uc-f03-15-defend-against-instructions-hidden-in-content.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-17 Only allowed data leaves](br-f03-17-only-allowed-data-leaves.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-19 Personal connections for allowed services](br-f03-19-personal-connections-for-allowed-services.md)
