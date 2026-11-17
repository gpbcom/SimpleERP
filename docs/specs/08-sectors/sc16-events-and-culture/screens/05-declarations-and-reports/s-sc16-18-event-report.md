🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-05 Declarations and reports](README.md) › 🖥️ S-SC16-18 Event report

# 🖥️ S-SC16-18 Event report

**Status:** 🔄 waiting for the owner

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to report after the event
([UC-SC16-18](../../use-cases/05-declarations-and-reports/uc-sc16-18-report-after-the-event.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-05 step 4, U43 | desktop | ![FL-SC16-05 step 4, U43, light](../../images/05-declarations-and-reports/u43-event-producer/4-report-desktop-light.png) | ![FL-SC16-05 step 4, U43, dark](../../images/05-declarations-and-reports/u43-event-producer/4-report-desktop-dark.png) |
| FL-SC16-05 step 4, U43 | phone | ![FL-SC16-05 step 4, U43, light](../../images/05-declarations-and-reports/u43-event-producer/4-report-phone-light.png) | ![FL-SC16-05 step 4, U43, dark](../../images/05-declarations-and-reports/u43-event-producer/4-report-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-18-event-report-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-18-event-report-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-18-event-report-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-18-event-report-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-18-event-report-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-18-event-report-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-18-event-report-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-18-event-report-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-01 Show](../../data/e-sc16-01-show.md),
[E-SC16-02 Event budget](../../data/e-sc16-02-event-budget.md), shown as the entity pages list them, with their
examples.

## Actions

- Close the budget: [UC-SC16-18](../../use-cases/05-declarations-and-reports/uc-sc16-18-report-after-the-event.md), step
  1.
- Gather figures: [UC-SC16-18](../../use-cases/05-declarations-and-reports/uc-sc16-18-report-after-the-event.md), step
  2.
- Share: [UC-SC16-18](../../use-cases/05-declarations-and-reports/uc-sc16-18-report-after-the-event.md), step 3.
- Read: [UC-SC16-18](../../use-cases/05-declarations-and-reports/uc-sc16-18-report-after-the-event.md), step 4.

## States

- Normal: budget against actual, attendance and satisfaction.
- Empty: "No figure yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, figures missing: they are shown.
- Read-only: shared reports are read-only.
- Offline: not available offline: office work on budgets, contracts and declarations. Offline work is kept for the phone
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

- [FL-SC16-05 Declarations and reports](../../flows/fl-sc16-05-declarations-and-reports.md)

## Open questions

None.

---

⬅️ [S-SC16-17 Refunds](../02-ticketing/s-sc16-17-refunds.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-19 Attendee messages](../04-on-site/s-sc16-19-attendee-messages.md)
