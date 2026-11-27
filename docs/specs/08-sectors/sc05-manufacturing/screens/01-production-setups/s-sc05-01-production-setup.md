🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-01 Production setups](README.md) › 🖥️ S-SC05-01 Production setup

# 🖥️ S-SC05-01 Production setup

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Used to set up the production type
([UC-SC05-01](../../use-cases/01-production-setups/uc-sc05-01-set-up-the-production-type.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-01 step 1, U21 | desktop | ![FL-SC05-01 step 1, U21, light](../../images/01-production-setups/u21-production-planner/1-production-type-desktop-light.png) | ![FL-SC05-01 step 1, U21, dark](../../images/01-production-setups/u21-production-planner/1-production-type-desktop-dark.png) |
| FL-SC05-01 step 1, U21 | phone | ![FL-SC05-01 step 1, U21, light](../../images/01-production-setups/u21-production-planner/1-production-type-phone-light.png) | ![FL-SC05-01 step 1, U21, dark](../../images/01-production-setups/u21-production-planner/1-production-type-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-01-production-setup-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-01-production-setup-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-01-production-setup-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-01-production-setup-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-01-production-setup-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-01-production-setup-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc05-01-production-setup-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc05-01-production-setup-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC05-01 Production setup](../../data/e-sc05-01-production-setup.md), shown as the entity pages list
them, with their examples.

## Actions

- Choose the type: [UC-SC05-01](../../use-cases/01-production-setups/uc-sc05-01-set-up-the-production-type.md), step 1.
- Install its setup: [UC-SC05-01](../../use-cases/01-production-setups/uc-sc05-01-set-up-the-production-type.md), step
  2.
- Adjust: [UC-SC05-01](../../use-cases/01-production-setups/uc-sc05-01-set-up-the-production-type.md), step 3.
- Plan the first orders: [UC-SC05-01](../../use-cases/01-production-setups/uc-sc05-01-set-up-the-production-type.md),
  step 4.

## States

- Normal: the sites with their production type and installed setup.
- Empty: "No setup installed".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a setup changed while a plan is running: the planner is warned
  and the change applies to new orders only.
- Read-only: only administrators change it.
- Offline: not available offline: office work on shared quality and planning records. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC05-01 Production setup](../../data/e-sc05-01-production-setup.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-01 Production setup | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U21 | `u07-administrator/s-sc05-01-production-setup-e-sc05-01-production-setup-active-desktop-{light,dark}.png`, `u21-production-planner/s-sc05-01-production-setup-e-sc05-01-production-setup-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC05-01 Production setups](../../flows/fl-sc05-01-production-setups.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC05-02 Recipes](s-sc05-02-recipes.md)
