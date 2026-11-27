🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-06 Move records before removing a status

# 📏 BR-F2-06 Move records before removing a status

**Status:** ✅ specified

## Statement

A status still used by records cannot be removed or archived until those records are moved to another status; SimpleERP
offers to move them in one go.

## Why

No record is left in a status that no longer exists. See
[D107](../../../06-decisions/f02-no-code-configuration/d107-move-records-before-removing.md).

## Examples

| Case | Result |
|---|---|
| Remove "Waiting for site visit", used by 14 quotes | Refused; "Move 14 quotes to..." offered |
| Moved to "Draft" | The status can be removed |

## Applies to

- [UC-F2-02](../use-cases/01-configure-a-record-type/uc-f02-02-change-the-statuses-of-a-record-type.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-05 Core statuses are locked](br-f02-05-core-statuses-are-locked.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-07 Layout is not security](br-f02-07-layout-is-not-security.md)
