🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-06 Privacy and AI duties](README.md) › 🖥️ S-F15-10 Privacy and AI register

# 🖥️ S-F15-10 Privacy and AI register

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md), who handles requests and the inventory
- [U06 Human resources](../../../../01-users/personas/u06-hr.md), who handles employees' and candidates' requests
- [U13 Owner](../../../../01-users/personas/u13-owner.md), who approves impact assessments

## Purpose

Handle data-subject requests within their month and keep the inventory of AI uses with their assessments.

## Entry points

Legal menu, Privacy and AI; a request notification; turning on an AI feature in F1.

## Wireframe

```text
Privacy and AI register                          [Requests 2] [AI uses 6]
-------------------------------------------------------------------------------
Requests: Sophie Bernard, access, received 2026-11-12, due 2026-12-12, verified
          J. Martin, erasure, received 2026-11-03, due 2026-12-03, overdue in 4 d
AI uses:  Assistant, local model, limited, on
          Candidate scoring, local model, high, off (assessment to approve)
-------------------------------------------------------------------------------
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-06 step 1, U07 | desktop | ![FL-F15-06 step 1, U07, light](../../images/06-privacy-and-ai-duties/u07-administrator/1-privacy-and-ai-register-desktop-light.png) | ![FL-F15-06 step 1, U07, dark](../../images/06-privacy-and-ai-duties/u07-administrator/1-privacy-and-ai-register-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/06-privacy-and-ai-duties/u07-administrator/e1-privacy-and-ai-register-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/06-privacy-and-ai-duties/u07-administrator/e1-privacy-and-ai-register-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-10-privacy-and-ai-register-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-10-privacy-and-ai-register-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-10-privacy-and-ai-register-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-10-privacy-and-ai-register-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-10-privacy-and-ai-register-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-10-privacy-and-ai-register-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f15-10-privacy-and-ai-register-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f15-10-privacy-and-ai-register-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Person | E-F15-08 person | name | no | yes |
| Kind | E-F15-08 kind | access, erasure, correction, objection | yes | yes |
| Due | E-F15-08 due | date | no (computed) | yes |
| Feature | E-F15-09 feature | name | no | yes |
| Risk class | E-F15-09 risk class | minimal, limited, high | no | yes |
| Assessment | E-F15-09 assessment | file | yes | if high |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Record a request | requests tab | administrator, HR | due date set |
| Check identity | request | administrator, HR | verified |
| Send copy or erase | request | administrator | answered, person told |
| Draft assessment | AI use | administrator | draft with the AI assistant |
| Approve | AI use | owner | use may be turned on |

## States

- Normal: requests with their due dates and states, and the AI uses with their risk class and assessment.
- Empty: "No request and no AI use": shown when no request was received and no AI feature is on.
- Loading: the frame and titles show at once with placeholder rows for the requests and AI uses; within 1 second (D408)
  the data replaces them, and a longer load shows a progress line saying what loads.
- Error: an overdue request in red with text, or a high-risk use refused without assessment.
- Read-only: the owner reads requests; HR handles only employees' and candidates' requests.
- Offline: not available offline: searching the data runs on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F15-09 AI use](../../data/e-f15-09-ai-use.md),
[E-F15-08 Data-subject request](../../data/e-f15-08-data-subject-request.md),
[E-F15-13 Data protection impact assessment](../../data/e-f15-13-data-protection-impact-assessment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-09 AI use | On | Badge "On"; next: Off (UC-F15-11); fields editable within the role | U01, U06, U07, U09, U13 | `u01-employee/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-on-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-on-desktop-{light,dark}.png`, `u07-administrator/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-on-desktop-{light,dark}.png`, `u09-customer/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-on-phone-{light,dark}.png`, `u13-owner/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-on-{desktop,phone}-{light,dark}.png` |
| E-F15-09 AI use | Off | Badge "Off"; final: read-only, no next state; the history shows how it got here | U01, U06, U07, U09, U13 | `u01-employee/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-off-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-off-desktop-{light,dark}.png`, `u07-administrator/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-off-desktop-{light,dark}.png`, `u09-customer/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-off-phone-{light,dark}.png`, `u13-owner/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-off-{desktop,phone}-{light,dark}.png` |
| E-F15-08 Data-subject request | Received | Badge "Received"; a new record starts here; next: Verified or Overdue (UC-F15-10); fields editable within the role | U01, U06, U07, U09, U13 | `u01-employee/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-received-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-received-desktop-{light,dark}.png`, `u07-administrator/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-received-desktop-{light,dark}.png`, `u09-customer/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-received-phone-{light,dark}.png`, `u13-owner/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-received-{desktop,phone}-{light,dark}.png` |
| E-F15-08 Data-subject request | Verified | Badge "Verified"; next: Answered or Overdue (UC-F15-10); fields editable within the role | U01, U06, U07, U09, U13 | `u01-employee/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-verified-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-verified-desktop-{light,dark}.png`, `u07-administrator/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-verified-desktop-{light,dark}.png`, `u09-customer/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-verified-phone-{light,dark}.png`, `u13-owner/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-verified-{desktop,phone}-{light,dark}.png` |
| E-F15-08 Data-subject request | Overdue | Badge "Overdue"; next: Answered (UC-F15-10); fields editable within the role | U01, U06, U07, U09, U13 | `u01-employee/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-overdue-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-overdue-desktop-{light,dark}.png`, `u07-administrator/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-overdue-desktop-{light,dark}.png`, `u09-customer/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-overdue-phone-{light,dark}.png`, `u13-owner/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-overdue-{desktop,phone}-{light,dark}.png` |
| E-F15-08 Data-subject request | Answered | Badge "Answered"; final: read-only, no next state; the history shows how it got here | U01, U06, U07, U09, U13 | `u01-employee/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-answered-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-answered-desktop-{light,dark}.png`, `u07-administrator/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-answered-desktop-{light,dark}.png`, `u09-customer/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-answered-phone-{light,dark}.png`, `u13-owner/s-f15-10-privacy-and-ai-register-e-f15-08-data-subject-request-answered-{desktop,phone}-{light,dark}.png` |
| E-F15-09 AI use | Listed | Badge "Listed"; a new record starts here; next: Assessed or On (UC-F15-11); fields editable within the role | U01, U06, U07, U09, U13 | `u01-employee/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-listed-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-listed-desktop-{light,dark}.png`, `u07-administrator/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-listed-desktop-{light,dark}.png`, `u09-customer/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-listed-phone-{light,dark}.png`, `u13-owner/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-listed-{desktop,phone}-{light,dark}.png` |
| E-F15-09 AI use | Assessed | Badge "Assessed"; next: On (UC-F15-11); fields editable within the role | U01, U06, U07, U09, U13 | `u01-employee/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-assessed-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-assessed-desktop-{light,dark}.png`, `u07-administrator/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-assessed-desktop-{light,dark}.png`, `u09-customer/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-assessed-phone-{light,dark}.png`, `u13-owner/s-f15-10-privacy-and-ai-register-e-f15-09-ai-use-assessed-{desktop,phone}-{light,dark}.png` |
| E-F15-13 Data protection impact assessment | Draft | Badge "Draft"; a new record starts here; next: Approved or Refused (UC-F15-11); fields editable within the role | U01, U06, U07, U09, U13 | `u01-employee/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-draft-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-draft-desktop-{light,dark}.png`, `u07-administrator/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-draft-desktop-{light,dark}.png`, `u09-customer/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-draft-phone-{light,dark}.png`, `u13-owner/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-draft-{desktop,phone}-{light,dark}.png` |
| E-F15-13 Data protection impact assessment | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U01, U06, U07, U09, U13 | `u01-employee/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-approved-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-approved-desktop-{light,dark}.png`, `u07-administrator/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-approved-desktop-{light,dark}.png`, `u09-customer/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-approved-phone-{light,dark}.png`, `u13-owner/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-approved-{desktop,phone}-{light,dark}.png` |
| E-F15-13 Data protection impact assessment | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U01, U06, U07, U09, U13 | `u01-employee/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-refused-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-refused-desktop-{light,dark}.png`, `u07-administrator/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-refused-desktop-{light,dark}.png`, `u09-customer/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-refused-phone-{light,dark}.png`, `u13-owner/s-f15-10-privacy-and-ai-register-e-f15-13-data-protection-impact-assessment-refused-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F15-06 Privacy and AI duties](../../flows/fl-f15-06-privacy-and-ai-duties.md)

## Open questions

None.

---

⬅️ [S-F15-09 Company records](../05-duties-and-records/s-f15-09-company-records.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-11 Lawyer hand-off](../01-ask-a-legal-question/s-f15-11-lawyer-hand-off.md)
