🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-22 Deposits are refunded for returned items only

# 📏 BR-F7-22 Deposits are refunded for returned items only

**Status:** 🔄 waiting for the owner

## Statement

A deposit is refunded only for packaging counted as returned, in the quantity returned and at the deposit agreed for its
state; packaging not returned keeps its deposit, and a refund above the returns is refused.

## Why

Refunding a deposit for packaging that did not come back loses both the packaging and the money. The owner asked for
returnable packaging and deposits
([D526](../../../06-decisions/f07-purchasing-and-stock/d526-benchmark-gaps-f07-purchasing-and-stock.md)).

## Examples

| Case | Result |
|---|---|
| 30 of 40 crates returned in good state | 30 deposits refunded, 10 still held |
| Crates returned damaged | refund reduced as the deposit terms say |
| A refund for 35 crates after 30 returned | refused |
| Packaging lost and agreed by the customer | the deposit is kept and the packaging written off |
| A supplier's deposit invoice with no packaging out | held for purchasing |

## Applies to

- [UC-F7-28](../use-cases/10-consignment-scanning-and-edi/uc-f07-28-track-returnable-packaging-and-deposits.md)
- [E-F7-25 Packaging deposit](../data/e-f07-25-packaging-deposit.md)
- [E-F6-05 Invoice](../../f06-customers-and-sales/data/e-f06-05-invoice.md)
- [E-F7-22 Delivery note](../data/e-f07-22-delivery-note.md)

## Exceptions

None.

## Configurable

Yes: per packaging type, the unit deposit, the refund for damaged packaging and the time before a reminder.

## Open questions

None.

---

⬅️ [BR-F7-21 Periodic valuation posts only at period end](br-f07-21-periodic-valuation-posts-only-at-period-end.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F7-23 EDI messages are acknowledged or retried](br-f07-23-edi-messages-are-acknowledged-or-retried.md)
