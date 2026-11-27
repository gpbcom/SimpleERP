🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F11-11](README.md) ›
🖥️ S-F11-32 Cross-border

# 🖥️ S-F11-32 Cross-border

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): opens and prices the countries, on
  a desktop.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): sees the price, VAT and delivery of their country, on a
  phone.

## Purpose

Open countries for sale and show the shopper the right price, VAT, delivery and duties.

## Entry points

Online shop › Cross-border; the checkout's country choice.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Cross-border                                   Countries open: 4   Paused: 1        [Add a country] |
| ------------------------------------------------------------------------------------------- |
| COUNTRY      CURRENCY   LANGUAGE   VAT   PRICE RULE         DELIVERY           STATE        |
| France       Euro       French     20    Shop price         Parcel 4.90        Active       |
| Germany      Euro       German     19    Converted, to .90  Parcel 6.90        Active       |
| Switzerland  CHF        German     -     Fixed by product   Parcel 12.00       Draft   [Open] |
| Duties for Switzerland: collected by the carrier on delivery   Not served: 38 shoppers this month |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f11-32-cross-border-empty-desktop-{light,dark}.png`,
`s-f11-32-cross-border-empty-phone-{light,dark}.png`, `s-f11-32-cross-border-loading-desktop-{light,dark}.png`,
`s-f11-32-cross-border-loading-phone-{light,dark}.png`, `s-f11-32-cross-border-offline-desktop-{light,dark}.png`,
`s-f11-32-cross-border-offline-phone-{light,dark}.png`, `s-f11-32-cross-border-read-only-desktop-{light,dark}.png`,
`s-f11-32-cross-border-read-only-phone-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-11 step 4, U12 | desktop | ![FL-F11-11 step 4, U12, light](../../images/11-donations-gift-cards-and-cross-border/u12-marketing/4-cross-border-desktop-light.png) | ![FL-F11-11 step 4, U12, dark](../../images/11-donations-gift-cards-and-cross-border/u12-marketing/4-cross-border-desktop-dark.png) |
| FL-F11-11 step 4, U12 | desktop | ![FL-F11-11 step 4, U12, light](../../images/11-donations-gift-cards-and-cross-border/u12-marketing/4-cross-border-desktop-light.png) | ![FL-F11-11 step 4, U12, dark](../../images/11-donations-gift-cards-and-cross-border/u12-marketing/4-cross-border-desktop-dark.png) |
| FL-F11-11 step 4, U12 | phone | ![FL-F11-11 step 4, U12, light](../../images/11-donations-gift-cards-and-cross-border/u12-marketing/4-cross-border-phone-light.png) | ![FL-F11-11 step 4, U12, dark](../../images/11-donations-gift-cards-and-cross-border/u12-marketing/4-cross-border-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-32-cross-border-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-32-cross-border-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-32-cross-border-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-32-cross-border-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-32-cross-border-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-32-cross-border-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-32-cross-border-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-32-cross-border-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Country | E-F11-27 country, language | text | draft only | yes |
| Currency and price rule | E-F11-27 currency, rule | choice | yes | yes |
| VAT rate | E-F11-27 VAT rate | percent | from the tax rates | yes |
| Delivery and duties | E-F11-27 delivery, duties | list and choice | yes | yes |
| State | E-F11-27 state | badge | by action | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a country | header | marketing | a Draft price list (UC-F11-33) |
| Open | row | marketing | the country is open for sale |
| Pause | row | marketing | orders to the country are paused |
| Retire | row | marketing | the country is closed |
| Show not served | header | marketing | the countries shoppers asked for, as counts |

## States

- Normal: the countries with currency, VAT, price rule, delivery and state; the shopper sees the price and delivery of
  their country.
- Empty: No country but the home country: a hint to add the first.
- Loading: The countries as placeholders, then the prices.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a country not
  served says so with the countries served.
- Read-only: a retired country: its history shown, with no action.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F11-27 Country price list](../../data/e-f11-27-country-price-list.md),
[E-F11-01 Website](../../data/e-f11-01-website.md), [E-F11-07 Delivery method](../../data/e-f11-07-delivery-method.md),
[E-F8-33 Tax rate](../../../f08-accounting/data/e-f08-33-tax-rate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-27 Country price list | Draft | Badge "Draft"; a new record starts here; next: Active or Retired (UC-F11-33); fields editable within the role | U12, U09 | `u12-marketing/s-f11-32-cross-border-e-f11-27-country-price-list-draft-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f11-32-cross-border-e-f11-27-country-price-list-draft-phone-{light,dark}.png` |
| E-F11-27 Country price list | Active | Badge "Active"; next: Suspended or Retired (UC-F11-33); fields editable within the role | U12, U09 | `u12-marketing/s-f11-32-cross-border-e-f11-27-country-price-list-active-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f11-32-cross-border-e-f11-27-country-price-list-active-phone-{light,dark}.png` |
| E-F11-27 Country price list | Suspended | Badge "Suspended"; next: Active or Retired (UC-F11-33); fields editable within the role | U12, U09 | `u12-marketing/s-f11-32-cross-border-e-f11-27-country-price-list-suspended-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f11-32-cross-border-e-f11-27-country-price-list-suspended-phone-{light,dark}.png` |
| E-F11-27 Country price list | Retired | Badge "Retired"; final state, read-only | U12, U09 | `u12-marketing/s-f11-32-cross-border-e-f11-27-country-price-list-retired-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f11-32-cross-border-e-f11-27-country-price-list-retired-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

Desktop for marketing; on a phone the shopper sees a country choice and the totals in order.

## Accessibility

Currency and VAT are read as words with the amount; keyboard: next country, open, pause.

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

⬅️ [S-F11-31 Gift cards online](s-f11-31-gift-cards-online.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-L01 Websites](../00-lists/s-f11-l01-websites.md)
