🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-02 Run](README.md) › 🖥️ S-F23-05 Run

# 🖥️ S-F23-05 Run

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Run the scenario on a copy with the real rules.

## Entry points

What-if simulation and impact in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-02 step 1, U05 | desktop | ![FL-F23-02 step 1, U05, light](../../images/02-run/u05-accounting/1-run-desktop-light.png) | ![FL-F23-02 step 1, U05, dark](../../images/02-run/u05-accounting/1-run-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-05-run-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-05-run-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-05-run-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-05-run-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-05-run-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-05-run-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f23-05-run-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f23-05-run-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the run's progress and result.
- Empty: "Not run yet".
- Loading: the frame and titles show at once with placeholder rows for the run; within 1 second (D408) the data replaces
  them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: finished runs read-only.
- Offline: not available offline: runs on the server. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

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

- [FL-F23-02 Run](../../flows/fl-f23-02-run.md)

## Open questions

None.

---

⬅️ [S-F23-04 Ranges](../01-build-a-scenario/s-f23-04-ranges.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-06 Sales impact](../03-see-the-impact/s-f23-06-sales-impact.md)
