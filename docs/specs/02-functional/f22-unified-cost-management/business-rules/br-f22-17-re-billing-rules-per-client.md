🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F22-17 Re-billing rules per client

# 📏 BR-F22-17 Re-billing rules per client

**Status:** ✅ specified

## Statement

An IT provider re-bills each client by its rule: a margin on cost, a rounding, an included amount per month; the
client's statement shows its usage and the rule, and never another client's data.

## Why

IT providers re-bill many clients (D479).

## Examples

| Case | Result |
|---|---|
| Margin 15 %, 50.00 EUR included, usage 80.00 EUR | passes: billed 34.50 EUR |
| Client with no rule | passes: default rule, provider told |
| Statement showing another client's usage | fails: never |

## Applies to

- [UC-F22-25 Set re-billing rules per client](../use-cases/07-it-provider-re-billing/uc-f22-25-set-re-billing-rules-per-client.md)
- [UC-F22-26 Send each client its usage statement](../use-cases/07-it-provider-re-billing/uc-f22-26-send-each-client-its-usage-statement.md)
- [UC-F22-16 Re-bill clients as an IT provider](../use-cases/05-billing/uc-f22-16-re-bill-clients-as-an-it-provider.md)

## Exceptions

None.

## Configurable

The provider sets rules per client.

## Open questions

None.

---

⬅️ [BR-F22-16](br-f22-16-recommendations-show-their-saving-and-never-act-alone.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F22-18 Automatic top-ups stay within the budget](br-f22-18-automatic-top-ups-stay-within-the-budget.md)
