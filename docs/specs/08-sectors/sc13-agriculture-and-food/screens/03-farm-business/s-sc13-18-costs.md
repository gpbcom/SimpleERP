🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-03 Farm business](README.md) › 🖥️ S-SC13-18 Costs

# 🖥️ S-SC13-18 Costs

**Status:** ✅ specified

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to follow costs per crop, herd and product
([UC-SC13-18](../../use-cases/03-farm-business/uc-sc13-18-follow-costs-per-crop-herd-and-product.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-03 step 4, U40 | desktop | ![FL-SC13-03 step 4, U40, light](../../images/03-farm-business/u40-farmer/4-costs-desktop-light.png) | ![FL-SC13-03 step 4, U40, dark](../../images/03-farm-business/u40-farmer/4-costs-desktop-dark.png) |
| FL-SC13-03 step 4, U40 | phone | ![FL-SC13-03 step 4, U40, light](../../images/03-farm-business/u40-farmer/4-costs-phone-light.png) | ![FL-SC13-03 step 4, U40, dark](../../images/03-farm-business/u40-farmer/4-costs-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-18-costs-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-18-costs-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-18-costs-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-18-costs-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-18-costs-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-18-costs-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-18-costs-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-18-costs-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-02 Crop plan](../../data/e-sc13-02-crop-plan.md),
[E-SC13-07 Machine](../../data/e-sc13-07-machine.md), shown as the entity pages list them, with their examples.

## Actions

- Allocate costs: [UC-SC13-18](../../use-cases/03-farm-business/uc-sc13-18-follow-costs-per-crop-herd-and-product.md),
  step 1.
- Compute: [UC-SC13-18](../../use-cases/03-farm-business/uc-sc13-18-follow-costs-per-crop-herd-and-product.md), step 2.
- Compare years: [UC-SC13-18](../../use-cases/03-farm-business/uc-sc13-18-follow-costs-per-crop-herd-and-product.md),
  step 3.
- Decide: [UC-SC13-18](../../use-cases/03-farm-business/uc-sc13-18-follow-costs-per-crop-herd-and-product.md), step 4.

## States

- Normal: margins per crop, herd and product.
- Empty: "No cost".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, costs missing: they are shown.
- Read-only: the farmer reads.
- Offline: not available offline: office work on aid, accounts and margins. Offline work is kept for the phone forms of
  the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC13-02 Crop plan](../../data/e-sc13-02-crop-plan.md),
[E-SC13-07 Machine](../../data/e-sc13-07-machine.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-02 Crop plan | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U40 | `u05-accounting/s-sc13-18-costs-e-sc13-02-crop-plan-active-desktop-{light,dark}.png`, `u40-farmer/s-sc13-18-costs-e-sc13-02-crop-plan-active-{desktop,phone}-{light,dark}.png` |
| E-SC13-07 Machine | Overdue | Badge "Overdue"; a new record starts here; next: Flagged (UC-SC13-08); fields editable within the role | U05, U40 | `u05-accounting/s-sc13-18-costs-e-sc13-07-machine-overdue-desktop-{light,dark}.png`, `u40-farmer/s-sc13-18-costs-e-sc13-07-machine-overdue-{desktop,phone}-{light,dark}.png` |
| E-SC13-07 Machine | Flagged | Badge "Flagged"; next: Overdue (UC-SC13-08); fields editable within the role | U05, U40 | `u05-accounting/s-sc13-18-costs-e-sc13-07-machine-flagged-desktop-{light,dark}.png`, `u40-farmer/s-sc13-18-costs-e-sc13-07-machine-flagged-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-03 Farm business](../../flows/fl-sc13-03-farm-business.md)

## Open questions

None.

---

⬅️ [S-SC13-17 Shelf life](../05-food-processing/s-sc13-17-shelf-life.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-19 Farm reports](s-sc13-19-farm-reports.md)
