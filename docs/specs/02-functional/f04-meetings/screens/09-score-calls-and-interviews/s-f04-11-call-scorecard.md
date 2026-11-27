🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-09 Score calls and interviews](README.md) › 🖥️ S-F4-11 Call scorecard

# 🖥️ S-F4-11 Call scorecard

**Status:** ✅ specified

## Personas

See its use case.

## Purpose

A sales call's scorecard (UC-F4-12).

## Entry points

The meeting of kind sales call.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-09 step 1, U03 | desktop | ![FL-F4-09 step 1, U03, light](../../images/09-score-calls-and-interviews/u03-sales/1-sales-scorecard-desktop-light.png) | ![FL-F4-09 step 1, U03, dark](../../images/09-score-calls-and-interviews/u03-sales/1-sales-scorecard-desktop-dark.png) |
| FL-F4-09 step 1, U03 | phone | ![FL-F4-09 step 1, U03, light](../../images/09-score-calls-and-interviews/u03-sales/1-sales-scorecard-phone-light.png) | ![FL-F4-09 step 1, U03, dark](../../images/09-score-calls-and-interviews/u03-sales/1-sales-scorecard-phone-dark.png) |
| FL-F4-09 step 1, U03 | tablet | ![FL-F4-09 step 1, U03, light](../../images/09-score-calls-and-interviews/u03-sales/1-sales-scorecard-tablet-light.png) | ![FL-F4-09 step 1, U03, dark](../../images/09-score-calls-and-interviews/u03-sales/1-sales-scorecard-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-11-call-scorecard-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-11-call-scorecard-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-11-call-scorecard-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-11-call-scorecard-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-11-call-scorecard-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-11-call-scorecard-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-11-call-scorecard-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-11-call-scorecard-offline-phone-dark.png) |

## Fields and columns

Criteria, scores, evidence, talk-time, deal fields proposed.

## Actions

As its use case's main flow.

## States

- Normal: A sales call's scorecard (UC-F4-12), as the wireframe shows.
- Empty: no scorecard yet for this call: Score the call.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a scorecard for the scored seller.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F4-06 Scorecard](../../data/e-f04-06-scorecard.md),
[E-F4-20 Human review request](../../data/e-f04-20-human-review-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-06 Scorecard | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U02, U03 | `u02-manager/s-f04-11-call-scorecard-e-f04-06-scorecard-recorded-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-11-call-scorecard-e-f04-06-scorecard-recorded-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-20 Human review request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U03 | `u02-manager/s-f04-11-call-scorecard-e-f04-20-human-review-request-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-11-call-scorecard-e-f04-20-human-review-request-active-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-F4-10 Share and export](../08-share-and-reuse-outside/s-f04-10-share-and-export.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-12 Interview evaluation](s-f04-12-interview-evaluation.md)
