🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-02 Record in person or by phone](README.md) ›
🖥️ S-F4-03 Phone recorder

# 🖥️ S-F4-03 Phone recorder

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)
- Any internal participant

## Purpose

Record an in-person meeting, online or offline (D220).

## Entry points

"Record a meeting" on the phone app's Today or a task.

## Wireframe

```text
+------------------------------+
| < Record a meeting           |
| About: Visit V-212           |
| (o) RECORDING   00:12:41     |
| Offline: will upload later   |
|        [ STOP ]              |
+------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-02 step 1, U03 | desktop | ![FL-F4-02 step 1, U03, light](../../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-desktop-light.png) | ![FL-F4-02 step 1, U03, dark](../../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-desktop-dark.png) |
| FL-F4-02 step 1, U03 | phone | ![FL-F4-02 step 1, U03, light](../../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-phone-light.png) | ![FL-F4-02 step 1, U03, dark](../../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-phone-dark.png) |
| FL-F4-02 step 1, U03 | tablet | ![FL-F4-02 step 1, U03, light](../../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-tablet-light.png) | ![FL-F4-02 step 1, U03, dark](../../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-03-phone-recorder-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-03-phone-recorder-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-03-phone-recorder-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-03-phone-recorder-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-03-phone-recorder-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-03-phone-recorder-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-03-phone-recorder-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-03-phone-recorder-offline-phone-dark.png) |

## Fields and columns

Context, timer, network state.

## Actions

| Action | Who | Result |
|---|---|---|
| Start | participant | After confirming everyone was told |
| Stop | anyone | Recording ends |

## States

- Normal: Record an in-person meeting, online or offline (D220), as the wireframe shows.
- Empty: ready to record, with the consent reminder.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: microphone refused (D122).
- Read-only: an uploaded recording.
- Offline: Works offline: the phone records, keeps the audio encrypted and uploads it when the network is back, then
  removes it ([D220](../../../../06-decisions/f04-meetings/d220-offline-recording.md)).
- Asking to confirm, recording, offline, uploading, uploaded.

Shown entities (VD-15): [E-F4-01 Meeting](../../data/e-f04-01-meeting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U03, U14 | `u03-sales/s-f04-03-phone-recorder-e-f04-01-meeting-planned-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-f04-03-phone-recorder-e-f04-01-meeting-planned-phone-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U03, U14 | `u03-sales/s-f04-03-phone-recorder-e-f04-01-meeting-live-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-f04-03-phone-recorder-e-f04-01-meeting-live-phone-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U03, U14 | `u03-sales/s-f04-03-phone-recorder-e-f04-01-meeting-ended-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-f04-03-phone-recorder-e-f04-01-meeting-ended-phone-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U03, U14 | `u03-sales/s-f04-03-phone-recorder-e-f04-01-meeting-waiting-for-review-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-f04-03-phone-recorder-e-f04-01-meeting-waiting-for-review-phone-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U03, U14 | `u03-sales/s-f04-03-phone-recorder-e-f04-01-meeting-checked-{desktop,phone,tablet}-{light,dark}.png`, `u14-field-worker/s-f04-03-phone-recorder-e-f04-01-meeting-checked-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone; the same on a computer.

## Accessibility

A large Stop button; the state announced.

## Components

- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)

## Shown in

- [FL-F4-02 Record in person or by phone](../../flows/fl-f04-02-record-in-person-or-by-phone.md)

## Open questions

None.

---

⬅️ [S-F4-02 Live transcript](../01-record-an-online-meeting/s-f04-02-live-transcript.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-04 Call](s-f04-04-call.md)
