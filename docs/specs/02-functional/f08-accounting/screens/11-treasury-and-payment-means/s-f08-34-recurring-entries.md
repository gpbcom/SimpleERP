🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F8-34 Recurring entries

# 🖥️ S-F8-34 Recurring entries

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the templates and the drafts to review.

## Purpose

Create entry templates, schedule them and review the entries they create.

## Entry points

Accounting › Recurring entries; a posted entry's Make it recurring action.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Entry template: Office rent                     Active    Next 2026-12-01   Ends 2027-09-30  |
|---------------------------------------------------------------------------------------------|
| Frequency monthly    Journal Miscellaneous    Mode  create as a draft                       |
| LINES   ACCOUNT        DEBIT     CREDIT                                                      |
|         613200 Rent    2,400.00                                                              |
|         401000 Landlord           2,400.00                                                   |
| Balance 0.00   Entries created 1   Drafts waiting 1       [Pause] [End now]                 |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-11 step 6, U05 | desktop | ![FL-F8-11 step 6, U05, light](../../images/11-treasury-and-payment-means/u05-accounting/6-recurring-entries-desktop-light.png) | ![FL-F8-11 step 6, U05, dark](../../images/11-treasury-and-payment-means/u05-accounting/6-recurring-entries-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-34-recurring-entries-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-34-recurring-entries-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-34-recurring-entries-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-34-recurring-entries-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-34-recurring-entries-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-34-recurring-entries-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-34-recurring-entries-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-34-recurring-entries-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Name and journal | E-F8-39 | text | yes while Draft | yes |
| Lines | E-F8-39 | table of account, debit, credit | yes while Draft | yes |
| Frequency, start, end | E-F8-39 | list and dates | yes | yes |
| Mode | E-F8-39 | draft or post | yes | yes |
| Next due date | E-F8-39 | date | no | no |
| Entries created | E-F8-03 | count and links | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Activate | header | accounting | the template starts creating entries |
| Pause | header | accounting | no entry is created until resumed |
| End now | header | accounting | the template ends |
| Review the drafts | header | accounting | the entries created and not yet posted |

## States

- Normal: the template's lines, its schedule and the entries it has created.
- Empty: No template yet, with New template.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a template that
  does not balance shows the difference.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-39 Entry template](../../data/e-f08-39-entry-template.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-39 Entry template | Draft | Badge "Draft"; a new record starts here; next: Active (UC-F8-35); fields editable within the role | U05 | `u05-accounting/s-f08-34-recurring-entries-e-f08-39-entry-template-draft-desktop-{light,dark}.png` |
| E-F8-39 Entry template | Active | Badge "Active"; next: Paused or Ended (UC-F8-35, BR-F8-27); fields editable within the role | U05 | `u05-accounting/s-f08-34-recurring-entries-e-f08-39-entry-template-active-desktop-{light,dark}.png` |
| E-F8-39 Entry template | Paused | Badge "Paused"; next: Active or Ended (UC-F8-35); fields editable within the role | U05 | `u05-accounting/s-f08-34-recurring-entries-e-f08-39-entry-template-paused-desktop-{light,dark}.png` |
| E-F8-39 Entry template | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f08-34-recurring-entries-e-f08-39-entry-template-ended-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-11 Treasury and payment means](../../flows/fl-f08-11-treasury-and-payment-means.md)

## Open questions

None.

---

⬅️ [S-F8-33 Payment initiation](s-f08-33-payment-initiation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-35 Auditor workspace](../12-audit-leases-and-special-books/s-f08-35-auditor-workspace.md)
