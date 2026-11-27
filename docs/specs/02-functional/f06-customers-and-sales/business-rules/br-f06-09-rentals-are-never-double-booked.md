🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F6-09 Rentals are never double-booked

# 📏 BR-F6-09 Rentals are never double-booked

**Status:** ✅ specified

## Statement

An item is rented only when free for the period, padding included; an overdue return is flagged and charged by the price
list.

## Why

See [D304](../../../06-decisions/f06-customers-and-sales/d304-f6-benchmark-gaps.md).

## Examples

| Case | Result |
|---|---|
| Scaffold rented 1 to 5 Dec | Not offered for 3 Dec |

## Applies to

UC-F6-15

## Exceptions

None.

## Configurable

Padding and overdue prices.

## Open questions

None.

---

⬅️ [BR-F6-08 VAT is shown wherever it matters](br-f06-08-vat-is-shown-wherever-it-matters.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-10 Usage is billed from metered data](br-f06-10-usage-is-billed-from-metered-data.md)
