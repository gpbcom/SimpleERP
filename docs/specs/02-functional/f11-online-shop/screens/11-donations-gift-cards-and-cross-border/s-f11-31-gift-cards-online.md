🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F11-11](README.md) ›
🖥️ S-F11-31 Gift cards online

# 🖥️ S-F11-31 Gift cards online

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): buys and spends a card, on a phone.
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): follows the cards, on a desktop.

## Purpose

Buy a gift card, spend it at checkout and follow the cards sold.

## Entry points

The shop's Gift cards page; checkout › Gift card code; Online shop › Gift cards.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Gift cards                                                                 Cards sold: 128  |
| ------------------------------------------------------------------------------------------- |
| Amount     [ 25 ]  [ 50 ]  [ 100 ]  [ Other ]                                               |
| To         sonia@example.com        Send on  2026-12-24                                     |
| Message    Happy birthday!                                                                  |
| ------------------------------------------------------------------------------------------- |
| Spend a card at checkout:  Code [ 8H4K-2Q9T ]  [Apply]      Balance 20.00 EUR               |
| [Buy the card - 50.00 EUR]                                                                  |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f11-31-gift-cards-online-empty-desktop-{light,dark}.png`,
`s-f11-31-gift-cards-online-empty-phone-{light,dark}.png`,
`s-f11-31-gift-cards-online-loading-desktop-{light,dark}.png`,
`s-f11-31-gift-cards-online-loading-phone-{light,dark}.png`,
`s-f11-31-gift-cards-online-offline-desktop-{light,dark}.png`,
`s-f11-31-gift-cards-online-offline-phone-{light,dark}.png`,
`s-f11-31-gift-cards-online-read-only-desktop-{light,dark}.png`,
`s-f11-31-gift-cards-online-read-only-phone-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-11 step 3, U09 | phone | ![FL-F11-11 step 3, U09, light](../../images/11-donations-gift-cards-and-cross-border/u09-customer/3-gift-cards-online-phone-light.png) | ![FL-F11-11 step 3, U09, dark](../../images/11-donations-gift-cards-and-cross-border/u09-customer/3-gift-cards-online-phone-dark.png) |
| FL-F11-11 step 3, U09 | phone | ![FL-F11-11 step 3, U09, light](../../images/11-donations-gift-cards-and-cross-border/u09-customer/3-gift-cards-online-phone-light.png) | ![FL-F11-11 step 3, U09, dark](../../images/11-donations-gift-cards-and-cross-border/u09-customer/3-gift-cards-online-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f11-31-gift-cards-online-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f11-31-gift-cards-online-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f11-31-gift-cards-online-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f11-31-gift-cards-online-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f11-31-gift-cards-online-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f11-31-gift-cards-online-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-31-gift-cards-online-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-31-gift-cards-online-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Amount | E-F11-26 amount sold | choice or money | yes | yes |
| Recipient and message | E-F11-26 recipient, message | email and text | yes | yes |
| Send on | E-F11-26 delivery date | date | yes | no |
| Code | E-F11-26 code | text | yes | at checkout |
| Balance and state | E-F11-26 balance and state | money and badge | store manager | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Buy the card | page | the shopper | a card is issued (UC-F11-32) |
| Apply a code | checkout | the holder | the balance is used on the order |
| Block | card row | the store manager | no channel accepts the card |
| Adjust | card row | the store manager | the balance changes with a reason |

## States

- Normal: the buying form and the code field at checkout; for the store manager, the cards sold with balance and state.
- Empty: No card sold yet: a hint on the amounts offered and the delivery date.
- Loading: The form and the balance as placeholders.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a wrong code
  says so without telling whether the card exists.
- Read-only: a card that is used or expired: its history is shown, with no action.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F11-26 Online gift card](../../data/e-f11-26-online-gift-card.md),
[E-F10-10 Loyalty card and gift card](../../../f10-point-of-sale/data/e-f10-10-loyalty-card-and-gift-card.md),
[E-F11-09 Customer account](../../data/e-f11-09-customer-account.md),
[E-F11-05 Checkout](../../data/e-f11-05-checkout.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-26 Online gift card | Issued | Badge "Issued"; a new record starts here; next: Active or Cancelled (UC-F11-32); fields editable within the role | U09, U23 | `u09-customer/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-issued-phone-{light,dark}.png`; `u23-store-manager/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-issued-{desktop,phone,tablet}-{light,dark}.png` |
| E-F11-26 Online gift card | Active | Badge "Active"; next: Partly used or Used or Expired or Cancelled (BR-F11-27, UC-F11-32); fields editable within the role | U09, U23 | `u09-customer/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-active-phone-{light,dark}.png`; `u23-store-manager/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F11-26 Online gift card | Partly used | Badge "Partly used"; next: Partly used or Used or Expired (BR-F11-27); fields editable within the role | U09, U23 | `u09-customer/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-partly-used-phone-{light,dark}.png`; `u23-store-manager/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-partly-used-{desktop,phone,tablet}-{light,dark}.png` |
| E-F11-26 Online gift card | Used | Badge "Used"; final state, read-only | U09, U23 | `u09-customer/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-used-phone-{light,dark}.png`; `u23-store-manager/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-used-{desktop,phone,tablet}-{light,dark}.png` |
| E-F11-26 Online gift card | Expired | Badge "Expired"; final state, read-only | U09, U23 | `u09-customer/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-expired-phone-{light,dark}.png`; `u23-store-manager/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-expired-{desktop,phone,tablet}-{light,dark}.png` |
| E-F11-26 Online gift card | Cancelled | Badge "Cancelled"; final state, read-only | U09, U23 | `u09-customer/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-cancelled-phone-{light,dark}.png`; `u23-store-manager/s-f11-31-gift-cards-online-e-f11-26-online-gift-card-cancelled-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

On a phone the form is one column with large amount buttons; the card list is desktop.

## Accessibility

Amounts and balances are read as money in words; the code field accepts pasting; keyboard: next field, buy, apply.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F11-11 Donations, wishlists, gift cards and cross-border](../../flows/fl-f11-11-donations-gift-cards-and-cross-border.md)

## Open questions

None.

---

⬅️ [S-F11-30 Wishlists](s-f11-30-wishlists.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-32 Cross-border](s-f11-32-cross-border.md)
