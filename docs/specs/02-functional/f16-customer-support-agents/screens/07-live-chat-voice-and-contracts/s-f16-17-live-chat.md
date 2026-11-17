🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-07 Forum, live chat, voice and support contracts](README.md) › 🖥️ S-F16-17 Live chat

# 🖥️ S-F16-17 Live chat

**Status:** 🔄 waiting for the owner

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): the chats of their queue, with the
  transcript.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the chat window on their phone.

## Purpose

Chat with visitors, let the AI agent answer first and hand over to a person with the full history.

## Entry points

The chat window of the website or portal; Customer support agents › Live chat.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Live chat       Waiting 2   With agents 5   AI only 31   Average wait 38 s                  |
|---------------------------------------------------------------------------------------------|
| VISITOR       PAGE         LANG  STATE        WAIT   HANDLED BY                             |
| Julien R.     /orders      fr    Waiting      0:52   AI agent, asked for a person           |
| Visitor 4821  /pricing     en    With agent   -      Sana K.                                |
| TRANSCRIPT  AI: I am an AI. Your order ships tomorrow.  Julien: I want to speak to a person |
| [Take chat] [Transfer] [Close] [Create request]                                             |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-07 step 2, U16 | desktop | ![FL-F16-07 step 2, U16, light](../../images/07-live-chat-voice-and-contracts/u16-office-worker/2-live-chat-desktop-light.png) | ![FL-F16-07 step 2, U16, dark](../../images/07-live-chat-voice-and-contracts/u16-office-worker/2-live-chat-desktop-dark.png) |
| FL-F16-07 step 2, U16 | phone | ![FL-F16-07 step 2, U16, light](../../images/07-live-chat-voice-and-contracts/u16-office-worker/2-live-chat-phone-light.png) | ![FL-F16-07 step 2, U16, dark](../../images/07-live-chat-voice-and-contracts/u16-office-worker/2-live-chat-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-17-live-chat-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-17-live-chat-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-17-live-chat-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-17-live-chat-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-17-live-chat-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-17-live-chat-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-17-live-chat-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-17-live-chat-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Visitor and page | E-F16-14 visitor, page | text | no | yes |
| Language | E-F16-14 language | language | no | yes |
| State and wait | E-F16-14 state, wait | badge and time | no | yes |
| Handled by | E-F16-14 handled by | AI agent or person | by Take or Transfer | yes |
| Transcript | E-F16-14 messages | messages | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Take chat | row | office worker | the chat is theirs, with its history |
| Transfer | chat | office worker | another agent receives it with the history |
| Close | chat | office worker | the chat ends and the rating is asked |
| Create request | chat | office worker | the matter becomes a request |
| Ask for a person | chat window | visitor | the chat moves to Waiting |

## States

- Normal: the queue of chats with state, wait and who handles each; the open transcript.
- Empty: No chat now, with the opening hours shown.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a failed
  handover shows the visitor the options: call back or request.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F16-14 Chat session](../../data/e-f16-14-chat-session.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-14 Chat session | With AI | Badge "With AI"; a new record starts here; next: Waiting or Closed (BR-F16-15, UC-F16-19); fields editable within the role | U16, U09 | `u16-office-worker/s-f16-17-live-chat-e-f16-14-chat-session-with-ai-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-17-live-chat-e-f16-14-chat-session-with-ai-phone-{light,dark}.png` |
| E-F16-14 Chat session | Waiting | Badge "Waiting"; next: With agent or Missed (BR-F16-15, UC-F16-19); fields editable within the role | U16, U09 | `u16-office-worker/s-f16-17-live-chat-e-f16-14-chat-session-waiting-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-17-live-chat-e-f16-14-chat-session-waiting-phone-{light,dark}.png` |
| E-F16-14 Chat session | With agent | Badge "With agent"; next: Closed (UC-F16-19); fields editable within the role | U16, U09 | `u16-office-worker/s-f16-17-live-chat-e-f16-14-chat-session-with-agent-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-17-live-chat-e-f16-14-chat-session-with-agent-phone-{light,dark}.png` |
| E-F16-14 Chat session | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U16, U09 | `u16-office-worker/s-f16-17-live-chat-e-f16-14-chat-session-closed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-17-live-chat-e-f16-14-chat-session-closed-phone-{light,dark}.png` |
| E-F16-14 Chat session | Missed | Badge "Missed"; final: read-only, no next state; the history shows how it got here | U16, U09 | `u16-office-worker/s-f16-17-live-chat-e-f16-14-chat-session-missed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-17-live-chat-e-f16-14-chat-session-missed-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The visitor chats on a phone or a desktop; the agent's desk is desktop only.

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

⬅️ [S-F16-16 Forum](s-f16-16-forum.md) · ⬆️ [Up](README.md) · ➡️ [S-F16-18 Voice agent](s-f16-18-voice-agent.md)
