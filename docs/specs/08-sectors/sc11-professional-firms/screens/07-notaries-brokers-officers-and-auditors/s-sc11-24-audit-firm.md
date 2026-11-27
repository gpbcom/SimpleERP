🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-07 Notaries, brokers, judicial officers and audit firms](README.md) ›
🖥️ S-SC11-24 Audit firm

# 🖥️ S-SC11-24 Audit firm

**Status:** ✅ specified

## Personas

- [U49 Statutory auditor](../../../../01-users/personas/u49-statutory-auditor.md): the engagements of their team, their
  requests and their samples.
- [U36 Professional](../../../../01-users/personas/u36-professional.md): the mandates, the signing partners and the
  rotation dates.

## Purpose

Follow each mandate's years, signing partner and rotation date, and the requests and samples of each audit.

## Entry points

Professional firm › Audit engagements; the client's matter; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Engagement AE-2026-014: Tuileries SA (public-interest entity)             Active   [Rotate]      |
| Mandate 2026 to 2031   Signing partner Mrs Girard since 2026   Rotation due 2033                 |
| Independence check 2026-09-02  Engagement letter signed 2026-09-10                               |
| Year  Opinion      Hours   Requests   Samples                                                    |
| 2026  In progress  310     12 / 14    40 invoices                                                |
| Rotation warnings: 12 months, 6 months, 3 months before the date                                 |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-07 step 4, U49 | desktop | ![FL-SC11-07 step 4, U49, light](../../images/07-notaries-brokers-officers-and-auditors/u49-statutory-auditor/4-audit-firm-desktop-light.png) | ![FL-SC11-07 step 4, U49, dark](../../images/07-notaries-brokers-officers-and-auditors/u49-statutory-auditor/4-audit-firm-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-24-audit-firm-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-24-audit-firm-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-24-audit-firm-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-24-audit-firm-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-24-audit-firm-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-24-audit-firm-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc11-24-audit-firm-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc11-24-audit-firm-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Client | E-SC11-19 client | link | yes while Proposed | yes |
| Mandate years | E-SC11-19 first year, length | year and number | yes while Proposed | yes |
| Signing partner | E-SC11-19 signing partner | employee link | yes | yes |
| Rotation date | E-SC11-19 rotation date | date | no | no |
| Independence check | E-SC11-19 independence checked on | date | yes while Proposed | yes |
| Requests and samples | E-SC11-19 requests | list | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Accept the engagement | engagement | partner | the engagement becomes Active |
| Send a request | engagement | auditor | a request to the client's accountant |
| Rotate the partner | engagement | partner | a replacing signing partner, the history kept |
| End | engagement | partner | the engagement becomes Ended |

## States

- Normal: the mandate, its signing partner and rotation date, and the requests and samples of the year.
- Empty: No engagement yet, with New engagement.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  independence check or a partner at rotation, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC11-19 Audit engagement](../../data/e-sc11-19-audit-engagement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-19 Audit engagement | Proposed | Badge "Proposed"; a new record starts here; next: Active (UC-SC11-24); fields editable within the role | U49, U36 | `u49-statutory-auditor/s-sc11-24-audit-firm-e-sc11-19-audit-engagement-proposed-desktop-{light,dark}.png`, `u36-professional/s-sc11-24-audit-firm-e-sc11-19-audit-engagement-proposed-{desktop,phone}-{light,dark}.png` |
| E-SC11-19 Audit engagement | Active | Badge "Active"; next: Rotation due or Ended (BR-SC11-19, UC-SC11-24); fields editable within the role | U49, U36 | `u49-statutory-auditor/s-sc11-24-audit-firm-e-sc11-19-audit-engagement-active-desktop-{light,dark}.png`, `u36-professional/s-sc11-24-audit-firm-e-sc11-19-audit-engagement-active-{desktop,phone}-{light,dark}.png` |
| E-SC11-19 Audit engagement | Rotation due | Badge "Rotation due"; next: Active (BR-SC11-19); fields editable within the role | U49, U36 | `u49-statutory-auditor/s-sc11-24-audit-firm-e-sc11-19-audit-engagement-rotation-due-desktop-{light,dark}.png`, `u36-professional/s-sc11-24-audit-firm-e-sc11-19-audit-engagement-rotation-due-{desktop,phone}-{light,dark}.png` |
| E-SC11-19 Audit engagement | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U49, U36 | `u49-statutory-auditor/s-sc11-24-audit-firm-e-sc11-19-audit-engagement-ended-desktop-{light,dark}.png`, `u36-professional/s-sc11-24-audit-firm-e-sc11-19-audit-engagement-ended-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC11-07](../../flows/fl-sc11-07-notaries-brokers-officers-and-auditors.md)

## Open questions

None.

---

⬅️ [S-SC11-23 Judicial officer](s-sc11-23-judicial-officer.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-L01 Client identities](../00-lists/s-sc11-l01-client-identities.md)
