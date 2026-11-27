🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F6-17 A dispute pauses reminders on what is disputed

# 📏 BR-F6-17 A dispute pauses reminders on what is disputed

**Status:** ✅ specified

## Statement

A disputed amount is not reminded nor charged late penalties while the dispute is open; the rest of the invoice is
reminded as usual.

## Why

Reminding a customer for what they contest damages the relation (D463).

## Examples

| Case | Result |
|---|---|
| 86 EUR of 1,240 EUR disputed | 1,154 EUR reminded |
| Dispute rejected | 86 EUR reminded |

## Applies to

- [UC-F6-24 Handle a disputed invoice](../use-cases/08-collect-and-settle/uc-f06-24-handle-a-disputed-invoice.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F6-16 An instalment plan replaces the due date](br-f06-16-an-instalment-plan-replaces-the-due-date.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F6-18 Commissions follow paid invoices](br-f06-18-commissions-follow-paid-invoices.md)
