🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-05 Food processing](README.md) › 🖥️ S-SC13-17 Shelf life

# 🖥️ S-SC13-17 Shelf life

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Used to manage shelf life, rotation and recalls
([UC-SC13-17](../../use-cases/05-food-processing/uc-sc13-17-manage-shelf-life-rotation-and-recalls.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-05 step 5, U27 | desktop | ![FL-SC13-05 step 5, U27, light](../../images/05-food-processing/u27-quality-manager/5-recall-desktop-light.png) | ![FL-SC13-05 step 5, U27, dark](../../images/05-food-processing/u27-quality-manager/5-recall-desktop-dark.png) |
| FL-SC13-05 step 5, U27 | tablet | ![FL-SC13-05 step 5, U27, light](../../images/05-food-processing/u27-quality-manager/5-recall-tablet-light.png) | ![FL-SC13-05 step 5, U27, dark](../../images/05-food-processing/u27-quality-manager/5-recall-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-17-shelf-life-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-17-shelf-life-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-17-shelf-life-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-17-shelf-life-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-17-shelf-life-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-17-shelf-life-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc13-17-shelf-life-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc13-17-shelf-life-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC13-04 Lot](../../data/e-sc13-04-lot.md), [E-SC13-15 Recall](../../data/e-sc13-15-recall.md), shown as
the entity pages list them, with their examples.

## Actions

- Follow dates: [UC-SC13-17](../../use-cases/05-food-processing/uc-sc13-17-manage-shelf-life-rotation-and-recalls.md),
  step 1.
- Block expired lots:
  [UC-SC13-17](../../use-cases/05-food-processing/uc-sc13-17-manage-shelf-life-rotation-and-recalls.md), step 2.
- Recall: [UC-SC13-17](../../use-cases/05-food-processing/uc-sc13-17-manage-shelf-life-rotation-and-recalls.md), step 3.
- Tell customers: [UC-SC13-17](../../use-cases/05-food-processing/uc-sc13-17-manage-shelf-life-rotation-and-recalls.md),
  step 4.

## States

- Normal: lots by date, blocks and recalls.
- Empty: "No lot near its date".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a recall: customers are told.
- Read-only: closed recalls are read-only.
- Offline: not available offline: office work on aid, accounts and margins. Offline work is kept for the phone forms of
  the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC13-15 Recall](../../data/e-sc13-15-recall.md),
[E-SC13-04 Lot](../../data/e-sc13-04-lot.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-15 Recall | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U15, U27 | `u15-warehouse-operator/s-sc13-17-shelf-life-e-sc13-15-recall-active-{phone,tablet}-{light,dark}.png`, `u27-quality-manager/s-sc13-17-shelf-life-e-sc13-15-recall-active-{desktop,tablet}-{light,dark}.png` |
| E-SC13-04 Lot | Blocked | Badge "Blocked"; a new record starts here; next: Expired or Refused (UC-SC13-17, UC-SC13-04); fields editable within the role | U15, U27 | `u15-warehouse-operator/s-sc13-17-shelf-life-e-sc13-04-lot-blocked-{phone,tablet}-{light,dark}.png`, `u27-quality-manager/s-sc13-17-shelf-life-e-sc13-04-lot-blocked-{desktop,tablet}-{light,dark}.png` |
| E-SC13-04 Lot | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U15, U27 | `u15-warehouse-operator/s-sc13-17-shelf-life-e-sc13-04-lot-expired-{phone,tablet}-{light,dark}.png`, `u27-quality-manager/s-sc13-17-shelf-life-e-sc13-04-lot-expired-{desktop,tablet}-{light,dark}.png` |
| E-SC13-04 Lot | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U15, U27 | `u15-warehouse-operator/s-sc13-17-shelf-life-e-sc13-04-lot-refused-{phone,tablet}-{light,dark}.png`, `u27-quality-manager/s-sc13-17-shelf-life-e-sc13-04-lot-refused-{desktop,tablet}-{light,dark}.png` |

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

⬅️ [S-SC13-16 Labels](s-sc13-16-labels.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-18 Costs](../03-farm-business/s-sc13-18-costs.md)
