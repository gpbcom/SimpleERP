🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-06 Staffing, agencies, certification and tender library](README.md) ›
🖥️ S-SC03-17 Agency approvals

# 🖥️ S-SC03-17 Agency approvals

**Status:** ✅ specified

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md): every proof and media cost of their
  engagements.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the proofs sent to them.

## Purpose

Send proofs, record the client's approvals and rebill the media bought at cost plus the fee.

## Entry points

Services › Creative proofs; the client portal for the client; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Proof: Spring poster, version 4                                   Sent   [Upload] [Remind]       |
| Engagement Spring campaign   Deliverable Poster 4x3   Sent 2026-11-14   Waiting for Julie M.     |
| History  v1 changes asked - v2 changes asked - v3 changes asked - v4 sent                        |
| Media    Bus shelters   12,400.00 EUR cost   Fee 10 %   1,240.00 EUR   Total 13,640.00 EUR       |
| Supplier invoice  attached                              Production  blocked until approval       |
| Approvals  Julie M. waiting   Marc L. approved                                                   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-06 step 2, U24 | desktop | ![FL-SC03-06 step 2, U24, light](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/2-agency-approvals-desktop-light.png) | ![FL-SC03-06 step 2, U24, dark](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/2-agency-approvals-desktop-dark.png) |
| FL-SC03-06 step 2, U24 | phone | ![FL-SC03-06 step 2, U24, light](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/2-agency-approvals-phone-light.png) | ![FL-SC03-06 step 2, U24, dark](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/2-agency-approvals-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-17-agency-approvals-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-17-agency-approvals-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-17-agency-approvals-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-17-agency-approvals-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-17-agency-approvals-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-17-agency-approvals-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-17-agency-approvals-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-17-agency-approvals-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Engagement and deliverable | E-SC03-18 engagement, deliverable | links | no | yes |
| Version | E-SC03-18 version | number | yes while Draft | yes |
| File | E-SC03-18 file | image, film or document | yes while Draft | yes |
| Approvers and answers | E-SC03-18 approvals | person, answer, date | no | yes |
| Comments | E-SC03-18 comments | text on the image | yes | no |
| Media cost and fee | E-SC03-06 amount, fee | amounts | yes while Active | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Upload version | header | engagement manager | a new proof version in Sent |
| Approve | proof | client | the proof becomes Approved |
| Ask for changes | proof | client | the proof becomes Revising with the comments |
| Rebill media | media row | engagement manager | the media cost goes to the next invoice with its fee |

## States

- Normal: the proof with its history, approvers and answers, and the media cost with the fee.
- Empty: No proof yet, with Upload a proof.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a blocked
  production step or a media cost without its supplier invoice, with what is missing.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC03-18 Creative proof](../../data/e-sc03-18-creative-proof.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-18 Creative proof | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-SC03-17); fields editable within the role | U24, U09 | `u24-engagement-manager/s-sc03-17-agency-approvals-e-sc03-18-creative-proof-draft-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc03-17-agency-approvals-e-sc03-18-creative-proof-draft-phone-{light,dark}.png` |
| E-SC03-18 Creative proof | Sent | Badge "Sent"; next: Revising or Approved (UC-SC03-17, BR-SC03-17); fields editable within the role | U24, U09 | `u24-engagement-manager/s-sc03-17-agency-approvals-e-sc03-18-creative-proof-sent-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc03-17-agency-approvals-e-sc03-18-creative-proof-sent-phone-{light,dark}.png` |
| E-SC03-18 Creative proof | Revising | Badge "Revising"; next: Sent (UC-SC03-17); fields editable within the role | U24, U09 | `u24-engagement-manager/s-sc03-17-agency-approvals-e-sc03-18-creative-proof-revising-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc03-17-agency-approvals-e-sc03-18-creative-proof-revising-phone-{light,dark}.png` |
| E-SC03-18 Creative proof | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U24, U09 | `u24-engagement-manager/s-sc03-17-agency-approvals-e-sc03-18-creative-proof-approved-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc03-17-agency-approvals-e-sc03-18-creative-proof-approved-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the agency; the client's view on the phone shows the proof, a comment tool and the Approve and Ask for
changes buttons.

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

⬅️ [S-SC03-16 Staffing assignments](s-sc03-16-staffing-assignments.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-18 Certification audits](s-sc03-18-certification-audits.md)
