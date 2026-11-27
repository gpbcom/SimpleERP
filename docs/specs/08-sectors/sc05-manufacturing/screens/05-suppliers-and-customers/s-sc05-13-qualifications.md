🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-05 Suppliers and customers](README.md) › 🖥️ S-SC05-13 Qualifications

# 🖥️ S-SC05-13 Qualifications

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Used to qualify staff for operations
([UC-SC05-13](../../use-cases/05-suppliers-and-customers/uc-sc05-13-qualify-staff-for-operations.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-05 step 3, U27 | desktop | ![FL-SC05-05 step 3, U27, light](../../images/05-suppliers-and-customers/u27-quality-manager/3-qualifications-desktop-light.png) | ![FL-SC05-05 step 3, U27, dark](../../images/05-suppliers-and-customers/u27-quality-manager/3-qualifications-desktop-dark.png) |
| FL-SC05-05 step 3, U27 | tablet | ![FL-SC05-05 step 3, U27, light](../../images/05-suppliers-and-customers/u27-quality-manager/3-qualifications-tablet-light.png) | ![FL-SC05-05 step 3, U27, dark](../../images/05-suppliers-and-customers/u27-quality-manager/3-qualifications-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-13-qualifications-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-13-qualifications-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-13-qualifications-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-13-qualifications-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-13-qualifications-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-13-qualifications-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc05-13-qualifications-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc05-13-qualifications-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC05-13 Operation qualification](../../data/e-sc05-13-operation-qualification.md),
[E-F12-17 Qualification requirement](../../../../02-functional/f12-manufacturing/data/e-f12-17-qualification-requirement.md),
shown as the entity pages list them, with their examples.

## Actions

- Train: [UC-SC05-13](../../use-cases/05-suppliers-and-customers/uc-sc05-13-qualify-staff-for-operations.md), step 1.
- Qualify: [UC-SC05-13](../../use-cases/05-suppliers-and-customers/uc-sc05-13-qualify-staff-for-operations.md), step 2.
- Renew: [UC-SC05-13](../../use-cases/05-suppliers-and-customers/uc-sc05-13-qualify-staff-for-operations.md), step 3.
- Sign in where qualified:
  [UC-SC05-13](../../use-cases/05-suppliers-and-customers/uc-sc05-13-qualify-staff-for-operations.md), step 4.

## States

- Normal: operators' qualifications per operation with expiry.
- Empty: "No qualification".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, not qualified: the operator's start is refused,
  [BR-SC05-13](../../business-rules/br-sc05-13-operators-qualified-for-the-operation.md),
  [BR-F12-17](../../../../02-functional/f12-manufacturing/business-rules/br-f12-17-operators-sign-in-only-where-qualified.md).
- Read-only: operators read their own.
- Offline: not available offline: office work on shared quality and planning records. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15):
[E-F12-17 Qualification requirement](../../../../02-functional/f12-manufacturing/data/e-f12-17-qualification-requirement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-17 Qualification requirement | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06, U20, U27 | `u06-hr/s-sc05-13-qualifications-e-f12-17-qualification-requirement-active-desktop-{light,dark}.png`, `u20-production-operator/s-sc05-13-qualifications-e-f12-17-qualification-requirement-active-tablet-{light,dark}.png`, `u27-quality-manager/s-sc05-13-qualifications-e-f12-17-qualification-requirement-active-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC05-05 Suppliers and customers](../../flows/fl-sc05-05-suppliers-and-customers.md)

## Open questions

None.

---

⬅️ [S-SC05-12 Calibration](../04-quality-system/s-sc05-12-calibration.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-14 Management review](s-sc05-14-management-review.md)
