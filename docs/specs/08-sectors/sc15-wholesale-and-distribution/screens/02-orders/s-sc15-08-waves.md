🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-02 Orders](README.md) › 🖥️ S-SC15-08 Waves

# 🖥️ S-SC15-08 Waves

**Status:** 🔄 waiting for the owner

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Used to take orders by EDI from retailers
([UC-SC15-04](../../use-cases/02-orders/uc-sc15-04-take-orders-by-edi-from-retailers.md)); to pick in waves and
cross-dock ([UC-SC15-08](../../use-cases/03-warehouse/uc-sc15-08-pick-in-waves-and-cross-dock.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-02 step 1, U15 | phone | ![FL-SC15-02 step 1, U15, light](../../images/02-orders/u15-warehouse-operator/1-edi-phone-light.png) | ![FL-SC15-02 step 1, U15, dark](../../images/02-orders/u15-warehouse-operator/1-edi-phone-dark.png) |
| FL-SC15-02 step 1, U15 | tablet | ![FL-SC15-02 step 1, U15, light](../../images/02-orders/u15-warehouse-operator/1-edi-tablet-light.png) | ![FL-SC15-02 step 1, U15, dark](../../images/02-orders/u15-warehouse-operator/1-edi-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc15-08-waves-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc15-08-waves-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc15-08-waves-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc15-08-waves-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc15-08-waves-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc15-08-waves-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-08-waves-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-08-waves-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md),
[E-SC15-05 Pick wave](../../data/e-sc15-05-pick-wave.md), shown as the entity pages list them, with their examples.

## Actions

- Release to picking: [UC-SC15-04](../../use-cases/02-orders/uc-sc15-04-take-orders-by-edi-from-retailers.md), step 4.
- Build waves: [UC-SC15-08](../../use-cases/03-warehouse/uc-sc15-08-pick-in-waves-and-cross-dock.md), step 1.
- Pick: [UC-SC15-08](../../use-cases/03-warehouse/uc-sc15-08-pick-in-waves-and-cross-dock.md), step 2.
- Cross-dock: [UC-SC15-08](../../use-cases/03-warehouse/uc-sc15-08-pick-in-waves-and-cross-dock.md), step 3.
- Close the wave: [UC-SC15-08](../../use-cases/03-warehouse/uc-sc15-08-pick-in-waves-and-cross-dock.md), step 4.

## States

- Normal: waves with orders, zones and pick progress.
- Empty: "No wave".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a price differs: the order is held.
- Read-only: closed waves are read-only.
- Offline: scans are kept on the scanner and sync later,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): [E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md),
[E-SC15-05 Pick wave](../../data/e-sc15-05-pick-wave.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-04 Sales order | Confirmed | Badge "Confirmed"; a new record starts here; next: Partly shipped or Held (BR-SC15-05, UC-SC15-04); fields editable within the role | U03, U15 | `u03-sales/s-sc15-08-waves-e-sc15-04-sales-order-confirmed-{desktop,phone,tablet}-{light,dark}.png`, `u15-warehouse-operator/s-sc15-08-waves-e-sc15-04-sales-order-confirmed-{phone,tablet}-{light,dark}.png` |
| E-SC15-04 Sales order | Held | Badge "Held"; next: Confirmed (UC-SC15-04); fields editable within the role | U03, U15 | `u03-sales/s-sc15-08-waves-e-sc15-04-sales-order-held-{desktop,phone,tablet}-{light,dark}.png`, `u15-warehouse-operator/s-sc15-08-waves-e-sc15-04-sales-order-held-{phone,tablet}-{light,dark}.png` |
| E-SC15-04 Sales order | Partly shipped | Badge "Partly shipped"; next: Shipped (UC-SC15-04); fields editable within the role | U15 | `u15-warehouse-operator/s-sc15-08-waves-e-sc15-04-sales-order-partly-shipped-{phone,tablet}-{light,dark}.png` |
| E-SC15-04 Sales order | Shipped | Badge "Shipped"; final: read-only, no next state; the history shows how it got here | U15 | `u15-warehouse-operator/s-sc15-08-waves-e-sc15-04-sales-order-shipped-{phone,tablet}-{light,dark}.png` |
| E-SC15-05 Pick wave | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U15 | `u15-warehouse-operator/s-sc15-08-waves-e-sc15-05-pick-wave-active-{phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC15-03 Warehouse](../../flows/fl-sc15-03-warehouse.md)

## Open questions

None.

---

⬅️ [S-SC15-07 Drop-shipping](s-sc15-07-drop-shipping.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-09 Pallets](../03-warehouse/s-sc15-09-pallets.md)
