🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-08 Views and bookings](README.md) › 🖥️ S-F2-18 Booking settings

# 🖥️ S-F2-18 Booking settings

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Make a record type bookable and set its hours, slots, capacity and rules.

## Entry points

A record type › Make bookable.

## Wireframe

```text
+------------------------------------------------------------------+
| Consulting rooms › Bookable                          [On]        |
| Hours  Mon-Fri 08:00-20:00   Sat 08:00-12:00                     |
| Slot [15 min v]  Capacity [1]  Buffer [5 min]                    |
| Book up to [60] days ahead   Cancel [24] h before                |
| Who books  [x] Users [x] Portal [ ] Public page                  |
| Creates    [ ] Invoice line  [x] Task for the practitioner       |
|                                       [Preview] [Publish]        |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-08 step 2, U07 | desktop | ![FL-F2-08 step 2, U07, light](../../images/08-views-and-bookings/u07-administrator/2-booking-settings-desktop-light.png) | ![FL-F2-08 step 2, U07, dark](../../images/08-views-and-bookings/u07-administrator/2-booking-settings-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-18-booking-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-18-booking-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-18-booking-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-18-booking-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-18-booking-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-18-booking-settings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-18-booking-settings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-18-booking-settings-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Hours, slot, capacity, buffer, rules | E-F2-17 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Publish | configurator | Record type bookable |

## States

- Normal: make a record type bookable and set its hours, slots, capacity and rules.
- Empty: not bookable yet: Make bookable.
- Loading: placeholders in the form.
- Error: the error message pattern (D122).
- Read-only: for users who are not configurators.
- Offline: Not available offline: a configuration screen on live, shared settings
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F2-05 Record type](../../data/e-f02-05-record-type.md),
[E-F2-17 Bookable resource setting](../../data/e-f02-17-bookable-resource-setting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-05 Record type | Draft | Badge "Draft"; a new record starts here; next: Live (UC-F2-04); fields editable within the role | U07 | `u07-administrator/s-f02-18-booking-settings-e-f02-05-record-type-draft-desktop-{light,dark}.png` |
| E-F2-05 Record type | Live | Badge "Live"; next: Archived (UC-F2-04); fields editable within the role | U07 | `u07-administrator/s-f02-18-booking-settings-e-f02-05-record-type-live-desktop-{light,dark}.png` |
| E-F2-05 Record type | Archived | Badge "Archived"; next: Live (UC-F2-04); fields editable within the role | U07 | `u07-administrator/s-f02-18-booking-settings-e-f02-05-record-type-archived-desktop-{light,dark}.png` |
| E-F2-17 Bookable resource setting | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-18); fields editable within the role | U07 | `u07-administrator/s-f02-18-booking-settings-e-f02-17-bookable-resource-setting-draft-desktop-{light,dark}.png` |
| E-F2-17 Bookable resource setting | Published | Badge "Published"; next: Archived (UC-F2-18); fields editable within the role | U07 | `u07-administrator/s-f02-18-booking-settings-e-f02-17-bookable-resource-setting-published-desktop-{light,dark}.png` |
| E-F2-17 Bookable resource setting | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-18-booking-settings-e-f02-17-bookable-resource-setting-archived-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; drag and drop has a keyboard equivalent; fields have labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-08 Views and bookings](../../flows/fl-f02-08-views-and-bookings.md)

## Open questions

None.

---

⬅️ [S-F2-17 View designer](s-f02-17-view-designer.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-19 Booking calendar](s-f02-19-booking-calendar.md)
