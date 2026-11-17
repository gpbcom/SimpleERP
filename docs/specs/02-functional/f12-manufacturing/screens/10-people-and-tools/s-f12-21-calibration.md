🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-10 People and tools](README.md) › 🖥️ S-F12-21 Calibration

# 🖥️ S-F12-21 Calibration

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Follow measuring instruments' calibrations and block those out of tolerance.

## Entry points

Quality › Calibration.

## Wireframe

```text
+------------------------------------------------------------------+
| Calibration                                                       |
| Instrument   Interval  Last        Result     Next        Status  |
| Caliper C-12 6 months  2026-11-15  out of tol. -          blocked |
| Gauge G-04   12 months 2026-03-02  within     2027-03-02  ok      |
| Checks to review since 05-15: 84                 [Review]         |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-10 step 1, U27 | desktop | ![FL-F12-10 step 1, U27, light](../../images/10-people-and-tools/u27-quality-manager/1-calibration-desktop-light.png) | ![FL-F12-10 step 1, U27, dark](../../images/10-people-and-tools/u27-quality-manager/1-calibration-desktop-dark.png) |
| FL-F12-10 step 1, U27 | tablet | ![FL-F12-10 step 1, U27, light](../../images/10-people-and-tools/u27-quality-manager/1-calibration-tablet-light.png) | ![FL-F12-10 step 1, U27, dark](../../images/10-people-and-tools/u27-quality-manager/1-calibration-tablet-dark.png) |
| Error E1, U27 | desktop | ![Error E1, U27, light](../../images/10-people-and-tools/u27-quality-manager/e1-calibration-refused-desktop-light.png) | ![Error E1, U27, dark](../../images/10-people-and-tools/u27-quality-manager/e1-calibration-refused-desktop-dark.png) |
| Error E1, U27 | tablet | ![Error E1, U27, light](../../images/10-people-and-tools/u27-quality-manager/e1-calibration-refused-tablet-light.png) | ![Error E1, U27, dark](../../images/10-people-and-tools/u27-quality-manager/e1-calibration-refused-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-21-calibration-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-21-calibration-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-21-calibration-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-21-calibration-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-21-calibration-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-21-calibration-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-f12-21-calibration-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-f12-21-calibration-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Instrument, interval, result, next | E-F12-16 | results |

## Actions

| Action | Who | Result |
|---|---|---|
| Record result | quality manager | Next date or block |
| Review | quality manager | Checks listed |

## States

- Normal: follow measuring instruments' calibrations and block those out of tolerance.
- Empty: no instrument yet: Add an instrument.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for operators: read.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F12-09 Equipment](../../data/e-f12-09-equipment.md),
[E-F12-16 Calibration](../../data/e-f12-16-calibration.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-09 Equipment | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U27 | `u27-quality-manager/s-f12-21-calibration-e-f12-09-equipment-active-{desktop,tablet}-{light,dark}.png` |
| E-F12-16 Calibration | Blocked | Badge "Blocked"; a new record starts here; no other state; fields editable within the role | U27 | `u27-quality-manager/s-f12-21-calibration-e-f12-16-calibration-blocked-{desktop,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F12-10 People and tools](../../flows/fl-f12-10-people-and-tools.md)

## Open questions

None.

---

⬅️ [S-F12-20 Production assistant](../08-report-and-assist/s-f12-20-production-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-22 Qualifications matrix](s-f12-22-qualifications-matrix.md)
