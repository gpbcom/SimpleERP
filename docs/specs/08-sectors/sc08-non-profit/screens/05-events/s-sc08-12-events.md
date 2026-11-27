🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-05 Events](README.md) › 🖥️ S-SC08-12 Events

# 🖥️ S-SC08-12 Events

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to run events and ticketing ([UC-SC08-12](../../use-cases/05-events/uc-sc08-12-run-events-and-ticketing.md)).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-05 step 1, U13 | desktop | ![FL-SC08-05 step 1, U13, light](../../images/05-events/u13-owner/1-event-desktop-light.png) | ![FL-SC08-05 step 1, U13, dark](../../images/05-events/u13-owner/1-event-desktop-dark.png) |
| FL-SC08-05 step 1, U13 | phone | ![FL-SC08-05 step 1, U13, light](../../images/05-events/u13-owner/1-event-phone-light.png) | ![FL-SC08-05 step 1, U13, dark](../../images/05-events/u13-owner/1-event-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-12-events-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-12-events-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-12-events-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-12-events-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-12-events-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-12-events-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-12-events-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-12-events-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-12 Association event](../../data/e-sc08-12-association-event.md),
[E-F5-07 Registration event](../../../../02-functional/f05-social-media/data/e-f05-07-registration-event.md),
[E-F5-12 Event ticket](../../../../02-functional/f05-social-media/data/e-f05-12-event-ticket.md), shown as the entity
pages list them, with their examples.

## Actions

- Create the event: [UC-SC08-12](../../use-cases/05-events/uc-sc08-12-run-events-and-ticketing.md), step 1.
- Set tickets: [UC-SC08-12](../../use-cases/05-events/uc-sc08-12-run-events-and-ticketing.md), step 2.
- Buy or book: [UC-SC08-12](../../use-cases/05-events/uc-sc08-12-run-events-and-ticketing.md), step 3.
- Check in: [UC-SC08-12](../../use-cases/05-events/uc-sc08-12-run-events-and-ticketing.md), step 4.

## States

- Normal: events with tickets, places and check-ins.
- Empty: "No event".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, sold out: guests go on a waiting list.
- Read-only: a past event is read-only.
- Offline: door scans follow the ticketing model's offline rule,
  [UC-F5-18](../../../../02-functional/f05-social-media/use-cases/07-events-and-ticketing/uc-f05-18-sell-at-the-box-office-and-scan-tickets.md).

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC08-05 Events](../../flows/fl-sc08-05-events.md)

## Open questions

None.

---

⬅️ [S-SC08-11 Volunteer time](../04-volunteers/s-sc08-11-volunteer-time.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-13 Temporary bar](s-sc08-13-temporary-bar.md)
