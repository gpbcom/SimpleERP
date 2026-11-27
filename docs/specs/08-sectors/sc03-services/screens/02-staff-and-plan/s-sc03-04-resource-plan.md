🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-02 Staff and plan](README.md) › 🖥️ S-SC03-04 Resource plan

# 🖥️ S-SC03-04 Resource plan

**Status:** 🔄 waiting for the owner

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to staff the engagement ([UC-SC03-03](../../use-cases/02-staff-and-plan/uc-sc03-03-staff-the-engagement.md)); to
plan resources and utilisation
([UC-SC03-04](../../use-cases/02-staff-and-plan/uc-sc03-04-plan-resources-and-utilisation.md)).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-02 step 1, U24 | desktop | ![FL-SC03-02 step 1, U24, light](../../images/02-staff-and-plan/u24-engagement-manager/1-staffing-desktop-light.png) | ![FL-SC03-02 step 1, U24, dark](../../images/02-staff-and-plan/u24-engagement-manager/1-staffing-desktop-dark.png) |
| FL-SC03-02 step 1, U24 | phone | ![FL-SC03-02 step 1, U24, light](../../images/02-staff-and-plan/u24-engagement-manager/1-staffing-phone-light.png) | ![FL-SC03-02 step 1, U24, dark](../../images/02-staff-and-plan/u24-engagement-manager/1-staffing-phone-dark.png) |
| Error E1, U24 | desktop | ![Error E1, U24, light](../../images/02-staff-and-plan/u24-engagement-manager/e1-over-allocated-desktop-light.png) | ![Error E1, U24, dark](../../images/02-staff-and-plan/u24-engagement-manager/e1-over-allocated-desktop-dark.png) |
| Error E1, U24 | phone | ![Error E1, U24, light](../../images/02-staff-and-plan/u24-engagement-manager/e1-over-allocated-phone-light.png) | ![Error E1, U24, dark](../../images/02-staff-and-plan/u24-engagement-manager/e1-over-allocated-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-04-resource-plan-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-04-resource-plan-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-04-resource-plan-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-04-resource-plan-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-04-resource-plan-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-04-resource-plan-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-04-resource-plan-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-04-resource-plan-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-04 Staffing assignment](../../data/e-sc03-04-staffing-assignment.md),
[E-SC03-11 Skill](../../data/e-sc03-11-skill.md), shown as the entity pages list them, with their examples.

## Actions

- See it in the plan: [UC-SC03-03](../../use-cases/02-staff-and-plan/uc-sc03-03-staff-the-engagement.md), step 4.
- Open the plan: [UC-SC03-04](../../use-cases/02-staff-and-plan/uc-sc03-04-plan-resources-and-utilisation.md), step 1.
- Move bookings: [UC-SC03-04](../../use-cases/02-staff-and-plan/uc-sc03-04-plan-resources-and-utilisation.md), step 2.
- Follow utilisation: [UC-SC03-04](../../use-cases/02-staff-and-plan/uc-sc03-04-plan-resources-and-utilisation.md), step
  3.
- Decide on the bench: [UC-SC03-04](../../use-cases/02-staff-and-plan/uc-sc03-04-plan-resources-and-utilisation.md),
  step 4.

## States

- Normal: people per week with bookings, tentative bookings, leave and utilisation.
- Empty: "No booking in this period".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an over-allocation: the owner's approval is asked,
  [BR-SC03-04](../../business-rules/br-sc03-04-staffing-respects-availability.md),
  [BR-F9-21](../../../../02-functional/f09-hr-and-projects/business-rules/br-f09-21-planned-load-stays-within-available-hours.md).
- Read-only: consultants see their own bookings.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC03-02 Staff and plan](../../flows/fl-sc03-02-staff-and-plan.md)

## Open questions

None.

---

⬅️ [S-SC03-03 Staffing](s-sc03-03-staffing.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-05 Timesheets](../03-deliver-and-record/s-sc03-05-timesheets.md)
