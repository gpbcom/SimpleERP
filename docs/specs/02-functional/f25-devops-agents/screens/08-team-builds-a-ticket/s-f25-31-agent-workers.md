🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F25-31 Agent workers

# 🖥️ S-F25-31 Agent workers

**Status:** 🔄 waiting for the owner

## Personas

- [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md): the workers of each run, with
  their branches, tasks and blockers.
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md): the runners, turns, time and cost of
  each worker.

## Purpose

Follow the workers of a run, each in its own worktree, and stop one when needed.

## Entry points

DevOps agents › Agent team › a run › Workers; the approved contract; the agent costs screen (S-F25-18).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Agent workers  Run 57  Ticket 314  Start a3f9c21  Contract v2 Approved       [Stop the run] |
|---------------------------------------------------------------------------------------------|
| ROLE               BRANCH                  TASK  TOOLS        TURNS  COST       STATE       |
| Test Engineer      team/314/test-engineer  T0    write, test  18/40  0.21 EUR   Handed over |
| Backend Engineer   team/314/backend        T1    write, test  31/60  0.64 EUR   Working     |
| Frontend Engineer  team/314/frontend       T3    write, test  12/60  0.18 EUR   Working     |
| Code Reviewer      -                       -     read only    -      -          Waiting     |
|---------------------------------------------------------------------------------------------|
| ! Backend Engineer: write to web/payroll/exports/list refused, owned by Frontend    [Open]  |
| Run budget 1.03 of 5.00 EUR    Time 22 of 90 min                     [Stop this worker]     |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-08 step 3, U47 | desktop | ![FL-F25-08 step 3, U47, light](../../images/08-team-builds-a-ticket/u47-simple-erp-maintainer/3-agent-workers-desktop-light.png) | ![FL-F25-08 step 3, U47, dark](../../images/08-team-builds-a-ticket/u47-simple-erp-maintainer/3-agent-workers-desktop-dark.png) |
| FL-F25-08 step 3, U47 | phone | ![FL-F25-08 step 3, U47, light](../../images/08-team-builds-a-ticket/u47-simple-erp-maintainer/3-agent-workers-phone-light.png) | ![FL-F25-08 step 3, U47, dark](../../images/08-team-builds-a-ticket/u47-simple-erp-maintainer/3-agent-workers-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-31-agent-workers-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-31-agent-workers-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-31-agent-workers-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-31-agent-workers-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-31-agent-workers-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-31-agent-workers-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-31-agent-workers-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-31-agent-workers-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Role | E-F25-20 name | text | no | yes |
| Branch and worktree | the worker's own branch | text | no | yes |
| Task | E-F25-19 tasks | text | no | yes |
| Tools | E-F25-20 tools | list | no | yes |
| Turns, time and cost | E-F25-10 cost, E-F25-20 limits | number, amount with currency | no | yes |
| Blockers | the worker's blockers | text | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Stop this worker | row | maintainer, hosting engineer | stops the worker and keeps its worktree and commits for the handoff |
| Stop the run | header | maintainer, hosting engineer | stops every worker, the run can be resumed later (UC-F25-37) |
| Open | blocker | maintainer, hosting engineer | opens the refused write or the failed check |
| Open the role | row | maintainer, hosting engineer | opens the role's tools and limits (S-F25-L20) |

## States

- Normal: the workers of the run with their branch, task, tools, turns, cost and state, and the blockers under them.
- Empty: No worker yet: the contract waits for approval.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a stopped
  worker shows its blocker and its last check with the exit code.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)). The app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F25-20 Agent role](../../data/e-f25-20-agent-role.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-20 Agent role | Active | Badge "Active"; a new record starts here; next: Suspended or Retired (UC-F25-31, UC-F25-17); fields editable within the role | U47, U48 | `u47-simple-erp-maintainer/s-f25-31-agent-workers-e-f25-20-agent-role-active-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f25-31-agent-workers-e-f25-20-agent-role-active-{desktop,phone}-{light,dark}.png` |
| E-F25-20 Agent role | Suspended | Badge "Suspended"; next: Active or Retired (UC-F25-17); fields editable within the role | U47, U48 | `u47-simple-erp-maintainer/s-f25-31-agent-workers-e-f25-20-agent-role-suspended-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f25-31-agent-workers-e-f25-20-agent-role-suspended-{desktop,phone}-{light,dark}.png` |
| E-F25-20 Agent role | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U47, U48 | `u47-simple-erp-maintainer/s-f25-31-agent-workers-e-f25-20-agent-role-retired-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f25-31-agent-workers-e-f25-20-agent-role-retired-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F25-30 Contract approval](s-f25-30-contract-approval.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-32 Worker handoff](s-f25-32-worker-handoff.md)
