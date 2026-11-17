🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-14 Video messages, webinars and templates](README.md) ›
🖥️ S-F4-25 Video message

# 🖥️ S-F4-25 Video message

**Status:** ✅ specified

## Personas

- - [U03 Sales](../../../../01-users/personas/u03-sales.md): messages to customers.
- - [U01 Employee](../../../../01-users/personas/u01-employee.md): messages to colleagues, on a phone.

## Purpose

Record, preview, share and follow a video message.

## Entry points

A record's menu › Video message; Meetings › Video messages; the phone app.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Video message                         Source: screen and camera      [Record] [Stop]        |
| ------------------------------------------------------------------------------------------- |
| PREVIEW  [ video 2:10 ]   Cut start [0:04]  Cut end [2:08]                                  |
| SUMMARY  Walk-through of quote 2031: the option B price and the delivery date.              |
| SHARE    With: customer Dupont SA    Link ends: 2026-12-14    Password [ ]   [Share]        |
| VIEWS    Opened 2 times, 2 min 10 at most                                                   |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-14 step 1, U03 | desktop | ![FL-F4-14 step 1, U03, light](../../images/14-video-messages-and-webinars/u03-sales/1-video-message-desktop-light.png) | ![FL-F4-14 step 1, U03, dark](../../images/14-video-messages-and-webinars/u03-sales/1-video-message-desktop-dark.png) |
| FL-F4-14 step 1, U03 | desktop | ![FL-F4-14 step 1, U03, light](../../images/14-video-messages-and-webinars/u03-sales/1-video-message-desktop-light.png) | ![FL-F4-14 step 1, U03, dark](../../images/14-video-messages-and-webinars/u03-sales/1-video-message-desktop-dark.png) |
| FL-F4-14 step 1, U03 | phone | ![FL-F4-14 step 1, U03, light](../../images/14-video-messages-and-webinars/u03-sales/1-video-message-phone-light.png) | ![FL-F4-14 step 1, U03, dark](../../images/14-video-messages-and-webinars/u03-sales/1-video-message-phone-dark.png) |
| FL-F4-14 step 1, U03 | tablet | ![FL-F4-14 step 1, U03, light](../../images/14-video-messages-and-webinars/u03-sales/1-video-message-tablet-light.png) | ![FL-F4-14 step 1, U03, dark](../../images/14-video-messages-and-webinars/u03-sales/1-video-message-tablet-dark.png) |
| Error E1, U03 | desktop | ![Error E1, U03, light](../../images/14-video-messages-and-webinars/u03-sales/e1-the-recording-fails-desktop-light.png) | ![Error E1, U03, dark](../../images/14-video-messages-and-webinars/u03-sales/e1-the-recording-fails-desktop-dark.png) |
| Error E1, U03 | phone | ![Error E1, U03, light](../../images/14-video-messages-and-webinars/u03-sales/e1-the-recording-fails-phone-light.png) | ![Error E1, U03, dark](../../images/14-video-messages-and-webinars/u03-sales/e1-the-recording-fails-phone-dark.png) |
| Error E1, U03 | tablet | ![Error E1, U03, light](../../images/14-video-messages-and-webinars/u03-sales/e1-the-recording-fails-tablet-light.png) | ![Error E1, U03, dark](../../images/14-video-messages-and-webinars/u03-sales/e1-the-recording-fails-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-25-video-message-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-25-video-message-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-25-video-message-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-25-video-message-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-25-video-message-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-25-video-message-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-25-video-message-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-25-video-message-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Source | E-F4-27 source | screen, camera, both | yes | yes |
| Preview | E-F4-27 recording | video | cut only | yes |
| Summary | E-F4-27 summary | text | yes | no |
| Share with | E-F4-27 shared with | people or a link | yes | no |
| Link ends | E-F4-27 link ends | date | yes | yes |
| Views | E-F4-27 views | count and time | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Record, Stop | header | the user | the recording starts or ends |
| Share | share | the user | a link is created and sent |
| Stop sharing | share | the user | the link no longer opens |
| Delete | header | the user | the message is deleted (BR-F4-33) |

## States

- Normal: the recording controls, the preview, the summary and the share box.
- Empty: No message yet. Choose a source and record.
- Loading: The upload and the transcription show their progress.
- Error: the error message pattern (D122); a failed recording says why and offers Record again.
- Read-only: a message past its retention: its summary and view counts, without the video.
- Offline: A message recorded offline uploads when the network is back
  ([BR-F4-10](../../business-rules/br-f04-10-offline-recordings-upload-later.md)).

Shown entities (VD-15): [E-F4-27 Video message](../../data/e-f04-27-video-message.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-27 Video message | Recording | Badge "Recording"; a new record starts here; next: Uploaded (UC-F4-28); fields editable within the role | U03, U01 | `u03-sales/s-f04-25-video-message-e-f04-27-video-message-recording-{desktop,phone,tablet}-{light,dark}.png`, `u01-employee/s-f04-25-video-message-e-f04-27-video-message-recording-{desktop,phone}-{light,dark}.png` |
| E-F4-27 Video message | Uploaded | Badge "Uploaded"; next: Shared or Deleted (UC-F4-28, BR-F4-33); fields editable within the role | U03, U01 | `u03-sales/s-f04-25-video-message-e-f04-27-video-message-uploaded-{desktop,phone,tablet}-{light,dark}.png`, `u01-employee/s-f04-25-video-message-e-f04-27-video-message-uploaded-{desktop,phone}-{light,dark}.png` |
| E-F4-27 Video message | Shared | Badge "Shared"; next: Uploaded or Expired (UC-F4-28); fields editable within the role | U03, U01 | `u03-sales/s-f04-25-video-message-e-f04-27-video-message-shared-{desktop,phone,tablet}-{light,dark}.png`, `u01-employee/s-f04-25-video-message-e-f04-27-video-message-shared-{desktop,phone}-{light,dark}.png` |
| E-F4-27 Video message | Expired | Badge "Expired"; next: Deleted (BR-F4-33); fields editable within the role | U03, U01 | `u03-sales/s-f04-25-video-message-e-f04-27-video-message-expired-{desktop,phone,tablet}-{light,dark}.png`, `u01-employee/s-f04-25-video-message-e-f04-27-video-message-expired-{desktop,phone}-{light,dark}.png` |
| E-F4-27 Video message | Deleted | Badge "Deleted"; final: read-only, no next state; the history shows how it got here | U03, U01 | `u03-sales/s-f04-25-video-message-e-f04-27-video-message-deleted-{desktop,phone,tablet}-{light,dark}.png`, `u01-employee/s-f04-25-video-message-e-f04-27-video-message-deleted-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Works on a phone with the camera; screen recording needs a desktop.

## Accessibility

The recorded message carries captions; the controls are labelled buttons; the recording indicator is text and icon;
keyboard: record, stop.

## Components

- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [FL-F4-14 Video messages, webinars and templates](../../flows/fl-f04-14-video-messages-and-webinars.md)

## Open questions

None.

---

⬅️ [S-F4-24 Employee calendar](../s-f04-24-employee-calendar.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-26 Webinar](s-f04-26-webinar.md)
