🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-05 Food processing](README.md) › 🖥️ S-SC13-16 Labels

# 🖥️ S-SC13-16 Labels

**Status:** 🔄 waiting for the owner

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Used to label products ([UC-SC13-16](../../use-cases/05-food-processing/uc-sc13-16-label-products.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-05 step 4, U27 | desktop | ![FL-SC13-05 step 4, U27, light](../../images/05-food-processing/u27-quality-manager/4-label-desktop-light.png) | ![FL-SC13-05 step 4, U27, dark](../../images/05-food-processing/u27-quality-manager/4-label-desktop-dark.png) |
| FL-SC13-05 step 4, U27 | tablet | ![FL-SC13-05 step 4, U27, light](../../images/05-food-processing/u27-quality-manager/4-label-tablet-light.png) | ![FL-SC13-05 step 4, U27, dark](../../images/05-food-processing/u27-quality-manager/4-label-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-16-labels-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-16-labels-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-16-labels-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-16-labels-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-16-labels-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-16-labels-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc13-16-labels-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc13-16-labels-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC13-14 Product label](../../data/e-sc13-14-product-label.md), shown as the entity pages list them,
with their examples.

## Actions

- Generate: [UC-SC13-16](../../use-cases/05-food-processing/uc-sc13-16-label-products.md), step 1.
- Check: [UC-SC13-16](../../use-cases/05-food-processing/uc-sc13-16-label-products.md), step 2.
- Print: [UC-SC13-16](../../use-cases/05-food-processing/uc-sc13-16-label-products.md), step 3.
- Apply: [UC-SC13-16](../../use-cases/05-food-processing/uc-sc13-16-label-products.md), step 4.

## States

- Normal: labels from recipes with ingredients, allergens and nutrition.
- Empty: "No label".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an allergen unknown: printing is blocked.
- Read-only: printed labels are read-only.
- Offline: not available offline: office work on aid, accounts and margins. Offline work is kept for the phone forms of
  the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC13-14 Product label](../../data/e-sc13-14-product-label.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-14 Product label | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U21, U27 | `u21-production-planner/s-sc13-16-labels-e-sc13-14-product-label-active-{desktop,phone}-{light,dark}.png`, `u27-quality-manager/s-sc13-16-labels-e-sc13-14-product-label-active-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC13-05 Food processing](../../flows/fl-sc13-05-food-processing.md)

## Open questions

None.

---

⬅️ [S-SC13-15 HACCP](s-sc13-15-haccp.md) · ⬆️ [Up](README.md) · ➡️ [S-SC13-17 Shelf life](s-sc13-17-shelf-life.md)
