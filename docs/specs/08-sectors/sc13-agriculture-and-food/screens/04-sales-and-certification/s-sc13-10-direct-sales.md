🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-04 Sales and certification](README.md) › 🖥️ S-SC13-10 Direct sales

# 🖥️ S-SC13-10 Direct sales

**Status:** ✅ specified

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to sell directly ([UC-SC13-10](../../use-cases/04-sales-and-certification/uc-sc13-10-sell-directly.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-04 step 1, U40 | desktop | ![FL-SC13-04 step 1, U40, light](../../images/04-sales-and-certification/u40-farmer/1-direct-desktop-light.png) | ![FL-SC13-04 step 1, U40, dark](../../images/04-sales-and-certification/u40-farmer/1-direct-desktop-dark.png) |
| FL-SC13-04 step 1, U40 | phone | ![FL-SC13-04 step 1, U40, light](../../images/04-sales-and-certification/u40-farmer/1-direct-phone-light.png) | ![FL-SC13-04 step 1, U40, dark](../../images/04-sales-and-certification/u40-farmer/1-direct-phone-dark.png) |
| Error E1, U40 | desktop | ![Error E1, U40, light](../../images/04-sales-and-certification/u40-farmer/e1-lot-blocked-desktop-light.png) | ![Error E1, U40, dark](../../images/04-sales-and-certification/u40-farmer/e1-lot-blocked-desktop-dark.png) |
| Error E1, U40 | phone | ![Error E1, U40, light](../../images/04-sales-and-certification/u40-farmer/e1-lot-blocked-phone-light.png) | ![Error E1, U40, dark](../../images/04-sales-and-certification/u40-farmer/e1-lot-blocked-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-10-direct-sales-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-10-direct-sales-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-10-direct-sales-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-10-direct-sales-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-10-direct-sales-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-10-direct-sales-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-10-direct-sales-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-10-direct-sales-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-09 Direct sale](../../data/e-sc13-09-direct-sale.md), shown as the entity pages list them, with
their examples.

## Actions

- Prepare products: [UC-SC13-10](../../use-cases/04-sales-and-certification/uc-sc13-10-sell-directly.md), step 1.
- Buy: [UC-SC13-10](../../use-cases/04-sales-and-certification/uc-sc13-10-sell-directly.md), step 2.
- Record lots sold: [UC-SC13-10](../../use-cases/04-sales-and-certification/uc-sc13-10-sell-directly.md), step 3.
- Close the day: [UC-SC13-10](../../use-cases/04-sales-and-certification/uc-sc13-10-sell-directly.md), step 4.

## States

- Normal: products, lots and sales by place.
- Empty: "No sale".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a lot blocked: it cannot be sold.
- Read-only: closed days are read-only.
- Offline: the till sells offline at markets,
  [UC-F10-14](../../../../02-functional/f10-point-of-sale/use-cases/06-mobile-and-delivery/uc-f10-14-sell-on-the-move-and-offline.md).

Shown entities (VD-15): [E-SC13-09 Direct sale](../../data/e-sc13-09-direct-sale.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-09 Direct sale | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U40 | `u09-customer/s-sc13-10-direct-sales-e-sc13-09-direct-sale-active-phone-{light,dark}.png`, `u40-farmer/s-sc13-10-direct-sales-e-sc13-09-direct-sale-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-04 Sales and certification](../../flows/fl-sc13-04-sales-and-certification.md)

## Open questions

None.

---

⬅️ [S-SC13-09 Seasonal work](../03-farm-business/s-sc13-09-seasonal-work.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-11 Cooperative](s-sc13-11-cooperative.md)
