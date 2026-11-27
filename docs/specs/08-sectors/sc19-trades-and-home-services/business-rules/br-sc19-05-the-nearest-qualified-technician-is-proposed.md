🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-05 The nearest qualified technician is proposed

# 📏 BR-SC19-05 The nearest qualified technician is proposed

**Status:** ✅ specified

## Statement

The technician proposed for an intervention is the nearest one who holds the qualification the trade needs, and an
intervention is not dispatched to anyone else without a reason kept in the history. When nobody is qualified the request
stays open and the dispatcher is told.

## Why

A wrong technician wastes a visit and may break the law on qualified work
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). The France-pack rule is
[CR-FR-210 Qualifications the law ties to tasks](../../../10-country-packs/france/labour/cr-fr-210-qualifications-tied-to-tasks.md):
a task the law reserves to the holder of a qualification, such as electrical work, is given only to someone who holds
it, current.

## Examples

| Case | Result |
|---|---|
| One qualified technician nearby | proposed with the arrival time |
| Two equally near | the lighter day is proposed |
| Nobody qualified | stays Requested and warned |
| Override | reason kept in the history |
| Technician refuses | the next one is proposed |

## Applies to

- [UC-SC19-05](../use-cases/02-on-site-intervention/uc-sc19-05-dispatch-an-intervention.md)
- [E-SC19-04 Intervention](../data/e-sc19-04-intervention.md)
- [E-SC19-04 Intervention](../data/e-sc19-04-intervention.md)
- [E-F9-12](../../../02-functional/f09-hr-and-projects/data/e-f09-12-certification.md)

## Exceptions

None.

## Configurable

The weight of distance and load in the proposal, set by the dispatcher.

## Open questions

None.

---

⬅️ [BR-SC19-04](br-sc19-04-renewals-follow-the-notice-and-index-clauses.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC19-06 Reports carry time, place and photos](br-sc19-06-reports-carry-time-place-and-photos.md)
