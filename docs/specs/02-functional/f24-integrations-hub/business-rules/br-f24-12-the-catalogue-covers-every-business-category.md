🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-12 The catalogue covers every business category

# 📏 BR-F24-12 The catalogue covers every business category

**Status:** ✅ specified

## Statement

The catalogue lists connectors in these categories: office suites, CRM, ATS, banks, payments, online shops, accounting,
payroll and HR, carriers, e-invoicing platforms, automation tools, and sourcing and messaging (Unipile, for LinkedIn,
D518); each connector shows its category, icon, vendor country, cost and the rights it asks.

## Why

Banks, payments, shops, accounting, payroll and carriers were absent (D481).

## Examples

| Case | Result |
|---|---|
| Filter "banks" | passes: bank connectors listed with icons |
| Connector with no category | fails: not published |
| Paid connector | passes: cost shown before connecting (BR-F24-11) |

## Applies to

- [UC-F24-21 Connect a bank, payment, shop, accounting or carrier tool](../use-cases/06-business-tools/uc-f24-21-connect-a-bank-payment-shop-accounting-or-carrier-tool.md)
- [UC-F24-01 Browse the connector catalogue](../use-cases/01-find-and-connect/uc-f24-01-browse-the-connector-catalogue.md)
- [UC-F9-40 Search and rank LinkedIn profiles](../../f09-hr-and-projects/use-cases/02-recruit/uc-f09-40-search-and-rank-linkedin-profiles.md)

## Exceptions

None.

## Configurable

No; the maintainers keep the list (UC-F24-18).

## Open questions

None.

---

⬅️ [BR-F24-11 Connector costs are metered](br-f24-11-connector-costs-metered.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F24-13](br-f24-13-automation-tools-through-signed-webhooks-and-the-api.md)
