🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-02 Recruit](README.md) ›
🖥️ S-F9-39 Prospect conversations

# 🖥️ S-F9-39 Prospect conversations

**Status:** ✅ specified

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md): the threads of their sequences.

## Purpose

Read each prospect's thread with the AI assistant's class of each reply, and act on it.

## Entry points

S-F9-38 › Threads; the notification of a question or a positive reply.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Prospect conversations: site manager   Waiting for HR (1)  Applicants (3)  No answer (4)     |
|---------------------------------------------------------------------------------------------|
| THREADS                  | Julien R.  site manager at BTP Rhône  score 92                    |
| > Julien R.  question    | Day 0  Invitation with a note sent                                |
|   Sonia M.   positive    | Day 7  Follow-up 1 sent                                           |
|   Karim D.   negative    | Day 9  Is the job open to remote work two days a week?           |
|                          |        AI assistant: question, asks about remote work            |
|                          | [Mark negative] [Mark positive] [Reply]                           |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-14 step 5, U06 | desktop | ![FL-F9-14 step 5, U06, light](../../images/14-source-candidates-on-linkedin/u06-hr/5-prospect-conversations-desktop-light.png) | ![FL-F9-14 step 5, U06, dark](../../images/14-source-candidates-on-linkedin/u06-hr/5-prospect-conversations-desktop-dark.png) |
| FL-F9-14 step 6, U06 | desktop | ![FL-F9-14 step 6, U06, light](../../images/14-source-candidates-on-linkedin/u06-hr/6-prospect-conversations-desktop-light.png) | ![FL-F9-14 step 6, U06, dark](../../images/14-source-candidates-on-linkedin/u06-hr/6-prospect-conversations-desktop-dark.png) |
| Error E4, U06 | desktop | ![Error E4, U06, light](../../images/14-source-candidates-on-linkedin/u06-hr/e4-erasure-request-desktop-light.png) | ![Error E4, U06, dark](../../images/14-source-candidates-on-linkedin/u06-hr/e4-erasure-request-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-39-prospect-conversations-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-39-prospect-conversations-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-39-prospect-conversations-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-39-prospect-conversations-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-39-prospect-conversations-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-39-prospect-conversations-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-39-prospect-conversations-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-39-prospect-conversations-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Threads | E-F9-45 with their last message | name, class, state | no | yes |
| Messages | E-F9-47 | day, text, direction | no | yes |
| Class | E-F9-47 class, reason, confidence | word and reason | yes, by HR | for a reply |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Reply | thread | HR | a message written by HR, sent in the thread |
| Mark positive | thread | HR | the applicant created and the booking link sent (UC-F9-42) |
| Mark negative | thread | HR | declined, erased at the end of the sequence |
| Erase | thread | HR | the prospect and the messages erased at once (BR-F9-11) |

## States

- Normal: the threads on the left, the chosen thread on the right with each reply's class.
- Empty: No reply yet, with Open the sequence.
- Loading: The threads load first; the messages follow.
- Error: the error message pattern (D122); a message not sent shows why and when it is tried again.
- Read-only: the threads of an ended sequence.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-45 Prospect](../../data/e-f09-45-prospect.md),
[E-F9-47 Outreach message](../../data/e-f09-47-outreach-message.md),
[E-F9-06 Job position](../../data/e-f09-06-job-position.md), [E-F9-07 Applicant](../../data/e-f09-07-applicant.md),
[E-F9-46 Outreach sequence](../../data/e-f09-46-outreach-sequence.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-45 Prospect | Invited | the thread's badge and actions | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-45-prospect-invited-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Connected | the thread's badge and actions | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-45-prospect-connected-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Waiting for HR | the thread's badge and actions | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-45-prospect-waiting-for-hr-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Applicant | the thread's badge and actions | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-45-prospect-applicant-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Declined | the thread's badge and actions | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-45-prospect-declined-desktop-{light,dark}.png` |
| E-F9-45 Prospect | No answer | the thread's badge and actions | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-45-prospect-no-answer-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Erased | the thread's badge and actions | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-45-prospect-erased-desktop-{light,dark}.png` |
| E-F9-47 Outreach message | Planned | each line of the thread | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-47-outreach-message-planned-desktop-{light,dark}.png` |
| E-F9-47 Outreach message | Sent | each line of the thread | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-47-outreach-message-sent-desktop-{light,dark}.png` |
| E-F9-47 Outreach message | Failed | each line of the thread | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-47-outreach-message-failed-desktop-{light,dark}.png` |
| E-F9-47 Outreach message | Cancelled | each line of the thread | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-47-outreach-message-cancelled-desktop-{light,dark}.png` |
| E-F9-47 Outreach message | Received | each line of the thread | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-47-outreach-message-received-desktop-{light,dark}.png` |
| E-F9-47 Outreach message | Classified | each line of the thread | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-47-outreach-message-classified-desktop-{light,dark}.png` |
| E-F9-47 Outreach message | Reviewed | each line of the thread | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-47-outreach-message-reviewed-desktop-{light,dark}.png` |
| E-F9-06 Job position | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-06-job-position-active-desktop-{light,dark}.png` |
| E-F9-07 Applicant | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-07-applicant-active-desktop-{light,dark}.png` |
| E-F9-46 Outreach sequence | Draft | Badge "Draft"; a new record starts here; next: Running (BR-F9-36); fields editable within the role | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-46-outreach-sequence-draft-desktop-{light,dark}.png` |
| E-F9-46 Outreach sequence | Running | Badge "Running"; next: Draft, Paused or Ended (BR-F9-36, BR-F9-41, BR-F9-37); fields editable within the role | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-46-outreach-sequence-running-desktop-{light,dark}.png` |
| E-F9-46 Outreach sequence | Paused | Badge "Paused"; next: Running or Ended (BR-F9-41, BR-F9-37); fields editable within the role | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-46-outreach-sequence-paused-desktop-{light,dark}.png` |
| E-F9-46 Outreach sequence | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-46-outreach-sequence-ended-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Found | Badge "Found"; a new record starts here; next: Shortlisted or Discarded (UC-F9-40); fields editable within the role | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-45-prospect-found-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Discarded | Badge "Discarded"; next: Erased (BR-F9-39); fields editable within the role | U06 | `u06-hr/s-f09-39-prospect-conversations-e-f09-45-prospect-discarded-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Each class is a word with its reason; new replies are announced; keyboard: next thread, reply.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-14 Source candidates on LinkedIn](../../flows/fl-f09-14-source-candidates-on-linkedin.md)
- [FL-F9-02 Recruit](../../flows/fl-f09-02-recruit.md)

## Open questions

None.

---

⬅️ [S-F9-38 Outreach sequence](s-f09-38-outreach-sequence.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-40 Work location](../15-work-location-headcount-and-learning/s-f09-40-work-location.md)
