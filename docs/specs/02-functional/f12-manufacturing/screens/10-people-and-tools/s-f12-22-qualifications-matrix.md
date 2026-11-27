🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-10 People and tools](README.md) › 🖥️ S-F12-22 Qualifications matrix

# 🖥️ S-F12-22 Qualifications matrix

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U06 Human resources](../../../../01-users/personas/u06-hr.md)

## Purpose

Show who is qualified for each work centre and set requirements.

## Entry points

Manufacturing › Qualifications.

## Wireframe

```text
+------------------------------------------------------------------+
| Qualifications     Press P2      Press P3      Packing          |
| requires           press safety  press safety  -                |
| Paul Morel         ok            ok            ok               |
| Hugo Blanc         expired       expired       ok  [Train]      |
| Lea Roux           expiring 30d  -             ok               |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-10 step 2, U21 | desktop | ![FL-F12-10 step 2, U21, light](../../images/10-people-and-tools/u21-production-planner/2-qualifications-matrix-desktop-light.png) | ![FL-F12-10 step 2, U21, dark](../../images/10-people-and-tools/u21-production-planner/2-qualifications-matrix-desktop-dark.png) |
| FL-F12-10 step 2, U21 | phone | ![FL-F12-10 step 2, U21, light](../../images/10-people-and-tools/u21-production-planner/2-qualifications-matrix-phone-light.png) | ![FL-F12-10 step 2, U21, dark](../../images/10-people-and-tools/u21-production-planner/2-qualifications-matrix-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-22-qualifications-matrix-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-22-qualifications-matrix-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-22-qualifications-matrix-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-22-qualifications-matrix-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-22-qualifications-matrix-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-22-qualifications-matrix-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-22-qualifications-matrix-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-22-qualifications-matrix-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Work centres, operators, status | E-F12-17, E-F9-12 | requirements |

## Actions

| Action | Who | Result |
|---|---|---|
| Set requirements | planner | Saved |
| Train | planner | Training plan (UC-F9-25) |

## States

- Normal: show who is qualified for each work centre and set requirements.
- Empty: no requirement set: "Any operator may work everywhere".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for HR: read.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F12-10 People and tools](../../flows/fl-f12-10-people-and-tools.md)

## Open questions

None.

---

⬅️ [S-F12-21 Calibration](s-f12-21-calibration.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-23 Finite schedule](../11-finite-schedule-and-the-tablet/s-f12-23-finite-schedule.md)
