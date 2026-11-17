🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-08 Product content and listings](README.md) › 🖥️ S-F11-24 Product feeds

# 🖥️ S-F11-24 Product feeds

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Purpose

Set and follow product feeds to comparators.

## Entry points

Shop › Feeds.

## Wireframe

```text
+------------------------------------------------------------------+
| Feeds                                            [+ Feed]         |
| Destination          Products  Last refresh  Refused             |
| Google Shopping FR   1,240     11-12 06:00   12 (GTIN)  [See]    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-08 step 3, U12 | desktop | ![FL-F11-08 step 3, U12, light](../../images/08-product-content-and-listings/u12-marketing/3-product-feeds-desktop-light.png) | ![FL-F11-08 step 3, U12, dark](../../images/08-product-content-and-listings/u12-marketing/3-product-feeds-desktop-dark.png) |
| FL-F11-08 step 3, U12 | phone | ![FL-F11-08 step 3, U12, light](../../images/08-product-content-and-listings/u12-marketing/3-product-feeds-phone-light.png) | ![FL-F11-08 step 3, U12, dark](../../images/08-product-content-and-listings/u12-marketing/3-product-feeds-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-24-product-feeds-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-24-product-feeds-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-24-product-feeds-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-24-product-feeds-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-24-product-feeds-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-24-product-feeds-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-24-product-feeds-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-24-product-feeds-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Destination, products, refresh, refused | E-F11-19 | settings |

## Actions

| Action | Who | Result |
|---|---|---|
| Create | marketing | Feed published |

## States

- Normal: set and follow product feeds to comparators.
- Empty: no feed: Add a feed.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: paused feeds.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F11-19 Product feed](../../data/e-f11-19-product-feed.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-19 Product feed | Active | Badge "Active"; a new record starts here; next: Paused (UC-F11-24); fields editable within the role | U12 | `u12-marketing/s-f11-24-product-feeds-e-f11-19-product-feed-active-{desktop,phone}-{light,dark}.png` |
| E-F11-19 Product feed | Paused | Badge "Paused"; next: Active (UC-F11-24); fields editable within the role | U12 | `u12-marketing/s-f11-24-product-feeds-e-f11-19-product-feed-paused-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F11-08 Product content and listings](../../flows/fl-f11-08-product-content-and-listings.md)

## Open questions

None.

---

⬅️ [S-F11-23 Product content](s-f11-23-product-content.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-25 Product safety](s-f11-25-product-safety.md)
