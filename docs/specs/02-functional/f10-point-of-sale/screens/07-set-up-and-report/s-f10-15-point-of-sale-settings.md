🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-07 Set up and report](README.md) › 🖥️ S-F10-15 Point of sale settings

# 🖥️ S-F10-15 Point of sale settings

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Set up a point of sale and its hardware.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-07 step 1, U07 | desktop | ![FL-F10-07 step 1, U07, light](../../images/07-set-up-and-report/u07-administrator/1-settings-desktop-light.png) | ![FL-F10-07 step 1, U07, dark](../../images/07-set-up-and-report/u07-administrator/1-settings-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-15-point-of-sale-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-15-point-of-sale-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-15-point-of-sale-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-15-point-of-sale-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-15-point-of-sale-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-15-point-of-sale-settings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f10-15-point-of-sale-settings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f10-15-point-of-sale-settings-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Set up a point of sale and its hardware, as the wireframe shows.
- Empty: No point of sale yet, with New point of sale.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F10-01 Point of sale](../../data/e-f10-01-point-of-sale.md),
[E-F10-14 Point of sale device](../../data/e-f10-14-point-of-sale-device.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-01 Point of sale | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U07 | `u02-manager/s-f10-15-point-of-sale-settings-e-f10-01-point-of-sale-active-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f10-15-point-of-sale-settings-e-f10-01-point-of-sale-active-desktop-{light,dark}.png` |
| E-F10-14 Point of sale device | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02 | `u02-manager/s-f10-15-point-of-sale-settings-e-f10-14-point-of-sale-device-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F10-07 Set up and report](../../flows/fl-f10-07-set-up-and-report.md)

## Open questions

None.

---

⬅️ [S-F10-14 Mobile till](../06-mobile-and-delivery/s-f10-14-mobile-till.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-16 Staff login](../01-till-session/s-f10-16-staff-login.md)
