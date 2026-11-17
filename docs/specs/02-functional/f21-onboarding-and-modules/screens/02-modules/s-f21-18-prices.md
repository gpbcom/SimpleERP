🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-02 Modules](README.md) › 🖥️ S-F21-18 Prices

# 🖥️ S-F21-18 Prices

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

See what each module costs in the hosted edition.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-02 step 5, U13 | desktop | ![FL-F21-02 step 5, U13, light](../../images/02-modules/u13-owner/5-prices-desktop-light.png) | ![FL-F21-02 step 5, U13, dark](../../images/02-modules/u13-owner/5-prices-desktop-dark.png) |
| FL-F21-02 step 5, U13 | phone | ![FL-F21-02 step 5, U13, light](../../images/02-modules/u13-owner/5-prices-phone-light.png) | ![FL-F21-02 step 5, U13, dark](../../images/02-modules/u13-owner/5-prices-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-18-prices-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-18-prices-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-18-prices-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-18-prices-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-18-prices-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-18-prices-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-18-prices-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-18-prices-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: modules with prices excluding VAT.
- Empty: never empty.
- Loading: the frame and titles show at once with placeholder rows for the prices; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: administrators ask the owner.
- Offline: not available offline: prices are read online. D38 keeps only today's schedule, time and intervention records
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

- [FL-F21-02 Modules](../../flows/fl-f21-02-modules.md)

## Open questions

None.

---

⬅️ [S-F21-17 First sign-in](../04-learn-and-improve/s-f21-17-first-sign-in.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-19 Provider templates](../04-learn-and-improve/s-f21-19-provider-templates.md)
