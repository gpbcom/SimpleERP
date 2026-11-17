🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D107 Move records before removing a status

# 📜 D107 Move records before removing a status

**Status:** ✅ decided

## Context

What happens to records in a status that is removed or archived.

## Options

- Must be moved first.
- Kept as they are.

## Choice

Removing a status is refused while records use it; simple-ERP offers to move them to another status in one go.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

No record is ever left in a removed status.

## Related

- [UC-F2-02](../../02-functional/f02-no-code-configuration/use-cases/01-configure-a-record-type/uc-f02-02-change-the-statuses-of-a-record-type.md)
- [BR-F2-06](../../02-functional/f02-no-code-configuration/business-rules/br-f02-06-move-records-before-removing-a-status.md)

---

⬅️ [D106 Core statuses are locked](d106-core-statuses-locked.md) · ⬆️ [Up](README.md) ·
➡️ [D108 Form layout options](d108-form-layout-options.md)
