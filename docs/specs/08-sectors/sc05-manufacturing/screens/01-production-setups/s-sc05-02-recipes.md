🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-01 Production setups](README.md) › 🖥️ S-SC05-02 Recipes

# 🖥️ S-SC05-02 Recipes

**Status:** 🔄 waiting for the owner

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Used to manage recipes with potency, yields and batch scaling,
[UC-SC05-02](../../use-cases/01-production-setups/uc-sc05-02-manage-recipes-with-potency-yields-and-batch-scaling.md).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-01 step 2, U21 | desktop | ![FL-SC05-01 step 2, U21, light](../../images/01-production-setups/u21-production-planner/2-recipe-desktop-light.png) | ![FL-SC05-01 step 2, U21, dark](../../images/01-production-setups/u21-production-planner/2-recipe-desktop-dark.png) |
| FL-SC05-01 step 2, U21 | phone | ![FL-SC05-01 step 2, U21, light](../../images/01-production-setups/u21-production-planner/2-recipe-phone-light.png) | ![FL-SC05-01 step 2, U21, dark](../../images/01-production-setups/u21-production-planner/2-recipe-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-02-recipes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-02-recipes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-02-recipes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-02-recipes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-02-recipes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-02-recipes-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc05-02-recipes-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc05-02-recipes-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC05-02 Batch recipe](../../data/e-sc05-02-batch-recipe.md),
[E-F12-25 Recipe](../../../../02-functional/f12-manufacturing/data/e-f12-25-recipe.md), shown as the entity pages list
them, with their examples.

## Actions

- Write the recipe:
  [UC-SC05-02](../../use-cases/01-production-setups/uc-sc05-02-manage-recipes-with-potency-yields-and-batch-scaling.md),
  step 1.
- Set potencies:
  [UC-SC05-02](../../use-cases/01-production-setups/uc-sc05-02-manage-recipes-with-potency-yields-and-batch-scaling.md),
  step 2.
- Scale to the batch:
  [UC-SC05-02](../../use-cases/01-production-setups/uc-sc05-02-manage-recipes-with-potency-yields-and-batch-scaling.md),
  step 3.
- Record the yield:
  [UC-SC05-02](../../use-cases/01-production-setups/uc-sc05-02-manage-recipes-with-potency-yields-and-batch-scaling.md),
  step 4.

## States

- Normal: the recipe's ingredients with nominal and measured potency, tolerances, batch size, scaled quantities and
  yields.
- Empty: "No recipe yet", with New recipe.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a lot without a measured potency: the nominal potency is used and
  the batch flagged.
- Read-only: an approved version is read-only.
- Offline: the shop-floor tablet keeps working without the network,
  [UC-F12-26](../../../../02-functional/f12-manufacturing/use-cases/11-finite-schedule-and-the-tablet/uc-f12-26-keep-working-on-the-tablet-without-the-network.md),
  yields recorded at the line sync in order when it is back,
  [BR-F12-21](../../../../02-functional/f12-manufacturing/business-rules/br-f12-21-tablet-records-sync-in-order.md).

Shown entities (VD-15): [E-SC05-02 Batch recipe](../../data/e-sc05-02-batch-recipe.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-02 Batch recipe | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U20, U21 | `u20-production-operator/s-sc05-02-recipes-e-sc05-02-batch-recipe-active-tablet-{light,dark}.png`, `u21-production-planner/s-sc05-02-recipes-e-sc05-02-batch-recipe-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC05-01 Production setups](../../flows/fl-sc05-01-production-setups.md)

## Open questions

None.

---

⬅️ [S-SC05-01 Production setup](s-sc05-01-production-setup.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-03 Configurator](../02-made-to-order/s-sc05-03-configurator.md)
