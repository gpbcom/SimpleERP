🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-07 Forum, live chat, voice and support contracts](README.md) › 🖥️ S-F16-18 Voice agent

# 🖥️ S-F16-18 Voice agent

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): the call, from their phone.
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): the calls handled and the transfers.

## Purpose

Set the voice agent's number, announcement and languages, and review each call it handled.

## Entry points

Customer support agents › Voice agent; Meetings › Phone numbers.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Voice agent        Number +33 1 23 45 67 89     Languages fr, en    Hours 24/7      [Edit]  |
|---------------------------------------------------------------------------------------------|
| Announcement: "You speak with an AI. This call may be recorded. Say agent for a person."    |
| TIME   CALLER         INTENT           OUTCOME         CONFIDENCE  RECORDING                |
| 10:42  +33 6 12 ..    Parcel status    Answered        0.94        Kept 30 days             |
| 10:51  +33 6 98 ..    Refund           Transferred     0.61        Kept 30 days             |
| [Open call] [Listen] [Transcript] [Create request]                                          |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-07 step 3, U09 | phone | ![FL-F16-07 step 3, U09, light](../../images/07-live-chat-voice-and-contracts/u09-customer/3-voice-agent-phone-light.png) | ![FL-F16-07 step 3, U09, dark](../../images/07-live-chat-voice-and-contracts/u09-customer/3-voice-agent-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f16-18-voice-agent-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f16-18-voice-agent-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f16-18-voice-agent-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f16-18-voice-agent-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f16-18-voice-agent-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f16-18-voice-agent-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-18-voice-agent-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-18-voice-agent-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Number and languages | telephony number, languages | text | owner | yes |
| Announcement | announcement text per language | text | owner | yes |
| Call | time, caller, intent | text | no | yes |
| Outcome | answered, transferred, dropped, request | badge | no | yes |
| Confidence | number | 0 to 1 | no | no |
| Recording | retention | text | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Edit | header | owner | changes the number, the languages and the announcement |
| Listen or read | row | supervisor | opens the recording or the transcript |
| Create request | row | supervisor | turns the call into a request |
| Transfer to a person | call | caller by voice | the call goes to an agent |

## States

- Normal: the voice agent's settings and the calls with intent, outcome and confidence.
- Empty: No call yet, with the number to dial.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a call that
  failed to route shows the number and the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

The caller uses a phone call. The review screen is desktop only.

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

⬅️ [S-F16-17 Live chat](s-f16-17-live-chat.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-19 Proactive outreach](s-f16-19-proactive-outreach.md)
