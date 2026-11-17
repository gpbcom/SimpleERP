🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-04 Learn and improve](README.md) › 🖥️ S-F21-19 Provider templates

# 🖥️ S-F21-19 Provider templates

**Status:** ✅ specified

## Personas

- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)

## Purpose

Reuse a set-up for several clients.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-04 step 5, U11 | desktop | ![FL-F21-04 step 5, U11, light](../../images/04-learn-and-improve/u11-provider-admin/5-provider-template-desktop-light.png) | ![FL-F21-04 step 5, U11, dark](../../images/04-learn-and-improve/u11-provider-admin/5-provider-template-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-19-provider-templates-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-19-provider-templates-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-19-provider-templates-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-19-provider-templates-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-19-provider-templates-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-19-provider-templates-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f21-19-provider-templates-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f21-19-provider-templates-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: provider templates and clients.
- Empty: "No template saved".
- Loading: the frame and titles show at once with placeholder rows for the templates; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: clients see the result only.
- Offline: not available offline: applied online. D38 keeps only today's schedule, time and intervention records
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

- [FL-F21-04 Learn and improve](../../flows/fl-f21-04-learn-and-improve.md)

## Open questions

None.

---

⬅️ [S-F21-18 Prices](../02-modules/s-f21-18-prices.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-20 Onboarding figures](s-f21-20-onboarding-figures.md)
