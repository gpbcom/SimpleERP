🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-11 Finite schedule and the tablet](README.md) › 🖥️ S-F12-23 Finite schedule

# 🖥️ S-F12-23 Finite schedule

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Schedule operations within each work centre's capacity.

## Entry points

Manufacturing › Schedule.

## Wireframe

```text
+------------------------------------------------------------------+
| Schedule week 50          [Forward v]           [Publish]         |
|           Mon 08          Tue 09          Wed 10                  |
| Press P2  [MO-410][MO-411] [MO-412.....]  [maintenance]          |
| Press P3  [MO-409]         [   free    ]                         |
| Late: MO-412 by 2 days (P2 full)  [Move to P3]                   |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-11 step 1, U21 | desktop | ![FL-F12-11 step 1, U21, light](../../images/11-finite-schedule-and-the-tablet/u21-production-planner/1-finite-schedule-desktop-light.png) | ![FL-F12-11 step 1, U21, dark](../../images/11-finite-schedule-and-the-tablet/u21-production-planner/1-finite-schedule-desktop-dark.png) |
| FL-F12-11 step 1, U21 | phone | ![FL-F12-11 step 1, U21, light](../../images/11-finite-schedule-and-the-tablet/u21-production-planner/1-finite-schedule-phone-light.png) | ![FL-F12-11 step 1, U21, dark](../../images/11-finite-schedule-and-the-tablet/u21-production-planner/1-finite-schedule-phone-dark.png) |
| Error E1, U21 | desktop | ![Error E1, U21, light](../../images/11-finite-schedule-and-the-tablet/u21-production-planner/e1-finite-schedule-refused-desktop-light.png) | ![Error E1, U21, dark](../../images/11-finite-schedule-and-the-tablet/u21-production-planner/e1-finite-schedule-refused-desktop-dark.png) |
| Error E1, U21 | phone | ![Error E1, U21, light](../../images/11-finite-schedule-and-the-tablet/u21-production-planner/e1-finite-schedule-refused-phone-light.png) | ![Error E1, U21, dark](../../images/11-finite-schedule-and-the-tablet/u21-production-planner/e1-finite-schedule-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-23-finite-schedule-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-23-finite-schedule-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-23-finite-schedule-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-23-finite-schedule-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-23-finite-schedule-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-23-finite-schedule-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-23-finite-schedule-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-23-finite-schedule-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Work centres, slots, late orders | E-F12-18 | drag to move |

## Actions

| Action | Who | Result |
|---|---|---|
| Schedule | planner | Slots placed |
| Publish | planner | To the tablets |

## States

- Normal: schedule operations within each work centre's capacity.
- Empty: nothing released: "Release orders to schedule them".
- Loading: the Gantt greyed with "Scheduling" while slots compute.
- Error: the error message pattern (D122).
- Read-only: past days.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F12-18 Schedule slot](../../data/e-f12-18-schedule-slot.md),
[E-F12-05 Work order](../../data/e-f12-05-work-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-18 Schedule slot | Planned | Badge "Planned"; a new record starts here; next: Published (UC-F12-23); fields editable within the role | U21 | `u21-production-planner/s-f12-23-finite-schedule-e-f12-18-schedule-slot-planned-{desktop,phone}-{light,dark}.png` |
| E-F12-18 Schedule slot | Published | Badge "Published"; next: Done (UC-F12-23); fields editable within the role | U21 | `u21-production-planner/s-f12-23-finite-schedule-e-f12-18-schedule-slot-published-{desktop,phone}-{light,dark}.png` |
| E-F12-18 Schedule slot | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U21 | `u21-production-planner/s-f12-23-finite-schedule-e-f12-18-schedule-slot-done-{desktop,phone}-{light,dark}.png` |
| E-F12-05 Work order | New | Badge "New"; a new record starts here; next: Done or Late (UC-F12-04, UC-F12-20); fields editable within the role | U21 | `u21-production-planner/s-f12-23-finite-schedule-e-f12-05-work-order-new-{desktop,phone}-{light,dark}.png` |
| E-F12-05 Work order | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U21 | `u21-production-planner/s-f12-23-finite-schedule-e-f12-05-work-order-done-{desktop,phone}-{light,dark}.png` |
| E-F12-05 Work order | Late | Badge "Late"; next: Done (UC-F12-04); fields editable within the role | U21 | `u21-production-planner/s-f12-23-finite-schedule-e-f12-05-work-order-late-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F12-11 Finite schedule and the tablet](../../flows/fl-f12-11-finite-schedule-and-the-tablet.md)

## Open questions

None.

---

⬅️ [S-F12-22 Qualifications matrix](../10-people-and-tools/s-f12-22-qualifications-matrix.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-24 FMEA](../12-quality-engineering/s-f12-24-fmea.md)
