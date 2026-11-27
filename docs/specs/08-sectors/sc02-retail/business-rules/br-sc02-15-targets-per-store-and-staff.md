🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🛍️ [SC02 Retail](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC02-15 Targets per store and staff

# 📏 BR-SC02-15 Targets per store and staff

**Status:** ✅ specified

## Statement

Targets follow the shared targets and commissions,
[UC-F6-25](../../../02-functional/f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-25-set-sales-targets-and-pay-commissions.md),
[BR-F6-18 Commissions follow paid invoices](../../../02-functional/f06-customers-and-sales/business-rules/br-f06-18-commissions-follow-paid-invoices.md).
Retail adds only this: a store's target is split by day and staff member, and each sale counts for the staff member
signed in at the till.

## Why

See [D320](../../../06-decisions/sectors/d320-retail-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| Sale by L. B. | Counts for L. B. and Lyon 2 |

## Applies to

Every SC02 use case concerned.

## Exceptions

None.

## Configurable

Targets.

## Open questions

None.

---

⬅️ [BR-SC02-14 Clienteling with consent](br-sc02-14-clienteling-with-consent.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC02-16](br-sc02-16-book-discounts-never-exceed-5-of-the-publishers-price.md)
