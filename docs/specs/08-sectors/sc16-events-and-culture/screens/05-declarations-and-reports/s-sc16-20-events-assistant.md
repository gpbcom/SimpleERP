🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-05 Declarations and reports](README.md) ›
🖥️ S-SC16-20 Events assistant

# 🖥️ S-SC16-20 Events assistant

**Status:** ✅ specified

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)
- [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md)

## Purpose

Used to ask the AI assistant
([UC-SC16-20](../../use-cases/05-declarations-and-reports/uc-sc16-20-ask-the-assistant.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-05 step 5, U43 | desktop | ![FL-SC16-05 step 5, U43, light](../../images/05-declarations-and-reports/u43-event-producer/5-assistant-desktop-light.png) | ![FL-SC16-05 step 5, U43, dark](../../images/05-declarations-and-reports/u43-event-producer/5-assistant-desktop-dark.png) |
| FL-SC16-05 step 5, U43 | phone | ![FL-SC16-05 step 5, U43, light](../../images/05-declarations-and-reports/u43-event-producer/5-assistant-phone-light.png) | ![FL-SC16-05 step 5, U43, dark](../../images/05-declarations-and-reports/u43-event-producer/5-assistant-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-20-events-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-20-events-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-20-events-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-20-events-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-20-events-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-20-events-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-20-events-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-20-events-assistant-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-01 Show](../../data/e-sc16-01-show.md),
[E-SC16-10 Staffing post](../../data/e-sc16-10-staffing-post.md), shown
as the entity pages list them, with their examples.

## Actions

- Ask: [UC-SC16-20](../../use-cases/05-declarations-and-reports/uc-sc16-20-ask-the-assistant.md), step 1.
- Confirm a draft: [UC-SC16-20](../../use-cases/05-declarations-and-reports/uc-sc16-20-ask-the-assistant.md), step 4.

## States

- Normal: the conversation with answers, links and drafts.
- Empty: suggested questions.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an action beyond the user's rights: the AI assistant refuses.
- Read-only: answers only for roles that cannot act.
- Offline: not available offline: the AI assistant needs the network; the last answers stay readable.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

⬅️ [S-SC16-19 Attendee messages](../04-on-site/s-sc16-19-attendee-messages.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-21 Cashless payments](../06-cashless-cinemas-tours-and-photos/s-sc16-21-cashless.md)
