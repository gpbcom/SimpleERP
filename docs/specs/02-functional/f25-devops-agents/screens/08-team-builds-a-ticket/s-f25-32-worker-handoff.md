🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F25-32 Worker handoff

# 🖥️ S-F25-32 Worker handoff

**Status:** ✅ specified

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md): the handoff of each worker,
  its check result and its blockers.

## Purpose

Show a worker's structured handoff and whether the handoff check accepted it.

## Entry points

DevOps agents › Agent team › a run › Handoffs; a worker row on the agent workers screen; the notification of a blocked
handoff.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Worker handoff  Run 57  Ticket 314  Backend Engineer                     State Accepted     |
|---------------------------------------------------------------------------------------------|
| Worktree team-314-backend     Branch team/314/backend    Starting commit a3f9c21 (contract) |
| COMMITS IN ORDER                                        CHANGED FILES                       |
|  1 c41e0b2  Add the export line shape                   services/payroll/export/line        |
|  2 9d07a1e  Write the export file per period            services/payroll/export/file        |
| CHECKS            COMMAND                       EXIT CODE   MATCHES THE RECORDED RUN        |
|  unit tests       run unit payroll              0           yes                             |
|  lint             run lint                      0           yes                             |
| BLOCKERS  none                                                                              |
| [Open the branch] [Open the contract]                 [Clear the blocker] [Stop the run]    |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-08 step 4, U47 | desktop | ![FL-F25-08 step 4, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/4-worker-handoff-desktop-light.png) | ![FL-F25-08 step 4, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/4-worker-handoff-desktop-dark.png) |
| FL-F25-08 step 4, U47 | phone | ![FL-F25-08 step 4, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/4-worker-handoff-phone-light.png) | ![FL-F25-08 step 4, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/4-worker-handoff-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-32-worker-handoff-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-32-worker-handoff-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-32-worker-handoff-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-32-worker-handoff-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-32-worker-handoff-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-32-worker-handoff-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-32-worker-handoff-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-32-worker-handoff-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Role | E-F25-21 role | text | no | yes |
| Worktree and branch | E-F25-21 worktree, branch | text | no | yes |
| Starting commit | E-F25-21 starting commit | commit hash | no | yes |
| Commits in order | E-F25-21 commits | commit hashes with messages | no | yes |
| Changed files | E-F25-21 changed files | list of paths | no | yes |
| Checks | E-F25-21 checks | command, exit code, matches | no | yes |
| Blockers | E-F25-21 blockers | text | no | no |
| Refusal reason | E-F25-21 reason | text | no | when Refused |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open the branch | footer | maintainer | opens the worker's branch in GitHub |
| Open the contract | footer | maintainer | opens the work contract (S-F25-29) |
| Clear the blocker | footer | maintainer | writes the decision, the worker resumes and the handoff is Submitted again |
| Stop the run | footer | maintainer | stops the run, the handoff is Abandoned and the branch kept |

## States

- Normal: the handoff with its commits, files, checks and exit codes, and the result of the handoff check.
- Empty: No handoff yet: the worker is still working, with its turns and cost.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  handoff names what is missing or wrong: a commit, a check, an exit code, a file of another role or the starting
  commit.
- Read-only: an Accepted or Integrated handoff: values shown, nothing editable.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)). The app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F25-21 Worker handoff](../../data/e-f25-21-worker-handoff.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-21 Worker handoff | Submitted | Badge "Submitted"; a new record starts here; next: Accepted, Refused or Blocked (BR-F25-25, UC-F25-32); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-32-worker-handoff-e-f25-21-worker-handoff-submitted-{desktop,phone}-{light,dark}.png` |
| E-F25-21 Worker handoff | Accepted | Badge "Accepted"; next: Integrated (UC-F25-33); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-32-worker-handoff-e-f25-21-worker-handoff-accepted-{desktop,phone}-{light,dark}.png` |
| E-F25-21 Worker handoff | Refused | Badge "Refused"; next: Submitted or Abandoned (UC-F25-32, BR-F25-25); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-32-worker-handoff-e-f25-21-worker-handoff-refused-{desktop,phone}-{light,dark}.png` |
| E-F25-21 Worker handoff | Blocked | Badge "Blocked"; next: Submitted or Abandoned (UC-F25-32); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-32-worker-handoff-e-f25-21-worker-handoff-blocked-{desktop,phone}-{light,dark}.png` |
| E-F25-21 Worker handoff | Integrated | Badge "Integrated"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simpleerp-maintainer/s-f25-32-worker-handoff-e-f25-21-worker-handoff-integrated-{desktop,phone}-{light,dark}.png` |
| E-F25-21 Worker handoff | Abandoned | Badge "Abandoned"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simpleerp-maintainer/s-f25-32-worker-handoff-e-f25-21-worker-handoff-abandoned-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F25-31 Agent workers](s-f25-31-agent-workers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-33 Integration](s-f25-33-integration.md)
