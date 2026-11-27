🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F25-35 Repair cycles

# 🖥️ S-F25-35 Repair cycles

**Status:** 🔄 waiting for the owner

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md): the cycles of a run, their
  findings, and the blockers to decide on.

## Purpose

Show each repair cycle of a run: the findings, the role they went to, the new candidate commit, and the maintainer's
choices once the two cycles are used.

## Entry points

DevOps agents › Verifications › a run; the notification of the blockers.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Repair cycles   #314 Payslip export          Cycle 2 of 2 used          Blockers 1          |
|---------------------------------------------------------------------------------------------|
| CYCLE  FINDING                                  ROLE               NEW COMMIT  RESULT       |
| 1      export line 42, net pay rounded down     backend engineer   4b7d0a3     Fixed        |
| 1      payslip screen: no full-flow test        test engineer      4b7d0a3     Fixed        |
| 2      totals differ on a part-time payslip     backend engineer   c81e5f0     Rejected     |
| BLOCKERS FOR THE MAINTAINER                                                                 |
|  The part-time case is not in the acceptance criteria of the contract.                      |
| [Change the contract] [Ask for changes by hand] [Take over] [Decline the run]               |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-08 step 7, U47 | desktop | ![FL-F25-08 step 7, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/7-repair-cycles-desktop-light.png) | ![FL-F25-08 step 7, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/7-repair-cycles-desktop-dark.png) |
| FL-F25-08 step 7, U47 | phone | ![FL-F25-08 step 7, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/7-repair-cycles-phone-light.png) | ![FL-F25-08 step 7, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/7-repair-cycles-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-35-repair-cycles-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-35-repair-cycles-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-35-repair-cycles-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-35-repair-cycles-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-35-repair-cycles-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-35-repair-cycles-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-35-repair-cycles-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-35-repair-cycles-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Cycle | E-F25-22 cycle | number of 2 | no | yes |
| Finding | E-F25-22 findings | text with file and line | no | yes |
| Role | E-F25-20 role | text | no | yes |
| New commit | E-F25-22 candidate commit | shortened identifier | no | no |
| Blockers | the open findings after the second cycle | list | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Change the contract | blockers | maintainer | opens the contract for a change, approved again (UC-F25-30) |
| Ask for changes by hand | blockers | maintainer | comments as in UC-F25-13 |
| Take over | blockers | maintainer | a person goes on from the last candidate commit |
| Decline the run | blockers | maintainer | stops the run; the commits stay on their branches |

## States

- Normal: the cycles with their findings, roles, new commits and results.
- Empty: No repair yet: the first candidate passed or is being verified.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  handoff shows the weakened test and the finding kept open.
- Read-only: a run whose maintainer has decided: the cycles and the decision shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F25-08](../../flows/fl-f25-08-team-builds-a-ticket.md)

## Open questions

None.

---

⬅️ [S-F25-34 Candidate verification](s-f25-34-candidate-verification.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-36 Draft pull request](s-f25-36-draft-pull-request.md)
