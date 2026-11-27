🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-05 Declarations and reports](README.md) › 🖥️ S-SC16-15 Ticket tax

# 🖥️ S-SC16-15 Ticket tax

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)

## Purpose

Used to declare the ticket tax
([UC-SC16-15](../../use-cases/05-declarations-and-reports/uc-sc16-15-declare-the-ticket-tax.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-05 step 2, U05 | desktop | ![FL-SC16-05 step 2, U05, light](../../images/05-declarations-and-reports/u05-accounting/2-ticket-tax-desktop-light.png) | ![FL-SC16-05 step 2, U05, dark](../../images/05-declarations-and-reports/u05-accounting/2-ticket-tax-desktop-dark.png) |
| Error E1, U05 | desktop | ![Error E1, U05, light](../../images/05-declarations-and-reports/u05-accounting/e1-tax-late-desktop-light.png) | ![Error E1, U05, dark](../../images/05-declarations-and-reports/u05-accounting/e1-tax-late-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-15-ticket-tax-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-15-ticket-tax-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-15-ticket-tax-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-15-ticket-tax-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-15-ticket-tax-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-15-ticket-tax-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc16-15-ticket-tax-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc16-15-ticket-tax-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC16-15 Show declaration](../../data/e-sc16-15-show-declaration.md), shown as the entity pages list
them, with their examples.

## Actions

- Compute: [UC-SC16-15](../../use-cases/05-declarations-and-reports/uc-sc16-15-declare-the-ticket-tax.md), step 1.
- Check: [UC-SC16-15](../../use-cases/05-declarations-and-reports/uc-sc16-15-declare-the-ticket-tax.md), step 2.
- Declare: [UC-SC16-15](../../use-cases/05-declarations-and-reports/uc-sc16-15-declare-the-ticket-tax.md), step 3.
- Pay: [UC-SC16-15](../../use-cases/05-declarations-and-reports/uc-sc16-15-declare-the-ticket-tax.md), step 4.

## States

- Normal: receipts per show and the tax due.
- Empty: "No show to declare".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, late: accounting is alerted.
- Read-only: declared ones are read-only.
- Offline: not available offline: office work on budgets, contracts and declarations. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC16-15 Show declaration](../../data/e-sc16-15-show-declaration.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-15 Show declaration | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U43 | `u05-accounting/s-sc16-15-ticket-tax-e-sc16-15-show-declaration-active-desktop-{light,dark}.png`, `u43-event-producer/s-sc16-15-ticket-tax-e-sc16-15-show-declaration-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC16-05 Declarations and reports](../../flows/fl-sc16-05-declarations-and-reports.md)

## Open questions

None.

---

⬅️ [S-SC16-14 Copyright](s-sc16-14-copyright.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-16 Memberships](s-sc16-16-memberships.md)
