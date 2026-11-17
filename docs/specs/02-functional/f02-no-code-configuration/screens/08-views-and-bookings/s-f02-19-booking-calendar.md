🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-08 Views and bookings](README.md) › 🖥️ S-F2-19 Booking calendar

# 🖥️ S-F2-19 Booking calendar

**Status:** ✅ specified

## Personas

- [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md)
- [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md)
- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

See what is free and book a resource.

## Entry points

The bookable record type's menu; Book on a linked record; the portal or booking page.

## Wireframe

```text
+------------------------------------------------------------------+
| Booking calendar   [Rooms v]  Dec 18 - Dec 20     [Find a slot]  |
|          Thu 18          Fri 19          Sat 20                  |
| Room 203 [Martin......] [..............]                         |
| Room 204 [free.........][free..........] [Garnier]               |
| Room 205 [Leroy..................................]               |
| New booking: Room 204, 18 Dec 15:00 to 20 Dec 11:00              |
|   For [ M. Garnier v ]  Linked to [ Stay 3381 ]   [Book]         |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-08 step 3, U28 | desktop | ![FL-F2-08 step 3, U28, light](../../images/08-views-and-bookings/u28-hotel-receptionist/3-booking-calendar-desktop-light.png) | ![FL-F2-08 step 3, U28, dark](../../images/08-views-and-bookings/u28-hotel-receptionist/3-booking-calendar-desktop-dark.png) |
| FL-F2-08 step 3, U28 | tablet | ![FL-F2-08 step 3, U28, light](../../images/08-views-and-bookings/u28-hotel-receptionist/3-booking-calendar-tablet-light.png) | ![FL-F2-08 step 3, U28, dark](../../images/08-views-and-bookings/u28-hotel-receptionist/3-booking-calendar-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-19-booking-calendar-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-19-booking-calendar-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-19-booking-calendar-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-19-booking-calendar-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-19-booking-calendar-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-19-booking-calendar-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-f02-19-booking-calendar-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-f02-19-booking-calendar-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Resources, slots, bookings | E-F2-18, E-F2-17 | book, change, cancel |

## Actions

| Action | Who | Result |
|---|---|---|
| Book | users with the right, portal users | Booking confirmed or requested |
| Change, cancel | the booker, the resource's owner | Within the rules |

## States

- Normal: see what is free and book a resource.
- Empty: no resource yet in this record type: Add a resource.
- Loading: the grid's slots greyed until availability arrives.
- Error: the error message pattern (D122).
- Read-only: bookings of others, outside one's record rules: shown as busy without details.
- Offline: Not available offline: availability is live, to avoid double bookings
  ([BR-F2-18](../../business-rules/br-f02-18-one-booking-per-resource-and-slot.md)).

Shown entities (VD-15): [E-F2-17 Bookable resource setting](../../data/e-f02-17-bookable-resource-setting.md),
[E-F2-18 Resource booking](../../data/e-f02-18-resource-booking.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-17 Bookable resource setting | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-18); fields editable within the role | U28, U33 | `u28-hotel-receptionist/s-f02-19-booking-calendar-e-f02-17-bookable-resource-setting-draft-{desktop,tablet}-{light,dark}.png`, `u33-medical-secretary/s-f02-19-booking-calendar-e-f02-17-bookable-resource-setting-draft-desktop-{light,dark}.png` |
| E-F2-17 Bookable resource setting | Published | Badge "Published"; next: Archived (UC-F2-18); fields editable within the role | U28, U33 | `u28-hotel-receptionist/s-f02-19-booking-calendar-e-f02-17-bookable-resource-setting-published-{desktop,tablet}-{light,dark}.png`, `u33-medical-secretary/s-f02-19-booking-calendar-e-f02-17-bookable-resource-setting-published-desktop-{light,dark}.png` |
| E-F2-17 Bookable resource setting | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U28, U33 | `u28-hotel-receptionist/s-f02-19-booking-calendar-e-f02-17-bookable-resource-setting-archived-{desktop,tablet}-{light,dark}.png`, `u33-medical-secretary/s-f02-19-booking-calendar-e-f02-17-bookable-resource-setting-archived-desktop-{light,dark}.png` |
| E-F2-18 Resource booking | Requested | Badge "Requested"; a new record starts here; next: Confirmed (UC-F2-19); fields editable within the role | U28, U33 | `u28-hotel-receptionist/s-f02-19-booking-calendar-e-f02-18-resource-booking-requested-{desktop,tablet}-{light,dark}.png`, `u33-medical-secretary/s-f02-19-booking-calendar-e-f02-18-resource-booking-requested-desktop-{light,dark}.png` |
| E-F2-18 Resource booking | Confirmed | Badge "Confirmed"; a new record starts here; next: Cancelled, Done or No show (UC-F2-19); fields editable within the role | U28, U33 | `u28-hotel-receptionist/s-f02-19-booking-calendar-e-f02-18-resource-booking-confirmed-{desktop,tablet}-{light,dark}.png`, `u33-medical-secretary/s-f02-19-booking-calendar-e-f02-18-resource-booking-confirmed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop, tablet and phone: on a phone, one resource per day as a list.

## Accessibility

Every status is a word, not only a colour; drag and drop has a keyboard equivalent; fields have labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-08 Views and bookings](../../flows/fl-f02-08-views-and-bookings.md)

## Open questions

None.

---

⬅️ [S-F2-18 Booking settings](s-f02-18-booking-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-20 Portal settings](../09-portals-and-offline-forms/s-f02-20-portal-settings.md)
