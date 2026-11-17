🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-08 Product content and listings](README.md) › 🖥️ S-F11-25 Product safety

# 🖥️ S-F11-25 Product safety

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)
- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Record each product's manufacturer, EU responsible person, identifiers and warnings.

## Entry points

A product › Safety.

## Wireframe

```text
+------------------------------------------------------------------+
| Toy truck T-12   Safety information                               |
| Manufacturer    [Toys SA, Lyon]                                    |
| EU responsible  [Toys SA, Lyon]                                    |
| Identifiers     model [T-12] batch [on product]                    |
| Warnings  fr [Ne convient pas aux moins de 3 ans] en [Not for...]  |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-08 step 2, U04 | desktop | ![FL-F11-08 step 2, U04, light](../../images/08-product-content-and-listings/u04-purchasing/2-product-safety-desktop-light.png) | ![FL-F11-08 step 2, U04, dark](../../images/08-product-content-and-listings/u04-purchasing/2-product-safety-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-25-product-safety-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-25-product-safety-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-25-product-safety-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-25-product-safety-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-25-product-safety-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-25-product-safety-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-25-product-safety-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-25-product-safety-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Manufacturer, EU person, identifiers, warnings | E-F11-20 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Save | marketing, purchasing | Listing allowed |

## States

- Normal: record each product's manufacturer, EU responsible person, identifiers and warnings.
- Empty: nothing recorded: "The listing waits for its safety information".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a recalled product.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F11-03 Online product](../../data/e-f11-03-online-product.md),
[E-F11-20 Product safety information](../../data/e-f11-20-product-safety-information.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-03 Online product | New | Badge "New"; a new record starts here; next: Published (UC-F11-02); fields editable within the role | U04 | `u04-purchasing/s-f11-25-product-safety-e-f11-03-online-product-new-desktop-{light,dark}.png` |
| E-F11-03 Online product | Published | Badge "Published"; next: Delivered (UC-F11-13); fields editable within the role | U04 | `u04-purchasing/s-f11-25-product-safety-e-f11-03-online-product-published-desktop-{light,dark}.png` |
| E-F11-03 Online product | Delivered | Badge "Delivered"; next: Complete (UC-F11-23); fields editable within the role | U04 | `u04-purchasing/s-f11-25-product-safety-e-f11-03-online-product-delivered-desktop-{light,dark}.png` |
| E-F11-20 Product safety information | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04 | `u04-purchasing/s-f11-25-product-safety-e-f11-20-product-safety-information-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F11-08 Product content and listings](../../flows/fl-f11-08-product-content-and-listings.md)

## Open questions

None.

---

⬅️ [S-F11-24 Product feeds](s-f11-24-product-feeds.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-26 Pre-order](../09-pre-orders-and-b2b-buying/s-f11-26-pre-order.md)
