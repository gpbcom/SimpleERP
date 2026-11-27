🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F25-29 Work contract

# 🖥️ S-F25-29 Work contract

**Status:** 🔄 waiting for the owner

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md): the contract of each ticket
  the team works on, with its gaps and overlaps.

## Purpose

Show the work contract of a ticket: criteria, shared contracts, files per role, tasks, checks and evidence, with what is
missing or overlapping.

## Entry points

DevOps agents › Agent team › a run › Contract; the link in the approval request; the comment on the ticket.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Work contract  Ticket 314 Payslip export file   Start a3f9c21   Version 2   State Proposed  |
|---------------------------------------------------------------------------------------------|
| ACCEPTANCE CRITERIA                                       CHECK                             |
|  1 The export holds one line per payslip                  test export lines                 |
|  2 The file name carries the period                       ! gap: no check                   |
| SHARED CONTRACTS  GET /payroll/exports/{period}    Payslip export line (7 fields)           |
|---------------------------------------------------------------------------------------------|
| ROLE                FILES OWNED                         TASKS     DEPENDS ON                |
| Test Engineer       tests/payroll/export/               T0        -                         |
| Backend Engineer    services/payroll/export/            T1, T2    T0                        |
| Frontend Engineer   web/payroll/exports/                T3        T0, shared contract       |
| ! Overlap: services/payroll/routes owned by Backend Engineer and Frontend Engineer          |
| HANDOFF EVIDENCE  commits in order, changed files, checks with exit codes, blockers         |
| [Open the study note] [Stop the run]          [Ask for a revision] [Approve the contract >] |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-08 step 1, U47 | desktop | ![FL-F25-08 step 1, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/1-work-contract-desktop-light.png) | ![FL-F25-08 step 1, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/1-work-contract-desktop-dark.png) |
| FL-F25-08 step 1, U47 | phone | ![FL-F25-08 step 1, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/1-work-contract-phone-light.png) | ![FL-F25-08 step 1, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/1-work-contract-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-29-work-contract-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-29-work-contract-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-29-work-contract-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-29-work-contract-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-29-work-contract-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-29-work-contract-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-29-work-contract-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-29-work-contract-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Ticket | E-F25-19 ticket | link | no | yes |
| Starting commit | E-F25-19 starting commit | commit hash | no | yes |
| Acceptance criteria | E-F25-19 acceptance criteria | numbered list, the check of each | Architect | yes |
| Shared contracts | E-F25-19 shared contracts | API operations and data shapes | Architect | no |
| Files owned | E-F25-19 file ownership | paths per role | Architect | yes |
| Tasks and dependencies | E-F25-19 tasks | list with dependencies | Architect | yes |
| Required checks | E-F25-19 required checks | commands | Architect | yes |
| Gaps and overlaps | E-F25-19 gaps and overlaps | flags | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open the study note | footer | maintainer | opens the study the contract is built from (S-F25-05) |
| Ask for a revision | footer | maintainer | sends a comment to the Architect, who writes a new version |
| Approve the contract | footer | maintainer | opens the contract approval (S-F25-30) |
| Stop the run | footer | maintainer | stops the team, the contract is Abandoned |

## States

- Normal: the criteria with their checks, the shared contracts, the roles with their files and tasks, the required
  checks and the evidence, with the gaps and overlaps flagged.
- Empty: No contract yet: the Architect is writing it, with the run's progress and its cost so far.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a contract that
  cannot be written shows the Architect's reason, such as no study note or a limit reached, and the ticket stays in
  Ready.
- Read-only: an Approved, Refused, Closed or Abandoned contract: values shown, only a new version can change it.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)). The app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F25-19 Work contract](../../data/e-f25-19-work-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-19 Work contract | Draft | Badge "Draft"; a new record starts here; next: Proposed or Abandoned (UC-F25-29); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-29-work-contract-e-f25-19-work-contract-draft-{desktop,phone}-{light,dark}.png` |
| E-F25-19 Work contract | Proposed | Badge "Proposed"; next: Draft, Approved or Refused (UC-F25-30, BR-F25-23); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-29-work-contract-e-f25-19-work-contract-proposed-{desktop,phone}-{light,dark}.png` |
| E-F25-19 Work contract | Approved | Badge "Approved"; next: Draft or Closed (BR-F25-26, UC-F25-36); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-29-work-contract-e-f25-19-work-contract-approved-{desktop,phone}-{light,dark}.png` |
| E-F25-19 Work contract | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simpleerp-maintainer/s-f25-29-work-contract-e-f25-19-work-contract-refused-{desktop,phone}-{light,dark}.png` |
| E-F25-19 Work contract | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simpleerp-maintainer/s-f25-29-work-contract-e-f25-19-work-contract-closed-{desktop,phone}-{light,dark}.png` |
| E-F25-19 Work contract | Abandoned | Badge "Abandoned"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simpleerp-maintainer/s-f25-29-work-contract-e-f25-19-work-contract-abandoned-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only. On a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F25-08](../../flows/fl-f25-08-team-builds-a-ticket.md)

## Open questions

None.

---

⬅️ [S-F25-28 Module changelog](../07-roadmap-beta-and-credits/s-f25-28-module-changelog.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-30 Contract approval](s-f25-30-contract-approval.md)
