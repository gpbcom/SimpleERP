🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-07 Forum, live chat, voice and support contracts](README.md) › 🖥️ S-F16-19 Proactive outreach

# 🖥️ S-F16-19 Proactive outreach

**Status:** 🔄 waiting for the owner

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): the outreaches they prepare and their
  replies.

## Purpose

Select the customers a known cause affects, write one message and follow the replies.

## Entry points

Customer support agents › Proactive outreach; a late-delivery alert.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Outreach: batch 7 delayed                              Draft     [Preview] [Approve] [Send]  |
|---------------------------------------------------------------------------------------------|
| Cause   Orders of batch 7, delayed 3 days        Audience  214 customers   Unreachable 6    |
| Channel Email, then SMS if it bounces            Send      2026-11-15 09:00 (quiet hours ok)|
| Message Hello {first name}, order {order} will arrive on {new date} ...                     |
| Sent 0   Delivered 0   Replies 0   Needs approval above 500 customers                       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-07 step 4, U16 | desktop | ![FL-F16-07 step 4, U16, light](../../images/07-live-chat-voice-and-contracts/u16-office-worker/4-proactive-outreach-desktop-light.png) | ![FL-F16-07 step 4, U16, dark](../../images/07-live-chat-voice-and-contracts/u16-office-worker/4-proactive-outreach-desktop-dark.png) |
| FL-F16-07 step 4, U16 | phone | ![FL-F16-07 step 4, U16, light](../../images/07-live-chat-voice-and-contracts/u16-office-worker/4-proactive-outreach-phone-light.png) | ![FL-F16-07 step 4, U16, dark](../../images/07-live-chat-voice-and-contracts/u16-office-worker/4-proactive-outreach-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-19-proactive-outreach-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-19-proactive-outreach-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-19-proactive-outreach-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-19-proactive-outreach-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-19-proactive-outreach-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-19-proactive-outreach-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-19-proactive-outreach-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-19-proactive-outreach-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Cause | E-F16-15 cause | text and selection | while Draft | yes |
| Audience | E-F16-15 audience | count and sample | no | yes |
| Channel and time | E-F16-15 channel, send time | text and date | while Draft | yes |
| Message | E-F16-15 message | text with variables | while Draft | yes |
| Counts | E-F16-15 sent, delivered, replies | numbers | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Preview | header | support | the message for three customers |
| Approve | header | second approver | the outreach may go out |
| Send | header | support | sends on each customer's channel |
| Cancel | header | support | stops a draft or an approved outreach |
| Close | header | support | ends the outreach when the cause is solved |

## States

- Normal: the cause, the audience, the message and, after sending, the counts and replies.
- Empty: No outreach yet, with New outreach.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused send
  shows the audience problem or the missing approval.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F16-15 Outreach](../../data/e-f16-15-outreach.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-15 Outreach | Draft | Badge "Draft"; a new record starts here; next: Approved or Cancelled (UC-F16-21); fields editable within the role | U16 | `u16-office-worker/s-f16-19-proactive-outreach-e-f16-15-outreach-draft-{desktop,phone}-{light,dark}.png` |
| E-F16-15 Outreach | Approved | Badge "Approved"; next: Sent or Cancelled (UC-F16-21); fields editable within the role | U16 | `u16-office-worker/s-f16-19-proactive-outreach-e-f16-15-outreach-approved-{desktop,phone}-{light,dark}.png` |
| E-F16-15 Outreach | Sent | Badge "Sent"; next: Closed (UC-F16-21); fields editable within the role | U16 | `u16-office-worker/s-f16-19-proactive-outreach-e-f16-15-outreach-sent-{desktop,phone}-{light,dark}.png` |
| E-F16-15 Outreach | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U16 | `u16-office-worker/s-f16-19-proactive-outreach-e-f16-15-outreach-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F16-15 Outreach | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U16 | `u16-office-worker/s-f16-19-proactive-outreach-e-f16-15-outreach-closed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F16-07](../../flows/fl-f16-07-live-chat-voice-and-contracts.md)

## Open questions

None.

---

⬅️ [S-F16-18 Voice agent](s-f16-18-voice-agent.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-20 Support contracts](s-f16-20-support-contracts.md)
