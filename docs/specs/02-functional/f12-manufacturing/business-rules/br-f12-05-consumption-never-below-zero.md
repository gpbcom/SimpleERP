🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-05 Consumption never below zero

# 📏 BR-F12-05 Consumption never below zero

**Status:** ✅ specified

## Statement

Consuming components never makes stock negative (D275): the shortage is shown and the operator waits or the planner
substitutes.

## Why

See [D312](../../../06-decisions/f12-manufacturing/d312-manufacturing-coverage.md).

## Examples

| Case | Result |
|---|---|
| 10 needed, 8 in stock | 8 consumed, shortage of 2 shown |

## Applies to

Every F12 use case concerned.

- [UC-F12-26 Keep working on the tablet without the network](../use-cases/11-finite-schedule-and-the-tablet/uc-f12-26-keep-working-on-the-tablet-without-the-network.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F12-04 Lots traced both ways](br-f12-04-lots-traced-both-ways.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F12-06 A failed check blocks the step](br-f12-06-a-failed-check-blocks-the-step.md)
