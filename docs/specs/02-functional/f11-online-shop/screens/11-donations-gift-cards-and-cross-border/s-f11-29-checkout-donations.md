🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F11-11](README.md) ›
🖥️ S-F11-29 Checkout donations

# 🖥️ S-F11-29 Checkout donations

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): gives at checkout, on a phone.
- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): sets the campaign, on a desktop.

## Purpose

Offer a donation at checkout and follow the campaign.

## Entry points

The checkout page; Online shop › Donations for the campaign.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Checkout                                                                     Cart: 47.60 EUR |
| ------------------------------------------------------------------------------------------- |
| Add a donation to Cats Shelter, an association that feeds and homes stray cats              |
|   [ 1 EUR ]  [ 2 EUR ]  [ 5 EUR ]  [ Other amount ]  [ Round up: 0.40 EUR ]                 |
| Donation (no VAT)                     2.00 EUR        Remove                                |
| Goods and delivery                   47.60 EUR                                              |
| Total to pay                         49.60 EUR        A tax receipt will be sent to you.    |
| [Pay 49.60 EUR]                                                                             |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f11-29-checkout-donations-empty-desktop-{light,dark}.png`,
`s-f11-29-checkout-donations-empty-phone-{light,dark}.png`,
`s-f11-29-checkout-donations-loading-desktop-{light,dark}.png`,
`s-f11-29-checkout-donations-loading-phone-{light,dark}.png`,
`s-f11-29-checkout-donations-offline-desktop-{light,dark}.png`,
`s-f11-29-checkout-donations-offline-phone-{light,dark}.png`,
`s-f11-29-checkout-donations-read-only-desktop-{light,dark}.png`,
`s-f11-29-checkout-donations-read-only-phone-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-11 step 1, U09 | phone | ![FL-F11-11 step 1, U09, light](../../images/11-donations-gift-cards-and-cross-border/u09-customer/1-checkout-donations-phone-light.png) | ![FL-F11-11 step 1, U09, dark](../../images/11-donations-gift-cards-and-cross-border/u09-customer/1-checkout-donations-phone-dark.png) |
| FL-F11-11 step 1, U09 | phone | ![FL-F11-11 step 1, U09, light](../../images/11-donations-gift-cards-and-cross-border/u09-customer/1-checkout-donations-phone-light.png) | ![FL-F11-11 step 1, U09, dark](../../images/11-donations-gift-cards-and-cross-border/u09-customer/1-checkout-donations-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f11-29-checkout-donations-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f11-29-checkout-donations-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f11-29-checkout-donations-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f11-29-checkout-donations-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f11-29-checkout-donations-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f11-29-checkout-donations-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-29-checkout-donations-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-29-checkout-donations-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Beneficiary | E-F11-24 beneficiary | name and text | campaign | yes |
| Amount | E-F11-24 amount | preset, free or round-up | yes | no |
| Donor | E-F11-24 donor | name and address | for a receipt | for a receipt |
| Total | checkout total | money | no | yes |
| State | E-F11-24 state | badge in the campaign view | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a donation | checkout | the shopper | a donation line is added (UC-F11-30) |
| Remove | donation line | the shopper | the donation is removed |
| Set a campaign | campaign page | marketing | a beneficiary and amounts are offered |
| Pass on | campaign page | the accountant | the donations are paid to the beneficiary |

## States

- Normal: the donation offer under the cart, with the beneficiary, the amounts and the new total.
- Empty: No campaign on: the offer is not shown to the shopper, and marketing sees a hint to create one.
- Loading: The offer and the total as placeholders.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  address for the receipt is asked under the field.
- Read-only: an ended campaign: its donations shown, with no action.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F11-24 Donation](../../data/e-f11-24-donation.md),
[E-F11-05 Checkout](../../data/e-f11-05-checkout.md),
[E-F8-19 Dedicated fund](../../../f08-accounting/data/e-f08-19-dedicated-fund.md),
[E-F11-09 Customer account](../../data/e-f11-09-customer-account.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-24 Donation | Pledged | Badge "Pledged"; a new record starts here; next: Paid or Removed (UC-F11-30); fields editable within the role | U09, U12 | `u09-customer/s-f11-29-checkout-donations-e-f11-24-donation-pledged-phone-{light,dark}.png`; `u12-marketing/s-f11-29-checkout-donations-e-f11-24-donation-pledged-{desktop,phone}-{light,dark}.png` |
| E-F11-24 Donation | Paid | Badge "Paid"; next: Receipted or Passed on or Refunded (BR-F11-25, UC-F11-30); fields editable within the role | U09, U12 | `u09-customer/s-f11-29-checkout-donations-e-f11-24-donation-paid-phone-{light,dark}.png`; `u12-marketing/s-f11-29-checkout-donations-e-f11-24-donation-paid-{desktop,phone}-{light,dark}.png` |
| E-F11-24 Donation | Removed | Badge "Removed"; final state, read-only | U09, U12 | `u09-customer/s-f11-29-checkout-donations-e-f11-24-donation-removed-phone-{light,dark}.png`; `u12-marketing/s-f11-29-checkout-donations-e-f11-24-donation-removed-{desktop,phone}-{light,dark}.png` |
| E-F11-24 Donation | Receipted | Badge "Receipted"; next: Passed on (BR-F11-25); fields editable within the role | U09, U12 | `u09-customer/s-f11-29-checkout-donations-e-f11-24-donation-receipted-phone-{light,dark}.png`; `u12-marketing/s-f11-29-checkout-donations-e-f11-24-donation-receipted-{desktop,phone}-{light,dark}.png` |
| E-F11-24 Donation | Passed on | Badge "Passed on"; final state, read-only | U09, U12 | `u09-customer/s-f11-29-checkout-donations-e-f11-24-donation-passed-on-phone-{light,dark}.png`; `u12-marketing/s-f11-29-checkout-donations-e-f11-24-donation-passed-on-{desktop,phone}-{light,dark}.png` |
| E-F11-24 Donation | Refunded | Badge "Refunded"; final state, read-only | U09, U12 | `u09-customer/s-f11-29-checkout-donations-e-f11-24-donation-refunded-phone-{light,dark}.png`; `u12-marketing/s-f11-29-checkout-donations-e-f11-24-donation-refunded-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

On a phone the amounts are large buttons under the cart; the campaign page is desktop.

## Accessibility

The beneficiary and the effect on the total are written in words; the amounts are buttons with labels; keyboard: choose,
add, remove.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)

## Shown in

- [FL-F11-11 Donations, wishlists, gift cards and cross-border](../../flows/fl-f11-11-donations-gift-cards-and-cross-border.md)

## Open questions

None.

---

⬅️ [S-F11-28 Shop reports](../10-fulfil-from-stores-and-report/s-f11-28-shop-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-30 Wishlists](s-f11-30-wishlists.md)
