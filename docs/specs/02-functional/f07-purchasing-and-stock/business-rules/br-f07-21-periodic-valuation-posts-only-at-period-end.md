🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-21 Periodic valuation posts only at period end

# 📏 BR-F7-21 Periodic valuation posts only at period end

**Status:** 🔄 waiting for the owner

## Statement

A periodic valuation posts its stock variation entry only on the last day of its period and only for an approved count;
it never posts during the period, and it is posted again only by reversing the first entry while the period is open.

## Why

The periodic method values stock at the end of the period only; posting earlier would mix it with movements still to
come. The owner asked for periodic valuation
([D526](../../../06-decisions/f07-purchasing-and-stock/d526-benchmark-gaps-f07-purchasing-and-stock.md)); posted entries
never change ([BR-F8-01](../../f08-accounting/business-rules/br-f08-01-posted-entries-never-change.md)).

## Examples

| Case | Result |
|---|---|
| Approved count, period ends today | one entry posted today |
| Approved count, 5 days before the end | waits for the end |
| A count not yet approved at the end | nothing is posted and the checklist keeps the step open |
| A late invoice after posting | the entry is reversed and posted again |
| A locked period | refused, carried to the next open period |

## Applies to

- [UC-F7-27](../use-cases/10-consignment-scanning-and-edi/uc-f07-27-value-stock-periodically.md)
- [E-F7-24 Periodic count](../data/e-f07-24-periodic-count.md)
- [E-F8-03 Journal entry](../../f08-accounting/data/e-f08-03-journal-entry.md)
- [E-F8-10 Fiscal period](../../f08-accounting/data/e-f08-10-fiscal-period.md)

## Exceptions

None.

## Configurable

Yes: per item category, perpetual or periodic valuation
([BR-F7-07 Costing method per category](br-f07-07-costing-method-per-category.md)).

## Open questions

None.

---

⬅️ [BR-F7-20](br-f07-20-a-scan-that-does-not-match-the-expected-item-stops-the-step.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F7-22](br-f07-22-deposits-are-refunded-for-returned-items-only.md)
