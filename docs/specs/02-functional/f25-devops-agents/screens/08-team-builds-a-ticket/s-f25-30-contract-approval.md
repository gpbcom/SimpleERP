🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F25-30 Contract approval

# 🖥️ S-F25-30 Contract approval

**Status:** 🔄 waiting for the owner

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md): the contracts waiting for
  approval, with their flags and their cost so far.

## Purpose

Approve, send back or refuse a ticket's work contract before any worker starts.

## Entry points

DevOps agents › Approvals › Contracts; the notification that a contract waits; Approve on the work contract screen.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Contract approval      Waiting 2                                                            |
|---------------------------------------------------------------------------------------------|
| TICKET  TITLE                       VERSION  START     ROLES  FLAGS           COST SO FAR   |
| 314     Payslip export file         2        a3f9c21   4      none            0.38 EUR      |
| 318     Stock counts on a phone     1        a3f9c21   5      1 overlap       0.52 EUR      |
|---------------------------------------------------------------------------------------------|
| 314  Criteria 3, each with a check     Order T0 > T1 > T2, T3                               |
|      Required checks: unit, lint, specs, end-to-end                                         |
|      Evidence: commits, changed files, checks with exit codes, blockers                     |
|      Changed since version 1: the file name criterion now has its check                     |
| Comment [...............................................................................]   |
| [Open the contract]      [Refuse and stop the run] [Ask for a revision] [Approve version 2] |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-08 step 2, U47 | desktop | ![FL-F25-08 step 2, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/2-contract-approval-desktop-light.png) | ![FL-F25-08 step 2, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/2-contract-approval-desktop-dark.png) |
| FL-F25-08 step 2, U47 | phone | ![FL-F25-08 step 2, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/2-contract-approval-phone-light.png) | ![FL-F25-08 step 2, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/2-contract-approval-phone-dark.png) |
| Error E1, U47 | desktop | ![Error E1, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/e1-the-contract-is-not-approved-desktop-light.png) | ![Error E1, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/e1-the-contract-is-not-approved-desktop-dark.png) |
| Error E1, U47 | phone | ![Error E1, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/e1-the-contract-is-not-approved-phone-light.png) | ![Error E1, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/e1-the-contract-is-not-approved-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-30-contract-approval-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-30-contract-approval-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-30-contract-approval-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-30-contract-approval-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-30-contract-approval-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-30-contract-approval-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-30-contract-approval-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-30-contract-approval-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Ticket and title | E-F25-19 ticket | link | no | yes |
| Version | E-F25-19 version | number | no | yes |
| Starting commit | E-F25-19 starting commit | commit hash | no | yes |
| Flags | E-F25-19 gaps and overlaps | badges | no | yes |
| Cost so far | E-F25-10 cost | amount with currency | no | yes |
| Comment | the maintainer's comment | text | maintainer | for a revision or a refusal |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Approve | footer | maintainer | approves this version, and the workers start (BR-F25-23) |
| Ask for a revision | footer | maintainer | sends the comment to the Architect, the contract goes back to Draft |
| Refuse and stop the run | footer | maintainer | refuses the contract and stops the run, the ticket stays in Ready |
| Open the contract | footer | maintainer | opens the work contract (S-F25-29) |

## States

- Normal: the contracts waiting for approval, and the selected one with its criteria, order, checks, evidence and
  changes since the last version.
- Empty: No contract waits for approval.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  approval names the overlap left, the ticket's approval label put back, or the role that is not a maintainer's.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)). The app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

⬅️ [S-F25-29 Work contract](s-f25-29-work-contract.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-31 Agent workers](s-f25-31-agent-workers.md)
