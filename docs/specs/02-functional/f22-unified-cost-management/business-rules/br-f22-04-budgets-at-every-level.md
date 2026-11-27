🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F22-04 Budgets at every level

# 📏 BR-F22-04 Budgets at every level

**Status:** ✅ specified

## Statement

Budgets are set per company, module, feature, connector and user, per month; the lowest budget reached applies first.

## Why

See [D398](../../../06-decisions/f22-unified-cost-management/d398-budgets-warn-then-stop.md).

## Examples

| Case | Result |
|---|---|
| User budget reached, module not | That user's paid calls stop |

## Applies to

Every F22 use case concerned.

## Exceptions

None.

## Configurable

Levels and amounts.

## Open questions

None.

---

⬅️ [BR-F22-03 Prices versioned per provider](br-f22-03-prices-versioned-per-provider.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F22-05 Warnings at thresholds](br-f22-05-warn-at-thresholds.md)
