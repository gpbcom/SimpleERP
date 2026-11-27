🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📦 [Decisions: F7 Purchasing and stock](README.md) ›
📜 D526 Benchmark gaps of F7 Purchasing and stock

# 📜 D526 Benchmark gaps of F7 Purchasing and stock

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found six features
that F7 had no use case for: consignment stock, a warehouse barcode app, periodic valuation, returnable packaging,
supplier EDI and slotting.

## Options

- G10 Consignment stock: stock owned by a supplier or a customer, or all stock counted as own.
- G11 Warehouse barcode app: a scanning app with checks, or typing on the phone.
- G51 Periodic valuation: periodic valuation, or perpetual valuation only.
- G52 Returnable packaging: returnable packaging with deposits, or none.
- G53 Supplier EDI: supplier EDI, or email and portal only.
- G54 Slotting: slotting proposals, or fixed locations.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F7 gets six use cases in one new flow, each with its screen and its rule, and five entities with their lists; the
barcode app has no entity of its own. All at full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G10 | Consignment stock | UC-F7-25: consignment stock never valued as own stock | "Consignment stock" |
| G11 | Warehouse barcode app | UC-F7-26: a barcode app that stops a step on a scan that does not match | "Warehouse barcode app" |
| G51 | Periodic valuation | UC-F7-27: periodic valuation that posts only at period end | "Periodic valuation" |
| G52 | Returnable packaging | UC-F7-28: returnable packaging with deposits refunded for returned items only | "Returnable packaging" |
| G53 | Supplier EDI | UC-F7-29: supplier EDI whose messages are acknowledged or retried | "Supplier EDI" |
| G54 | Slotting | UC-F7-30: slotting whose re-slotting tasks never block open picks | "Slotting" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "F7 Purchasing and stock").

## Consequences

- G10 Consignment stock:
  [UC-F7-25](../../02-functional/f07-purchasing-and-stock/use-cases/10-consignment-scanning-and-edi/uc-f07-25-keep-consignment-stock.md),
  [S-F7-25](../../02-functional/f07-purchasing-and-stock/screens/10-consignment-scanning-and-edi/s-f07-25-consignment-stock.md)
  and
  [BR-F7-19](../../02-functional/f07-purchasing-and-stock/business-rules/br-f07-19-consigned-stock-is-never-valued-as-own-stock.md),
  with [E-F7-23](../../02-functional/f07-purchasing-and-stock/data/e-f07-23-stock-owner.md) Stock owner and its list
  [S-F7-L23](../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l23-stock-owners.md).
- G11 Warehouse barcode app:
  [UC-F7-26](../../02-functional/f07-purchasing-and-stock/use-cases/10-consignment-scanning-and-edi/uc-f07-26-scan-in-the-warehouse-app.md),
  [S-F7-26](../../02-functional/f07-purchasing-and-stock/screens/10-consignment-scanning-and-edi/s-f07-26-barcode-app.md)
  and
  [BR-F7-20](../../02-functional/f07-purchasing-and-stock/business-rules/br-f07-20-a-scan-that-does-not-match-the-expected-item-stops-the-step.md).
- G51 Periodic valuation:
  [UC-F7-27](../../02-functional/f07-purchasing-and-stock/use-cases/10-consignment-scanning-and-edi/uc-f07-27-value-stock-periodically.md),
  [S-F7-27](../../02-functional/f07-purchasing-and-stock/screens/10-consignment-scanning-and-edi/s-f07-27-periodic-valuation.md)
  and
  [BR-F7-21](../../02-functional/f07-purchasing-and-stock/business-rules/br-f07-21-periodic-valuation-posts-only-at-period-end.md),
  with [E-F7-24](../../02-functional/f07-purchasing-and-stock/data/e-f07-24-periodic-count.md) Periodic count and its
  list [S-F7-L24](../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l24-periodic-counts.md).
- G52 Returnable packaging:
  [UC-F7-28](../../02-functional/f07-purchasing-and-stock/use-cases/10-consignment-scanning-and-edi/uc-f07-28-track-returnable-packaging-and-deposits.md),
  [S-F7-28](../../02-functional/f07-purchasing-and-stock/screens/10-consignment-scanning-and-edi/s-f07-28-returnable-packaging.md)
  and
  [BR-F7-22](../../02-functional/f07-purchasing-and-stock/business-rules/br-f07-22-deposits-are-refunded-for-returned-items-only.md),
  with [E-F7-25](../../02-functional/f07-purchasing-and-stock/data/e-f07-25-packaging-deposit.md) Packaging deposit and
  its list [S-F7-L25](../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l25-packaging-deposits.md).
- G53 Supplier EDI:
  [UC-F7-29](../../02-functional/f07-purchasing-and-stock/use-cases/10-consignment-scanning-and-edi/uc-f07-29-exchange-orders-and-invoices-by-edi-with-suppliers.md),
  [S-F7-29](../../02-functional/f07-purchasing-and-stock/screens/10-consignment-scanning-and-edi/s-f07-29-supplier-edi.md)
  and
  [BR-F7-23](../../02-functional/f07-purchasing-and-stock/business-rules/br-f07-23-edi-messages-are-acknowledged-or-retried.md),
  with [E-F7-26](../../02-functional/f07-purchasing-and-stock/data/e-f07-26-edi-message.md) EDI message and its list
  [S-F7-L26](../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l26-edi-messages.md).
- G54 Slotting:
  [UC-F7-30](../../02-functional/f07-purchasing-and-stock/use-cases/10-consignment-scanning-and-edi/uc-f07-30-optimise-storage-locations.md),
  [S-F7-30](../../02-functional/f07-purchasing-and-stock/screens/10-consignment-scanning-and-edi/s-f07-30-slotting.md)
  and
  [BR-F7-24](../../02-functional/f07-purchasing-and-stock/business-rules/br-f07-24-re-slotting-tasks-never-block-open-picks.md),
  with [E-F7-27](../../02-functional/f07-purchasing-and-stock/data/e-f07-27-slotting-proposal.md) Slotting proposal and
  its list [S-F7-L27](../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l27-slotting-proposals.md).
- Drawn in [FL-F7-10](../../02-functional/f07-purchasing-and-stock/flows/fl-f07-10-consignment-scanning-and-edi.md)
  Consignment, scanning, packaging and EDI.

## Related

- [FL-F7-10](../../02-functional/f07-purchasing-and-stock/flows/fl-f07-10-consignment-scanning-and-edi.md)
- [BR-F7-07](../../02-functional/f07-purchasing-and-stock/business-rules/br-f07-07-costing-method-per-category.md)
- [BR-F7-05](../../02-functional/f07-purchasing-and-stock/business-rules/br-f07-05-every-move-is-traced.md)

---

⬅️ [D525](../f06-customers-and-sales/d525-benchmark-gaps-f06-customers-and-sales.md) · ⬆️ [Up](README.md) ·
➡️ [D527 Benchmark gaps of F8 Accounting](../f08-accounting/d527-benchmark-gaps-f08-accounting.md)
