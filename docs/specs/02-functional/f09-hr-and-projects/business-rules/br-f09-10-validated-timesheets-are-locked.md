🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-10 Validated timesheets are locked

# 📏 BR-F9-10 Validated timesheets are locked

**Status:** ✅ specified

## Statement

A validated timesheet can no longer be changed by its author; a manager reopens it with a reason; billed time cannot
change.

## Why

See [D289](../../../06-decisions/f09-hr-and-projects/d289-hr-coverage.md).

## Examples

| Case | Result |
|---|---|
| Validated week | Locked |
| Already invoiced hours | Never changed |

## Applies to

Every F9 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F9-09 Shifts respect people and rules](br-f09-09-shifts-respect-people-and-rules.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-11 Candidate data has a term](br-f09-11-candidate-data-has-a-term.md)
