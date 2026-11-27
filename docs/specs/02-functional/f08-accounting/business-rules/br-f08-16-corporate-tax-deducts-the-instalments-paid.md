🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-16 Corporate tax deducts the instalments paid

# 📏 BR-F8-16 Corporate tax deducts the instalments paid

**Status:** ✅ specified

## Statement

Corporate tax is computed from the result and its adjustments; instalments paid are deducted and the balance and next
instalments are scheduled on their legal dates.

## Why

Missing an instalment date costs penalties.

## Examples

| Case | Result |
|---|---|
| Tax 41,250, paid 36,000 | Balance 5,250 |
| Instalment date passed | Flagged |

## Applies to

- [UC-F8-24 Compute and pay corporate tax and local business taxes](../use-cases/08-year-end-duties/uc-f08-24-compute-and-pay-corporate-tax-and-local-business-taxes.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F8-15 Dedicated funds keep their purpose](br-f08-15-dedicated-funds-keep-their-purpose.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-17](br-f08-17-annual-accounts-are-approved-within-six-months.md)
