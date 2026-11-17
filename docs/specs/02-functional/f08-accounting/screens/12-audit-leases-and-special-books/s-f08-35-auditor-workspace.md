🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F8-35 Auditor workspace

# 🖥️ S-F8-35 Auditor workspace

**Status:** 🔄 waiting for the owner

## Personas

- [U49 Statutory auditor](../../../../01-users/personas/u49-statutory-auditor.md): the books and their own requests,
  read-only.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the requests and the answers.

## Purpose

Give the statutory auditor read-only access to the books and manage their requests and the answers.

## Entry points

Accounting › Audit; the auditor's own sign-in to the workspace.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Auditor workspace: year 2026                 Auditor: Cabinet Lemaire     Access to 2027-04-30  |
|---------------------------------------------------------------------------------------------|
| READ-ONLY   Trial balance | Ledgers | Journals | Entries | Fixed assets | Closing checklist   |
| REQUESTS    Open 5   Provided 8   Queried 1   Closed 12                                      |
| REQUEST                          DUE         STATE     ANSWER                               |
| Contracts above 50,000 EUR       2026-12-15  Provided  6 documents                           |
| Stock count minutes              2026-12-20  Open      -                                     |
| [Raise a request] [Answer] [Close] [Query]        Views today: 142    Refused attempts: 1    |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-12 step 1, U49 | desktop | ![FL-F8-12 step 1, U49, light](../../images/12-audit-leases-and-special-books/u49-statutory-auditor/1-auditor-workspace-desktop-light.png) | ![FL-F8-12 step 1, U49, dark](../../images/12-audit-leases-and-special-books/u49-statutory-auditor/1-auditor-workspace-desktop-dark.png) |
| Error E1, U49 | desktop | ![Error E1, U49, light](../../images/12-audit-leases-and-special-books/u49-statutory-auditor/e1-the-auditor-tries-to-change-the-books-desktop-light.png) | ![Error E1, U49, dark](../../images/12-audit-leases-and-special-books/u49-statutory-auditor/e1-the-auditor-tries-to-change-the-books-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-35-auditor-workspace-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-35-auditor-workspace-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-35-auditor-workspace-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-35-auditor-workspace-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-35-auditor-workspace-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-35-auditor-workspace-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-35-auditor-workspace-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-35-auditor-workspace-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Request | E-F8-40 | text | auditor while Open | yes |
| Due date | E-F8-40 | date | yes | yes |
| State | E-F8-40 | badge | no | yes |
| Answer | E-F8-40 documents and note | files and text | accounting | for Provided |
| Books | E-F8-03, E-F8-01, E-F8-07 | read-only tables | never | - |
| View log | E-F8-40 views | count and list | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Raise a request | header | auditor, accounting | a request with a due date |
| Answer | row | accounting | documents and a note; the request becomes Provided |
| Close | row | auditor | the request is Closed |
| Query | row | auditor | the request goes back to accounting with a question |
| End access | header | accounting | the auditor's access ends |

## States

- Normal: the books in read-only tables on one side, the requests with their states on the other.
- Empty: No request yet, with Raise a request.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an attempt to
  change the books shows "read-only access" and is logged.
- Read-only: the whole workspace is read-only for the auditor: every field and action that changes the books is absent,
  never greyed.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-40 Audit request](../../data/e-f08-40-audit-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-40 Audit request | Open | Badge "Open"; a new record starts here; next: Provided or Closed (UC-F8-36); fields editable within the role | U49, U05 | `u49-statutory-auditor/s-f08-35-auditor-workspace-e-f08-40-audit-request-open-desktop-{light,dark}.png`, `u05-accounting/s-f08-35-auditor-workspace-e-f08-40-audit-request-open-desktop-{light,dark}.png` |
| E-F8-40 Audit request | Provided | Badge "Provided"; next: Queried or Closed (UC-F8-36); fields editable within the role | U49, U05 | `u49-statutory-auditor/s-f08-35-auditor-workspace-e-f08-40-audit-request-provided-desktop-{light,dark}.png`, `u05-accounting/s-f08-35-auditor-workspace-e-f08-40-audit-request-provided-desktop-{light,dark}.png` |
| E-F8-40 Audit request | Queried | Badge "Queried"; next: Provided (UC-F8-36); fields editable within the role | U49, U05 | `u49-statutory-auditor/s-f08-35-auditor-workspace-e-f08-40-audit-request-queried-desktop-{light,dark}.png`, `u05-accounting/s-f08-35-auditor-workspace-e-f08-40-audit-request-queried-desktop-{light,dark}.png` |
| E-F8-40 Audit request | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U49, U05 | `u49-statutory-auditor/s-f08-35-auditor-workspace-e-f08-40-audit-request-closed-desktop-{light,dark}.png`, `u05-accounting/s-f08-35-auditor-workspace-e-f08-40-audit-request-closed-desktop-{light,dark}.png` |

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

- [FL-F8-12](../../flows/fl-f08-12-audit-leases-and-special-books.md)

## Open questions

None.

---

⬅️ [S-F8-34 Recurring entries](../11-treasury-and-payment-means/s-f08-34-recurring-entries.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-36 Leases](s-f08-36-leases.md)
