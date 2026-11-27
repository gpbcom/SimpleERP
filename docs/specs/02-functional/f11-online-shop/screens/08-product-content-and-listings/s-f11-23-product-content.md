🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-08 Product content and listings](README.md) › 🖥️ S-F11-23 Product content

# 🖥️ S-F11-23 Product content

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)
- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Complete each product's attributes, media and texts per channel and language.

## Entry points

Shop › Product content.

## Wireframe

```text
+------------------------------------------------------------------+
| Navy coat   Shop 100 %   Marketplace 90 %   B2B 100 %   Feed 95 % |
| Attributes  material [wool 80 %]  care code [   ] (marketplace)    |
| Media       6 images  [+]                                          |
| Texts       [fr] [en draft]  [Draft with the assistant]            |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-08 step 1, U12 | desktop | ![FL-F11-08 step 1, U12, light](../../images/08-product-content-and-listings/u12-marketing/1-product-content-desktop-light.png) | ![FL-F11-08 step 1, U12, dark](../../images/08-product-content-and-listings/u12-marketing/1-product-content-desktop-dark.png) |
| FL-F11-08 step 1, U12 | phone | ![FL-F11-08 step 1, U12, light](../../images/08-product-content-and-listings/u12-marketing/1-product-content-phone-light.png) | ![FL-F11-08 step 1, U12, dark](../../images/08-product-content-and-listings/u12-marketing/1-product-content-phone-dark.png) |
| Error E1, U12 | desktop | ![Error E1, U12, light](../../images/08-product-content-and-listings/u12-marketing/e1-product-content-refused-desktop-light.png) | ![Error E1, U12, dark](../../images/08-product-content-and-listings/u12-marketing/e1-product-content-refused-desktop-dark.png) |
| Error E1, U12 | phone | ![Error E1, U12, light](../../images/08-product-content-and-listings/u12-marketing/e1-product-content-refused-phone-light.png) | ![Error E1, U12, dark](../../images/08-product-content-and-listings/u12-marketing/e1-product-content-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-23-product-content-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-23-product-content-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-23-product-content-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-23-product-content-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-23-product-content-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-23-product-content-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-23-product-content-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-23-product-content-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Attributes, media, texts, completeness | E-F11-18 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Draft | marketing | Text drafted |
| Publish | marketing | On complete channels |

## States

- Normal: complete each product's attributes, media and texts per channel and language.
- Empty: no product content yet: "Pick a product".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for buyers: read.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F11-03 Online product](../../data/e-f11-03-online-product.md),
[E-F11-18 Product content](../../data/e-f11-18-product-content.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-03 Online product | New | Badge "New"; a new record starts here; next: Published (UC-F11-02); fields editable within the role | U12 | `u12-marketing/s-f11-23-product-content-e-f11-03-online-product-new-{desktop,phone}-{light,dark}.png` |
| E-F11-03 Online product | Published | Badge "Published"; next: Delivered (UC-F11-13); fields editable within the role | U12 | `u12-marketing/s-f11-23-product-content-e-f11-03-online-product-published-{desktop,phone}-{light,dark}.png` |
| E-F11-03 Online product | Delivered | Badge "Delivered"; next: Complete (UC-F11-23); fields editable within the role | U12 | `u12-marketing/s-f11-23-product-content-e-f11-03-online-product-delivered-{desktop,phone}-{light,dark}.png` |
| E-F11-03 Online product | Complete | Badge "Complete"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f11-23-product-content-e-f11-03-online-product-complete-{desktop,phone}-{light,dark}.png` |
| E-F11-18 Product content | Draft | Badge "Draft"; a new record starts here; next: Complete (UC-F11-23); fields editable within the role | U12 | `u12-marketing/s-f11-23-product-content-e-f11-18-product-content-draft-{desktop,phone}-{light,dark}.png` |
| E-F11-18 Product content | Complete | Badge "Complete"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f11-23-product-content-e-f11-18-product-content-complete-{desktop,phone}-{light,dark}.png` |

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
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F11-08 Product content and listings](../../flows/fl-f11-08-product-content-and-listings.md)

## Open questions

None.

---

⬅️ [S-F11-22 Chargebacks](../07-payment-risk/s-f11-22-chargebacks.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-24 Product feeds](s-f11-24-product-feeds.md)
