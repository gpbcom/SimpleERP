🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-06 Staffing, agencies, certification and tender library](README.md) ›
🖥️ S-SC03-18 Certification audits

# 🖥️ S-SC03-18 Certification audits

**Status:** 🔄 waiting for the owner

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md): every audit and certificate of the
  body.
- [U36 Professional](../../../../01-users/personas/u36-professional.md): the audits they are assigned to.

## Purpose

Plan audits with qualified and impartial auditors, record the decision and follow each certificate until its
surveillance audit.

## Entry points

Services › Certificates; the engagement's Audits tab; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Certificate C-2026-044: Atelier Roux SAS, quality management               Issued                |
| Scope  Manufacture of wooden furniture     Issued 2026-02-01   Valid to 2029-01-31               |
| Audit              Date         Auditor        Result                                            |
| Initial            2026-01-12   Sophie V.      Positive, 2 minor findings                        |
| Surveillance 1     2027-01-31   to plan        Due in 78 days                                    |
| Surveillance 2     2028-01-31   not yet        -                                                 |
| Impartiality  checked 2026-01-05, no advice given to the client                                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-06 step 3, U24 | desktop | ![FL-SC03-06 step 3, U24, light](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/3-certification-audits-desktop-light.png) | ![FL-SC03-06 step 3, U24, dark](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/3-certification-audits-desktop-dark.png) |
| FL-SC03-06 step 3, U24 | phone | ![FL-SC03-06 step 3, U24, light](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/3-certification-audits-phone-light.png) | ![FL-SC03-06 step 3, U24, dark](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/3-certification-audits-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-18-certification-audits-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-18-certification-audits-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-18-certification-audits-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-18-certification-audits-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-18-certification-audits-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-18-certification-audits-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-18-certification-audits-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-18-certification-audits-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Client and standard | E-SC03-19 client, standard | link and text | no | yes |
| Scope | E-SC03-19 scope | text | yes while Pending | yes |
| Issue and validity | E-SC03-19 issued on, valid to | two dates | no | no |
| Surveillance dates | E-SC03-19 surveillance dates | dates | no | no |
| Audits | E-SC03-19 audits | date, auditor, result | yes while Pending or Issued | no |
| Impartiality check | E-SC03-19 impartiality | text and date | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Plan audit | header | engagement manager | an audit with days and auditors |
| Record findings | audit | auditor | the findings and recommendation |
| Decide | certificate | engagement manager | the certificate is Issued or refused |
| Withdraw | certificate | engagement manager | the certificate is Withdrawn with its reason |

## States

- Normal: the certificate with its scope, validity, surveillance dates and audits.
- Empty: No certificate yet, with New certification.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a failed
  impartiality check or an incomplete report, with the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC03-19 Certificate](../../data/e-sc03-19-certificate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-19 Certificate | Pending | Badge "Pending"; a new record starts here; next: Issued or Withdrawn (UC-SC03-18); fields editable within the role | U24, U36 | `u24-engagement-manager/s-sc03-18-certification-audits-e-sc03-19-certificate-pending-{desktop,phone}-{light,dark}.png`, `u36-professional/s-sc03-18-certification-audits-e-sc03-19-certificate-pending-{desktop,phone}-{light,dark}.png` |
| E-SC03-19 Certificate | Issued | Badge "Issued"; next: Lapsed, Expired or Withdrawn (BR-SC03-18, UC-SC03-18); fields editable within the role | U24, U36 | `u24-engagement-manager/s-sc03-18-certification-audits-e-sc03-19-certificate-issued-{desktop,phone}-{light,dark}.png`, `u36-professional/s-sc03-18-certification-audits-e-sc03-19-certificate-issued-{desktop,phone}-{light,dark}.png` |
| E-SC03-19 Certificate | Lapsed | Badge "Lapsed"; next: Issued (UC-SC03-18); fields editable within the role | U24, U36 | `u24-engagement-manager/s-sc03-18-certification-audits-e-sc03-19-certificate-lapsed-{desktop,phone}-{light,dark}.png`, `u36-professional/s-sc03-18-certification-audits-e-sc03-19-certificate-lapsed-{desktop,phone}-{light,dark}.png` |
| E-SC03-19 Certificate | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U24, U36 | `u24-engagement-manager/s-sc03-18-certification-audits-e-sc03-19-certificate-expired-{desktop,phone}-{light,dark}.png`, `u36-professional/s-sc03-18-certification-audits-e-sc03-19-certificate-expired-{desktop,phone}-{light,dark}.png` |
| E-SC03-19 Certificate | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U24, U36 | `u24-engagement-manager/s-sc03-18-certification-audits-e-sc03-19-certificate-withdrawn-{desktop,phone}-{light,dark}.png`, `u36-professional/s-sc03-18-certification-audits-e-sc03-19-certificate-withdrawn-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC03-06](../../flows/fl-sc03-06-staffing-agencies-and-certification.md)

## Open questions

None.

---

⬅️ [S-SC03-17 Agency approvals](s-sc03-17-agency-approvals.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-19 Answer library](s-sc03-19-answer-library.md)
