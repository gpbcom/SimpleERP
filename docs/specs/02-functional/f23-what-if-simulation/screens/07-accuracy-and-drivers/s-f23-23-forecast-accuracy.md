🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-07 Accuracy and drivers](README.md) › 🖥️ S-F23-23 Forecast accuracy

# 🖥️ S-F23-23 Forecast accuracy

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Show forecast errors per driver and recalibration proposals.

## Entry points

Simulation, Accuracy; the monthly notice.

## Wireframe

```text
Forecast accuracy        October 2026
-------------------------------------------------------------------------------
Driver          Forecast   Actual   Error   Proposal
Sales volume    100        109      9 %     seasonality     [Accept] [Refuse]
Purchases       52 000     51 200   1.5 %   -
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-07 step 1, U05 | desktop | ![FL-F23-07 step 1, U05, light](../../images/07-accuracy-and-drivers/u05-accounting/1-forecast-accuracy-desktop-light.png) | ![FL-F23-07 step 1, U05, dark](../../images/07-accuracy-and-drivers/u05-accounting/1-forecast-accuracy-desktop-dark.png) |
| Error E1, U05 | desktop | ![Error E1, U05, light](../../images/07-accuracy-and-drivers/u05-accounting/e1-forecast-accuracy-refused-desktop-light.png) | ![Error E1, U05, dark](../../images/07-accuracy-and-drivers/u05-accounting/e1-forecast-accuracy-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-23-forecast-accuracy-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-23-forecast-accuracy-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-23-forecast-accuracy-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-23-forecast-accuracy-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-23-forecast-accuracy-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-23-forecast-accuracy-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f23-23-forecast-accuracy-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f23-23-forecast-accuracy-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Driver | E-F23-13 driver | text | no | yes |
| Forecast, actual | E-F23-13 | numbers | no | yes |
| Error | E-F23-13 error | percent | no | yes |
| Proposal | E-F23-13 recalibration | list | yes (accounting) | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Accept | row | accounting | baseline rebuilt |
| Refuse | row | accounting | reason kept |

## States

- Normal: drivers with errors and proposals.
- Empty: "No month closed yet".
- Loading: the frame and titles show at once with placeholder rows for the drivers; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a month not closed.
- Read-only: the owner reads.
- Offline: not available offline: computed on the server. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F23-13 Driver accuracy](../../data/e-f23-13-driver-accuracy.md),
[E-F23-01 Baseline forecast](../../data/e-f23-01-baseline-forecast.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-13 Driver accuracy | Measured | Badge "Measured"; a new record starts here; next: Proposed (UC-F23-24); fields editable within the role | U05, U13 | `u05-accounting/s-f23-23-forecast-accuracy-e-f23-13-driver-accuracy-measured-desktop-{light,dark}.png`, `u13-owner/s-f23-23-forecast-accuracy-e-f23-13-driver-accuracy-measured-{desktop,phone}-{light,dark}.png` |
| E-F23-13 Driver accuracy | Proposed | Badge "Proposed"; next: Accepted or Refused (UC-F23-01, UC-F23-24); fields editable within the role | U05, U13 | `u05-accounting/s-f23-23-forecast-accuracy-e-f23-13-driver-accuracy-proposed-desktop-{light,dark}.png`, `u13-owner/s-f23-23-forecast-accuracy-e-f23-13-driver-accuracy-proposed-{desktop,phone}-{light,dark}.png` |
| E-F23-01 Baseline forecast | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-f23-23-forecast-accuracy-e-f23-01-baseline-forecast-active-desktop-{light,dark}.png`, `u13-owner/s-f23-23-forecast-accuracy-e-f23-01-baseline-forecast-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F23-07 Accuracy and drivers](../../flows/fl-f23-07-accuracy-and-drivers.md)

## Open questions

None.

---

⬅️ [S-F23-22 Financing](../06-goals-and-financing/s-f23-22-financing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-24 Sector drivers](s-f23-24-sector-drivers.md)
