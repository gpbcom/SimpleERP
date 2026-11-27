🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-12 Quality engineering](README.md) › 🖥️ S-F12-24 FMEA

# 🖥️ S-F12-24 FMEA

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Analyse failure modes and follow their actions.

## Entry points

Quality › FMEA.

## Wireframe

```text
+------------------------------------------------------------------+
| FMEA  Bracket B-20                                                |
| Step     Mode   Effect    S  O  D  RPN  Action            Due     |
| Welding  crack  breakage  8  4  5  160  weld inspection   12-20   |
| Cutting  burr   injury    5  3  3  45   -                         |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-12 step 1, U27 | desktop | ![FL-F12-12 step 1, U27, light](../../images/12-quality-engineering/u27-quality-manager/1-fmea-desktop-light.png) | ![FL-F12-12 step 1, U27, dark](../../images/12-quality-engineering/u27-quality-manager/1-fmea-desktop-dark.png) |
| FL-F12-12 step 1, U27 | tablet | ![FL-F12-12 step 1, U27, light](../../images/12-quality-engineering/u27-quality-manager/1-fmea-tablet-light.png) | ![FL-F12-12 step 1, U27, dark](../../images/12-quality-engineering/u27-quality-manager/1-fmea-tablet-dark.png) |
| Error E1, U27 | desktop | ![Error E1, U27, light](../../images/12-quality-engineering/u27-quality-manager/e1-fmea-refused-desktop-light.png) | ![Error E1, U27, dark](../../images/12-quality-engineering/u27-quality-manager/e1-fmea-refused-desktop-dark.png) |
| Error E1, U27 | tablet | ![Error E1, U27, light](../../images/12-quality-engineering/u27-quality-manager/e1-fmea-refused-tablet-light.png) | ![Error E1, U27, dark](../../images/12-quality-engineering/u27-quality-manager/e1-fmea-refused-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-24-fmea-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-24-fmea-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-24-fmea-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-24-fmea-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-24-fmea-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-24-fmea-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-f12-24-fmea-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-f12-24-fmea-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Step, mode, ratings, action | E-F12-19 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Add a line | quality manager | Rated |
| Close action | owner | Re-rated |

## States

- Normal: analyse failure modes and follow their actions.
- Empty: no FMEA on this product: Start one.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for planners: read.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F12-19 FMEA line](../../data/e-f12-19-fmea-line.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-19 FMEA line | Open | Badge "Open"; a new record starts here; next: Done (UC-F12-24); fields editable within the role | U27 | `u27-quality-manager/s-f12-24-fmea-e-f12-19-fmea-line-open-{desktop,tablet}-{light,dark}.png` |
| E-F12-19 FMEA line | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U27 | `u27-quality-manager/s-f12-24-fmea-e-f12-19-fmea-line-done-{desktop,tablet}-{light,dark}.png` |

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

- [FL-F12-12 Quality engineering](../../flows/fl-f12-12-quality-engineering.md)

## Open questions

None.

---

⬅️ [S-F12-23 Finite schedule](../11-finite-schedule-and-the-tablet/s-f12-23-finite-schedule.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-25 Control chart](s-f12-25-control-chart.md)
