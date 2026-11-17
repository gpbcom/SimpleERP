🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-09 Shifts respect people and rules

# 📏 BR-F9-09 Shifts respect people and rules

**Status:** ✅ specified

## Statement

A shift cannot overlap another for the same person, nor fall on their time off or outside their contract; auto-planning
follows roles, availability and rest rules; the legal assistant warns on rest breaches (F15).

## Why

See [D289](../../../06-decisions/f09-hr-and-projects/d289-hr-coverage.md).

Legal values from the France country pack:
[CR-FR-042 Working time and rest](../../../10-country-packs/france/labour/cr-fr-042-working-time-and-rest.md).

## Examples

| Case | Result |
|---|---|
| Overlapping shift | Refused |
| 9 h between two shifts | Warning (BR-F15-07) |

## Applies to

Every F9 use case concerned.

- [UC-F9-30 Plan rounds and optimise routes](../use-cases/11-capacity-rounds-and-partners/uc-f09-30-plan-rounds-and-optimise-routes.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F9-08 Overtime needs approval](br-f09-08-overtime-needs-approval.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-10 Validated timesheets are locked](br-f09-10-validated-timesheets-are-locked.md)
