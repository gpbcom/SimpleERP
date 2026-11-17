🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-09 Recipes and batches](README.md) › 🖥️ S-F12-30 Recipe and batch

# 🖥️ S-F12-30 Recipe and batch

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md)
- [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md)

## Purpose

Define recipes and plan batches scaled to their size.

## Entry points

Manufacturing › Recipes.

## Wireframe

```text
+------------------------------------------------------------------+
| Recipe Tomme   for 100 L milk   yield 10 kg   best-before 120 d   |
| Ingredient   Qty     Tolerance   Allergen                          |
| Milk         100 L   -           milk                              |
| Rennet       25 ml   +-2 %       -                                 |
| Salt         1.8 kg  +-5 %       -                                 |
| Batch size [400 L] -> rennet 100 ml, salt 7.2 kg   [Plan batch]   |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-09 step 1, U21 | desktop | ![FL-F12-09 step 1, U21, light](../../images/09-recipes-and-batches/u21-production-planner/1-recipe-and-batch-desktop-light.png) | ![FL-F12-09 step 1, U21, dark](../../images/09-recipes-and-batches/u21-production-planner/1-recipe-and-batch-desktop-dark.png) |
| FL-F12-09 step 1, U21 | phone | ![FL-F12-09 step 1, U21, light](../../images/09-recipes-and-batches/u21-production-planner/1-recipe-and-batch-phone-light.png) | ![FL-F12-09 step 1, U21, dark](../../images/09-recipes-and-batches/u21-production-planner/1-recipe-and-batch-phone-dark.png) |
| Error E1, U21 | desktop | ![Error E1, U21, light](../../images/09-recipes-and-batches/u21-production-planner/e1-recipe-and-batch-refused-desktop-light.png) | ![Error E1, U21, dark](../../images/09-recipes-and-batches/u21-production-planner/e1-recipe-and-batch-refused-desktop-dark.png) |
| Error E1, U21 | phone | ![Error E1, U21, light](../../images/09-recipes-and-batches/u21-production-planner/e1-recipe-and-batch-refused-phone-light.png) | ![Error E1, U21, dark](../../images/09-recipes-and-batches/u21-production-planner/e1-recipe-and-batch-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-30-recipe-and-batch-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-30-recipe-and-batch-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-30-recipe-and-batch-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-30-recipe-and-batch-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-30-recipe-and-batch-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-30-recipe-and-batch-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-30-recipe-and-batch-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-30-recipe-and-batch-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Ingredients, tolerances, steps, yield | E-F12-25 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Plan batch | planner | Batch order scaled |

## States

- Normal: define recipes and plan batches scaled to their size.
- Empty: no recipe yet: Create a recipe.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: approved versions: copied to change.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F12-25 Recipe](../../data/e-f12-25-recipe.md),
[E-F12-04 Manufacturing order](../../data/e-f12-04-manufacturing-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-25 Recipe | Draft | Badge "Draft"; a new record starts here; next: Approved (BR-SC06-04); fields editable within the role | U21 | `u21-production-planner/s-f12-30-recipe-and-batch-e-f12-25-recipe-draft-{desktop,phone}-{light,dark}.png` |
| E-F12-25 Recipe | Approved | Badge "Approved"; next: Superseded (BR-SC06-04); fields editable within the role | U21 | `u21-production-planner/s-f12-30-recipe-and-batch-e-f12-25-recipe-approved-{desktop,phone}-{light,dark}.png` |
| E-F12-25 Recipe | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U21 | `u21-production-planner/s-f12-30-recipe-and-batch-e-f12-25-recipe-superseded-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | Draft | Badge "Draft"; a new record starts here; next: Confirmed or Cancelled (UC-F12-04, BR-F12-02); fields editable within the role | U21 | `u21-production-planner/s-f12-30-recipe-and-batch-e-f12-04-manufacturing-order-draft-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | Confirmed | Badge "Confirmed"; next: In progress or Cancelled (UC-F12-27, BR-F12-02); fields editable within the role | U21 | `u21-production-planner/s-f12-30-recipe-and-batch-e-f12-04-manufacturing-order-confirmed-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | In progress | Badge "In progress"; next: Done or Cancelled (UC-F12-04, BR-F12-02); fields editable within the role | U21 | `u21-production-planner/s-f12-30-recipe-and-batch-e-f12-04-manufacturing-order-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F12-04 Manufacturing order | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U21 | `u21-production-planner/s-f12-30-recipe-and-batch-e-f12-04-manufacturing-order-done-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; batches on the tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F12-09 Recipes and batches](../../flows/fl-f12-09-recipes-and-batches.md)

## Open questions

None.

---

⬅️ [S-F12-29 Product passport](../13-energy-passport-and-work-in-progress/s-f12-29-product-passport.md) ·
⬆️ [Up](README.md) · ➡️ [S-F12-31 CAD link](../14-cad-kanban-mps-and-tools/s-f12-31-cad-link.md)
