🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-07 Events and ticketing](README.md) › 🖥️ S-F5-18 Ticket scan

# 🖥️ S-F5-18 Ticket scan

**Status:** 🔄 waiting for the owner

## Personas

- [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md)
- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)

## Purpose

Scan tickets at the door and see the counts.

## Entry points

Events › Doors, on a phone.

## Wireframe

```text
+----------------------------+
| 12 Mar 20:30   scanned 412 |
|  [   camera viewfinder   ] |
|  G10  VALID  Full          |
|  (green)                   |
|  Last: G11 valid 20:05     |
+----------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-07 step 4, U44 | desktop | ![FL-F5-07 step 4, U44, light](../../images/07-events-and-ticketing/u44-box-office-agent/4-ticket-scan-desktop-light.png) | ![FL-F5-07 step 4, U44, dark](../../images/07-events-and-ticketing/u44-box-office-agent/4-ticket-scan-desktop-dark.png) |
| FL-F5-07 step 4, U44 | phone | ![FL-F5-07 step 4, U44, light](../../images/07-events-and-ticketing/u44-box-office-agent/4-ticket-scan-phone-light.png) | ![FL-F5-07 step 4, U44, dark](../../images/07-events-and-ticketing/u44-box-office-agent/4-ticket-scan-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-18-ticket-scan-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-18-ticket-scan-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-18-ticket-scan-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-18-ticket-scan-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-18-ticket-scan-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-18-ticket-scan-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-18-ticket-scan-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-18-ticket-scan-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Result, ticket, counts | E-F5-12 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Scan | door staff | Valid, already used or wrong session |

## States

- Normal: scan tickets at the door and see the counts.
- Empty: no ticket scanned yet: the counter shows 0.
- Loading: "Loading the session's tickets" before the first scan.
- Error: the error message pattern (D122).
- Read-only: always: a scan only reads and marks.
- Offline: Scans are checked against the ticket list loaded before the doors opened and synced when the network is back
  (Proposed); the screen shows Offline and the count waiting.

Shown entities (VD-15): [E-F5-11 Ticket type and seat map](../../data/e-f05-11-ticket-type-and-seat-map.md),
[E-F5-12 Event ticket](../../data/e-f05-12-event-ticket.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-11 Ticket type and seat map | Draft | Badge "Draft"; a new record starts here; next: Closed (UC-F5-17); fields editable within the role | U43, U44 | `u43-event-producer/s-f05-18-ticket-scan-e-f05-11-ticket-type-and-seat-map-draft-{desktop,phone}-{light,dark}.png`, `u44-box-office-agent/s-f05-18-ticket-scan-e-f05-11-ticket-type-and-seat-map-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-11 Ticket type and seat map | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U43, U44 | `u43-event-producer/s-f05-18-ticket-scan-e-f05-11-ticket-type-and-seat-map-closed-{desktop,phone}-{light,dark}.png`, `u44-box-office-agent/s-f05-18-ticket-scan-e-f05-11-ticket-type-and-seat-map-closed-{desktop,phone}-{light,dark}.png` |
| E-F5-12 Event ticket | Sold | Badge "Sold"; a new record starts here; next: Scanned or Refunded (UC-F5-18, UC-SC08-12); fields editable within the role | U44 | `u44-box-office-agent/s-f05-18-ticket-scan-e-f05-12-event-ticket-sold-{desktop,phone}-{light,dark}.png` |
| E-F5-12 Event ticket | Scanned | Badge "Scanned"; final: read-only, no next state; the history shows how it got here | U44 | `u44-box-office-agent/s-f05-18-ticket-scan-e-f05-12-event-ticket-scanned-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)

## Shown in

- [FL-F5-07 Events and ticketing](../../flows/fl-f05-07-events-and-ticketing.md)

## Open questions

None.

---

⬅️ [S-F5-17 Ticketing setup](s-f05-17-ticketing-setup.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-19 Landing page editor](../08-pages-forms-surveys-and-whatsapp/s-f05-19-landing-page-editor.md)
