🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-13 Outside people and follow-up](README.md) ›
🖥️ S-F4-22 Speaker requests

# 🖥️ S-F4-22 Speaker requests

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Register and handle outside speakers' objection and erasure requests.

## Entry points

Meeting settings › Speaker requests.

## Wireframe

```text
+------------------------------------------------------------------+
| Speaker requests                                 [+ Request]     |
| Person              Kind      Meetings  Due         Status       |
| J. Morel, Lemoine   erasure   2         2026-12-12  14 passages  |
|                       [Remove] [Restrict with reason] [Answer]   |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-13 step 1, U07 | desktop | ![FL-F4-13 step 1, U07, light](../../images/13-outside-people-and-follow-up/u07-administrator/1-speaker-requests-desktop-light.png) | ![FL-F4-13 step 1, U07, dark](../../images/13-outside-people-and-follow-up/u07-administrator/1-speaker-requests-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/13-outside-people-and-follow-up/u07-administrator/e1-speaker-requests-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/13-outside-people-and-follow-up/u07-administrator/e1-speaker-requests-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-22-speaker-requests-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-22-speaker-requests-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-22-speaker-requests-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-22-speaker-requests-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-22-speaker-requests-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-22-speaker-requests-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f04-22-speaker-requests-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f04-22-speaker-requests-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Person, kind, meetings, due, outcome | E-F4-14 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Remove, restrict | administrator | Passages handled |
| Answer | administrator | Person told |

## States

- Normal: register and handle outside speakers' objection and erasure requests.
- Empty: "No request from outside speakers".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: answered requests.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F4-14 Speaker request](../../data/e-f04-14-speaker-request.md),
[E-F4-02 Transcript](../../data/e-f04-02-transcript.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-14 Speaker request | Received | Badge "Received"; a new record starts here; next: Done or Refused (UC-F4-23); fields editable within the role | U07 | `u07-administrator/s-f04-22-speaker-requests-e-f04-14-speaker-request-received-desktop-{light,dark}.png` |
| E-F4-14 Speaker request | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f04-22-speaker-requests-e-f04-14-speaker-request-done-desktop-{light,dark}.png` |
| E-F4-14 Speaker request | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f04-22-speaker-requests-e-f04-14-speaker-request-refused-desktop-{light,dark}.png` |
| E-F4-02 Transcript | Live | Badge "Live"; a new record starts here; next: Complete (BR-F4-03); fields editable within the role | U07 | `u07-administrator/s-f04-22-speaker-requests-e-f04-02-transcript-live-desktop-{light,dark}.png` |
| E-F4-02 Transcript | Complete | Badge "Complete"; next: Checked (BR-F4-03); fields editable within the role | U07 | `u07-administrator/s-f04-22-speaker-requests-e-f04-02-transcript-complete-desktop-{light,dark}.png` |
| E-F4-02 Transcript | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f04-22-speaker-requests-e-f04-02-transcript-checked-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F4-13 Outside people and follow-up](../../flows/fl-f04-13-outside-people-and-follow-up.md)

## Open questions

None.

---

⬅️ [S-F4-21 Client video meeting](../12-rooms-and-client-video/s-f04-21-client-video-meeting.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-23 Agreed actions](s-f04-23-agreed-actions.md)
