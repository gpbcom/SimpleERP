🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-02 Record in person or by phone](README.md) › 🖥️ S-F4-04 Call

# 🖥️ S-F4-04 Call

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)
- Any user of the phone system

## Purpose

A call being recorded, and its record afterwards (D221, D222).

## Entry points

An incoming or outgoing call; the contact's Calls tab.

## Wireframe

```text
+------------------------------------------------------------------+
| Call with +33 4 72 .. .. ..   (o) Recorded          [Stop]        |
| Suggested: [J. Durand, Durand SA]  [Confirm] [Change]             |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-02 step 3, U03 | desktop | ![FL-F4-02 step 3, U03, light](../../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-desktop-light.png) | ![FL-F4-02 step 3, U03, dark](../../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-desktop-dark.png) |
| FL-F4-02 step 3, U03 | phone | ![FL-F4-02 step 3, U03, light](../../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-phone-light.png) | ![FL-F4-02 step 3, U03, dark](../../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-phone-dark.png) |
| FL-F4-02 step 3, U03 | tablet | ![FL-F4-02 step 3, U03, light](../../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-tablet-light.png) | ![FL-F4-02 step 3, U03, dark](../../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-04-call-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-04-call-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-04-call-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-04-call-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-04-call-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-04-call-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-04-call-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-04-call-offline-phone-dark.png) |

## Fields and columns

Number, contact suggested, recording state, duration.

## Actions

| Action | Who | Result |
|---|---|---|
| Stop | the user | Recording stops |
| Confirm or change the link | the user | BR-F4-12 |

## States

- Normal: A call being recorded, and its record afterwards (D221, D222), as the wireframe shows.
- Empty: no call yet today, with the dial pad.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: phone system unreachable (D122).
- Read-only: an ended call's record for users who did not take it.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.
- Ringing, recorded, stopped, ended.

Shown entities (VD-15): [E-F4-18 Recording notice](../../data/e-f04-18-recording-notice.md),
[E-F4-01 Meeting](../../data/e-f04-01-meeting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-18 Recording notice | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U04 | `u03-sales/s-f04-04-call-e-f04-18-recording-notice-active-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f04-04-call-e-f04-18-recording-notice-active-desktop-{light,dark}.png` |
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U03, U04 | `u03-sales/s-f04-04-call-e-f04-01-meeting-planned-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f04-04-call-e-f04-01-meeting-planned-desktop-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U03, U04 | `u03-sales/s-f04-04-call-e-f04-01-meeting-live-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f04-04-call-e-f04-01-meeting-live-desktop-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U03, U04 | `u03-sales/s-f04-04-call-e-f04-01-meeting-ended-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f04-04-call-e-f04-01-meeting-ended-desktop-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U03, U04 | `u03-sales/s-f04-04-call-e-f04-01-meeting-waiting-for-review-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f04-04-call-e-f04-01-meeting-waiting-for-review-desktop-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U03, U04 | `u03-sales/s-f04-04-call-e-f04-01-meeting-checked-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-f04-04-call-e-f04-01-meeting-checked-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

Recording state as text, not colour alone.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-06 Toast](../../../../04-ux/design-system/components/c-06-toast.md)

## Shown in

- [FL-F4-02 Record in person or by phone](../../flows/fl-f04-02-record-in-person-or-by-phone.md)

## Open questions

None.

---

⬅️ [S-F4-03 Phone recorder](s-f04-03-phone-recorder.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-05 Meeting review](../03-review-a-meeting/s-f04-05-meeting-review.md)
