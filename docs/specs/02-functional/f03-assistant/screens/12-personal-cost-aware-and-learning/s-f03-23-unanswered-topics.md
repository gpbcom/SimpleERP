🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-12 Personal, cost-aware and learning](README.md) ›
🖥️ S-F3-23 Unanswered topics

# 🖥️ S-F3-23 Unanswered topics

**Status:** ✅ specified

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

See the topics the AI assistant could not answer and turn them into knowledge proposals.

## Entry points

Knowledge base › Unanswered topics.

## Wireframe

```text
+------------------------------------------------------------------+
| Unanswered topics  [This month v]                                |
| Topic                         Questions  Status                  |
| Parental leave for fathers    14         open  [Draft proposal]  |
| Expense limit abroad          6          proposal                |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-12 step 3, U06 | desktop | ![FL-F3-12 step 3, U06, light](../../images/12-personal-cost-aware-and-learning/u06-hr/3-unanswered-topics-desktop-light.png) | ![FL-F3-12 step 3, U06, dark](../../images/12-personal-cost-aware-and-learning/u06-hr/3-unanswered-topics-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-23-unanswered-topics-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-23-unanswered-topics-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-23-unanswered-topics-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-23-unanswered-topics-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-23-unanswered-topics-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-23-unanswered-topics-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-23-unanswered-topics-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-23-unanswered-topics-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Topic, count, samples, status | E-F3-21 | status |

## Actions

| Action | Who | Result |
|---|---|---|
| Draft proposal | knowledge editor | Proposal for review |

## States

- Normal: see the topics the AI assistant could not answer and turn them into knowledge proposals.
- Empty: "Every question found an answer this month".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users who are not editors.
- Offline: Not available offline: it reads live settings and results
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F3-21 Unanswered topic](../../data/e-f03-21-unanswered-topic.md),
[E-F3-11 Knowledge proposal](../../data/e-f03-11-knowledge-proposal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-21 Unanswered topic | Open | Badge "Open"; a new record starts here; next: Proposal (UC-F3-19); fields editable within the role | U06 | `u06-hr/s-f03-23-unanswered-topics-e-f03-21-unanswered-topic-open-desktop-{light,dark}.png` |
| E-F3-21 Unanswered topic | Proposal | Badge "Proposal"; next: Answered (UC-F3-19); fields editable within the role | U06 | `u06-hr/s-f03-23-unanswered-topics-e-f03-21-unanswered-topic-proposal-desktop-{light,dark}.png` |
| E-F3-21 Unanswered topic | Answered | Badge "Answered"; final: read-only, no next state; the history shows how it got here | U06 | `u06-hr/s-f03-23-unanswered-topics-e-f03-21-unanswered-topic-answered-desktop-{light,dark}.png` |
| E-F3-11 Knowledge proposal | Open | Badge "Open"; a new record starts here; next: Approved or Declined (UC-F3-19, UC-F3-07); fields editable within the role | U06 | `u06-hr/s-f03-23-unanswered-topics-e-f03-11-knowledge-proposal-open-desktop-{light,dark}.png` |
| E-F3-11 Knowledge proposal | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U06 | `u06-hr/s-f03-23-unanswered-topics-e-f03-11-knowledge-proposal-approved-desktop-{light,dark}.png` |
| E-F3-11 Knowledge proposal | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U06 | `u06-hr/s-f03-23-unanswered-topics-e-f03-11-knowledge-proposal-declined-desktop-{light,dark}.png` |

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

- [FL-F3-12 Personal, cost-aware and learning](../../flows/fl-f03-12-personal-cost-aware-and-learning.md)

## Open questions

None.

---

⬅️ [S-F3-22 Cost estimate](s-f03-22-cost-estimate.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-24 Voice mode](../13-voice-agents-and-briefings/s-f03-24-voice-mode.md)
