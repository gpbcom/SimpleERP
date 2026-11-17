🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-02 Modules](README.md) › 🖥️ S-F21-06 Switch off

# 🖥️ S-F21-06 Switch off

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Switch a module off and keep its data.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-02 step 3, U07 | desktop | ![FL-F21-02 step 3, U07, light](../../images/02-modules/u07-administrator/3-switch-off-desktop-light.png) | ![FL-F21-02 step 3, U07, dark](../../images/02-modules/u07-administrator/3-switch-off-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-06-switch-off-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-06-switch-off-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-06-switch-off-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-06-switch-off-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-06-switch-off-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-06-switch-off-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f21-06-switch-off-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f21-06-switch-off-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the confirmation and what stays read-only.
- Empty: never empty: opens from a module.
- Loading: the frame and titles show at once with placeholder rows for the module; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: modules others need cannot be switched off.
- Offline: not available offline: switching runs online. D38 keeps only today's schedule, time and intervention records
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

⬅️ [S-F21-05 Dependencies](s-f21-05-dependencies.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-07 Identity](../01-first-run/s-f21-07-identity.md)
