🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F6-03 The portal shows only the customer's own

# 📏 BR-F6-03 The portal shows only the customer's own

**Status:** ✅ specified

## Statement

A customer sees only their own company's documents, orders and requests: through a secure link per document, or with an
account covering their company's whole history (D17); a link expires (Proposed: after 90 days) and can be revoked.

## Why

Customers must never see another customer's data. See
[D252](../../../06-decisions/f06-customers-and-sales/d252-customer-portal.md).

## Examples

| Case | Result |
|---|---|
| A link to an invoice forwarded to someone else | It opens that invoice only; a second factor for payment details changes |
| An account at Durand SA | All of Durand SA's quotes, invoices and requests |

## Applies to

Every F6 use case concerned.

- [UC-F6-17 Organise accounts with their timeline and emails](../use-cases/06-accounts-and-credit/uc-f06-17-organise-accounts-with-their-timeline-and-emails.md)

## Exceptions

None.

## Configurable

The link lifetime.

## Open questions

None.

---

⬅️ [BR-F6-02 No card number in simple-ERP](br-f06-02-no-card-number-in-simple-erp.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-04 Large discounts need approval](br-f06-04-large-discounts-need-approval.md)
