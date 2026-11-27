🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-02 Ticketing](README.md) › 🖥️ S-SC16-17 Refunds

# 🖥️ S-SC16-17 Refunds

**Status:** ✅ specified

## Personas

- [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md)
- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)

## Purpose

Used to handle cancellations and refunds
([UC-SC16-17](../../use-cases/02-ticketing/uc-sc16-17-handle-cancellations-and-refunds.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-02 step 4, U44 | desktop | ![FL-SC16-02 step 4, U44, light](../../images/02-ticketing/u44-box-office-agent/4-refunds-desktop-light.png) | ![FL-SC16-02 step 4, U44, dark](../../images/02-ticketing/u44-box-office-agent/4-refunds-desktop-dark.png) |
| FL-SC16-02 step 4, U44 | phone | ![FL-SC16-02 step 4, U44, light](../../images/02-ticketing/u44-box-office-agent/4-refunds-phone-light.png) | ![FL-SC16-02 step 4, U44, dark](../../images/02-ticketing/u44-box-office-agent/4-refunds-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-17-refunds-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-17-refunds-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-17-refunds-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-17-refunds-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-17-refunds-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-17-refunds-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-17-refunds-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-17-refunds-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-07 Ticket order](../../data/e-sc16-07-ticket-order.md), shown as the entity pages list them, with
their examples.

## Actions

- Cancel: [UC-SC16-17](../../use-cases/02-ticketing/uc-sc16-17-handle-cancellations-and-refunds.md), step 1.
- Refund or exchange: [UC-SC16-17](../../use-cases/02-ticketing/uc-sc16-17-handle-cancellations-and-refunds.md), step 2.
- Tell holders: [UC-SC16-17](../../use-cases/02-ticketing/uc-sc16-17-handle-cancellations-and-refunds.md), step 3.
- Reconcile: [UC-SC16-17](../../use-cases/02-ticketing/uc-sc16-17-handle-cancellations-and-refunds.md), step 4.

## States

- Normal: cancelled events, refunds and exchanges.
- Empty: "No cancellation".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the payment means expired: another means is asked.
- Read-only: refunded ones are read-only.
- Offline: not available offline: office work on budgets, contracts and declarations. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC16-07 Ticket order](../../data/e-sc16-07-ticket-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-07 Ticket order | Paid | Badge "Paid"; a new record starts here; next: Refunded (UC-SC16-17); fields editable within the role | U05, U43, U44 | `u05-accounting/s-sc16-17-refunds-e-sc16-07-ticket-order-paid-desktop-{light,dark}.png`, `u43-event-producer/s-sc16-17-refunds-e-sc16-07-ticket-order-paid-{desktop,phone}-{light,dark}.png`, `u44-box-office-agent/s-sc16-17-refunds-e-sc16-07-ticket-order-paid-{desktop,phone}-{light,dark}.png` |
| E-SC16-07 Ticket order | Refunded | Badge "Refunded"; next: Exchanged (UC-SC16-17); fields editable within the role | U05, U43, U44 | `u05-accounting/s-sc16-17-refunds-e-sc16-07-ticket-order-refunded-desktop-{light,dark}.png`, `u43-event-producer/s-sc16-17-refunds-e-sc16-07-ticket-order-refunded-{desktop,phone}-{light,dark}.png`, `u44-box-office-agent/s-sc16-17-refunds-e-sc16-07-ticket-order-refunded-{desktop,phone}-{light,dark}.png` |
| E-SC16-07 Ticket order | Exchanged | Badge "Exchanged"; final: read-only, no next state; the history shows how it got here | U05, U43, U44 | `u05-accounting/s-sc16-17-refunds-e-sc16-07-ticket-order-exchanged-desktop-{light,dark}.png`, `u43-event-producer/s-sc16-17-refunds-e-sc16-07-ticket-order-exchanged-{desktop,phone}-{light,dark}.png`, `u44-box-office-agent/s-sc16-17-refunds-e-sc16-07-ticket-order-exchanged-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC16-02 Ticketing](../../flows/fl-sc16-02-ticketing.md)

## Open questions

None.

---

⬅️ [S-SC16-16 Memberships](../05-declarations-and-reports/s-sc16-16-memberships.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-18 Event report](../05-declarations-and-reports/s-sc16-18-event-report.md)
