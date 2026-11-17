🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D105 Status configuration

# 📜 D105 Status configuration

**Status:** ✅ decided

## Context

What a configurator can do to a record type's statuses.

## Options

- Add, rename, reorder.
- Allowed transitions.
- Conditions per transition.
- Colours and icons.

## Choice

All four: add, rename and reorder statuses; choose which status can follow which; set conditions per transition
(required fields, a role needed); choose each status's colour and icon.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Statuses form a small state machine per record type.

## Related

- [UC-F2-02](../../02-functional/f02-no-code-configuration/use-cases/01-configure-a-record-type/uc-f02-02-change-the-statuses-of-a-record-type.md)

---

⬅️ [D104 Labels per language](d104-labels-per-language.md) · ⬆️ [Up](README.md) ·
➡️ [D106 Core statuses are locked](d106-core-statuses-locked.md)
