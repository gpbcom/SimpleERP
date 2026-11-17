🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-07 Prepare and capture anywhere](README.md) ›
🖥️ S-F4-09 Desktop recorder

# 🖥️ S-F4-09 Desktop recorder

**Status:** ✅ specified

## Personas

See its use case.

## Purpose

Capture without a bot, upload a file (UC-F4-10).

## Entry points

The desktop app; Meetings › Upload.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-07 step 2, U02 | desktop | ![FL-F4-07 step 2, U02, light](../../images/07-prepare-and-capture-anywhere/u02-manager/2-desktop-capture-or-upload-desktop-light.png) | ![FL-F4-07 step 2, U02, dark](../../images/07-prepare-and-capture-anywhere/u02-manager/2-desktop-capture-or-upload-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-09-desktop-recorder-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-09-desktop-recorder-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-09-desktop-recorder-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-09-desktop-recorder-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-09-desktop-recorder-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-09-desktop-recorder-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-09-desktop-recorder-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-09-desktop-recorder-offline-phone-dark.png) |

## Fields and columns

Confirmation, timer, notice state; upload progress.

## Actions

As its use case's main flow.

## States

- Normal: Capture without a bot, upload a file (UC-F4-10), as the wireframe shows.
- Empty: nothing captured yet, with Record and Upload a file.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: an uploaded file being transcribed.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F4-01 Meeting](../../data/e-f04-01-meeting.md),
[E-F4-18 Recording notice](../../data/e-f04-18-recording-notice.md),
[E-F4-02 Transcript](../../data/e-f04-02-transcript.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U02 | `u02-manager/s-f04-09-desktop-recorder-e-f04-01-meeting-planned-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U02 | `u02-manager/s-f04-09-desktop-recorder-e-f04-01-meeting-live-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U02 | `u02-manager/s-f04-09-desktop-recorder-e-f04-01-meeting-ended-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U02 | `u02-manager/s-f04-09-desktop-recorder-e-f04-01-meeting-waiting-for-review-{desktop,phone}-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f04-09-desktop-recorder-e-f04-01-meeting-checked-{desktop,phone}-{light,dark}.png` |
| E-F4-18 Recording notice | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02 | `u02-manager/s-f04-09-desktop-recorder-e-f04-18-recording-notice-active-{desktop,phone}-{light,dark}.png` |
| E-F4-02 Transcript | Live | Badge "Live"; a new record starts here; next: Complete (BR-F4-03); fields editable within the role | U02 | `u02-manager/s-f04-09-desktop-recorder-e-f04-02-transcript-live-{desktop,phone}-{light,dark}.png` |
| E-F4-02 Transcript | Complete | Badge "Complete"; next: Checked (BR-F4-03); fields editable within the role | U02 | `u02-manager/s-f04-09-desktop-recorder-e-f04-02-transcript-complete-{desktop,phone}-{light,dark}.png` |
| E-F4-02 Transcript | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f04-09-desktop-recorder-e-f04-02-transcript-checked-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; phone where the use case says so.

## Accessibility

Labelled controls; scores and states as text, never colour alone.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [FL-F4-07 Prepare and capture anywhere](../../flows/fl-f04-07-prepare-and-capture-anywhere.md)

## Open questions

None.

---

⬅️ [S-F4-08 Meeting prep brief](s-f04-08-meeting-prep-brief.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-10 Share and export](../08-share-and-reuse-outside/s-f04-10-share-and-export.md)
