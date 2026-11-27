🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F25-37 Run resume

# 🖥️ S-F25-37 Run resume

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md): the active, queued and interrupted runs
  of each repository and their checkpoints.

## Purpose

Show the runs of each repository, the cause of a stop and the last checkpoint, and rerun an interrupted run from it.

## Entry points

DevOps agents › Runs; the notification of an interrupted run.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Run resume      Active 1   Queued 2   Interrupted 1        Repository [SimpleERP v]        |
|---------------------------------------------------------------------------------------------|
| RUN  TICKET  STATE        CAUSE              LAST CHECKPOINT       ELAPSED  COST            |
| 81   #314    Interrupted  30-minute timeout  integration done      30 min   4.10 USD        |
| 82   #318    Active       -                  worker commits        12 min   1.30 USD        |
| 83   #320    Queued       -                  -                     -        -               |
| Checkpoint of run 81: start 1a2b3c4, 3 worker branches, 5 commits, integration 7e9f         |
|  draft pull request: none yet   repair cycles 0   maintainer interventions 0                |
| [Rerun from the checkpoint] [Open the checkpoint] [Abandon] [Move in the queue]             |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-08 step 9, U48 | desktop | ![FL-F25-08 step 9, U48, light](../../images/08-team-builds-a-ticket/u48-hosting-engineer/9-run-resume-desktop-light.png) | ![FL-F25-08 step 9, U48, dark](../../images/08-team-builds-a-ticket/u48-hosting-engineer/9-run-resume-desktop-dark.png) |
| FL-F25-08 step 9, U48 | phone | ![FL-F25-08 step 9, U48, light](../../images/08-team-builds-a-ticket/u48-hosting-engineer/9-run-resume-phone-light.png) | ![FL-F25-08 step 9, U48, dark](../../images/08-team-builds-a-ticket/u48-hosting-engineer/9-run-resume-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-37-run-resume-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-37-run-resume-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-37-run-resume-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-37-run-resume-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-37-run-resume-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-37-run-resume-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-37-run-resume-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-37-run-resume-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Run and ticket | E-F25-23 run, ticket | number, link | no | yes |
| State and cause | E-F25-23 state, stop cause | badge, text | no | yes |
| Last checkpoint | E-F25-23 stage | text | no | yes |
| Starting commit and branches | E-F25-23 starting commit, worker branches | identifiers | no | yes |
| Elapsed time and AI cost | E-F25-23 metrics | duration, amount with currency | no | yes |
| Repair cycles and interventions | E-F25-23 metrics | numbers | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Rerun from the checkpoint | row | hosting engineer | resumes at the first unfinished stage |
| Open the checkpoint | row | hosting engineer, maintainer | shows every recorded stage |
| Abandon | row | maintainer | stops the run for good; branches and checkpoint kept |
| Move in the queue | row | hosting engineer | changes the order of the queued runs |

## States

- Normal: the runs of the repository with state, cause, last checkpoint, elapsed time and cost.
- Empty: No run on this repository yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a run that
  cannot resume names the missing commit or the unreadable checkpoint.
- Read-only: a Finished or Abandoned run: the checkpoint and the metrics shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F25-23 Run checkpoint](../../data/e-f25-23-run-checkpoint.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-23 Run checkpoint | Queued | Badge "Queued"; a new record starts here; next: Active or Abandoned (BR-F25-30, UC-F25-37); fields editable within the role | U48 | `u48-hosting-engineer/s-f25-37-run-resume-e-f25-23-run-checkpoint-queued-{desktop,phone}-{light,dark}.png` |
| E-F25-23 Run checkpoint | Active | Badge "Active"; a new record starts here; next: Interrupted or Finished (UC-F25-37, UC-F25-36); fields editable within the role | U48 | `u48-hosting-engineer/s-f25-37-run-resume-e-f25-23-run-checkpoint-active-{desktop,phone}-{light,dark}.png` |
| E-F25-23 Run checkpoint | Interrupted | Badge "Interrupted"; next: Active or Abandoned (UC-F25-37); fields editable within the role | U48 | `u48-hosting-engineer/s-f25-37-run-resume-e-f25-23-run-checkpoint-interrupted-{desktop,phone}-{light,dark}.png` |
| E-F25-23 Run checkpoint | Finished | Badge "Finished"; final: read-only, no next state; the history shows how it got here | U48 | `u48-hosting-engineer/s-f25-37-run-resume-e-f25-23-run-checkpoint-finished-{desktop,phone}-{light,dark}.png` |
| E-F25-23 Run checkpoint | Abandoned | Badge "Abandoned"; final: read-only, no next state; the history shows how it got here | U48 | `u48-hosting-engineer/s-f25-37-run-resume-e-f25-23-run-checkpoint-abandoned-{desktop,phone}-{light,dark}.png` |

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
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F25-08](../../flows/fl-f25-08-team-builds-a-ticket.md)

## Open questions

None.

---

⬅️ [S-F25-36 Draft pull request](s-f25-36-draft-pull-request.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-L01 Bug or feature requests](../00-lists/s-f25-l01-bug-or-feature-requests.md)
