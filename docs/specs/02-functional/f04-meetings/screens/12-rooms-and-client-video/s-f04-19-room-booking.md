🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-12 Rooms and client video](README.md) › 🖥️ S-F4-19 Room booking

# 🖥️ S-F4-19 Room booking

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Find and book a free meeting room with its equipment.

## Entry points

Book a room when planning a meeting; Meetings › Rooms.

## Wireframe

```text
+------------------------------------------------------------------+
| Book a room   Thu 14:00-15:00   People [8]   Needs [x] Screen    |
| Room          Site       Seats  Equipment        Free            |
| Room Loire    Lyon       10     screen, video    yes  [Book]     |
| Room Rhône    Lyon       12     screen           yes  [Book]     |
| Room Saône    Lyon       6      -                too small       |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-12 step 1, U01 | desktop | ![FL-F4-12 step 1, U01, light](../../images/12-rooms-and-client-video/u01-employee/1-room-booking-desktop-light.png) | ![FL-F4-12 step 1, U01, dark](../../images/12-rooms-and-client-video/u01-employee/1-room-booking-desktop-dark.png) |
| FL-F4-12 step 1, U01 | phone | ![FL-F4-12 step 1, U01, light](../../images/12-rooms-and-client-video/u01-employee/1-room-booking-phone-light.png) | ![FL-F4-12 step 1, U01, dark](../../images/12-rooms-and-client-video/u01-employee/1-room-booking-phone-dark.png) |
| Error E1, U01 | desktop | ![Error E1, U01, light](../../images/12-rooms-and-client-video/u01-employee/e1-room-booking-refused-desktop-light.png) | ![Error E1, U01, dark](../../images/12-rooms-and-client-video/u01-employee/e1-room-booking-refused-desktop-dark.png) |
| Error E1, U01 | phone | ![Error E1, U01, light](../../images/12-rooms-and-client-video/u01-employee/e1-room-booking-refused-phone-light.png) | ![Error E1, U01, dark](../../images/12-rooms-and-client-video/u01-employee/e1-room-booking-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-19-room-booking-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-19-room-booking-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-19-room-booking-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-19-room-booking-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-19-room-booking-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-19-room-booking-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-19-room-booking-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-19-room-booking-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Rooms, seats, equipment, free | E-F2-17, E-F2-18 | booking |

## Actions

| Action | Who | Result |
|---|---|---|
| Book | employees | Booked and added to the invitation |

## States

- Normal: find and book a free meeting room with its equipment.
- Empty: no meeting room set up: "Ask your administrator to make rooms bookable".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: rooms of other sites: shown, booked only with that site's right.
- Offline: Not available offline: availability is live,
  [BR-F2-18](../../../f02-no-code-configuration/business-rules/br-f02-18-one-booking-per-resource-and-slot.md).

Shown entities (VD-15):
[E-F2-17 Bookable resource setting](../../../f02-no-code-configuration/data/e-f02-17-bookable-resource-setting.md),
[E-F4-01 Meeting](../../data/e-f04-01-meeting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-17 Bookable resource setting | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-18); fields editable within the role | U01 | `u01-employee/s-f04-19-room-booking-e-f02-17-bookable-resource-setting-draft-{desktop,phone}-{light,dark}.png` |
| E-F2-17 Bookable resource setting | Published | Badge "Published"; next: Archived (UC-F2-18); fields editable within the role | U01 | `u01-employee/s-f04-19-room-booking-e-f02-17-bookable-resource-setting-published-{desktop,phone}-{light,dark}.png` |
| E-F2-17 Bookable resource setting | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U01 | `u01-employee/s-f04-19-room-booking-e-f02-17-bookable-resource-setting-archived-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U01 | `u01-employee/s-f04-19-room-booking-e-f04-01-meeting-planned-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U01 | `u01-employee/s-f04-19-room-booking-e-f04-01-meeting-live-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U01 | `u01-employee/s-f04-19-room-booking-e-f04-01-meeting-ended-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U01 | `u01-employee/s-f04-19-room-booking-e-f04-01-meeting-waiting-for-review-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U01 | `u01-employee/s-f04-19-room-booking-e-f04-01-meeting-checked-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F4-12 Rooms and client video](../../flows/fl-f04-12-rooms-and-client-video.md)

## Open questions

None.

---

⬅️ [S-F4-18 Topics](../11-insights-and-accessibility/s-f04-18-topics.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-20 Transcription accuracy](../11-insights-and-accessibility/s-f04-20-transcription-accuracy.md)
