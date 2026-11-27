🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-02 Keep stock right](README.md) › 🖥️ S-SC02-07 Store count

# 🖥️ S-SC02-07 Store count

**Status:** 🔄 waiting for the owner

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)

## Purpose

Used to count stock in store ([UC-SC02-07](../../use-cases/02-keep-stock-right/uc-sc02-07-count-stock-in-store.md)).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-02 step 3, U23 | desktop | ![FL-SC02-02 step 3, U23, light](../../images/02-keep-stock-right/u23-store-manager/3-count-desktop-light.png) | ![FL-SC02-02 step 3, U23, dark](../../images/02-keep-stock-right/u23-store-manager/3-count-desktop-dark.png) |
| FL-SC02-02 step 3, U23 | phone | ![FL-SC02-02 step 3, U23, light](../../images/02-keep-stock-right/u23-store-manager/3-count-phone-light.png) | ![FL-SC02-02 step 3, U23, dark](../../images/02-keep-stock-right/u23-store-manager/3-count-phone-dark.png) |
| FL-SC02-02 step 3, U23 | tablet | ![FL-SC02-02 step 3, U23, light](../../images/02-keep-stock-right/u23-store-manager/3-count-tablet-light.png) | ![FL-SC02-02 step 3, U23, dark](../../images/02-keep-stock-right/u23-store-manager/3-count-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-07-store-count-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-07-store-count-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-07-store-count-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-07-store-count-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-07-store-count-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-07-store-count-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-07-store-count-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-07-store-count-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-01 Store](../../data/e-sc02-01-store.md), shown as the entity pages list them, with their
examples.

## Actions

- Choose the area: [UC-SC02-07](../../use-cases/02-keep-stock-right/uc-sc02-07-count-stock-in-store.md), step 1.
- Scan: [UC-SC02-07](../../use-cases/02-keep-stock-right/uc-sc02-07-count-stock-in-store.md), step 2.
- Validate differences: [UC-SC02-07](../../use-cases/02-keep-stock-right/uc-sc02-07-count-stock-in-store.md), step 3.
- Plan the next area: [UC-SC02-07](../../use-cases/02-keep-stock-right/uc-sc02-07-count-stock-in-store.md), step 4.

## States

- Normal: the count's area, the expected and counted quantities and the differences.
- Empty: "No count open", with New count.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a big difference: a recount of that product is asked before
  validation.
- Read-only: a closed count is read-only.
- Offline: scans are kept on the phone and sync in order when the network is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

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

⬅️ [S-SC02-06 Sales periods](../01-set-up-the-stores/s-sc02-06-sales-periods.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-08 Cross-channel orders](../03-sell-and-return-across-channels/s-sc02-08-cross-channel-orders.md)
