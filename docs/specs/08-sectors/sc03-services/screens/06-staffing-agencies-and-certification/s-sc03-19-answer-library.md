🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-06 Staffing, agencies, certification and tender library](README.md) ›
🖥️ S-SC03-19 Answer library

# 🖥️ S-SC03-19 Answer library

**Status:** 🔄 waiting for the owner

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md): the answers of the firm and their
  reviews.
- [U03 Sales](../../../../01-users/personas/u03-sales.md): the answers they can reuse.

## Purpose

Find, reuse and review the answers used in tenders, with each answer's owner and review date.

## Entry points

Services › Answers; the tender's Questions tab; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Answer: Quality system, 120 words, English                            Approved                   |
| Owner Sophie V.   Reviewed 2026-03-01   Review due 2027-03-01   Used in 14 tenders               |
| Tags  quality, certification, method          Confidential  no                                   |
| Text  Our quality system is certified and audited every year ...                                 |
| Tender T-2026-019  Q12  Quality system        Linked   [Adapt] [Replace]                         |
| Stale answers in this tender: 1   [Send for review]                                              |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-06 step 4, U24 | desktop | ![FL-SC03-06 step 4, U24, light](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/4-answer-library-desktop-light.png) | ![FL-SC03-06 step 4, U24, dark](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/4-answer-library-desktop-dark.png) |
| FL-SC03-06 step 4, U24 | phone | ![FL-SC03-06 step 4, U24, light](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/4-answer-library-phone-light.png) | ![FL-SC03-06 step 4, U24, dark](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/4-answer-library-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-19-answer-library-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-19-answer-library-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-19-answer-library-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-19-answer-library-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-19-answer-library-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-19-answer-library-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-19-answer-library-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-19-answer-library-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Question or topic | E-SC03-20 topic | text | yes while Draft | yes |
| Text | E-SC03-20 text | text | yes while Draft | yes |
| Language and tags | E-SC03-20 language, tags | choice and tags | yes | no |
| Owner | E-SC03-20 owner | user | yes | yes |
| Reviewed on and due | E-SC03-20 reviewed on, review due | two dates | no | yes |
| Use count | E-SC03-20 used in | number | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Reuse | answer | engagement manager, sales | the answer is linked in the tender |
| Adapt | tender answer | engagement manager, sales | a copy edited for the tender |
| Review | answer | owner | the answer is confirmed or updated with a new date |
| Retire | answer | owner, engagement manager | the answer is no longer proposed |

## States

- Normal: the answer with its owner, review dates and use, and the tender's questions with their answers.
- Empty: No answer yet, with New answer.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a Stale answer
  added to a tender, with its review date.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC03-20 Answer](../../data/e-sc03-20-answer.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-20 Answer | Draft | Badge "Draft"; a new record starts here; next: Approved (UC-SC03-19); fields editable within the role | U24, U03 | `u24-engagement-manager/s-sc03-19-answer-library-e-sc03-20-answer-draft-{desktop,phone}-{light,dark}.png`, `u03-sales/s-sc03-19-answer-library-e-sc03-20-answer-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC03-20 Answer | Approved | Badge "Approved"; next: Stale or Retired (BR-SC03-19, UC-SC03-19); fields editable within the role | U24, U03 | `u24-engagement-manager/s-sc03-19-answer-library-e-sc03-20-answer-approved-{desktop,phone}-{light,dark}.png`, `u03-sales/s-sc03-19-answer-library-e-sc03-20-answer-approved-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC03-20 Answer | Stale | Badge "Stale"; next: Approved or Retired (UC-SC03-19, BR-SC03-19); fields editable within the role | U24, U03 | `u24-engagement-manager/s-sc03-19-answer-library-e-sc03-20-answer-stale-{desktop,phone}-{light,dark}.png`, `u03-sales/s-sc03-19-answer-library-e-sc03-20-answer-stale-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC03-20 Answer | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U24, U03 | `u24-engagement-manager/s-sc03-19-answer-library-e-sc03-20-answer-retired-{desktop,phone}-{light,dark}.png`, `u03-sales/s-sc03-19-answer-library-e-sc03-20-answer-retired-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-SC03-18 Certification audits](s-sc03-18-certification-audits.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-L01 Engagements](../00-lists/s-sc03-l01-engagements.md)
