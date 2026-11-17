🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F6-15 A pro-forma is not an invoice

# 📏 BR-F6-15 A pro-forma is not an invoice

**Status:** ✅ specified

## Statement

A pro-forma has its own number range, says "pro-forma, not an invoice", creates no accounting entry and no receivable;
only the real invoice does.

## Why

Mixing them breaks invoice numbering (BR-F6-07) and VAT.

## Examples

| Case | Result |
|---|---|
| Pro-forma PF-2026-031 | No entry |
| Order invoiced | Invoice from the invoice range |

## Applies to

- [UC-F6-22 Issue a pro-forma invoice and a statement of account](../use-cases/07-special-invoicing/uc-f06-22-issue-a-pro-forma-invoice-and-a-statement-of-account.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F6-14 Offline orders are checked again on sync](br-f06-14-offline-orders-are-checked-again-on-sync.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F6-16 An instalment plan replaces the due date](br-f06-16-an-instalment-plan-replaces-the-due-date.md)
