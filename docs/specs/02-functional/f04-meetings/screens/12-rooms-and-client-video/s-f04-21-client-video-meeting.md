🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-12 Rooms and client video](README.md) ›
🖥️ S-F4-21 Client video meeting

# 🖥️ S-F4-21 Client video meeting

**Status:** ✅ specified

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md)
- [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Hold a video meeting with a client, with a waiting room and consent to record.

## Entry points

The client's record or the appointment; the client's email or portal.

## Wireframe

```text
+------------------------------------------------------------------+
| Video: M. Garnier, 10:00            Waiting room: 1  [Let in]    |
| +---------------------------+  Record?  client: not asked        |
| |        video              |  [Ask consent]                     |
| +---------------------------+  Notes [                        ]  |
|                                   [End]                          |
+------------------------------------------------------------------+
Client (phone): "Your meeting with Dr Laurent starts soon. [Join]" 
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-12 step 2, U36 | desktop | ![FL-F4-12 step 2, U36, light](../../images/12-rooms-and-client-video/u36-professional/2-client-video-meeting-desktop-light.png) | ![FL-F4-12 step 2, U36, dark](../../images/12-rooms-and-client-video/u36-professional/2-client-video-meeting-desktop-dark.png) |
| FL-F4-12 step 2, U36 | phone | ![FL-F4-12 step 2, U36, light](../../images/12-rooms-and-client-video/u36-professional/2-client-video-meeting-phone-light.png) | ![FL-F4-12 step 2, U36, dark](../../images/12-rooms-and-client-video/u36-professional/2-client-video-meeting-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-21-client-video-meeting-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-21-client-video-meeting-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-21-client-video-meeting-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-21-client-video-meeting-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-21-client-video-meeting-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-21-client-video-meeting-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-21-client-video-meeting-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-21-client-video-meeting-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Client, waiting room, consent, notes | E-F4-16 | notes, consent |

## Actions

| Action | Who | Result |
|---|---|---|
| Let in | professional | Client joins |
| Ask consent | professional | Client accepts or refuses |
| End | professional | Notes linked to the record |

## States

- Normal: hold a video meeting with a client, with a waiting room and consent to record.
- Empty: no client yet: "Waiting for M. Garnier".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: an ended meeting and its notes.
- Offline: Not available offline: a live video meeting needs the network.

Shown entities (VD-15): [E-F4-01 Meeting](../../data/e-f04-01-meeting.md),
[E-F4-16 Client video meeting](../../data/e-f04-16-client-video-meeting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U09, U36 | `u09-customer/s-f04-21-client-video-meeting-e-f04-01-meeting-planned-phone-{light,dark}.png`, `u36-professional/s-f04-21-client-video-meeting-e-f04-01-meeting-planned-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U09, U36 | `u09-customer/s-f04-21-client-video-meeting-e-f04-01-meeting-live-phone-{light,dark}.png`, `u36-professional/s-f04-21-client-video-meeting-e-f04-01-meeting-live-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U09, U36 | `u09-customer/s-f04-21-client-video-meeting-e-f04-01-meeting-ended-phone-{light,dark}.png`, `u36-professional/s-f04-21-client-video-meeting-e-f04-01-meeting-ended-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U09, U36 | `u09-customer/s-f04-21-client-video-meeting-e-f04-01-meeting-waiting-for-review-phone-{light,dark}.png`, `u36-professional/s-f04-21-client-video-meeting-e-f04-01-meeting-waiting-for-review-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U09, U36 | `u09-customer/s-f04-21-client-video-meeting-e-f04-01-meeting-checked-phone-{light,dark}.png`, `u36-professional/s-f04-21-client-video-meeting-e-f04-01-meeting-checked-{desktop,phone}-{light,dark}.png` |
| E-F4-16 Client video meeting | Planned | Badge "Planned"; a new record starts here; next: Waiting (UC-F4-25); fields editable within the role | U09, U33, U36 | `u09-customer/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-planned-phone-{light,dark}.png`, `u33-medical-secretary/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-planned-desktop-{light,dark}.png`, `u36-professional/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-planned-{desktop,phone}-{light,dark}.png` |
| E-F4-16 Client video meeting | Waiting | Badge "Waiting"; next: Live (UC-F4-25); fields editable within the role | U09, U33, U36 | `u09-customer/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-waiting-phone-{light,dark}.png`, `u33-medical-secretary/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-waiting-desktop-{light,dark}.png`, `u36-professional/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-waiting-{desktop,phone}-{light,dark}.png` |
| E-F4-16 Client video meeting | Live | Badge "Live"; next: Ended (UC-F4-25); fields editable within the role | U09, U33, U36 | `u09-customer/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-live-phone-{light,dark}.png`, `u33-medical-secretary/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-live-desktop-{light,dark}.png`, `u36-professional/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-live-{desktop,phone}-{light,dark}.png` |
| E-F4-16 Client video meeting | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U09, U33, U36 | `u09-customer/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-ended-phone-{light,dark}.png`, `u33-medical-secretary/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-ended-desktop-{light,dark}.png`, `u36-professional/s-f04-21-client-video-meeting-e-f04-16-client-video-meeting-ended-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop, tablet and phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F4-12 Rooms and client video](../../flows/fl-f04-12-rooms-and-client-video.md)

## Open questions

None.

---

⬅️ [S-F4-20 Transcription accuracy](../11-insights-and-accessibility/s-f04-20-transcription-accuracy.md) ·
⬆️ [Up](README.md) · ➡️ [S-F4-22 Speaker requests](../13-outside-people-and-follow-up/s-f04-22-speaker-requests.md)
