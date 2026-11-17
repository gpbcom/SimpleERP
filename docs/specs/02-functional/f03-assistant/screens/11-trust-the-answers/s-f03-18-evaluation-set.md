🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-11 Trust the answers](README.md) › 🖥️ S-F3-18 Evaluation set

# 🖥️ S-F3-18 Evaluation set

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Keep the evaluation questions and read each run.

## Entry points

Assistant settings › Evaluation.

## Wireframe

```text
+------------------------------------------------------------------+
| Evaluation  40 questions   Bar 90 %          [+ Question] [Run]  |
| Last run 2026-11-12 model change: 88 %  (previous 95 %) BLOCKED  |
| Question                    As        Result   Expected          |
| Paid-leave policy?          Employee  failed   25 days, handbook |
| Salaries of Lyon?           Sales     passed   refusal           |
|                                [Override with a reason]          |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-11 step 1, U07 | desktop | ![FL-F3-11 step 1, U07, light](../../images/11-trust-the-answers/u07-administrator/1-evaluation-set-desktop-light.png) | ![FL-F3-11 step 1, U07, dark](../../images/11-trust-the-answers/u07-administrator/1-evaluation-set-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/11-trust-the-answers/u07-administrator/e1-evaluation-set-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/11-trust-the-answers/u07-administrator/e1-evaluation-set-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-18-evaluation-set-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-18-evaluation-set-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-18-evaluation-set-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-18-evaluation-set-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-18-evaluation-set-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-18-evaluation-set-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-18-evaluation-set-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-18-evaluation-set-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Questions, runs, results | E-F3-17, E-F3-18 | questions |

## Actions

| Action | Who | Result |
|---|---|---|
| Run | administrator | A run starts |
| Override | administrator | Change goes live, reason kept |

## States

- Normal: keep the evaluation questions and read each run.
- Empty: no question yet: Add a question, or ask the AI assistant to propose some.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for the owner, who reads.
- Offline: Not available offline: it reads live settings and results
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F3-17 Evaluation question](../../data/e-f03-17-evaluation-question.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-17 Evaluation question | Active | Badge "Active"; a new record starts here; next: Archived (UC-F3-14); fields editable within the role | U07 | `u07-administrator/s-f03-18-evaluation-set-e-f03-17-evaluation-question-active-desktop-{light,dark}.png` |
| E-F3-17 Evaluation question | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f03-18-evaluation-set-e-f03-17-evaluation-question-archived-desktop-{light,dark}.png` |

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

- [FL-F3-11 Trust the answers](../../flows/fl-f03-11-trust-the-answers.md)

## Open questions

None.

---

⬅️ [S-F3-17 Chat apps](../10-benchmark-additions/s-f03-17-chat-apps.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-19 Injection alerts](s-f03-19-injection-alerts.md)
