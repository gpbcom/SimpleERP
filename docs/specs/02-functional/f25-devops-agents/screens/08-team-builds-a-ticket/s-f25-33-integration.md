🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F25-33 Integration

# 🖥️ S-F25-33 Integration

**Status:** ✅ specified

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md): the integration of each run,
  its order, its conflicts and its candidate commit.

## Purpose

Follow the integration of the workers' commits in dependency order, and see a conflict sent back to the Architect.

## Entry points

DevOps agents › Agent team › a run › Integration; the notification of a conflict or of a candidate commit.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Integration  Run 57  Ticket 314  Branch team/314/integration  From a3f9c21  State Stopped   |
|---------------------------------------------------------------------------------------------|
| ORDER  ROLE               COMMIT    MESSAGE                                RESULT           |
|  1     Test Engineer      5be2d10   Add the export tests, failing          applied          |
|  2     Backend Engineer   c41e0b2   Add the export line shape              applied          |
|  3     Backend Engineer   9d07a1e   Write the export file per period       applied          |
|  4     Frontend Engineer  e88f3c4   Export button on the payslip list      conflict, aborted|
|---------------------------------------------------------------------------------------------|
| ! Conflict: services/payroll/routes, Backend Engineer and Frontend Engineer                 |
|   Sent to the Architect at 14:22. Contract version 3 waits for approval. [Open the contract]|
| Candidate commit: none yet     Checks: not run              [Open the branch] [Stop the run]|
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-08 step 5, U47 | desktop | ![FL-F25-08 step 5, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/5-integration-desktop-light.png) | ![FL-F25-08 step 5, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/5-integration-desktop-dark.png) |
| FL-F25-08 step 5, U47 | phone | ![FL-F25-08 step 5, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/5-integration-phone-light.png) | ![FL-F25-08 step 5, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/5-integration-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-33-integration-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-33-integration-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-33-integration-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-33-integration-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-33-integration-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-33-integration-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-33-integration-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-33-integration-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Order | the dependency order of the contract | number | no | yes |
| Role and commit | E-F25-21 role, commits | text, commit hash | no | yes |
| Result | applied, conflict and aborted, waiting | badge | no | yes |
| Conflict | files, roles and commits | text | no | no |
| Candidate commit | the head of the integration branch | commit hash | no | no |
| Checks | commands with exit codes | list | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open the contract | conflict | maintainer | opens the revised contract for approval (S-F25-30) |
| Open the branch | footer | maintainer | opens the integration branch in GitHub |
| Stop the run | footer | maintainer | stops the run, the branch is kept for a resume (UC-F25-37) |
| Open the verification | footer | maintainer | opens the verification of the candidate (S-F25-34), once recorded |

## States

- Normal: the commits in order with their result, the checks with their exit codes and the candidate commit.
- Empty: Waiting for handoffs: the roles whose handoff is not Accepted yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a conflict
  shows its files, the two roles and the commits, the aborted pick, and the contract version that waits for approval.
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

⬅️ [S-F25-32 Worker handoff](s-f25-32-worker-handoff.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-34 Candidate verification](s-f25-34-candidate-verification.md)
