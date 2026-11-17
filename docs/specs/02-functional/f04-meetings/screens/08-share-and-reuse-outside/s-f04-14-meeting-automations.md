🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-08 Share and reuse outside](README.md) ›
🖥️ S-F4-14 Meeting automations

# 🖥️ S-F4-14 Meeting automations

**Status:** ✅ specified

## Personas

See its use case.

## Purpose

Meeting integrations and digests (UC-F4-14, UC-F4-15).

## Entry points

Administration › Meetings › Automations; the AI assistant.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-08 step 2, U07 | desktop | ![FL-F4-08 step 2, U07, light](../../images/08-share-and-reuse-outside/u07-administrator/2-outside-tools-desktop-light.png) | ![FL-F4-08 step 2, U07, dark](../../images/08-share-and-reuse-outside/u07-administrator/2-outside-tools-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/08-share-and-reuse-outside/u07-administrator/e1-tool-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/08-share-and-reuse-outside/u07-administrator/e1-tool-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-14-meeting-automations-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-14-meeting-automations-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-14-meeting-automations-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-14-meeting-automations-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-14-meeting-automations-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-14-meeting-automations-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f04-14-meeting-automations-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f04-14-meeting-automations-offline-desktop-dark.png) |

## Fields and columns

Tools with allowed content; digests and their schedules.

## Actions

As its use case's main flow.

## States

- Normal: Meeting integrations and digests (UC-F4-14, UC-F4-15), as the wireframe shows.
- Empty: No automation yet, with Add an automation.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users other than administrators.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F4-09 Scheduled digest](../../data/e-f04-09-scheduled-digest.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-09 Scheduled digest | Active | Badge "Active"; a new record starts here; next: Paused (UC-F4-15); fields editable within the role | U02, U03, U07, U12, U13 | `u02-manager/s-f04-14-meeting-automations-e-f04-09-scheduled-digest-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-14-meeting-automations-e-f04-09-scheduled-digest-active-{desktop,phone,tablet}-{light,dark}.png`, `u07-administrator/s-f04-14-meeting-automations-e-f04-09-scheduled-digest-active-desktop-{light,dark}.png`, `u12-marketing/s-f04-14-meeting-automations-e-f04-09-scheduled-digest-active-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f04-14-meeting-automations-e-f04-09-scheduled-digest-active-{desktop,phone}-{light,dark}.png` |
| E-F4-09 Scheduled digest | Paused | Badge "Paused"; next: Active (UC-F4-15); fields editable within the role | U02, U03, U07, U12, U13 | `u02-manager/s-f04-14-meeting-automations-e-f04-09-scheduled-digest-paused-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-14-meeting-automations-e-f04-09-scheduled-digest-paused-{desktop,phone,tablet}-{light,dark}.png`, `u07-administrator/s-f04-14-meeting-automations-e-f04-09-scheduled-digest-paused-desktop-{light,dark}.png`, `u12-marketing/s-f04-14-meeting-automations-e-f04-09-scheduled-digest-paused-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f04-14-meeting-automations-e-f04-09-scheduled-digest-paused-{desktop,phone}-{light,dark}.png` |

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

- [FL-F4-08 Share and reuse outside](../../flows/fl-f04-08-share-and-reuse-outside.md)

## Open questions

None.

---

⬅️ [S-F4-13 Softphone](../07-prepare-and-capture-anywhere/s-f04-13-softphone.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-15 Chat](../10-benchmark-additions/s-f04-15-chat.md)
