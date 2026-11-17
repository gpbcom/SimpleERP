🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-01 First run](README.md) › 🖥️ S-F21-12 Guide assistant

# 🖥️ S-F21-12 Guide assistant

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Ask the AI assistant at any step.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-01 step 5, U13 | desktop | ![FL-F21-01 step 5, U13, light](../../images/01-first-run/u13-owner/5-assistant-desktop-light.png) | ![FL-F21-01 step 5, U13, dark](../../images/01-first-run/u13-owner/5-assistant-desktop-dark.png) |
| FL-F21-01 step 5, U13 | phone | ![FL-F21-01 step 5, U13, light](../../images/01-first-run/u13-owner/5-assistant-phone-light.png) | ![FL-F21-01 step 5, U13, dark](../../images/01-first-run/u13-owner/5-assistant-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-12-guide-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-12-guide-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-12-guide-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-12-guide-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-12-guide-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-12-guide-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-12-guide-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-12-guide-assistant-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the AI assistant panel at the step.
- Empty: example questions.
- Loading: the frame and titles show at once with placeholder rows for the conversation; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: answers within rights.
- Offline: the AI assistant says it is offline; the question is queued and answered when the network is back, with a
  notification (D182).

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

- [FL-F21-01 First run](../../flows/fl-f21-01-first-run.md)

## Open questions

None.

---

⬅️ [S-F21-11 Module guide](../02-modules/s-f21-11-module-guide.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-13 Demo data](../04-learn-and-improve/s-f21-13-demo-data.md)
