🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F2-09 New record types start closed

# 📏 BR-F2-09 New record types start closed

**Status:** ✅ specified

## Statement

A new record type is visible to no role until a configurator ticks roles for it in the role matrix.

## Why

No data is visible by accident. See
[D112](../../../06-decisions/f02-no-code-configuration/d112-new-record-types-start-closed.md).

## Examples

| Case | Result |
|---|---|
| "Vehicles" published, no role ticked | Nobody sees it, not even in the API (D12) |
| Fleet manager role ticked See and Change | They see and edit vehicles |
| The configurator who created it | Sees it in the editor, not its records, unless a role allows |

## Applies to

- [UC-F2-04](../use-cases/01-configure-a-record-type/uc-f02-04-create-a-new-record-type.md)

## Exceptions

The IT provider administrator sees everything (D90).

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-08 Read-only per status on every channel](br-f02-08-read-only-per-status-on-every-channel.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F2-10 Legal mentions are locked](br-f02-10-legal-mentions-are-locked.md)
