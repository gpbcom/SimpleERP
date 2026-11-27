🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-05 Grow the shop](README.md) › 🖥️ S-F11-15 Reviews

# 🖥️ S-F11-15 Reviews

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Collect and moderate reviews.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-05 step 2, U12 | desktop | ![FL-F11-05 step 2, U12, light](../../images/05-grow-the-shop/u12-marketing/2-reviews-desktop-light.png) | ![FL-F11-05 step 2, U12, dark](../../images/05-grow-the-shop/u12-marketing/2-reviews-desktop-dark.png) |
| FL-F11-05 step 2, U12 | phone | ![FL-F11-05 step 2, U12, light](../../images/05-grow-the-shop/u12-marketing/2-reviews-phone-light.png) | ![FL-F11-05 step 2, U12, dark](../../images/05-grow-the-shop/u12-marketing/2-reviews-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-15-reviews-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-15-reviews-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-15-reviews-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-15-reviews-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-15-reviews-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-15-reviews-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-15-reviews-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-15-reviews-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Collect and moderate reviews, as the wireframe shows.
- Empty: No review yet, with Ask for reviews.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F11-10 Product review](../../data/e-f11-10-product-review.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-10 Product review | To check | Badge "To check"; a new record starts here; next: Published or Rejected (UC-F11-15, BR-F11-09); fields editable within the role | U09, U12 | `u09-customer/s-f11-15-reviews-e-f11-10-product-review-to-check-phone-{light,dark}.png`, `u12-marketing/s-f11-15-reviews-e-f11-10-product-review-to-check-{desktop,phone}-{light,dark}.png` |
| E-F11-10 Product review | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f11-15-reviews-e-f11-10-product-review-published-phone-{light,dark}.png`, `u12-marketing/s-f11-15-reviews-e-f11-10-product-review-published-{desktop,phone}-{light,dark}.png` |
| E-F11-10 Product review | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f11-15-reviews-e-f11-10-product-review-rejected-phone-{light,dark}.png`, `u12-marketing/s-f11-15-reviews-e-f11-10-product-review-rejected-{desktop,phone}-{light,dark}.png` |

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

- [FL-F11-05 Grow the shop](../../flows/fl-f11-05-grow-the-shop.md)

## Open questions

None.

---

⬅️ [S-F11-14 Cart reminders](s-f11-14-cart-reminders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-16 SEO and languages](../01-build-the-shop/s-f11-16-seo-and-languages.md)
