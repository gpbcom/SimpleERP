🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F6-05 Reminders run on their own

# 📏 BR-F6-05 Reminders run on their own

**Status:** ✅ specified

## Statement

Each overdue invoice follows its customer's reminder sequence automatically, formal notice included, with the legal
late-payment penalties and the 40 EUR fixed recovery fee for business customers; a payment, a recorded promise to pay or
a dispute stops it; consumers get reminders without the business-only fee.

## Why

See [D256](../../../06-decisions/f06-customers-and-sales/d256-automatic-reminders.md).

Legal values from the France country pack:
[CR-FR-019 Late-payment penalties](../../../10-country-packs/france/invoicing/cr-fr-019-late-payment-penalties.md).

## Examples

| Case | Result |
|---|---|
| Invoice 7 days late | Second reminder sent |
| 30 days late | Formal notice sent automatically |
| Dispute recorded on day 10 | Sequence stopped |

## Applies to

Every F6 use case concerned.

- [UC-F6-23 Agree an instalment plan](../use-cases/08-collect-and-settle/uc-f06-23-agree-an-instalment-plan.md)

- [UC-F6-24 Handle a disputed invoice](../use-cases/08-collect-and-settle/uc-f06-24-handle-a-disputed-invoice.md)

## Exceptions

None.

## Configurable

Yes: sequences per customer profile.

## Open questions

None.

---

⬅️ [BR-F6-04 Large discounts need approval](br-f06-04-large-discounts-need-approval.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-06 Progress invoices and retention](br-f06-06-progress-invoices-and-retention.md)
