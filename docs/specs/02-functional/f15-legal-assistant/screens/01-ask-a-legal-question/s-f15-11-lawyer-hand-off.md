🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-01 Ask a legal question](README.md) › 🖥️ S-F15-11 Lawyer hand-off

# 🖥️ S-F15-11 Lawyer hand-off

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U06 Human resources](../../../../01-users/personas/u06-hr.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Build and send a package for a lawyer from a legal answer, choosing what to share.

## Entry points

"Hand over to a lawyer" on a legal answer.

## Wireframe

```text
Hand over to a lawyer                                 Confidence: low
-------------------------------------------------------------------------------
Question: Can I dismiss for repeated lateness?
Facts used:  [x] contract  [x] 3 written warnings  [ ] salary
Answer and sources: L1232-1 (in force since ...), agreement art. 12
Documents: [Add] warning-1.pdf warning-2.pdf warning-3.pdf
Lawyer email: [                         ]                    [Send]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-01 step 4, U13 | desktop | ![FL-F15-01 step 4, U13, light](../../images/01-ask-a-legal-question/u13-owner/4-lawyer-hand-off-desktop-light.png) | ![FL-F15-01 step 4, U13, dark](../../images/01-ask-a-legal-question/u13-owner/4-lawyer-hand-off-desktop-dark.png) |
| FL-F15-01 step 4, U13 | phone | ![FL-F15-01 step 4, U13, light](../../images/01-ask-a-legal-question/u13-owner/4-lawyer-hand-off-phone-light.png) | ![FL-F15-01 step 4, U13, dark](../../images/01-ask-a-legal-question/u13-owner/4-lawyer-hand-off-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-11-lawyer-hand-off-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-11-lawyer-hand-off-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-11-lawyer-hand-off-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-11-lawyer-hand-off-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-11-lawyer-hand-off-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-11-lawyer-hand-off-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-11-lawyer-hand-off-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-11-lawyer-hand-off-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Question | E-F15-10 question | text | no | yes |
| Facts | E-F15-10 facts | ticked list | yes (untick) | no |
| Answer, sources, confidence | E-F15-10 | text | no | yes |
| Documents | E-F15-10 documents | files | yes | no |
| Lawyer | E-F15-10 lawyer | email | yes | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Untick a fact | facts | asker | not sent |
| Add document | documents | asker | attached (only documents the asker may see) |
| Send | footer | asker | email sent, package kept privately |

## States

- Normal: the package with the facts ticked, the answer and the documents.
- Empty: never empty: it opens from an answer; with no facts used it says "General answer, no facts".
- Loading: the frame and titles show at once with placeholder rows for the package; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an undeliverable email, the draft kept with the reason.
- Read-only: a sent package is read-only in the asker's history.
- Offline: The draft stays on screen; sending needs the network. Nothing else is queued: D38 keeps only today's
  schedule, time and intervention records offline; a banner says the connection is lost and the actions come back with
  it.

Shown entities (VD-15): [E-F3-01 Conversation](../../../f03-assistant/data/e-f03-01-conversation.md),
[E-F15-10 Lawyer hand-off](../../data/e-f15-10-lawyer-hand-off.md),
[E-F15-01 Law pack](../../data/e-f15-01-law-pack.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-01 Conversation | Private | Badge "Private"; a new record starts here; next: Shared or Deleted (UC-F3-01, UC-F3-08); fields editable within the role | U01, U06, U13 | `u01-employee/s-f15-11-lawyer-hand-off-e-f03-01-conversation-private-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-11-lawyer-hand-off-e-f03-01-conversation-private-desktop-{light,dark}.png`, `u13-owner/s-f15-11-lawyer-hand-off-e-f03-01-conversation-private-{desktop,phone}-{light,dark}.png` |
| E-F3-01 Conversation | Shared | Badge "Shared"; next: Private or Deleted (UC-F15-01, UC-F3-08); fields editable within the role | U01, U06, U13 | `u01-employee/s-f15-11-lawyer-hand-off-e-f03-01-conversation-shared-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-11-lawyer-hand-off-e-f03-01-conversation-shared-desktop-{light,dark}.png`, `u13-owner/s-f15-11-lawyer-hand-off-e-f03-01-conversation-shared-{desktop,phone}-{light,dark}.png` |
| E-F3-01 Conversation | Deleted | Not shown: the record is gone in this state, so no screen shows it | U01, U06, U13 | None: system state, the user never sees it |
| E-F15-10 Lawyer hand-off | Draft | Badge "Draft"; a new record starts here; next: Sent or Discarded (UC-F15-12); fields editable within the role | U01, U06, U13 | `u01-employee/s-f15-11-lawyer-hand-off-e-f15-10-lawyer-hand-off-draft-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-11-lawyer-hand-off-e-f15-10-lawyer-hand-off-draft-desktop-{light,dark}.png`, `u13-owner/s-f15-11-lawyer-hand-off-e-f15-10-lawyer-hand-off-draft-{desktop,phone}-{light,dark}.png` |
| E-F15-10 Lawyer hand-off | Sent | Badge "Sent"; final: read-only, no next state; the history shows how it got here | U01, U06, U13 | `u01-employee/s-f15-11-lawyer-hand-off-e-f15-10-lawyer-hand-off-sent-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-11-lawyer-hand-off-e-f15-10-lawyer-hand-off-sent-desktop-{light,dark}.png`, `u13-owner/s-f15-11-lawyer-hand-off-e-f15-10-lawyer-hand-off-sent-{desktop,phone}-{light,dark}.png` |
| E-F15-10 Lawyer hand-off | Discarded | Badge "Discarded"; final: read-only, no next state; the history shows how it got here | U01, U06, U13 | `u01-employee/s-f15-11-lawyer-hand-off-e-f15-10-lawyer-hand-off-discarded-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-11-lawyer-hand-off-e-f15-10-lawyer-hand-off-discarded-desktop-{light,dark}.png`, `u13-owner/s-f15-11-lawyer-hand-off-e-f15-10-lawyer-hand-off-discarded-{desktop,phone}-{light,dark}.png` |
| E-F15-01 Law pack | Scheduled | Badge "Scheduled"; a new record starts here; no other state; fields editable within the role | U01, U06, U13 | `u01-employee/s-f15-11-lawyer-hand-off-e-f15-01-law-pack-scheduled-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-11-lawyer-hand-off-e-f15-01-law-pack-scheduled-desktop-{light,dark}.png`, `u13-owner/s-f15-11-lawyer-hand-off-e-f15-01-law-pack-scheduled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone (D34).

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F15-01 Ask a legal question](../../flows/fl-f15-01-ask-a-legal-question.md)

## Open questions

None.

---

⬅️ [S-F15-10 Privacy and AI register](../06-privacy-and-ai-duties/s-f15-10-privacy-and-ai-register.md) ·
⬆️ [Up](README.md) · ➡️ [S-F15-12 Cap table](../07-equity-contracts-and-disputes/s-f15-12-cap-table.md)
