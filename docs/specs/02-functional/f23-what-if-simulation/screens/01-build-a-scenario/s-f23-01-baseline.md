🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-01 Build a scenario](README.md) › 🖥️ S-F23-01 Baseline

# 🖥️ S-F23-01 Baseline

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

See the baseline forecast.

## Entry points

What-if simulation and impact in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-01 step 1, U13 | desktop | ![FL-F23-01 step 1, U13, light](../../images/01-build-a-scenario/u13-owner/1-baseline-desktop-light.png) | ![FL-F23-01 step 1, U13, dark](../../images/01-build-a-scenario/u13-owner/1-baseline-desktop-dark.png) |
| FL-F23-01 step 1, U13 | phone | ![FL-F23-01 step 1, U13, light](../../images/01-build-a-scenario/u13-owner/1-baseline-phone-light.png) | ![FL-F23-01 step 1, U13, dark](../../images/01-build-a-scenario/u13-owner/1-baseline-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-01-baseline-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-01-baseline-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-01-baseline-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-01-baseline-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-01-baseline-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-01-baseline-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f23-01-baseline-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f23-01-baseline-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the baseline forecast with its method and horizon.
- Empty: "Not enough history": the baseline uses budgets and plans only.
- Loading: the frame and titles show at once with placeholder rows for the forecast; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: not available offline: computed on the server. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F23-01 Baseline forecast](../../data/e-f23-01-baseline-forecast.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-01 Baseline forecast | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-f23-01-baseline-e-f23-01-baseline-forecast-active-desktop-{light,dark}.png`, `u13-owner/s-f23-01-baseline-e-f23-01-baseline-forecast-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F23-01 Build a scenario](../../flows/fl-f23-01-build-a-scenario.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F23-02 New scenario](s-f23-02-new-scenario.md)
