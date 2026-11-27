🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-07 Parts used lower the van's stock

# 📏 BR-SC19-07 Parts used lower the van's stock

**Status:** ✅ specified

## Statement

A part used on an intervention leaves the stock of the van of the technician at once and is added to the invoice lines.
A part that is not in the van is refused unless the technician records it as bought elsewhere, and a van stock is never
negative.

## Why

Parts used and not recorded are a loss, and a van stock that does not fall makes the next reload wrong
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)).

## Examples

| Case | Result |
|---|---|
| Part in the van | stock down by one, on the invoice |
| Part not in the van | refused, or recorded as bought elsewhere |
| Unused part returned | back into the van's stock |
| Part below the minimum | a refill is suggested |
| Unknown barcode | searched by name |

## Applies to

- [UC-SC19-07](../use-cases/02-on-site-intervention/uc-sc19-07-record-parts-used.md)
- [E-SC19-13 Van stock](../data/e-sc19-13-van-stock.md)
- [E-F7-06 Item](../../../02-functional/f07-purchasing-and-stock/data/e-f07-06-item.md)

## Exceptions

None.

## Configurable

Whether the technician sees prices, set by the owner.

## Open questions

None.

---

⬅️ [BR-SC19-06 Reports carry time, place and photos](br-sc19-06-reports-carry-time-place-and-photos.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC19-08 The invoice follows the signed report](br-sc19-08-the-invoice-follows-the-signed-report.md)
