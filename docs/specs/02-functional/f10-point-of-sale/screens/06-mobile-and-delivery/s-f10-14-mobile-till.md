🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-06 Mobile and delivery](README.md) › 🖥️ S-F10-14 Mobile till

# 🖥️ S-F10-14 Mobile till

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)

## Purpose

Sell on the move and offline.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-06 step 1, U17 | phone | ![FL-F10-06 step 1, U17, light](../../images/06-mobile-and-delivery/u17-cashier/1-mobile-offline-phone-light.png) | ![FL-F10-06 step 1, U17, dark](../../images/06-mobile-and-delivery/u17-cashier/1-mobile-offline-phone-dark.png) |
| FL-F10-06 step 1, U17 | desktop | ![FL-F10-06 step 1, U17, light](../../images/06-mobile-and-delivery/u17-cashier/1-mobile-offline-desktop-light.png) | ![FL-F10-06 step 1, U17, dark](../../images/06-mobile-and-delivery/u17-cashier/1-mobile-offline-desktop-dark.png) |
| FL-F10-06 step 1, U17 | tablet | ![FL-F10-06 step 1, U17, light](../../images/06-mobile-and-delivery/u17-cashier/1-mobile-offline-tablet-light.png) | ![FL-F10-06 step 1, U17, dark](../../images/06-mobile-and-delivery/u17-cashier/1-mobile-offline-tablet-dark.png) |
| Error E1, U17 | phone | ![Error E1, U17, light](../../images/06-mobile-and-delivery/u17-cashier/e1-offline-too-long-phone-light.png) | ![Error E1, U17, dark](../../images/06-mobile-and-delivery/u17-cashier/e1-offline-too-long-phone-dark.png) |
| Error E1, U17 | desktop | ![Error E1, U17, light](../../images/06-mobile-and-delivery/u17-cashier/e1-offline-too-long-desktop-light.png) | ![Error E1, U17, dark](../../images/06-mobile-and-delivery/u17-cashier/e1-offline-too-long-desktop-dark.png) |
| Error E1, U17 | tablet | ![Error E1, U17, light](../../images/06-mobile-and-delivery/u17-cashier/e1-offline-too-long-tablet-light.png) | ![Error E1, U17, dark](../../images/06-mobile-and-delivery/u17-cashier/e1-offline-too-long-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-14-mobile-till-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-14-mobile-till-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-14-mobile-till-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-14-mobile-till-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-14-mobile-till-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-14-mobile-till-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-14-mobile-till-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-14-mobile-till-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Sell on the move and offline, as the wireframe shows.
- Empty: No sale today yet, with New sale.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: The till keeps selling, numbering and chaining its sales locally and syncs on reconnect
  ([BR-F10-06](../../business-rules/br-f10-06-offline-keeps-selling.md)); a card terminal that loses its link cancels
  the payment; a warning shows after 24 hours offline.

Shown entities (VD-15): [E-F10-02 Till session](../../data/e-f10-02-till-session.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-02 Till session | Open | Badge "Open"; a new record starts here; next: Closing (UC-F10-01); fields editable within the role | U14, U17 | `u14-field-worker/s-f10-14-mobile-till-e-f10-02-till-session-open-phone-{light,dark}.png`, `u17-cashier/s-f10-14-mobile-till-e-f10-02-till-session-open-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-02 Till session | Closing | Badge "Closing"; next: Closed (UC-F10-01); fields editable within the role | U14, U17 | `u14-field-worker/s-f10-14-mobile-till-e-f10-02-till-session-closing-phone-{light,dark}.png`, `u17-cashier/s-f10-14-mobile-till-e-f10-02-till-session-closing-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-02 Till session | Closed | Badge "Closed"; next: Posted (UC-F10-01); fields editable within the role | U14, U17 | `u14-field-worker/s-f10-14-mobile-till-e-f10-02-till-session-closed-phone-{light,dark}.png`, `u17-cashier/s-f10-14-mobile-till-e-f10-02-till-session-closed-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-02 Till session | Posted | Badge "Posted"; final: read-only, no next state; the history shows how it got here | U14, U17 | `u14-field-worker/s-f10-14-mobile-till-e-f10-02-till-session-posted-phone-{light,dark}.png`, `u17-cashier/s-f10-14-mobile-till-e-f10-02-till-session-posted-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-F10-06 Mobile and delivery](../../flows/fl-f10-06-mobile-and-delivery.md)

## Open questions

None.

---

⬅️ [S-F10-13 Kiosk](../05-self-order-and-kiosk/s-f10-13-kiosk.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-15 Point of sale settings](../07-set-up-and-report/s-f10-15-point-of-sale-settings.md)
