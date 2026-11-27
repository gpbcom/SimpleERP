🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-13 Energy, passport and work in progress](README.md) › 🖥️ S-F12-29 Product passport

# 🖥️ S-F12-29 Product passport

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Build and publish a product's digital passport.

## Entry points

Quality › Product passport; the QR code for customers.

## Wireframe

```text
+------------------------------------------------------------------+
| Passport Bracket B-20  v2                     [Publish QR]        |
| Materials   steel 98 %, zinc 2 %      source: BOM                 |
| Substances  none above threshold      source: compliance file     |
| Energy      0.9 kWh/unit              source: meter               |
| Repair      [                    ]    missing                     |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-13 step 2, U27 | desktop | ![FL-F12-13 step 2, U27, light](../../images/13-energy-passport-and-work-in-progress/u27-quality-manager/2-product-passport-desktop-light.png) | ![FL-F12-13 step 2, U27, dark](../../images/13-energy-passport-and-work-in-progress/u27-quality-manager/2-product-passport-desktop-dark.png) |
| FL-F12-13 step 2, U27 | tablet | ![FL-F12-13 step 2, U27, light](../../images/13-energy-passport-and-work-in-progress/u27-quality-manager/2-product-passport-tablet-light.png) | ![FL-F12-13 step 2, U27, dark](../../images/13-energy-passport-and-work-in-progress/u27-quality-manager/2-product-passport-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-29-product-passport-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-29-product-passport-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-29-product-passport-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-29-product-passport-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-29-product-passport-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-29-product-passport-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-f12-29-product-passport-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-f12-29-product-passport-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Fields, sources | E-F12-24 | missing fields |

## Actions

| Action | Who | Result |
|---|---|---|
| Publish | quality manager | QR live |

## States

- Normal: build and publish a product's digital passport.
- Empty: no passport yet: Build from the product's records.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: published versions; customers read.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F12-24 Product passport](../../data/e-f12-24-product-passport.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-24 Product passport | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F12-30); fields editable within the role | U27 | `u27-quality-manager/s-f12-29-product-passport-e-f12-24-product-passport-draft-{desktop,tablet}-{light,dark}.png` |
| E-F12-24 Product passport | Published | Badge "Published"; next: Superseded (UC-F12-30); fields editable within the role | U27 | `u27-quality-manager/s-f12-29-product-passport-e-f12-24-product-passport-published-{desktop,tablet}-{light,dark}.png` |
| E-F12-24 Product passport | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U27 | `u27-quality-manager/s-f12-29-product-passport-e-f12-24-product-passport-superseded-{desktop,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the public page on a phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F12-13 Energy, passport and work in progress](../../flows/fl-f12-13-energy-passport-and-work-in-progress.md)

## Open questions

None.

---

⬅️ [S-F12-28 Energy](s-f12-28-energy.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-30 Recipe and batch](../09-recipes-and-batches/s-f12-30-recipe-and-batch.md)
