🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-07 Events and ticketing](README.md) › 🖥️ S-F5-11 Event

# 🖥️ S-F5-11 Event

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Organise events and sell tickets.

## Entry points

Social media and marketing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-07 step 1, U12 | desktop | ![FL-F5-07 step 1, U12, light](../../images/07-events-and-ticketing/u12-marketing/1-event-desktop-light.png) | ![FL-F5-07 step 1, U12, dark](../../images/07-events-and-ticketing/u12-marketing/1-event-desktop-dark.png) |
| FL-F5-07 step 1, U12 | phone | ![FL-F5-07 step 1, U12, light](../../images/07-events-and-ticketing/u12-marketing/1-event-phone-light.png) | ![FL-F5-07 step 1, U12, dark](../../images/07-events-and-ticketing/u12-marketing/1-event-phone-dark.png) |
| Error E1, U12 | desktop | ![Error E1, U12, light](../../images/07-events-and-ticketing/u12-marketing/e1-event-refused-desktop-light.png) | ![Error E1, U12, dark](../../images/07-events-and-ticketing/u12-marketing/e1-event-refused-desktop-dark.png) |
| Error E1, U12 | phone | ![Error E1, U12, light](../../images/07-events-and-ticketing/u12-marketing/e1-event-refused-phone-light.png) | ![Error E1, U12, dark](../../images/07-events-and-ticketing/u12-marketing/e1-event-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-11-event-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-11-event-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-11-event-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-11-event-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-11-event-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-11-event-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-11-event-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-11-event-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Organise events and sell tickets, as the wireframe shows.
- Empty: No event yet, with New event.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users without the marketing right; published items.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F5-07 Registration event](../../data/e-f05-07-registration-event.md),
[E-F5-11 Ticket type and seat map](../../data/e-f05-11-ticket-type-and-seat-map.md),
[E-F5-20 Waiting list](../../data/e-f05-20-waiting-list.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-07 Registration event | Draft | Badge "Draft"; a new record starts here; next: Planned or Cancelled (UC-SC08-12); fields editable within the role | U09, U12 | `u09-customer/s-f05-11-event-e-f05-07-registration-event-draft-phone-{light,dark}.png`, `u12-marketing/s-f05-11-event-e-f05-07-registration-event-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-07 Registration event | Planned | Badge "Planned"; next: Published or Cancelled (UC-F5-11, UC-SC08-12); fields editable within the role | U09, U12 | `u09-customer/s-f05-11-event-e-f05-07-registration-event-planned-phone-{light,dark}.png`, `u12-marketing/s-f05-11-event-e-f05-07-registration-event-planned-{desktop,phone}-{light,dark}.png` |
| E-F5-07 Registration event | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f05-11-event-e-f05-07-registration-event-cancelled-phone-{light,dark}.png`, `u12-marketing/s-f05-11-event-e-f05-07-registration-event-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F5-07 Registration event | Published | Badge "Published"; next: Approved or Cancelled (UC-SC16-01, UC-SC08-12); fields editable within the role | U09, U12 | `u09-customer/s-f05-11-event-e-f05-07-registration-event-published-phone-{light,dark}.png`, `u12-marketing/s-f05-11-event-e-f05-07-registration-event-published-{desktop,phone}-{light,dark}.png` |
| E-F5-07 Registration event | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f05-11-event-e-f05-07-registration-event-approved-phone-{light,dark}.png`, `u12-marketing/s-f05-11-event-e-f05-07-registration-event-approved-{desktop,phone}-{light,dark}.png` |
| E-F5-11 Ticket type and seat map | Draft | Badge "Draft"; a new record starts here; next: Closed (UC-F5-17); fields editable within the role | U09, U12 | `u09-customer/s-f05-11-event-e-f05-11-ticket-type-and-seat-map-draft-phone-{light,dark}.png`, `u12-marketing/s-f05-11-event-e-f05-11-ticket-type-and-seat-map-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-11 Ticket type and seat map | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U09, U12 | `u09-customer/s-f05-11-event-e-f05-11-ticket-type-and-seat-map-closed-phone-{light,dark}.png`, `u12-marketing/s-f05-11-event-e-f05-11-ticket-type-and-seat-map-closed-{desktop,phone}-{light,dark}.png` |
| E-F5-20 Waiting list | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U12 | `u09-customer/s-f05-11-event-e-f05-20-waiting-list-active-phone-{light,dark}.png`, `u12-marketing/s-f05-11-event-e-f05-20-waiting-list-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F5-05 Benchmark additions](../../flows/fl-f05-05-benchmark-additions.md)
- [FL-F5-07 Events and ticketing](../../flows/fl-f05-07-events-and-ticketing.md)

## Open questions

None.

---

⬅️ [S-F5-10 Journey designer](../06-audiences-consent-and-journeys/s-f05-10-journey-designer.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-12 Survey](../08-pages-forms-surveys-and-whatsapp/s-f05-12-survey.md)
