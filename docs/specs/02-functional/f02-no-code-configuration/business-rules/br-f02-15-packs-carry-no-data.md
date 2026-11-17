🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F2-15 Packs carry no data

# 📏 BR-F2-15 Packs carry no data

**Status:** ✅ specified

## Statement

A configuration pack carries configuration only: never records, users or secrets (connection credentials, AI keys); its
automations arrive inactive.

## Why

A pack is shared between companies; no company's data or secrets may travel with it. See
[D134](../../../06-decisions/f02-no-code-configuration/d134-pack-content.md).

## Examples

| In the exporting company | In the pack |
|---|---|
| The record type Vehicles and its fields | Yes |
| The 40 vehicles recorded | No |
| The rule "Remind after 3 days" | Yes, inactive on import |
| The role Fleet manager | Yes |
| The users holding it | No |
| The GitHub connection's token | No |

## Applies to

- [UC-F2-11](../use-cases/06-share-a-configuration/uc-f02-11-export-or-import-a-configuration-as-a-pack.md); BR-F1-19.
- [UC-F2-25 Merge a sector pack upgrade with local changes](../use-cases/10-change-safely/uc-f02-25-merge-a-sector-pack-upgrade-with-local-changes.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-14 AI steps return their declared format](br-f02-14-ai-steps-return-their-declared-format.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F2-16 A sandbox never touches live data](br-f02-16-sandbox-never-touches-live-data.md)
