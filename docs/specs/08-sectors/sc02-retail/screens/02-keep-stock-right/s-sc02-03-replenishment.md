🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-02 Keep stock right](README.md) › 🖥️ S-SC02-03 Replenishment

# 🖥️ S-SC02-03 Replenishment

**Status:** 🔄 waiting for the owner

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Used to replenish stores from the warehouse
([UC-SC02-03](../../use-cases/02-keep-stock-right/uc-sc02-03-replenish-stores-from-the-warehouse.md)).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-02 step 1, U23 | desktop | ![FL-SC02-02 step 1, U23, light](../../images/02-keep-stock-right/u23-store-manager/1-replenishment-desktop-light.png) | ![FL-SC02-02 step 1, U23, dark](../../images/02-keep-stock-right/u23-store-manager/1-replenishment-desktop-dark.png) |
| FL-SC02-02 step 1, U23 | phone | ![FL-SC02-02 step 1, U23, light](../../images/02-keep-stock-right/u23-store-manager/1-replenishment-phone-light.png) | ![FL-SC02-02 step 1, U23, dark](../../images/02-keep-stock-right/u23-store-manager/1-replenishment-phone-dark.png) |
| FL-SC02-02 step 1, U23 | tablet | ![FL-SC02-02 step 1, U23, light](../../images/02-keep-stock-right/u23-store-manager/1-replenishment-tablet-light.png) | ![FL-SC02-02 step 1, U23, dark](../../images/02-keep-stock-right/u23-store-manager/1-replenishment-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-03-replenishment-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-03-replenishment-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-03-replenishment-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-03-replenishment-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-03-replenishment-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-03-replenishment-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-03-replenishment-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-03-replenishment-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-05 Replenishment rule](../../data/e-sc02-05-replenishment-rule.md), shown as the entity pages list
them, with their examples.

## Actions

- Review proposals: [UC-SC02-03](../../use-cases/02-keep-stock-right/uc-sc02-03-replenish-stores-from-the-warehouse.md),
  step 1.
- Confirm: [UC-SC02-03](../../use-cases/02-keep-stock-right/uc-sc02-03-replenish-stores-from-the-warehouse.md), step 2.
- Pick and ship: [UC-SC02-03](../../use-cases/02-keep-stock-right/uc-sc02-03-replenish-stores-from-the-warehouse.md),
  step 3.
- Receive in store: [UC-SC02-03](../../use-cases/02-keep-stock-right/uc-sc02-03-replenish-stores-from-the-warehouse.md),
  step 4.

## States

- Normal: the proposals per store and product with stock, minimum, maximum, sales and quantity.
- Empty: "Nothing to replenish".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the warehouse is short: a partial delivery is shown and the rest
  stays proposed.
- Read-only: a confirmed proposal is read-only.
- Offline: not available offline: back-office work on stock and sales shared by all stores. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC02-02 Keep stock right](../../flows/fl-sc02-02-keep-stock-right.md)

## Open questions

None.

---

⬅️ [S-SC02-02 Collections](../01-set-up-the-stores/s-sc02-02-collections.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-04 Transfers](s-sc02-04-transfers.md)
