🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-07 Set up and report](README.md) › 🖥️ S-F10-18 Point of sale reports

# 🖥️ S-F10-18 Point of sale reports

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Report sales and keep the legal archives.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-07 step 2, U02 | desktop | ![FL-F10-07 step 2, U02, light](../../images/07-set-up-and-report/u02-manager/2-reports-desktop-light.png) | ![FL-F10-07 step 2, U02, dark](../../images/07-set-up-and-report/u02-manager/2-reports-desktop-dark.png) |
| FL-F10-07 step 2, U02 | phone | ![FL-F10-07 step 2, U02, light](../../images/07-set-up-and-report/u02-manager/2-reports-phone-light.png) | ![FL-F10-07 step 2, U02, dark](../../images/07-set-up-and-report/u02-manager/2-reports-phone-dark.png) |
| Error E1, U02 | desktop | ![Error E1, U02, light](../../images/07-set-up-and-report/u02-manager/e1-broken-chain-desktop-light.png) | ![Error E1, U02, dark](../../images/07-set-up-and-report/u02-manager/e1-broken-chain-desktop-dark.png) |
| Error E1, U02 | phone | ![Error E1, U02, light](../../images/07-set-up-and-report/u02-manager/e1-broken-chain-phone-light.png) | ![Error E1, U02, dark](../../images/07-set-up-and-report/u02-manager/e1-broken-chain-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-18-point-of-sale-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-18-point-of-sale-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-18-point-of-sale-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-18-point-of-sale-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-18-point-of-sale-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-18-point-of-sale-reports-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-18-point-of-sale-reports-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-18-point-of-sale-reports-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Report sales and keep the legal archives, as the wireframe shows.
- Empty: No sale in the period yet, with Change the period.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F10-07 Till archive](../../data/e-f10-07-till-archive.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-07 Till archive | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U05, U13 | `u02-manager/s-f10-18-point-of-sale-reports-e-f10-07-till-archive-active-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f10-18-point-of-sale-reports-e-f10-07-till-archive-active-desktop-{light,dark}.png`, `u13-owner/s-f10-18-point-of-sale-reports-e-f10-07-till-archive-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F10-17 Delivery orders](../06-mobile-and-delivery/s-f10-17-delivery-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-19 Customer display](../05-self-order-and-kiosk/s-f10-19-customer-display.md)
