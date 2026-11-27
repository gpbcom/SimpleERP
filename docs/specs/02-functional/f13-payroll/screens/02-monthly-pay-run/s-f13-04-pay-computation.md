🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-02 Monthly pay run](README.md) › 🖥️ S-F13-04 Pay computation

# 🖥️ S-F13-04 Pay computation

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)

## Purpose

Compute gross to net.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-02 step 2, U45 | desktop | ![FL-F13-02 step 2, U45, light](../../images/02-monthly-pay-run/u45-payroll-officer/2-compute-desktop-light.png) | ![FL-F13-02 step 2, U45, dark](../../images/02-monthly-pay-run/u45-payroll-officer/2-compute-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-04-pay-computation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-04-pay-computation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-04-pay-computation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-04-pay-computation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-04-pay-computation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-04-pay-computation-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-04-pay-computation-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-04-pay-computation-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: each employee's gross, contributions and net, with the variations from last month.
- Empty: "Nothing computed yet": shown before the inputs are closed, with a link to them.
- Loading: the frame and titles show at once with placeholder rows for the payslips being computed; within 1 second
  (D408) the data replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: a paid run is read-only (BR-F13-10).
- Offline: not available offline: the computation runs on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F13-02 Monthly pay run](../../flows/fl-f13-02-monthly-pay-run.md)

## Open questions

None.

---

⬅️ [S-F13-03 Pay inputs](s-f13-03-pay-inputs.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-05 Agreement rules](s-f13-05-agreement-rules.md)
