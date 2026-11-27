🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-03 Check a document against the law](README.md) › 🖥️ S-F15-03 Document check

# 🖥️ S-F15-03 Document check

**Status:** ✅ specified

## Personas

U06 HR, U13 Owner

## Purpose

The result of checking a document against the law (BR-F15-08).

## Entry points

Document templates (F2), a contract, or "Check against the law" in the AI assistant.

## Wireframe

```text
+------------------------------------------------------+
| Check: Fixed-term contract template                  |
| Found     Trial period, Pay, Working time          |
| Missing   Reason for recourse (L1242-12)  [Suggest]  |
| At risk   Renewal clause, 3 renewals (L1243-13)      |
+------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-03 step 1, U06 | desktop | ![FL-F15-03 step 1, U06, light](../../images/03-check-a-document-against-the-law/u06-hr/1-check-a-template-desktop-light.png) | ![FL-F15-03 step 1, U06, dark](../../images/03-check-a-document-against-the-law/u06-hr/1-check-a-template-desktop-dark.png) |
| Error E1, U06 | desktop | ![Error E1, U06, light](../../images/03-check-a-document-against-the-law/u06-hr/e1-unreadable-document-desktop-light.png) | ![Error E1, U06, dark](../../images/03-check-a-document-against-the-law/u06-hr/e1-unreadable-document-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-03-document-check-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-03-document-check-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-03-document-check-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-03-document-check-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-03-document-check-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-03-document-check-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f15-03-document-check-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f15-03-document-check-offline-desktop-dark.png) |

## Fields and columns

Clauses found, missing and at risk, each with its article.

## Actions

As the flow's steps.

## States

- Normal: each mandatory clause found or missing and each doubtful clause, with its article.
- Checking.
- Result.
- Empty: "No document checked yet": the formats accepted are listed.
- Loading: the frame and titles show at once with placeholder rows for the clauses; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a document that cannot be read (D122).
- Read-only: the document is never changed (BR-F15-08); the result is read-only.
- Offline: not available offline: the check reads the law corpus on the server. D38 keeps only today's schedule, time
  and intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action
  is disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F15-03 Document check](../../data/e-f15-03-document-check.md),
[E-F15-01 Law pack](../../data/e-f15-01-law-pack.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-03 Document check | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U06, U13 | `u06-hr/s-f15-03-document-check-e-f15-03-document-check-recorded-desktop-{light,dark}.png`, `u13-owner/s-f15-03-document-check-e-f15-03-document-check-recorded-{desktop,phone}-{light,dark}.png` |
| E-F15-01 Law pack | Scheduled | Badge "Scheduled"; a new record starts here; no other state; fields editable within the role | U06, U13 | `u06-hr/s-f15-03-document-check-e-f15-01-law-pack-scheduled-desktop-{light,dark}.png`, `u13-owner/s-f15-03-document-check-e-f15-01-law-pack-scheduled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Citations are links; warnings use an icon and text, never colour alone.

## Components

- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F15-03 Check a document against the law](../../flows/fl-f15-03-check-a-document-against-the-law.md)

## Open questions

None.

---

⬅️ [S-F15-02 Legal warning](../02-receive-a-legal-warning/s-f15-02-legal-warning.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-04 Legal assistant settings](../04-set-up-the-legal-assistant/s-f15-04-legal-assistant-settings.md)
