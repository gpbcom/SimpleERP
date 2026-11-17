🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-05 Billing](README.md) › 🖥️ S-F22-17 Platform costs

# 🖥️ S-F22-17 Platform costs

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Follow the hosting's own platform costs.

## Entry points

Unified platform cost management in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-05 step 3, U48 | desktop | ![FL-F22-05 step 3, U48, light](../../images/05-billing/u48-hosting-engineer/3-platform-desktop-light.png) | ![FL-F22-05 step 3, U48, dark](../../images/05-billing/u48-hosting-engineer/3-platform-desktop-dark.png) |
| FL-F22-05 step 3, U48 | phone | ![FL-F22-05 step 3, U48, light](../../images/05-billing/u48-hosting-engineer/3-platform-phone-light.png) | ![FL-F22-05 step 3, U48, dark](../../images/05-billing/u48-hosting-engineer/3-platform-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-17-platform-costs-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-17-platform-costs-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-17-platform-costs-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-17-platform-costs-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-17-platform-costs-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-17-platform-costs-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f22-17-platform-costs-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f22-17-platform-costs-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the hosting's own costs against revenue.
- Empty: "No data".
- Loading: the frame and titles show at once with placeholder rows for the costs; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: not available offline: computed online. D38 keeps only today's schedule, time and intervention records
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

- [FL-F22-05 Billing](../../flows/fl-f22-05-billing.md)

## Open questions

None.

---

⬅️ [S-F22-16 Client re-billing](s-f22-16-client-re-billing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-18 Anomalies](../03-runs/s-f22-18-anomalies.md)
