🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-12 Personal, cost-aware and learning](README.md) ›
🖥️ S-F3-22 Cost estimate

# 🖥️ S-F3-22 Cost estimate

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Show what a question will cost and take, and let the user confirm or narrow it.

## Entry points

Shown in the AI assistant panel before an expensive question.

## Wireframe

```text
+-------------------------------------------+
| This question will read 18,000 emails.    |
| About 4.20 EUR on the outside model,      |
| about 6 minutes.                          |
| [Narrow: last quarter] [Confirm] [Cancel] |
+-------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-12 step 2, U13 | desktop | ![FL-F3-12 step 2, U13, light](../../images/12-personal-cost-aware-and-learning/u13-owner/2-cost-estimate-desktop-light.png) | ![FL-F3-12 step 2, U13, dark](../../images/12-personal-cost-aware-and-learning/u13-owner/2-cost-estimate-desktop-dark.png) |
| FL-F3-12 step 2, U13 | phone | ![FL-F3-12 step 2, U13, light](../../images/12-personal-cost-aware-and-learning/u13-owner/2-cost-estimate-phone-light.png) | ![FL-F3-12 step 2, U13, dark](../../images/12-personal-cost-aware-and-learning/u13-owner/2-cost-estimate-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-22-cost-estimate-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-22-cost-estimate-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-22-cost-estimate-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-22-cost-estimate-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-22-cost-estimate-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-22-cost-estimate-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-22-cost-estimate-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-22-cost-estimate-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Records, cost, duration | F22 estimate | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Confirm, narrow, cancel | the user | Run, new estimate or nothing |

## States

- Normal: show what a question will cost and take, and let the user confirm or narrow it.
- Empty: never: shown only for an estimate.
- Loading: "Estimating" with a spinner.
- Error: the error message pattern (D122).
- Read-only: above the user's cap: Confirm becomes Ask the administrator.
- Offline: Not shown offline: the question is queued and estimated when the network is back
  ([D182](../../../../06-decisions/f03-assistant/d182-offline-assistant.md)).

Shown entities (VD-15): [E-F3-02 Assistant answer](../../data/e-f03-02-assistant-answer.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-02 Assistant answer | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f03-22-cost-estimate-e-f03-02-assistant-answer-recorded-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone, in the panel.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F3-12 Personal, cost-aware and learning](../../flows/fl-f03-12-personal-cost-aware-and-learning.md)

## Open questions

None.

---

⬅️ [S-F3-21 My assistant memory](s-f03-21-my-assistant-memory.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-23 Unanswered topics](s-f03-23-unanswered-topics.md)
