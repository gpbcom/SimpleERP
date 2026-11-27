🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-01 Set up the stores](README.md) › 🖥️ S-SC02-02 Collections

# 🖥️ S-SC02-02 Collections

**Status:** 🔄 waiting for the owner

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Purpose

Used to manage size and colour grids and seasons,
[UC-SC02-02](../../use-cases/01-set-up-the-stores/uc-sc02-02-manage-size-and-colour-grids-and-seasons.md).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-01 step 2, U23 | desktop | ![FL-SC02-01 step 2, U23, light](../../images/01-set-up-the-stores/u23-store-manager/2-grids-and-seasons-desktop-light.png) | ![FL-SC02-01 step 2, U23, dark](../../images/01-set-up-the-stores/u23-store-manager/2-grids-and-seasons-desktop-dark.png) |
| FL-SC02-01 step 2, U23 | phone | ![FL-SC02-01 step 2, U23, light](../../images/01-set-up-the-stores/u23-store-manager/2-grids-and-seasons-phone-light.png) | ![FL-SC02-01 step 2, U23, dark](../../images/01-set-up-the-stores/u23-store-manager/2-grids-and-seasons-phone-dark.png) |
| FL-SC02-01 step 2, U23 | tablet | ![FL-SC02-01 step 2, U23, light](../../images/01-set-up-the-stores/u23-store-manager/2-grids-and-seasons-tablet-light.png) | ![FL-SC02-01 step 2, U23, dark](../../images/01-set-up-the-stores/u23-store-manager/2-grids-and-seasons-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-02-collections-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-02-collections-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-02-collections-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-02-collections-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-02-collections-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-02-collections-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-02-collections-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-02-collections-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-03 Product grid](../../data/e-sc02-03-product-grid.md),
[E-SC02-04 Season](../../data/e-sc02-04-season.md), shown as the entity pages list them, with their examples.

## Actions

- Create the grid:
  [UC-SC02-02](../../use-cases/01-set-up-the-stores/uc-sc02-02-manage-size-and-colour-grids-and-seasons.md), step 1.
- Attach to the season:
  [UC-SC02-02](../../use-cases/01-set-up-the-stores/uc-sc02-02-manage-size-and-colour-grids-and-seasons.md), step 2.
- Order by grid:
  [UC-SC02-02](../../use-cases/01-set-up-the-stores/uc-sc02-02-manage-size-and-colour-grids-and-seasons.md), step 3.
- Start the season:
  [UC-SC02-02](../../use-cases/01-set-up-the-stores/uc-sc02-02-manage-size-and-colour-grids-and-seasons.md), step 4.

## States

- Normal: the product's grid of sizes and colours, each variant with its barcode and stock, and the season.
- Empty: "No grid yet", with New grid.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a size missing from the grid: the order line is refused with the
  grid's sizes.
- Read-only: a season that ended is read-only.
- Offline: not available offline: back-office work on stock and sales shared by all stores. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC02-04 Season](../../data/e-sc02-04-season.md),
[E-SC02-03 Product grid](../../data/e-sc02-03-product-grid.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC02-04 Season | Planned | Badge "Planned"; a new record starts here; next: Selling (UC-SC02-02); fields editable within the role | U12, U23 | `u12-marketing/s-sc02-02-collections-e-sc02-04-season-planned-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-sc02-02-collections-e-sc02-04-season-planned-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-04 Season | Selling | Badge "Selling"; next: Clearing (UC-SC02-02); fields editable within the role | U12, U23 | `u12-marketing/s-sc02-02-collections-e-sc02-04-season-selling-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-sc02-02-collections-e-sc02-04-season-selling-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-03 Product grid | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U12, U23 | `u12-marketing/s-sc02-02-collections-e-sc02-03-product-grid-active-{desktop,phone}-{light,dark}.png`, `u23-store-manager/s-sc02-02-collections-e-sc02-03-product-grid-active-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC02-01 Set up the stores](../../flows/fl-sc02-01-set-up-the-stores.md)

## Open questions

None.

---

⬅️ [S-SC02-01 Stores](s-sc02-01-stores.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-03 Replenishment](../02-keep-stock-right/s-sc02-03-replenishment.md)
