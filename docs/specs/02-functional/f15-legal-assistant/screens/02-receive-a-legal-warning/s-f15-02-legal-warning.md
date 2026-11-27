🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-02 Receive a legal warning](README.md) › 🖥️ S-F15-02 Legal warning

# 🖥️ S-F15-02 Legal warning

**Status:** ✅ specified

## Personas

Whoever acts, and those who must know

## Purpose

A warning next to what triggered it (BR-F15-07).

## Entry points

On a schedule, a leave request, a contract, a headcount change.

## Wireframe

```text
+------------------------------------------------------+
| (!) Daily rest under 11 hours for Paul Martin         |
| between 12 and 13 Nov. Code du travail, L3131-1.    |
| [Explain]  [Dismiss with a reason]   This does not   |
| block saving.                                         |
+------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-02 step 1, U02 | desktop | ![FL-F15-02 step 1, U02, light](../../images/02-receive-a-legal-warning/u02-manager/1-warning-on-a-schedule-desktop-light.png) | ![FL-F15-02 step 1, U02, dark](../../images/02-receive-a-legal-warning/u02-manager/1-warning-on-a-schedule-desktop-dark.png) |
| FL-F15-02 step 1, U02 | phone | ![FL-F15-02 step 1, U02, light](../../images/02-receive-a-legal-warning/u02-manager/1-warning-on-a-schedule-phone-light.png) | ![FL-F15-02 step 1, U02, dark](../../images/02-receive-a-legal-warning/u02-manager/1-warning-on-a-schedule-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-02-legal-warning-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-02-legal-warning-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-02-legal-warning-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-02-legal-warning-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-02-legal-warning-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-02-legal-warning-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-02-legal-warning-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-02-legal-warning-offline-phone-dark.png) |

## Fields and columns

Rule, article, version, what triggered it.

## Actions

As the flow's steps.

## States

- Normal: the warning next to what triggered it, with the rule, article, version, date and the facts it used.
- Shown, explained, dismissed.
- Off: not shown.
- Empty: no warning is shown when nothing triggers one, and none at all when warnings are off (D193).
- Loading: the frame and titles show at once with placeholder rows for the warning; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122): what happened, why, and the button that fixes it.
- Read-only: a dismissed warning stays visible with its reason, read-only.
- Offline: Warnings already shown stay; new ones appear after sync. D38's offline field records raise their warnings
  once synced. Nothing else is queued: D38 keeps only today's schedule, time and intervention records offline; a banner
  says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F15-11 Warning trigger](../../data/e-f15-11-warning-trigger.md),
[E-F15-02 Legal warning](../../data/e-f15-02-legal-warning.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-11 Warning trigger | On | Badge "On"; a new record starts here; next: Off (UC-F15-04); fields editable within the role | U01, U02, U06, U13 | `u01-employee/s-f15-02-legal-warning-e-f15-11-warning-trigger-on-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f15-02-legal-warning-e-f15-11-warning-trigger-on-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-02-legal-warning-e-f15-11-warning-trigger-on-desktop-{light,dark}.png`, `u13-owner/s-f15-02-legal-warning-e-f15-11-warning-trigger-on-{desktop,phone}-{light,dark}.png` |
| E-F15-11 Warning trigger | Off | Badge "Off"; next: On (UC-F15-02); fields editable within the role | U01, U02, U06, U13 | `u01-employee/s-f15-02-legal-warning-e-f15-11-warning-trigger-off-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f15-02-legal-warning-e-f15-11-warning-trigger-off-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-02-legal-warning-e-f15-11-warning-trigger-off-desktop-{light,dark}.png`, `u13-owner/s-f15-02-legal-warning-e-f15-11-warning-trigger-off-{desktop,phone}-{light,dark}.png` |
| E-F15-02 Legal warning | Shown | Badge "Shown"; a new record starts here; next: Dismissed (UC-F15-01); fields editable within the role | U01, U02, U06, U13 | `u01-employee/s-f15-02-legal-warning-e-f15-02-legal-warning-shown-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f15-02-legal-warning-e-f15-02-legal-warning-shown-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-02-legal-warning-e-f15-02-legal-warning-shown-desktop-{light,dark}.png`, `u13-owner/s-f15-02-legal-warning-e-f15-02-legal-warning-shown-{desktop,phone}-{light,dark}.png` |
| E-F15-02 Legal warning | Dismissed | Badge "Dismissed"; final: read-only, no next state; the history shows how it got here | U01, U02, U06, U13 | `u01-employee/s-f15-02-legal-warning-e-f15-02-legal-warning-dismissed-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f15-02-legal-warning-e-f15-02-legal-warning-dismissed-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-02-legal-warning-e-f15-02-legal-warning-dismissed-desktop-{light,dark}.png`, `u13-owner/s-f15-02-legal-warning-e-f15-02-legal-warning-dismissed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

Citations are links; warnings use an icon and text, never colour alone.

## Components

- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F15-02 Receive a legal warning](../../flows/fl-f15-02-receive-a-legal-warning.md)

## Open questions

None.

---

⬅️ [S-F15-01 Legal answer](../01-ask-a-legal-question/s-f15-01-legal-answer.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-03 Document check](../03-check-a-document-against-the-law/s-f15-03-document-check.md)
