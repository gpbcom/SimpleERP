🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D106 Core statuses are locked

# 📜 D106 Core statuses are locked

**Status:** ✅ decided

## Context

Whether the statuses the core logic relies on can be changed.

## Options

- Locked, extendable around.
- Fully editable.

## Choice

Locked: core statuses keep their meaning and cannot be removed; configurators add their own statuses before or after
them.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Invoicing, stock and accounting logic stay correct.

## Related

- [UC-F2-02](../../02-functional/f02-no-code-configuration/use-cases/01-configure-a-record-type/uc-f02-02-change-the-statuses-of-a-record-type.md)
- [BR-F2-05](../../02-functional/f02-no-code-configuration/business-rules/br-f02-05-core-statuses-are-locked.md)

---

⬅️ [D105 Status configuration](d105-status-configuration.md) · ⬆️ [Up](README.md) ·
➡️ [D107 Move records before removing a status](d107-move-records-before-removing.md)
