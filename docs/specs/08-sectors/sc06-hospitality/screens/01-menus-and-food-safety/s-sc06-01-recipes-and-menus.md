🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-01 Menus and food safety](README.md) › 🖥️ S-SC06-01 Recipes and menus

# 🖥️ S-SC06-01 Recipes and menus

**Status:** 🔄 waiting for the owner

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md)

## Purpose

Used to cost recipes and build menus
([UC-SC06-01](../../use-cases/01-menus-and-food-safety/uc-sc06-01-cost-recipes-and-build-menus.md)).

## Entry points

Restaurant and hospitality in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-01 step 1, U23 | desktop | ![FL-SC06-01 step 1, U23, light](../../images/01-menus-and-food-safety/u23-store-manager/1-recipe-desktop-light.png) | ![FL-SC06-01 step 1, U23, dark](../../images/01-menus-and-food-safety/u23-store-manager/1-recipe-desktop-dark.png) |
| FL-SC06-01 step 1, U23 | phone | ![FL-SC06-01 step 1, U23, light](../../images/01-menus-and-food-safety/u23-store-manager/1-recipe-phone-light.png) | ![FL-SC06-01 step 1, U23, dark](../../images/01-menus-and-food-safety/u23-store-manager/1-recipe-phone-dark.png) |
| FL-SC06-01 step 1, U23 | tablet | ![FL-SC06-01 step 1, U23, light](../../images/01-menus-and-food-safety/u23-store-manager/1-recipe-tablet-light.png) | ![FL-SC06-01 step 1, U23, dark](../../images/01-menus-and-food-safety/u23-store-manager/1-recipe-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-01-recipes-and-menus-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-01-recipes-and-menus-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-01-recipes-and-menus-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-01-recipes-and-menus-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-01-recipes-and-menus-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-01-recipes-and-menus-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc06-01-recipes-and-menus-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc06-01-recipes-and-menus-offline-phone-dark.png) |

## Fields and columns

The fields of [E-F12-25 Recipe](../../../../02-functional/f12-manufacturing/data/e-f12-25-recipe.md),
[E-SC06-02 Menu dish](../../data/e-sc06-02-menu-dish.md),
[E-F12-25 Recipe](../../../../02-functional/f12-manufacturing/data/e-f12-25-recipe.md), shown as the entity pages list
them, with their examples.

## Actions

- Write the recipe: [UC-SC06-01](../../use-cases/01-menus-and-food-safety/uc-sc06-01-cost-recipes-and-build-menus.md),
  step 1.
- See its cost: [UC-SC06-01](../../use-cases/01-menus-and-food-safety/uc-sc06-01-cost-recipes-and-build-menus.md), step
  2.
- Put it on a menu: [UC-SC06-01](../../use-cases/01-menus-and-food-safety/uc-sc06-01-cost-recipes-and-build-menus.md),
  step 3.
- Publish to the tills:
  [UC-SC06-01](../../use-cases/01-menus-and-food-safety/uc-sc06-01-cost-recipes-and-build-menus.md), step 4.

## States

- Normal: the recipe's ingredients, yield, cost per portion, and menus with price and food-cost ratio.
- Empty: "No recipe yet", with New recipe.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an ingredient without a price: the cost is marked partial and the
  ingredient named.
- Read-only: kitchen staff read costs only if their role allows.
- Offline: not available offline: front-office and back-office work on live bookings and shared figures. Offline work is
  kept for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC06-02 Menu dish](../../data/e-sc06-02-menu-dish.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-02 Menu dish | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U19, U23 | `u19-kitchen-staff/s-sc06-01-recipes-and-menus-e-sc06-02-menu-dish-active-desktop-{light,dark}.png`, `u23-store-manager/s-sc06-01-recipes-and-menus-e-sc06-02-menu-dish-active-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC06-01 Menus and food safety](../../flows/fl-sc06-01-menus-and-food-safety.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC06-02 Allergens](s-sc06-02-allergens.md)
