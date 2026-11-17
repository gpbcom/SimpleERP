🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ S-F25-34 Candidate verification

# 🖥️ S-F25-34 Candidate verification

**Status:** 🔄 waiting for the owner

## Personas

- [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md): the checks of each candidate
  commit, their evidence and the code reviewer's verdict.

## Purpose

Show, for one candidate commit, every required check with its command, exit code and evidence, the false-confidence
signals and the code reviewer's verdict.

## Entry points

DevOps agents › Verifications; the ticket's run; the draft pull request's verified commit.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Candidate verification   #314 Payslip export   Cycle 1 of 2   Commit 9f2c4e1  [Copy full]   |
|---------------------------------------------------------------------------------------------|
| REQUIRED CHECK         COMMAND                     EXIT  EVIDENCE        RESULT             |
| Build                  build the images            0     build.log       Passed             |
| Lint and types         lint, type check            0     lint.log        Passed             |
| Unit tests             unit test suite             0     junit.xml       Passed             |
| Acceptance 3 of 4      end to end, real images     1     e2e report      Failed             |
| False confidence: the payslip screen passed with mocks only; no full-flow test              |
| CODE REVIEWER, read-only   Verdict: CHANGES_REQUESTED for 9f2c4e1                           |
|  payroll export, line 42   net pay rounded down   round half up as the contract says        |
| [Open evidence] [Send to repair] [Send the blockers to the maintainer]                      |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-08 step 6, U47 | desktop | ![FL-F25-08 step 6, U47, light](../../images/08-team-builds-a-ticket/u47-simple-erp-maintainer/6-candidate-verification-desktop-light.png) | ![FL-F25-08 step 6, U47, dark](../../images/08-team-builds-a-ticket/u47-simple-erp-maintainer/6-candidate-verification-desktop-dark.png) |
| FL-F25-08 step 6, U47 | phone | ![FL-F25-08 step 6, U47, light](../../images/08-team-builds-a-ticket/u47-simple-erp-maintainer/6-candidate-verification-phone-light.png) | ![FL-F25-08 step 6, U47, dark](../../images/08-team-builds-a-ticket/u47-simple-erp-maintainer/6-candidate-verification-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-34-candidate-verification-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-34-candidate-verification-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-34-candidate-verification-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-34-candidate-verification-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-34-candidate-verification-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-34-candidate-verification-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-34-candidate-verification-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-34-candidate-verification-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Candidate commit | E-F25-22 candidate commit | full identifier, shortened with a copy button | no | yes |
| Cycle | E-F25-22 cycle | number of 2 | no | yes |
| Required checks | E-F25-22 checks | table: check, command, exit code, evidence, result | no | yes |
| False-confidence signals | E-F25-22 signals | list | no | no |
| Verdict | E-F25-22 verdict | PASS or CHANGES_REQUESTED | no | no |
| Findings | E-F25-22 findings | file and line, consequence, required correction | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open evidence | check row | maintainer | shows the raw output, report or screenshots of the check |
| Send to repair | toolbar | the run, after CHANGES_REQUESTED | starts a repair cycle (UC-F25-35) |
| Send the blockers to the maintainer | toolbar | the run, when Blocked or out of cycles | the maintainer decides (BR-F25-28) |
| Copy full | header | maintainer | copies the full commit identifier |

## States

- Normal: the candidate commit, its cycle, each required check with command, exit code, evidence and result, the
  false-confidence signals and the verdict.
- Empty: No candidate commit yet for this ticket: the workers are still building.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a Blocked check
  names what could not run and why; a refused edit names the file.
- Read-only: a Passed or Superseded verification: values and evidence shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F25-22 Verification](../../data/e-f25-22-verification.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-22 Verification | Running | Badge "Running"; a new record starts here; next: Checked, Changes requested or Blocked (UC-F25-34, UC-F25-35, BR-F25-27); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-34-candidate-verification-e-f25-22-verification-running-{desktop,phone}-{light,dark}.png` |
| E-F25-22 Verification | Checked | Badge "Checked"; next: Passed or Changes requested (BR-F25-27, UC-F25-35); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-34-candidate-verification-e-f25-22-verification-checked-{desktop,phone}-{light,dark}.png` |
| E-F25-22 Verification | Changes requested | Badge "Changes requested"; next: Superseded (UC-F25-35); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-34-candidate-verification-e-f25-22-verification-changes-requested-{desktop,phone}-{light,dark}.png` |
| E-F25-22 Verification | Blocked | Badge "Blocked"; next: Running (UC-F25-34); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-34-candidate-verification-e-f25-22-verification-blocked-{desktop,phone}-{light,dark}.png` |
| E-F25-22 Verification | Passed | Badge "Passed"; next: Superseded (BR-F25-27); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-34-candidate-verification-e-f25-22-verification-passed-{desktop,phone}-{light,dark}.png` |
| E-F25-22 Verification | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simple-erp-maintainer/s-f25-34-candidate-verification-e-f25-22-verification-superseded-{desktop,phone}-{light,dark}.png` |

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
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F25-08](../../flows/fl-f25-08-team-builds-a-ticket.md)

## Open questions

None.

---

⬅️ [S-F25-33 Integration](s-f25-33-integration.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-35 Repair cycles](s-f25-35-repair-cycles.md)
