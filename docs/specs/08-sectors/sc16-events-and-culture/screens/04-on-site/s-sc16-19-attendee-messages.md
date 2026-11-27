🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-04 On site](README.md) › 🖥️ S-SC16-19 Attendee messages

# 🖥️ S-SC16-19 Attendee messages

**Status:** 🔄 waiting for the owner

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to communicate with attendees ([UC-SC16-19](../../use-cases/04-on-site/uc-sc16-19-communicate-with-attendees.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-04 step 3, U43 | desktop | ![FL-SC16-04 step 3, U43, light](../../images/04-on-site/u43-event-producer/3-messages-desktop-light.png) | ![FL-SC16-04 step 3, U43, dark](../../images/04-on-site/u43-event-producer/3-messages-desktop-dark.png) |
| FL-SC16-04 step 3, U43 | phone | ![FL-SC16-04 step 3, U43, light](../../images/04-on-site/u43-event-producer/3-messages-phone-light.png) | ![FL-SC16-04 step 3, U43, dark](../../images/04-on-site/u43-event-producer/3-messages-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-19-attendee-messages-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-19-attendee-messages-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-19-attendee-messages-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-19-attendee-messages-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-19-attendee-messages-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-19-attendee-messages-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-19-attendee-messages-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-19-attendee-messages-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-07 Ticket order](../../data/e-sc16-07-ticket-order.md), shown as the entity pages list them, with
their examples.

## Actions

- Write: [UC-SC16-19](../../use-cases/04-on-site/uc-sc16-19-communicate-with-attendees.md), step 1.
- Choose recipients: [UC-SC16-19](../../use-cases/04-on-site/uc-sc16-19-communicate-with-attendees.md), step 2.
- Send: [UC-SC16-19](../../use-cases/04-on-site/uc-sc16-19-communicate-with-attendees.md), step 3.
- Read: [UC-SC16-19](../../use-cases/04-on-site/uc-sc16-19-communicate-with-attendees.md), step 4.

## States

- Normal: messages with recipients and state.
- Empty: "No message".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no consent: only practical information is sent.
- Read-only: sent ones are read-only.
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

- [FL-SC16-04 On site](../../flows/fl-sc16-04-on-site.md)

## Open questions

None.

---

⬅️ [S-SC16-18 Event report](../05-declarations-and-reports/s-sc16-18-event-report.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-20 Events assistant](../05-declarations-and-reports/s-sc16-20-events-assistant.md)
