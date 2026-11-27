🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F25-36 Draft pull request

# 🖥️ S-F25-36 Draft pull request

**Status:** 🔄 waiting for the owner

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md): the draft, its verified
  commit, its evidence and the GitHub CI results.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the plain-words progress of their company's request, on a
  phone.

## Purpose

Show the draft pull request of a ticket with its evidence, and tell the requester where their request stands.

## Entry points

DevOps agents › a ticket's run; the pull request link in GitHub; for the owner, My requests
([S-F25-14 My requests](../05-tell-the-customer/s-f25-14-my-requests.md)).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Draft pull request #57   #314 Payslip export   DRAFT   Head 9f2c4e1 = verified 9f2c4e1      |
|---------------------------------------------------------------------------------------------|
| ISSUE AND PROBLEM    The payroll firm cannot read the payslip export.                       |
| CHANGES              New export layout, rounding of the net pay, export screen.             |
| ACCEPTANCE           4 of 4 passed on 9f2c4e1                                               |
| COMMANDS             build 0   lint 0   types 0   unit tests 0   end to end 0  [Evidence]   |
| SPECIFICATION        [screenshot: export screen, desktop] [screenshot: export, phone]       |
| KNOWN LIMITS         Part-time payslips use the old layout until ticket #320.               |
| HOW TO REVIEW        Start with the export rule, then the screen.                           |
| GITHUB CI            Running, reported apart from the local checks                          |
| [Open in GitHub] [Open the verification] [Ask for changes]                                  |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-08 step 8, U47 | desktop | ![FL-F25-08 step 8, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/8-draft-pull-request-desktop-light.png) | ![FL-F25-08 step 8, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/8-draft-pull-request-desktop-dark.png) |
| FL-F25-08 step 8, U47 | phone | ![FL-F25-08 step 8, U47, light](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/8-draft-pull-request-phone-light.png) | ![FL-F25-08 step 8, U47, dark](../../images/08-team-builds-a-ticket/u47-simpleerp-maintainer/8-draft-pull-request-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-36-draft-pull-request-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-36-draft-pull-request-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-36-draft-pull-request-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-36-draft-pull-request-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-36-draft-pull-request-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-36-draft-pull-request-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-36-draft-pull-request-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-36-draft-pull-request-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Pull request and state | E-F25-05 number, draft | link and badge | no | yes |
| Head and verified commit | branch head, E-F25-22 candidate commit | two identifiers, equal | no | yes |
| Issue and problem, changes | the body | text | no | yes |
| Acceptance and commands | E-F25-22 checks | results with exit codes and evidence | no | yes |
| Specification screenshots | the specification's images | images, FRONTEND tickets | no | for FRONTEND |
| Known limits, how to review | the body | text | no | yes |
| GitHub CI | the pull request's checks | results, apart | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open in GitHub | header | maintainer | opens the draft to review, approve and merge (FL-F25-04) |
| Open the verification | header | maintainer | opens S-F25-34 for the verified commit |
| Ask for changes | footer | maintainer | as in UC-F25-13: a new run earns a new PASS |
| Follow | phone view | requesting company's owner | sends the status changes of the request |

## States

- Normal: the draft with its head and verified commit, its body's sections and the GitHub CI results apart.
- Empty: No draft yet: the candidate is being verified.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a head that
  differs from the verified commit, or a missing section, is named and the draft is not opened.
- Read-only: a merged or closed pull request: the body and the results shown, no action offered.
- Offline: The last status read is shown with its date on the phone; following waits for the network.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

On a phone the owner sees one card: the request's title in plain words, its status (built, waiting for the maintainers'
review), what changes in plain words and, for a change of screens, the specification's screenshots; never code, commits
or commands. The maintainer's view is desktop only.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F25-08](../../flows/fl-f25-08-team-builds-a-ticket.md)

## Open questions

None.

---

⬅️ [S-F25-35 Repair cycles](s-f25-35-repair-cycles.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-37 Run resume](s-f25-37-run-resume.md)
