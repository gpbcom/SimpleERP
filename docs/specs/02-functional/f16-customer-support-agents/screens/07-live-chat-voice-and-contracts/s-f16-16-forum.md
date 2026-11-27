🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-07 Forum, live chat, voice and support contracts](README.md) › 🖥️ S-F16-16 Forum

# 🖥️ S-F16-16 Forum

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): the questions and answers, from a phone.
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): the moderation queue and the staff answers.

## Purpose

Ask and answer questions, find similar ones and moderate flagged posts.

## Entry points

The customer portal › Community; Customer support agents › Forum.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Forum              Categories: Orders  Delivery  Billing  Setup         [Ask a question]    |
|---------------------------------------------------------------------------------------------|
| QUESTION                         CATEGORY  ANSWERS  VOTES  STATE                            |
| How do I change my address?      Delivery  3        14     Answered                         |
| Invoice shows the wrong VAT      Billing   0        2      Open                             |
| Moderation queue (staff): 2 posts waiting   [Publish] [Edit and publish] [Hide] [Remove]    |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-07 step 1, U09 | phone | ![FL-F16-07 step 1, U09, light](../../images/07-live-chat-voice-and-contracts/u09-customer/1-forum-phone-light.png) | ![FL-F16-07 step 1, U09, dark](../../images/07-live-chat-voice-and-contracts/u09-customer/1-forum-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f16-16-forum-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f16-16-forum-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f16-16-forum-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f16-16-forum-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f16-16-forum-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f16-16-forum-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-16-forum-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-16-forum-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Question and body | E-F16-13 title, body | text | by the author | yes |
| Category | E-F16-13 category | list | by the author | yes |
| Answers and votes | E-F16-13 children, votes | numbers | by readers | no |
| State | E-F16-13 state | badge | by moderators | yes |
| Flag reason | E-F16-13 flag reason | text | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Ask a question | header | customer | creates a question and checks it |
| Answer | question | customer, staff | adds an answer |
| Vote | answer | customer | adds a vote |
| Accept answer | answer | author of the question | marks the answer as accepted |
| Publish, hide, remove | queue | moderator | changes the visibility with a reason |

## States

- Normal: the questions with answers, votes and state; for staff, the moderation queue.
- Empty: No question yet, with Ask the first question.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a held post
  shows its reason to the author and to the moderator.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F16-13 Forum post](../../data/e-f16-13-forum-post.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-13 Forum post | Submitted | Badge "Submitted"; a new record starts here; next: Published or Flagged (UC-F16-18, BR-F16-14); fields editable within the role | U09, U16 | `u09-customer/s-f16-16-forum-e-f16-13-forum-post-submitted-phone-{light,dark}.png`, `u16-office-worker/s-f16-16-forum-e-f16-13-forum-post-submitted-{desktop,phone}-{light,dark}.png` |
| E-F16-13 Forum post | Published | Badge "Published"; next: Hidden (UC-F16-18); fields editable within the role | U09, U16 | `u09-customer/s-f16-16-forum-e-f16-13-forum-post-published-phone-{light,dark}.png`, `u16-office-worker/s-f16-16-forum-e-f16-13-forum-post-published-{desktop,phone}-{light,dark}.png` |
| E-F16-13 Forum post | Flagged | Badge "Flagged"; next: Published or Removed (BR-F16-14); fields editable within the role | U09, U16 | `u09-customer/s-f16-16-forum-e-f16-13-forum-post-flagged-phone-{light,dark}.png`, `u16-office-worker/s-f16-16-forum-e-f16-13-forum-post-flagged-{desktop,phone}-{light,dark}.png` |
| E-F16-13 Forum post | Removed | Badge "Removed"; final: read-only, no next state; the history shows how it got here | U09, U16 | `u09-customer/s-f16-16-forum-e-f16-13-forum-post-removed-phone-{light,dark}.png`, `u16-office-worker/s-f16-16-forum-e-f16-13-forum-post-removed-{desktop,phone}-{light,dark}.png` |
| E-F16-13 Forum post | Hidden | Badge "Hidden"; next: Published or Removed (UC-F16-18); fields editable within the role | U09, U16 | `u09-customer/s-f16-16-forum-e-f16-13-forum-post-hidden-phone-{light,dark}.png`, `u16-office-worker/s-f16-16-forum-e-f16-13-forum-post-hidden-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The customer's forum is on a phone: questions, answers, votes and the ask form. The moderation queue is desktop only.

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

⬅️ [S-F16-15 Arrival of your visit](../06-take-in-every-request/s-f16-15-arrival-of-your-visit.md) ·
⬆️ [Up](README.md) · ➡️ [S-F16-17 Live chat](s-f16-17-live-chat.md)
