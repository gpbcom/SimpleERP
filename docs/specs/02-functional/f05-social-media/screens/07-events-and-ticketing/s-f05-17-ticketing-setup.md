🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-07 Events and ticketing](README.md) › 🖥️ S-F5-17 Ticketing setup

# 🖥️ S-F5-17 Ticketing setup

**Status:** ✅ specified

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)
- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Purpose

Set sessions, ticket types, quotas and the seat map of an event.

## Entry points

An event › Ticketing.

## Wireframe

```text
+------------------------------------------------------------------+
| Season 2027 › 12 March 20:30          600 seats   Sale: open     |
| Ticket types: Full 32 EUR  Reduced 22 EUR  Pass                  |
| Quotas: online [450] box office [100] partners [50] until 03-05  |
|   STAGE                                                          |
|   A [x][x][ ][ ][ ][x] ...   category 1                         |
|   G [ ][ ][S][S][ ][ ] ...   S = sold                           |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-07 step 2, U43 | desktop | ![FL-F5-07 step 2, U43, light](../../images/07-events-and-ticketing/u43-event-producer/2-ticketing-setup-desktop-light.png) | ![FL-F5-07 step 2, U43, dark](../../images/07-events-and-ticketing/u43-event-producer/2-ticketing-setup-desktop-dark.png) |
| FL-F5-07 step 2, U43 | phone | ![FL-F5-07 step 2, U43, light](../../images/07-events-and-ticketing/u43-event-producer/2-ticketing-setup-phone-light.png) | ![FL-F5-07 step 2, U43, dark](../../images/07-events-and-ticketing/u43-event-producer/2-ticketing-setup-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-17-ticketing-setup-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-17-ticketing-setup-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-17-ticketing-setup-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-17-ticketing-setup-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-17-ticketing-setup-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-17-ticketing-setup-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-17-ticketing-setup-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-17-ticketing-setup-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Sessions, types, prices, quotas, seats | E-F5-11 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Open or close the sale | producer | Tickets on sale or not |

## States

- Normal: set sessions, ticket types, quotas and the seat map of an event.
- Empty: no session yet: Add a session.
- Loading: the seat map greyed until seat states arrive.
- Error: the error message pattern (D122).
- Read-only: a closed sale; prices of sold tickets.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F5-07 Registration event](../../data/e-f05-07-registration-event.md),
[E-F5-11 Ticket type and seat map](../../data/e-f05-11-ticket-type-and-seat-map.md),
[E-F5-20 Waiting list](../../data/e-f05-20-waiting-list.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-07 Registration event | Draft | Badge "Draft"; a new record starts here; next: Planned or Cancelled (UC-SC08-12); fields editable within the role | U43 | `u43-event-producer/s-f05-17-ticketing-setup-e-f05-07-registration-event-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-07 Registration event | Planned | Badge "Planned"; next: Published or Cancelled (UC-F5-11, UC-SC08-12); fields editable within the role | U43 | `u43-event-producer/s-f05-17-ticketing-setup-e-f05-07-registration-event-planned-{desktop,phone}-{light,dark}.png` |
| E-F5-07 Registration event | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U43 | `u43-event-producer/s-f05-17-ticketing-setup-e-f05-07-registration-event-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F5-07 Registration event | Published | Badge "Published"; next: Approved or Cancelled (UC-SC16-01, UC-SC08-12); fields editable within the role | U43 | `u43-event-producer/s-f05-17-ticketing-setup-e-f05-07-registration-event-published-{desktop,phone}-{light,dark}.png` |
| E-F5-07 Registration event | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U43 | `u43-event-producer/s-f05-17-ticketing-setup-e-f05-07-registration-event-approved-{desktop,phone}-{light,dark}.png` |
| E-F5-11 Ticket type and seat map | Draft | Badge "Draft"; a new record starts here; next: Closed (UC-F5-17); fields editable within the role | U43 | `u43-event-producer/s-f05-17-ticketing-setup-e-f05-11-ticket-type-and-seat-map-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-11 Ticket type and seat map | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U43 | `u43-event-producer/s-f05-17-ticketing-setup-e-f05-11-ticket-type-and-seat-map-closed-{desktop,phone}-{light,dark}.png` |
| E-F5-20 Waiting list | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U43 | `u43-event-producer/s-f05-17-ticketing-setup-e-f05-20-waiting-list-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F5-07 Events and ticketing](../../flows/fl-f05-07-events-and-ticketing.md)

## Open questions

None.

---

⬅️ [S-F5-16 Deliverability](../06-audiences-consent-and-journeys/s-f05-16-deliverability.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-18 Ticket scan](s-f05-18-ticket-scan.md)
