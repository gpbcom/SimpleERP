🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-07 Prepare and capture anywhere](README.md) › 🖥️ S-F4-13 Softphone

# 🖥️ S-F4-13 Softphone

**Status:** ✅ specified

## Personas

See its use case.

## Purpose

Call from simple-ERP (UC-F4-16).

## Entry points

A phone number on any record; the phone app.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-07 step 3, U03 | desktop | ![FL-F4-07 step 3, U03, light](../../images/07-prepare-and-capture-anywhere/u03-sales/3-softphone-call-desktop-light.png) | ![FL-F4-07 step 3, U03, dark](../../images/07-prepare-and-capture-anywhere/u03-sales/3-softphone-call-desktop-dark.png) |
| FL-F4-07 step 3, U03 | phone | ![FL-F4-07 step 3, U03, light](../../images/07-prepare-and-capture-anywhere/u03-sales/3-softphone-call-phone-light.png) | ![FL-F4-07 step 3, U03, dark](../../images/07-prepare-and-capture-anywhere/u03-sales/3-softphone-call-phone-dark.png) |
| Error E1, U03 | desktop | ![Error E1, U03, light](../../images/07-prepare-and-capture-anywhere/u03-sales/e1-sip-registration-failed-desktop-light.png) | ![Error E1, U03, dark](../../images/07-prepare-and-capture-anywhere/u03-sales/e1-sip-registration-failed-desktop-dark.png) |
| Error E1, U03 | phone | ![Error E1, U03, light](../../images/07-prepare-and-capture-anywhere/u03-sales/e1-sip-registration-failed-phone-light.png) | ![Error E1, U03, dark](../../images/07-prepare-and-capture-anywhere/u03-sales/e1-sip-registration-failed-phone-dark.png) |
| Error E1, U03 | tablet | ![Error E1, U03, light](../../images/07-prepare-and-capture-anywhere/u03-sales/e1-sip-registration-failed-tablet-light.png) | ![Error E1, U03, dark](../../images/07-prepare-and-capture-anywhere/u03-sales/e1-sip-registration-failed-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-13-softphone-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-13-softphone-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-13-softphone-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-13-softphone-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-13-softphone-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-13-softphone-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-13-softphone-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-13-softphone-offline-phone-dark.png) |

## Fields and columns

Dial pad, contact, recording state.

## Actions

As its use case's main flow.

## States

- Normal: Call from simple-ERP (UC-F4-16), as the wireframe shows.
- Empty: no call history yet, with the dial pad.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users without a phone line.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F4-01 Meeting](../../data/e-f04-01-meeting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U03 | `u03-sales/s-f04-13-softphone-e-f04-01-meeting-planned-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U03 | `u03-sales/s-f04-13-softphone-e-f04-01-meeting-live-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U03 | `u03-sales/s-f04-13-softphone-e-f04-01-meeting-ended-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U03 | `u03-sales/s-f04-13-softphone-e-f04-01-meeting-waiting-for-review-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-f04-13-softphone-e-f04-01-meeting-checked-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-F4-12 Interview evaluation](../09-score-calls-and-interviews/s-f04-12-interview-evaluation.md) ·
⬆️ [Up](README.md) · ➡️ [S-F4-14 Meeting automations](../08-share-and-reuse-outside/s-f04-14-meeting-automations.md)
