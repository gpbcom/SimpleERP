🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-03 Runs](README.md) › 🖥️ S-F22-18 Anomalies

# 🖥️ S-F22-18 Anomalies

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Spot anomalies and runaway agents.

## Entry points

Unified platform cost management in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-03 step 3, U07 | desktop | ![FL-F22-03 step 3, U07, light](../../images/03-runs/u07-administrator/3-anomaly-desktop-light.png) | ![FL-F22-03 step 3, U07, dark](../../images/03-runs/u07-administrator/3-anomaly-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-18-anomalies-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-18-anomalies-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-18-anomalies-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-18-anomalies-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-18-anomalies-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-18-anomalies-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f22-18-anomalies-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f22-18-anomalies-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: anomalies with pause or allow.
- Empty: "No anomaly".
- Loading: the frame and titles show at once with placeholder rows for the anomalies; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: managers read.
- Offline: not available offline: anomalies are handled online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F22-07 Cost alert](../../data/e-f22-07-cost-alert.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-07 Cost alert | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U48 | `u07-administrator/s-f22-18-anomalies-e-f22-07-cost-alert-active-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f22-18-anomalies-e-f22-07-cost-alert-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F22-03 Runs](../../flows/fl-f22-03-runs.md)

## Open questions

None.

---

⬅️ [S-F22-17 Platform costs](../05-billing/s-f22-17-platform-costs.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-19 Cost reports](../04-accounting/s-f22-19-cost-reports.md)
