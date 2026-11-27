🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-32 Who sees a person's position

# 📏 BR-F9-32 Who sees a person's position

**Status:** ✅ specified

## Statement

A person's position, at check-in and check-out or live, is seen only by their planner or dispatcher and their manager,
for planning only; by the customer, as an arrival time near their address during the visit's window, with nothing kept;
and by the person, who sees everything shared about them; nobody else sees it, whatever their role.

## Why

- The owner's decision VD-21 ([D503](../../../06-decisions/f09-hr-and-projects/d503-who-sees-peoples-positions.md)),
  word for word: "The customer (arrival time), Their manager, Their planner or dispatcher".
- The owner's decision VD-23
  [D505](../../../06-decisions/f09-hr-and-projects/d505-the-employee-sees-their-own-position-live.md): the employee
  sees a live indicator on their phone when their position is shared, what is recorded and who sees it, and their
  history in their profile.
- Legal values from the France country pack:
  [CR-FR-054](../../../10-country-packs/france/data-protection/cr-fr-054-location-with-consent.md).

## Examples

| Case | Result |
|---|---|
| The dispatcher of the driver's team | The live position on the planning map |
| A dispatcher of another site | Nothing |
| The driver's manager | The positions, for planning only |
| An HR officer who is not the person's manager | Nothing |
| The customer, window 14:00 to 16:00, at 14:20 | "Arriving in about 15 minutes", near their address |
| The same customer at 16:30, the visit done | Nothing |
| The employee | The indicator, what is shared and with whom, the pause, their history |

## Applies to

- [UC-F9-36](../use-cases/12-schedule-customer-requests/uc-f09-36-see-work-and-places-on-a-map.md)
- [UC-F9-37](../use-cases/12-schedule-customer-requests/uc-f09-37-share-my-position-during-work.md)
- [UC-F16-17](../../f16-customer-support-agents/use-cases/06-take-in-every-request/uc-f16-17-follow-the-arrival-of-a-visit.md)
- [E-F9-32 Live position](../data/e-f09-32-live-position.md)
- [E-F9-10 Attendance](../data/e-f09-10-attendance.md)
- [REQ-T13-06](../../../03-technical/t13-maps-and-geodata/requirements/req-t13-06-map-queries-respect-permissions.md)

## Exceptions

None.

## Configurable

No. "Their planner" is a holder of a planner role whose record rules cover the person's team.

## Open questions

None.

---

⬅️ [BR-F9-31 Live positions kept two months at most](br-f09-31-live-positions-kept-two-months.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-33 Automatic mode enabled by hand, stops on a problem](br-f09-33-automatic-mode-stops-on-a-problem.md)
