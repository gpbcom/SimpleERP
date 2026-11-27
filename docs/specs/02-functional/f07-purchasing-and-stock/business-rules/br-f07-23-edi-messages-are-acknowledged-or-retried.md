🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-23 EDI messages are acknowledged or retried

# 📏 BR-F7-23 EDI messages are acknowledged or retried

**Status:** ✅ specified

## Statement

Every outgoing EDI message must be acknowledged by the supplier within the agreed time; if it is not, it is sent again
up to the agreed number of times and then marked Failed with a notice to purchasing; an order is treated as confirmed
only after its acknowledgement.

## Why

A message nobody confirms may never have arrived, and an unconfirmed order cannot be planned on. The owner asked for
supplier EDI ([D526](../../../06-decisions/f07-purchasing-and-stock/d526-benchmark-gaps-f07-purchasing-and-stock.md)).

## Examples

| Case | Result |
|---|---|
| An order acknowledged in 5 minutes | Acknowledged, order confirmed |
| No answer after 1 hour, retry every hour | sent again up to 3 times |
| Three tries with no answer | Failed, purchasing notified |
| A message the supplier cannot read | Rejected with its reason |
| An incoming message already received | ignored as a duplicate by its reference |

## Applies to

- [UC-F7-29](../use-cases/10-consignment-scanning-and-edi/uc-f07-29-exchange-orders-and-invoices-by-edi-with-suppliers.md)
- [E-F7-26 EDI message](../data/e-f07-26-edi-message.md)
- [E-F7-03 Purchase order](../data/e-f07-03-purchase-order.md)
- [E-F7-05 Supplier invoice](../data/e-f07-05-supplier-invoice.md)

## Exceptions

None.

## Configurable

Yes: per supplier, the acknowledgement time, the number of tries and the formats.

## Open questions

None.

---

⬅️ [BR-F7-22](br-f07-22-deposits-are-refunded-for-returned-items-only.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F7-24 Re-slotting tasks never block open picks](br-f07-24-re-slotting-tasks-never-block-open-picks.md)
