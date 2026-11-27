🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-04 Bill and fund](README.md) › 🖥️ S-SC04-11 Travel time

# 🖥️ S-SC04-11 Travel time

**Status:** ✅ specified

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to pay carers' travel time and split shifts
([UC-SC04-11](../../use-cases/04-bill-and-fund/uc-sc04-11-pay-carers-travel-time-and-split-shifts.md)).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-04 step 4, U25 | desktop | ![FL-SC04-04 step 4, U25, light](../../images/04-bill-and-fund/u25-care-coordinator/4-travel-time-desktop-light.png) | ![FL-SC04-04 step 4, U25, dark](../../images/04-bill-and-fund/u25-care-coordinator/4-travel-time-desktop-dark.png) |
| FL-SC04-04 step 4, U25 | phone | ![FL-SC04-04 step 4, U25, light](../../images/04-bill-and-fund/u25-care-coordinator/4-travel-time-phone-light.png) | ![FL-SC04-04 step 4, U25, dark](../../images/04-bill-and-fund/u25-care-coordinator/4-travel-time-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-11-travel-time-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-11-travel-time-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-11-travel-time-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-11-travel-time-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-11-travel-time-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-11-travel-time-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-11-travel-time-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-11-travel-time-offline-phone-dark.png) |

## Fields and columns

The fields of [E-F9-26 Round](../../../../02-functional/f09-hr-and-projects/data/e-f09-26-round.md), shown as the entity
pages list them, with their examples.

## Actions

- Compute from rounds:
  [UC-SC04-11](../../use-cases/04-bill-and-fund/uc-sc04-11-pay-carers-travel-time-and-split-shifts.md), step 1.
- Check: [UC-SC04-11](../../use-cases/04-bill-and-fund/uc-sc04-11-pay-carers-travel-time-and-split-shifts.md), step 2.
- Send to payroll: [UC-SC04-11](../../use-cases/04-bill-and-fund/uc-sc04-11-pay-carers-travel-time-and-split-shifts.md),
  step 3.
- Lock the month: [UC-SC04-11](../../use-cases/04-bill-and-fund/uc-sc04-11-pay-carers-travel-time-and-split-shifts.md),
  step 4.

## States

- Normal: per carer and day: travel time, splits, mileage and their payroll state.
- Empty: "No round this month".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a split over the limit: it is flagged and needs the coordinator's
  reason.
- Read-only: inputs sent to payroll are read-only.
- Offline: not available offline: office work at the agency on shared planning and billing data. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC04-04 Bill and fund](../../flows/fl-sc04-04-bill-and-fund.md)

## Open questions

None.

---

⬅️ [S-SC04-10 Immediate advance](s-sc04-10-immediate-advance.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-12 Quality](../05-people-and-quality/s-sc04-12-quality.md)
