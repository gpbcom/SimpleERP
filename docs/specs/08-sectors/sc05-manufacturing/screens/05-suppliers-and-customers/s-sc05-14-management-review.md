🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-05 Suppliers and customers](README.md) ›
🖥️ S-SC05-14 Management review

# 🖥️ S-SC05-14 Management review

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)

## Purpose

Used to hold the management review
([UC-SC05-14](../../use-cases/05-suppliers-and-customers/uc-sc05-14-hold-the-management-review.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-05 step 4, U13 | desktop | ![FL-SC05-05 step 4, U13, light](../../images/05-suppliers-and-customers/u13-owner/4-management-review-desktop-light.png) | ![FL-SC05-05 step 4, U13, dark](../../images/05-suppliers-and-customers/u13-owner/4-management-review-desktop-dark.png) |
| FL-SC05-05 step 4, U13 | phone | ![FL-SC05-05 step 4, U13, light](../../images/05-suppliers-and-customers/u13-owner/4-management-review-phone-light.png) | ![FL-SC05-05 step 4, U13, dark](../../images/05-suppliers-and-customers/u13-owner/4-management-review-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-14-management-review-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-14-management-review-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-14-management-review-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-14-management-review-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-14-management-review-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-14-management-review-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc05-14-management-review-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc05-14-management-review-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC05-14 Management review](../../data/e-sc05-14-management-review.md), shown as the entity pages list
them, with their examples.

## Actions

- Prepare: [UC-SC05-14](../../use-cases/05-suppliers-and-customers/uc-sc05-14-hold-the-management-review.md), step 1.
- Review: [UC-SC05-14](../../use-cases/05-suppliers-and-customers/uc-sc05-14-hold-the-management-review.md), step 2.
- Record decisions: [UC-SC05-14](../../use-cases/05-suppliers-and-customers/uc-sc05-14-hold-the-management-review.md),
  step 3.
- Follow the decisions:
  [UC-SC05-14](../../use-cases/05-suppliers-and-customers/uc-sc05-14-hold-the-management-review.md), step 4.

## States

- Normal: objectives, indicators, decisions and actions.
- Empty: "No review held yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an objective without a target: it is flagged.
- Read-only: a recorded review is read-only.
- Offline: not available offline: office work on shared quality and planning records. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC05-14 Management review](../../data/e-sc05-14-management-review.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-14 Management review | Prepared | Badge "Prepared"; a new record starts here; next: Held (UC-SC05-14); fields editable within the role | U13, U27 | `u13-owner/s-sc05-14-management-review-e-sc05-14-management-review-prepared-{desktop,phone}-{light,dark}.png`, `u27-quality-manager/s-sc05-14-management-review-e-sc05-14-management-review-prepared-{desktop,tablet}-{light,dark}.png` |
| E-SC05-14 Management review | Held | Badge "Held"; next: Prepared (UC-SC05-14); fields editable within the role | U13, U27 | `u13-owner/s-sc05-14-management-review-e-sc05-14-management-review-held-{desktop,phone}-{light,dark}.png`, `u27-quality-manager/s-sc05-14-management-review-e-sc05-14-management-review-held-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC05-05 Suppliers and customers](../../flows/fl-sc05-05-suppliers-and-customers.md)

## Open questions

None.

---

⬅️ [S-SC05-13 Qualifications](s-sc05-13-qualifications.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-15 Quality assistant](../04-quality-system/s-sc05-15-quality-assistant.md)
