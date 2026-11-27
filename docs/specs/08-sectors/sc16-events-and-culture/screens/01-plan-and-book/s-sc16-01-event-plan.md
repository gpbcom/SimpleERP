🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-01 Plan and book](README.md) › 🖥️ S-SC16-01 Event plan

# 🖥️ S-SC16-01 Event plan

**Status:** ✅ specified

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to plan an event and its budget
([UC-SC16-01](../../use-cases/01-plan-and-book/uc-sc16-01-plan-an-event-and-its-budget.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-01 step 1, U43 | desktop | ![FL-SC16-01 step 1, U43, light](../../images/01-plan-and-book/u43-event-producer/1-budget-desktop-light.png) | ![FL-SC16-01 step 1, U43, dark](../../images/01-plan-and-book/u43-event-producer/1-budget-desktop-dark.png) |
| FL-SC16-01 step 1, U43 | phone | ![FL-SC16-01 step 1, U43, light](../../images/01-plan-and-book/u43-event-producer/1-budget-phone-light.png) | ![FL-SC16-01 step 1, U43, dark](../../images/01-plan-and-book/u43-event-producer/1-budget-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-01-event-plan-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-01-event-plan-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-01-event-plan-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-01-event-plan-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-01-event-plan-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-01-event-plan-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-01-event-plan-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-01-event-plan-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-01 Show](../../data/e-sc16-01-show.md),
[E-SC16-02 Event budget](../../data/e-sc16-02-event-budget.md),
[E-F5-07 Registration event](../../../../02-functional/f05-social-media/data/e-f05-07-registration-event.md), shown as
the entity pages list them, with their examples.

## Actions

- Create: [UC-SC16-01](../../use-cases/01-plan-and-book/uc-sc16-01-plan-an-event-and-its-budget.md), step 1.
- Budget: [UC-SC16-01](../../use-cases/01-plan-and-book/uc-sc16-01-plan-an-event-and-its-budget.md), step 2.
- Approve: [UC-SC16-01](../../use-cases/01-plan-and-book/uc-sc16-01-plan-an-event-and-its-budget.md), step 3.
- Follow: [UC-SC16-01](../../use-cases/01-plan-and-book/uc-sc16-01-plan-an-event-and-its-budget.md), step 4.

## States

- Normal: events with dates, venue, capacity, state and budget against actual.
- Empty: "No event".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, over budget: the producer and owner are alerted.
- Read-only: approved budgets change by the owner.
- Offline: not available offline: office work on budgets, contracts and declarations. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC16-02 Event budget](../../data/e-sc16-02-event-budget.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-02 Event budget | Open | Badge "Open"; a new record starts here; next: Approved or Refused (UC-SC16-01); fields editable within the role | U13, U43 | `u13-owner/s-sc16-01-event-plan-e-sc16-02-event-budget-open-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-01-event-plan-e-sc16-02-event-budget-open-{desktop,phone}-{light,dark}.png` |
| E-SC16-02 Event budget | Approved | Badge "Approved"; next: Closed or Refused (UC-SC16-18, UC-SC16-01); fields editable within the role | U13, U43 | `u13-owner/s-sc16-01-event-plan-e-sc16-02-event-budget-approved-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-01-event-plan-e-sc16-02-event-budget-approved-{desktop,phone}-{light,dark}.png` |
| E-SC16-02 Event budget | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U13, U43 | `u13-owner/s-sc16-01-event-plan-e-sc16-02-event-budget-refused-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-01-event-plan-e-sc16-02-event-budget-refused-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC16-01 Plan and book](../../flows/fl-sc16-01-plan-and-book.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC16-02 Venues](s-sc16-02-venues.md)
