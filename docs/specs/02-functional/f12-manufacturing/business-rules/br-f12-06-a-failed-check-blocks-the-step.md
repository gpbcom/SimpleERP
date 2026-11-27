🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-06 A failed check blocks the step

# 📏 BR-F12-06 A failed check blocks the step

**Status:** ✅ specified

## Statement

A failed mandatory quality check blocks the next operation and raises a non-conformity, until it is handled.

## Why

See [D312](../../../06-decisions/f12-manufacturing/d312-manufacturing-coverage.md).

## Examples

| Case | Result |
|---|---|
| Diameter out of tolerance | Next operation blocked, non-conformity NC-88 |

## Applies to

Every F12 use case concerned.

- [UC-F12-25 Monitor a process with control charts](../use-cases/12-quality-engineering/uc-f12-25-monitor-a-process-with-control-charts.md)

## Exceptions

None.

## Configurable

Checks per operation, mandatory or not.

## Open questions

None.

---

⬅️ [BR-F12-05 Consumption never below zero](br-f12-05-consumption-never-below-zero.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F12-07 Operators sign in at the work centre](br-f12-07-operators-sign-in-at-the-work-centre.md)
