🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F22-13 Anomalies flagged

# 📏 BR-F22-13 Anomalies flagged

**Status:** ✅ specified

## Statement

A cost rising far above its usual pace (a runaway agent, a looping workflow) is flagged at once and may be paused by the
administrator.

## Why

See [D398](../../../06-decisions/f22-unified-cost-management/d398-budgets-warn-then-stop.md).

## Examples

| Case | Result |
|---|---|
| Agent spends 10 times its hourly average | Alert, pause offered |

## Applies to

Every F22 use case concerned.

## Exceptions

None.

## Configurable

Sensitivity.

## Open questions

None.

---

⬅️ [BR-F22-12 Costs allocated to accounts](br-f22-12-allocation-to-accounts.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F22-14 Foreign prices converted at the day's rate](br-f22-14-foreign-prices-converted-at-the-days-rate.md)
