🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F6-18 Commissions follow paid invoices

# 📏 BR-F6-18 Commissions follow paid invoices

**Status:** ✅ specified

## Statement

A commission is earned on the paid amount of invoices credited to a rep by the plan, at the plan's rate and tier; a
later credit note reverses it on the next statement (paid, not invoiced).

## Why

Paying on unpaid invoices rewards bad debts.

## Examples

| Case | Result |
|---|---|
| Invoice paid 10,000 EUR at 3 % | 300 EUR |
| Credit 2,000 EUR after payment | -60 EUR next statement |

## Applies to

- [UC-F6-25 Set sales targets and pay commissions](../use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-25-set-sales-targets-and-pay-commissions.md)
- [UC-F6-26 Read sales and margin reports](../use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-26-read-sales-and-margin-reports.md)

## Exceptions

None.

## Configurable

Rate, tiers, base (paid or invoiced), splits.

## Open questions

None.

---

⬅️ [BR-F6-17](br-f06-17-a-dispute-pauses-reminders-on-what-is-disputed.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-19 Forwarded leads leave their owner's pipeline](br-f06-19-forwarded-leads-leave-their-owners-pipeline.md)
