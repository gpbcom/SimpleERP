🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F11-11](README.md) ›
🖥️ S-F11-30 Wishlists

# 🖥️ S-F11-30 Wishlists

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): their wishlists and the comparison, on a phone.

## Purpose

Keep wishlists, compare products and share a list on purpose.

## Entry points

The heart on a product; My account › Wishlists; Compare on a product list.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Wishlists                          Birthday (private)         [Share] [Archive] [New list]  |
| ------------------------------------------------------------------------------------------- |
| PRODUCT          PRICE    STOCK        ALERT          COMPARE                               |
| Red kettle       39.90    In stock     Price drop     [x]       [To cart] [Remove]          |
| Toaster 2 slots  29.00    Sold out     Back in stock  [x]       [To cart] [Remove]          |
| Filter coffee    89.00    In stock     -              [x]       [To cart] [Remove]          |
| [Compare 3 products]        Shared link: not shared                                         |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f11-30-wishlists-empty-desktop-{light,dark}.png`,
`s-f11-30-wishlists-empty-phone-{light,dark}.png`, `s-f11-30-wishlists-loading-desktop-{light,dark}.png`,
`s-f11-30-wishlists-loading-phone-{light,dark}.png`, `s-f11-30-wishlists-offline-desktop-{light,dark}.png`,
`s-f11-30-wishlists-offline-phone-{light,dark}.png`, `s-f11-30-wishlists-read-only-desktop-{light,dark}.png`,
`s-f11-30-wishlists-read-only-phone-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-11 step 2, U09 | phone | ![FL-F11-11 step 2, U09, light](../../images/11-donations-gift-cards-and-cross-border/u09-customer/2-wishlists-phone-light.png) | ![FL-F11-11 step 2, U09, dark](../../images/11-donations-gift-cards-and-cross-border/u09-customer/2-wishlists-phone-dark.png) |
| FL-F11-11 step 2, U09 | phone | ![FL-F11-11 step 2, U09, light](../../images/11-donations-gift-cards-and-cross-border/u09-customer/2-wishlists-phone-light.png) | ![FL-F11-11 step 2, U09, dark](../../images/11-donations-gift-cards-and-cross-border/u09-customer/2-wishlists-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f11-30-wishlists-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f11-30-wishlists-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f11-30-wishlists-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f11-30-wishlists-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f11-30-wishlists-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f11-30-wishlists-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-30-wishlists-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-30-wishlists-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| List | E-F11-25 name and state | text and badge | name | yes |
| Product and price | E-F11-03 product and price | text and money | no | yes |
| Stock and alert | E-F11-03 stock, E-F11-25 alerts | text and choice | alert | no |
| Compare | selection | check box, up to 4 | yes | no |
| Share link | E-F11-25 share link | address | create or stop | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add | heart | the shopper | the product joins the list (UC-F11-31) |
| Compare | list | the shopper | a table of up to 4 products opens |
| To cart | row | the shopper | the product is moved to the cart |
| Share, Stop sharing | header | the shopper | the link is created or stops working |
| Archive | header | the shopper | the list is archived |

## States

- Normal: the shopper's lists, the products with price, stock and alert, and the comparison table.
- Empty: No wishlist yet: a hint to tap the heart on a product.
- Loading: The products as placeholders, then the stock.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a fifth product
  to compare is refused with the limit.
- Read-only: an archived list or a shared list read by someone else: shown, with no action but To cart for a guest to
  add to their own cart.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F11-25 Wishlist](../../data/e-f11-25-wishlist.md),
[E-F11-03 Online product](../../data/e-f11-03-online-product.md),
[E-F11-09 Customer account](../../data/e-f11-09-customer-account.md), [E-F11-04 Cart](../../data/e-f11-04-cart.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-25 Wishlist | Private | Badge "Private"; a new record starts here; next: Shared or Archived (BR-F11-26, UC-F11-31); fields editable within the role | U09 | `u09-customer/s-f11-30-wishlists-e-f11-25-wishlist-private-phone-{light,dark}.png` |
| E-F11-25 Wishlist | Shared | Badge "Shared"; next: Private or Archived (BR-F11-26, UC-F11-31); fields editable within the role | U09 | `u09-customer/s-f11-30-wishlists-e-f11-25-wishlist-shared-phone-{light,dark}.png` |
| E-F11-25 Wishlist | Archived | Badge "Archived"; final state, read-only | U09 | `u09-customer/s-f11-30-wishlists-e-f11-25-wishlist-archived-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

On a phone, the list is a stack of product cards with the comparison as a swipeable table.

## Accessibility

The heart is a labelled button; the comparison table has row and column headers; keyboard: next product, add, compare.

## Components

- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)

## Shown in

- [FL-F11-11 Donations, wishlists, gift cards and cross-border](../../flows/fl-f11-11-donations-gift-cards-and-cross-border.md)

## Open questions

None.

---

⬅️ [S-F11-29 Checkout donations](s-f11-29-checkout-donations.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-31 Gift cards online](s-f11-31-gift-cards-online.md)
