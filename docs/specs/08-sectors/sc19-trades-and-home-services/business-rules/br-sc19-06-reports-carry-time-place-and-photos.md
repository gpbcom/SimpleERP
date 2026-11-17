🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-06 Reports carry time, place and photos

# 📏 BR-SC19-06 Reports carry time, place and photos

**Status:** 🔄 waiting for the owner

## Statement

A site report carries the arrival and departure times, the place checked against the address and at least one photo, and
it cannot be closed without them. A place farther than the tolerance from the address needs a reason from the
technician.

## Why

The report is the proof of the work for the invoice and for a dispute
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). (Proposed) The France-pack
rule is written later.

## Examples

| Case | Result |
|---|---|
| Place 40 metres from the address | accepted |
| Place 3 kilometres away | a reason is required |
| No photo | the report stays open |
| No position from the phone | place entered by hand and flagged |
| Work continues another day | report kept open |

## Applies to

- [UC-SC19-06](../use-cases/02-on-site-intervention/uc-sc19-06-report-on-site-with-photos.md)
- [E-SC19-05 Site report](../data/e-sc19-05-site-report.md)
- [E-SC19-05 Site report](../data/e-sc19-05-site-report.md)
- [E-SC19-04 Intervention](../data/e-sc19-04-intervention.md)

## Exceptions

None.

## Configurable

The place tolerance in metres, set by the owner.

## Open questions

None.

---

⬅️ [BR-SC19-05](br-sc19-05-the-nearest-qualified-technician-is-proposed.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC19-07 Parts used lower the van's stock](br-sc19-07-parts-used-lower-the-vans-stock.md)
