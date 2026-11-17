🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-30 Live position only as a team option, during working hours

# 📏 BR-F9-30 Live position only as a team option, during working hours

**Status:** 🔄 draft (GH-2 step S4b, from VD-22, VD-23 / D504, D505)

## Statement

A person's position is recorded at check-in and check-out only, by default (BR-F9-06); a live position during working
hours is an option switched on per team, for drivers and carers only, once its purpose is stated and its impact
assessment done; it is off outside working hours, paused by the employee during breaks, and never used to measure
speed or performance.

## Why

- The owner's decisions VD-22 and VD-23
  [D504](../../../06-decisions/f09-hr-and-projects/d504-positions-at-check-in-by-default-live-as-a-team-option-for-drivers-and-carers.md),
  [D505](../../../06-decisions/f09-hr-and-projects/d505-the-employee-sees-their-own-position-live.md): check-in and
  check-out by default; live position as a per-team option for drivers (SC07) and carers (SC04), with its purpose and
  impact assessment; a pause during breaks.
- Live positions help plan the next visit and tell the customer the arrival time; they are not a means of control.
- The drivers' rule already limits sharing to the trips:
  [BR-SC07-08](../../../08-sectors/sc07-transport/business-rules/br-sc07-08-location-only-while-working.md).
- Legal values from the France country pack:
  - [CR-FR-054](../../../10-country-packs/france/data-protection/cr-fr-054-location-with-consent.md);
  - [CR-FR-206](../../../10-country-packs/france/labour/cr-fr-206-cse-consulted-on-monitoring.md);
  - [CR-FR-211](../../../10-country-packs/france/data-protection/cr-fr-211-live-geolocation-of-employees.md).

## Examples

| Case | Result |
|---|---|
| A carers' team, option off | Positions at check-in and check-out only |
| A drivers' team, option on, 10:30 on a working day | The live position is shown to the driver's dispatcher (BR-F9-32) |
| The same driver at 19:00, after their working hours | Nothing recorded |
| A carer pauses during lunch | Nothing recorded until they resume; their phone shows "Paused" |
| The option asked for the sales representatives' team | Not offered: drivers and carers only |
| A manager asks for the drivers' average speed | Not available |
| The option without a purpose or an impact assessment | Cannot be switched on |

## Applies to

- [UC-F9-37](../use-cases/12-schedule-customer-requests/uc-f09-37-share-my-position-during-work.md)
- [E-F9-32 Live position](../data/e-f09-32-live-position.md)
- [E-F9-10 Attendance](../data/e-f09-10-attendance.md)
- [REQ-T13-05](../../../03-technical/t13-maps-and-geodata/requirements/req-t13-05-live-positions.md)

## Exceptions

None.

## Configurable

Per team, off by default, for drivers' and carers' teams only; switching it on needs the purpose and the impact
assessment. (Proposed) The staff committee is consulted and the employees told before it is switched on (CR-FR-206).

## Open questions

None.

---

⬅️ [BR-F9-29 Planners see eligibility, never sensitive details](br-f09-29-planners-see-eligibility-only.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F9-31 Live positions kept two months at most](br-f09-31-live-positions-kept-two-months.md)
