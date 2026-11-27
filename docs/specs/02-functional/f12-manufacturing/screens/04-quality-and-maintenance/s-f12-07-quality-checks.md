🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-04 Quality and maintenance](README.md) › 🖥️ S-F12-07 Quality checks

# 🖥️ S-F12-07 Quality checks

**Status:** ✅ specified

## Personas

- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Run quality checks and handle non-conformities.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-04 step 1, U20 | tablet | ![FL-F12-04 step 1, U20, light](../../images/04-quality-and-maintenance/u20-production-operator/1-quality-check-tablet-light.png) | ![FL-F12-04 step 1, U20, dark](../../images/04-quality-and-maintenance/u20-production-operator/1-quality-check-tablet-dark.png) |
| Error E1, U20 | tablet | ![Error E1, U20, light](../../images/04-quality-and-maintenance/u20-production-operator/e1-check-failed-tablet-light.png) | ![Error E1, U20, dark](../../images/04-quality-and-maintenance/u20-production-operator/e1-check-failed-tablet-dark.png) |
| Empty | tablet | ![Empty, light](../../images/states/s-f12-07-quality-checks-empty-tablet-light.png) | ![Empty, dark](../../images/states/s-f12-07-quality-checks-empty-tablet-dark.png) |
| Loading | tablet | ![Loading, light](../../images/states/s-f12-07-quality-checks-loading-tablet-light.png) | ![Loading, dark](../../images/states/s-f12-07-quality-checks-loading-tablet-dark.png) |
| Read-only | tablet | ![Read-only, light](../../images/states/s-f12-07-quality-checks-read-only-tablet-light.png) | ![Read-only, dark](../../images/states/s-f12-07-quality-checks-read-only-tablet-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-f12-07-quality-checks-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-f12-07-quality-checks-offline-tablet-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Run quality checks and handle non-conformities, as the wireframe shows.
- Empty: No quality check due yet, with Nothing due.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: Works offline on the shop-floor tablet,
  [UC-F12-26](../../use-cases/11-finite-schedule-and-the-tablet/uc-f12-26-keep-working-on-the-tablet-without-the-network.md),
  the work orders loaded at the start of the shift, their instructions and the operator's start, stop, quantity and
  check records stay on the tablet and are sent in order when the network is back.

Shown entities (VD-15): [E-F12-07 Quality control point](../../data/e-f12-07-quality-control-point.md),
[E-F12-08 Non-conformity](../../data/e-f12-08-non-conformity.md),
[E-F12-20 Control chart](../../data/e-f12-20-control-chart.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-07 Quality control point | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U20, U21 | `u20-production-operator/s-f12-07-quality-checks-e-f12-07-quality-control-point-active-tablet-{light,dark}.png`, `u21-production-planner/s-f12-07-quality-checks-e-f12-07-quality-control-point-active-{desktop,phone}-{light,dark}.png` |
| E-F12-08 Non-conformity | Open | Badge "Open"; a new record starts here; next: In progress (UC-F12-07); fields editable within the role | U20, U21 | `u20-production-operator/s-f12-07-quality-checks-e-f12-08-non-conformity-open-tablet-{light,dark}.png`, `u21-production-planner/s-f12-07-quality-checks-e-f12-08-non-conformity-open-{desktop,phone}-{light,dark}.png` |
| E-F12-08 Non-conformity | In progress | Badge "In progress"; next: Closed (UC-F12-07); fields editable within the role | U20, U21 | `u20-production-operator/s-f12-07-quality-checks-e-f12-08-non-conformity-in-progress-tablet-{light,dark}.png`, `u21-production-planner/s-f12-07-quality-checks-e-f12-08-non-conformity-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F12-08 Non-conformity | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U20, U21 | `u20-production-operator/s-f12-07-quality-checks-e-f12-08-non-conformity-closed-tablet-{light,dark}.png`, `u21-production-planner/s-f12-07-quality-checks-e-f12-08-non-conformity-closed-{desktop,phone}-{light,dark}.png` |
| E-F12-20 Control chart | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U20 | `u20-production-operator/s-f12-07-quality-checks-e-f12-20-control-chart-active-tablet-{light,dark}.png` |

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

## Shown in

- [FL-F12-04 Quality and maintenance](../../flows/fl-f12-04-quality-and-maintenance.md)
- [FL-F12-12 Quality engineering](../../flows/fl-f12-12-quality-engineering.md)

## Open questions

None.

---

⬅️ [S-F12-06 Consumption](../03-make-the-products/s-f12-06-consumption.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-08 Maintenance](s-f12-08-maintenance.md)
