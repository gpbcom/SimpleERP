🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-12 Quality engineering](README.md) › 🖥️ S-F12-25 Control chart

# 🖥️ S-F12-25 Control chart

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)
- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Plot measures against control limits and show signals.

## Entry points

Quality › Control charts; the tablet's check screen.

## Wireframe

```text
+------------------------------------------------------------------+
| Diameter op 30   limits 11.94 - 12.06                              |
| 12.08 |                                  x  <- signal             |
| 12.00 |  x x  x x x  x x x  x  x x  x                             |
| 11.94 |                                                            |
| Signal 12-08 10:42: above upper limit  cause [worn tool] [Save]   |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-12 step 3, U27 | desktop | ![FL-F12-12 step 3, U27, light](../../images/12-quality-engineering/u27-quality-manager/3-control-chart-desktop-light.png) | ![FL-F12-12 step 3, U27, dark](../../images/12-quality-engineering/u27-quality-manager/3-control-chart-desktop-dark.png) |
| FL-F12-12 step 3, U27 | tablet | ![FL-F12-12 step 3, U27, light](../../images/12-quality-engineering/u27-quality-manager/3-control-chart-tablet-light.png) | ![FL-F12-12 step 3, U27, dark](../../images/12-quality-engineering/u27-quality-manager/3-control-chart-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-25-control-chart-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-25-control-chart-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-25-control-chart-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-25-control-chart-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-25-control-chart-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-25-control-chart-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-f12-25-control-chart-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-f12-25-control-chart-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Measures, limits, signals | E-F12-20 | cause |

## Actions

| Action | Who | Result |
|---|---|---|
| Record cause | quality manager, operator | Signal closed |
| Recompute limits | quality manager | New limits |

## States

- Normal: plot measures against control limits and show signals.
- Empty: fewer measures than needed: "Limits after 25 measures".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: past charts.
- Offline: On the tablet, measures are recorded offline and plotted when synced,
  [UC-F12-26](../../use-cases/11-finite-schedule-and-the-tablet/uc-f12-26-keep-working-on-the-tablet-without-the-network.md).

Shown entities (VD-15): [E-F12-07 Quality control point](../../data/e-f12-07-quality-control-point.md),
[E-F12-20 Control chart](../../data/e-f12-20-control-chart.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-07 Quality control point | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U27 | `u27-quality-manager/s-f12-25-control-chart-e-f12-07-quality-control-point-active-{desktop,tablet}-{light,dark}.png` |
| E-F12-20 Control chart | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U27 | `u27-quality-manager/s-f12-25-control-chart-e-f12-20-control-chart-active-{desktop,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F12-12 Quality engineering](../../flows/fl-f12-12-quality-engineering.md)

## Open questions

None.

---

⬅️ [S-F12-24 FMEA](s-f12-24-fmea.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-26 Work in progress](../05-subcontracting-and-costs/s-f12-26-work-in-progress.md)
