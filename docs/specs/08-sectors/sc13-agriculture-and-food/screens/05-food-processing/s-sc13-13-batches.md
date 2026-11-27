🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-05 Food processing](README.md) › 🖥️ S-SC13-13 Batches

# 🖥️ S-SC13-13 Batches

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)

## Purpose

Used to manage recipes and batches for processing,
[UC-SC13-13](../../use-cases/05-food-processing/uc-sc13-13-manage-recipes-and-batches-for-processing.md).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-05 step 1, U21 | desktop | ![FL-SC13-05 step 1, U21, light](../../images/05-food-processing/u21-production-planner/1-batch-desktop-light.png) | ![FL-SC13-05 step 1, U21, dark](../../images/05-food-processing/u21-production-planner/1-batch-desktop-dark.png) |
| FL-SC13-05 step 1, U21 | phone | ![FL-SC13-05 step 1, U21, light](../../images/05-food-processing/u21-production-planner/1-batch-phone-light.png) | ![FL-SC13-05 step 1, U21, dark](../../images/05-food-processing/u21-production-planner/1-batch-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-13-batches-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-13-batches-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-13-batches-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-13-batches-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-13-batches-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-13-batches-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-13-batches-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-13-batches-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-12 Batch](../../data/e-sc13-12-batch.md), [E-SC13-04 Lot](../../data/e-sc13-04-lot.md),
[E-F12-25 Recipe](../../../../02-functional/f12-manufacturing/data/e-f12-25-recipe.md), shown as the entity pages list
them, with their examples.

## Actions

- Set the recipe:
  [UC-SC13-13](../../use-cases/05-food-processing/uc-sc13-13-manage-recipes-and-batches-for-processing.md), step 1.
- Scale the batch:
  [UC-SC13-13](../../use-cases/05-food-processing/uc-sc13-13-manage-recipes-and-batches-for-processing.md), step 2.
- Record lots used:
  [UC-SC13-13](../../use-cases/05-food-processing/uc-sc13-13-manage-recipes-and-batches-for-processing.md), step 3.
- Output the lot:
  [UC-SC13-13](../../use-cases/05-food-processing/uc-sc13-13-manage-recipes-and-batches-for-processing.md), step 4.

## States

- Normal: recipes, batches, lots used and output lots.
- Empty: "No batch".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an ingredient lot blocked: it is refused.
- Read-only: closed batches are read-only.
- Offline: the processing tablet keeps working offline,
  [UC-F12-26](../../../../02-functional/f12-manufacturing/use-cases/11-finite-schedule-and-the-tablet/uc-f12-26-keep-working-on-the-tablet-without-the-network.md).

Shown entities (VD-15): [E-F12-25 Recipe](../../../../02-functional/f12-manufacturing/data/e-f12-25-recipe.md),
[E-SC13-12 Batch](../../data/e-sc13-12-batch.md), [E-SC13-04 Lot](../../data/e-sc13-04-lot.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-25 Recipe | Draft | Badge "Draft"; a new record starts here; next: Approved (BR-SC06-04); fields editable within the role | U20, U21, U40 | `u20-production-operator/s-sc13-13-batches-e-f12-25-recipe-draft-tablet-{light,dark}.png`, `u21-production-planner/s-sc13-13-batches-e-f12-25-recipe-draft-{desktop,phone}-{light,dark}.png`, `u40-farmer/s-sc13-13-batches-e-f12-25-recipe-draft-{desktop,phone}-{light,dark}.png` |
| E-F12-25 Recipe | Approved | Badge "Approved"; next: Superseded (BR-SC06-04); fields editable within the role | U20, U21, U40 | `u20-production-operator/s-sc13-13-batches-e-f12-25-recipe-approved-tablet-{light,dark}.png`, `u21-production-planner/s-sc13-13-batches-e-f12-25-recipe-approved-{desktop,phone}-{light,dark}.png`, `u40-farmer/s-sc13-13-batches-e-f12-25-recipe-approved-{desktop,phone}-{light,dark}.png` |
| E-F12-25 Recipe | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U20, U21, U40 | `u20-production-operator/s-sc13-13-batches-e-f12-25-recipe-superseded-tablet-{light,dark}.png`, `u21-production-planner/s-sc13-13-batches-e-f12-25-recipe-superseded-{desktop,phone}-{light,dark}.png`, `u40-farmer/s-sc13-13-batches-e-f12-25-recipe-superseded-{desktop,phone}-{light,dark}.png` |
| E-SC13-12 Batch | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U20, U21, U40 | `u20-production-operator/s-sc13-13-batches-e-sc13-12-batch-active-tablet-{light,dark}.png`, `u21-production-planner/s-sc13-13-batches-e-sc13-12-batch-active-{desktop,phone}-{light,dark}.png`, `u40-farmer/s-sc13-13-batches-e-sc13-12-batch-active-{desktop,phone}-{light,dark}.png` |
| E-SC13-04 Lot | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U20, U21, U40 | `u20-production-operator/s-sc13-13-batches-e-sc13-04-lot-refused-tablet-{light,dark}.png`, `u21-production-planner/s-sc13-13-batches-e-sc13-04-lot-refused-{desktop,phone}-{light,dark}.png`, `u40-farmer/s-sc13-13-batches-e-sc13-04-lot-refused-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-05 Food processing](../../flows/fl-sc13-05-food-processing.md)

## Open questions

None.

---

⬅️ [S-SC13-12 Organic](../04-sales-and-certification/s-sc13-12-organic.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-14 Traceability](s-sc13-14-traceability.md)
