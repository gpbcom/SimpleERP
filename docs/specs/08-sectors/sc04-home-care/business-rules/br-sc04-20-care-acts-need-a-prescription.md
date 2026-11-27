🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏠 [SC04 Home care](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC04-20 Care acts need a prescription

# 📏 BR-SC04-20 Care acts need a prescription

**Status:** ✅ specified

## Statement

A care act is planned, recorded and counted in the service's activity only against a valid prescription: not ended and
with acts left of the care the coordinating nurse assessed on it. An act with no valid prescription is refused, and an
act already done without one is not counted as care of the service.

## Why

A home autonomy service gives nursing care on a medical prescription, which its coordinating nurse assesses; care
without one exposes the patient and the service. The care is funded by a yearly global allowance from the ARS, not
billed per act to the health insurance, and the law does not ask the prescription to state the acts and the period: the
count of acts is a product rule, kept as such by the owner
([D575](../../../06-decisions/foundations/d575-answers-of-2026-11-27-on-the-last-open-points.md)). The owner asked for nursing care services
([D548](../../../06-decisions/sectors/d548-benchmark-gaps-sc04-home-care.md)). The France-pack rule is
[CR-FR-233 Home nursing services (SSIAD)](../../../10-country-packs/france/health-practice/cr-fr-233-home-nursing-ssiad.md).

## Examples

| Case | Result |
|---|---|
| 28 acts prescribed, 12 done | 16 left, the next act is allowed |
| Prescription ended on 2026-11-28, act on 2026-11-29 | refused |
| No acts left | refused, renewal proposed |
| Act done without a prescription | not counted in the activity, incident opened |

## Applies to

- [UC-SC04-20](../use-cases/06-care-homes-cesu-and-nursing/uc-sc04-20-run-home-nursing-care.md)
- [E-SC04-18 Care act](../data/e-sc04-18-care-act.md)
- [E-SC04-04 Visit](../data/e-sc04-04-visit.md)
- France-pack rule:
  [CR-FR-233 Home nursing services (SSIAD)](../../../10-country-packs/france/health-practice/cr-fr-233-home-nursing-ssiad.md)

## Exceptions

An urgent act may be done and recorded with the prescription to follow within a set delay, as the service's procedure
says.

## Configurable

The days before the end of a prescription at which a renewal is proposed (14 by default), by the coordinator.

## Open questions

None.

---

⬅️ [BR-SC04-19 Family allowance aid follows the CAF rules](br-sc04-19-family-allowance-aid-follows-the-caf-rules.md) ·
⬆️ [Up](README.md)
