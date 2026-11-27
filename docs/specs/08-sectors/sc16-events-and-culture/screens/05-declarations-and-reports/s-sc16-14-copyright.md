🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-05 Declarations and reports](README.md) › 🖥️ S-SC16-14 Copyright

# 🖥️ S-SC16-14 Copyright

**Status:** ✅ specified

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to declare and pay copyright royalties,
[UC-SC16-14](../../use-cases/05-declarations-and-reports/uc-sc16-14-declare-and-pay-copyright-royalties.md).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-05 step 1, U43 | desktop | ![FL-SC16-05 step 1, U43, light](../../images/05-declarations-and-reports/u43-event-producer/1-copyright-desktop-light.png) | ![FL-SC16-05 step 1, U43, dark](../../images/05-declarations-and-reports/u43-event-producer/1-copyright-desktop-dark.png) |
| FL-SC16-05 step 1, U43 | phone | ![FL-SC16-05 step 1, U43, light](../../images/05-declarations-and-reports/u43-event-producer/1-copyright-phone-light.png) | ![FL-SC16-05 step 1, U43, dark](../../images/05-declarations-and-reports/u43-event-producer/1-copyright-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-14-copyright-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-14-copyright-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-14-copyright-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-14-copyright-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-14-copyright-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-14-copyright-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-14-copyright-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-14-copyright-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-15 Show declaration](../../data/e-sc16-15-show-declaration.md), shown as the entity pages list
them, with their examples.

## Actions

- Request: [UC-SC16-14](../../use-cases/05-declarations-and-reports/uc-sc16-14-declare-and-pay-copyright-royalties.md),
  step 1.
- Declare after the show:
  [UC-SC16-14](../../use-cases/05-declarations-and-reports/uc-sc16-14-declare-and-pay-copyright-royalties.md), step 2.
- Pay: [UC-SC16-14](../../use-cases/05-declarations-and-reports/uc-sc16-14-declare-and-pay-copyright-royalties.md), step
  3.
- Post: [UC-SC16-14](../../use-cases/05-declarations-and-reports/uc-sc16-14-declare-and-pay-copyright-royalties.md),
  step 4.

## States

- Normal: authorisations and declarations with set lists.
- Empty: "No declaration".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the set list missing: it is asked.
- Read-only: paid ones are read-only.
- Offline: not available offline: office work on budgets, contracts and declarations. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC16-15 Show declaration](../../data/e-sc16-15-show-declaration.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-15 Show declaration | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U43 | `u05-accounting/s-sc16-14-copyright-e-sc16-15-show-declaration-active-desktop-{light,dark}.png`, `u43-event-producer/s-sc16-14-copyright-e-sc16-15-show-declaration-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC16-05 Declarations and reports](../../flows/fl-sc16-05-declarations-and-reports.md)

## Open questions

None.

---

⬅️ [S-SC16-13 Safety](../04-on-site/s-sc16-13-safety.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-15 Ticket tax](s-sc16-15-ticket-tax.md)
