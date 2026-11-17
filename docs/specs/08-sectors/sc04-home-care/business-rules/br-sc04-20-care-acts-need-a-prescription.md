🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏠 [SC04 Home care](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC04-20 Care acts need a prescription

# 📏 BR-SC04-20 Care acts need a prescription

**Status:** 🔄 waiting for the owner

## Statement

A care act is planned, recorded and billed only against a valid prescription: not ended and with acts left. An act with
no valid prescription is refused, and an act already done without one cannot be billed.

## Why

Care without a prescription cannot be paid by the health insurance, and it exposes the patient and the service. The
owner asked for nursing care services ([D548](../../../06-decisions/sectors/d548-benchmark-gaps-sc04-home-care.md)).
(Proposed) The France-pack rule is written later.

## Examples

| Case | Result |
|---|---|
| 28 acts prescribed, 12 done | 16 left, the next act is allowed |
| Prescription ended on 2026-11-28, act on 2026-11-29 | refused |
| No acts left | refused, renewal proposed |
| Act done without a prescription | not billable, incident opened |

## Applies to

- [UC-SC04-20](../use-cases/06-care-homes-cesu-and-nursing/uc-sc04-20-run-home-nursing-care.md)
- [E-SC04-18 Care act](../data/e-sc04-18-care-act.md)
- [E-SC04-04 Visit](../data/e-sc04-04-visit.md)
- France-pack rule, (Proposed) until its law is read:
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
