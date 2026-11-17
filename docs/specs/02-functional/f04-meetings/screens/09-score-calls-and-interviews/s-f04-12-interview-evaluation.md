🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-09 Score calls and interviews](README.md) ›
🖥️ S-F4-12 Interview evaluation

# 🖥️ S-F4-12 Interview evaluation

**Status:** ✅ specified

## Personas

See its use case.

## Purpose

An interview's evaluation (UC-F4-13).

## Entry points

The meeting of kind interview.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-09 step 4, U06 | desktop | ![FL-F4-09 step 4, U06, light](../../images/09-score-calls-and-interviews/u06-hr/4-interview-evaluation-desktop-light.png) | ![FL-F4-09 step 4, U06, dark](../../images/09-score-calls-and-interviews/u06-hr/4-interview-evaluation-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-12-interview-evaluation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-12-interview-evaluation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-12-interview-evaluation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-12-interview-evaluation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-12-interview-evaluation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-12-interview-evaluation-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f04-12-interview-evaluation-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f04-12-interview-evaluation-offline-desktop-dark.png) |

## Fields and columns

Answers, grid scores, match score, evidence, validation state.

## Actions

As its use case's main flow.

## States

- Normal: An interview's evaluation (UC-F4-13), as the wireframe shows.
- Empty: no evaluation yet: Evaluate.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a submitted evaluation for other interviewers until they submit theirs.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F4-07 Evaluation grid](../../data/e-f04-07-evaluation-grid.md),
[E-F4-21 Interview debrief](../../data/e-f04-21-interview-debrief.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-07 Evaluation grid | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U06 | `u02-manager/s-f04-12-interview-evaluation-e-f04-07-evaluation-grid-active-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-12-interview-evaluation-e-f04-07-evaluation-grid-active-desktop-{light,dark}.png` |
| E-F4-21 Interview debrief | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U06 | `u02-manager/s-f04-12-interview-evaluation-e-f04-21-interview-debrief-active-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f04-12-interview-evaluation-e-f04-21-interview-debrief-active-desktop-{light,dark}.png` |

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

- [FL-F4-09 Score calls and interviews](../../flows/fl-f04-09-score-calls-and-interviews.md)

## Open questions

None.

---

⬅️ [S-F4-11 Call scorecard](s-f04-11-call-scorecard.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-13 Softphone](../07-prepare-and-capture-anywhere/s-f04-13-softphone.md)
