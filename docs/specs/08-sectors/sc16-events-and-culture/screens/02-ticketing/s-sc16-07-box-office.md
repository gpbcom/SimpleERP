🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-02 Ticketing](README.md) › 🖥️ S-SC16-07 Box office

# 🖥️ S-SC16-07 Box office

**Status:** ✅ specified

## Personas

- [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md)

## Purpose

Used to run the box office on the day
([UC-SC16-07](../../use-cases/02-ticketing/uc-sc16-07-run-the-box-office-on-the-day.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-02 step 2, U44 | desktop | ![FL-SC16-02 step 2, U44, light](../../images/02-ticketing/u44-box-office-agent/2-box-office-desktop-light.png) | ![FL-SC16-02 step 2, U44, dark](../../images/02-ticketing/u44-box-office-agent/2-box-office-desktop-dark.png) |
| FL-SC16-02 step 2, U44 | phone | ![FL-SC16-02 step 2, U44, light](../../images/02-ticketing/u44-box-office-agent/2-box-office-phone-light.png) | ![FL-SC16-02 step 2, U44, dark](../../images/02-ticketing/u44-box-office-agent/2-box-office-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-07-box-office-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-07-box-office-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-07-box-office-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-07-box-office-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-07-box-office-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-07-box-office-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-07-box-office-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-07-box-office-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-08 Admission ticket](../../data/e-sc16-08-admission-ticket.md), shown as the entity pages list
them, with their examples.

## Actions

- Sell: [UC-SC16-07](../../use-cases/02-ticketing/uc-sc16-07-run-the-box-office-on-the-day.md), step 1.
- Exchange: [UC-SC16-07](../../use-cases/02-ticketing/uc-sc16-07-run-the-box-office-on-the-day.md), step 2.
- Hand out will-call: [UC-SC16-07](../../use-cases/02-ticketing/uc-sc16-07-run-the-box-office-on-the-day.md), step 3.
- Close the till: [UC-SC16-07](../../use-cases/02-ticketing/uc-sc16-07-run-the-box-office-on-the-day.md), step 4.

## States

- Normal: the day's sales, exchanges and will-call.
- Empty: "No sale today".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, sold out: the buyer goes on the waiting list.
- Read-only: a closed till is read-only.
- Offline: the till keeps selling offline what it was given,
  [UC-F10-14](../../../../02-functional/f10-point-of-sale/use-cases/06-mobile-and-delivery/uc-f10-14-sell-on-the-move-and-offline.md);
  seats sync later.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

⬅️ [S-SC16-06 Access control](s-sc16-06-access-control.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-08 Accreditations](../03-people-and-partners/s-sc16-08-accreditations.md)
