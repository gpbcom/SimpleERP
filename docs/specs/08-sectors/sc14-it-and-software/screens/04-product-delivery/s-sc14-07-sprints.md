🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-04 Product delivery](README.md) › 🖥️ S-SC14-07 Sprints

# 🖥️ S-SC14-07 Sprints

**Status:** 🔄 waiting for the owner

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)

## Purpose

Used to plan IT projects in sprints with time
([UC-SC14-07](../../use-cases/04-product-delivery/uc-sc14-07-plan-it-projects-in-sprints-with-time.md)).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-04 step 1, U16 | desktop | ![FL-SC14-04 step 1, U16, light](../../images/04-product-delivery/u16-office-worker/1-sprint-desktop-light.png) | ![FL-SC14-04 step 1, U16, dark](../../images/04-product-delivery/u16-office-worker/1-sprint-desktop-dark.png) |
| FL-SC14-04 step 1, U16 | phone | ![FL-SC14-04 step 1, U16, light](../../images/04-product-delivery/u16-office-worker/1-sprint-phone-light.png) | ![FL-SC14-04 step 1, U16, dark](../../images/04-product-delivery/u16-office-worker/1-sprint-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-07-sprints-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-07-sprints-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-07-sprints-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-07-sprints-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-07-sprints-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-07-sprints-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-07-sprints-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-07-sprints-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-07 Sprint](../../data/e-sc14-07-sprint.md), shown as the entity pages list them, with their
examples.

## Actions

- Plan the sprint:
  [UC-SC14-07](../../use-cases/04-product-delivery/uc-sc14-07-plan-it-projects-in-sprints-with-time.md), step 1.
- Work and record time:
  [UC-SC14-07](../../use-cases/04-product-delivery/uc-sc14-07-plan-it-projects-in-sprints-with-time.md), step 2.
- Review: [UC-SC14-07](../../use-cases/04-product-delivery/uc-sc14-07-plan-it-projects-in-sprints-with-time.md), step 3.
- Bill: [UC-SC14-07](../../use-cases/04-product-delivery/uc-sc14-07-plan-it-projects-in-sprints-with-time.md), step 4.

## States

- Normal: sprints with items, time and budget.
- Empty: "No sprint".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, time over budget: the manager is alerted.
- Read-only: closed sprints are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-07 Sprint](../../data/e-sc14-07-sprint.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-07 Sprint | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U16, U24 | `u16-office-worker/s-sc14-07-sprints-e-sc14-07-sprint-active-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc14-07-sprints-e-sc14-07-sprint-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC14-04 Product delivery](../../flows/fl-sc14-04-product-delivery.md)

## Open questions

None.

---

⬅️ [S-SC14-06 Managed services](../03-support-and-services/s-sc14-06-managed-services.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-08 Release notes](s-sc14-08-release-notes.md)
