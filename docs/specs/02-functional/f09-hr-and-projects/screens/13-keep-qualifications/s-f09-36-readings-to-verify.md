🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-13 Keep employees' qualifications](README.md) › 🖥️ S-F9-36 Readings to verify

# 🖥️ S-F9-36 Readings to verify

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md): every reading of the employees they handle.

## Purpose

Verify each AI reading beside its source document: confirm, correct or reject.

## Entry points

HR and projects › Qualifications › Readings to verify; the banner on S-F9-35; the daily summary of readings waiting.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Readings to verify (7)                         Employee: all v   Document type: all v        |
|---------------------------------------------------------------------------------------------|
| QUEUE                     | SOURCE DOCUMENT                  | READING                       |
| > Paul Martin  licence    | [ scan of the driving licence,   | Type     Driving licence  97 %|
|   Lea Martin   diploma    |   the fields read highlighted ]  | Category B                95 %|
|   Hugo Leroy   CACES      |                                  | Issued   2018-06-01       91 %|
|   ...                     |                                  | Expires  2033-06-01  (!)  62 %|
|                           |                                  |   [ 2033-06-01 ] edit         |
|                           |                                  | [Confirm] [Correct and confirm]|
|                           |                                  | [Reject...]                   |
+---------------------------------------------------------------------------------------------+
Fields under the confidence threshold (80 %, D517) are marked (!) and must be looked at.
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-13 step 3, U06 | desktop | ![FL-F9-13 step 3, U06, light](../../images/13-keep-qualifications/u06-hr/3-readings-to-verify-desktop-light.png) | ![FL-F9-13 step 3, U06, dark](../../images/13-keep-qualifications/u06-hr/3-readings-to-verify-desktop-dark.png) |
| Error E2, U06 | desktop | ![Error E2, U06, light](../../images/13-keep-qualifications/u06-hr/e2-the-reading-disagrees-with-the-record-desktop-light.png) | ![Error E2, U06, dark](../../images/13-keep-qualifications/u06-hr/e2-the-reading-disagrees-with-the-record-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-36-readings-to-verify-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-36-readings-to-verify-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-36-readings-to-verify-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-36-readings-to-verify-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-36-readings-to-verify-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-36-readings-to-verify-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-36-readings-to-verify-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-36-readings-to-verify-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Queue | E-F9-31 in "to verify" | employee, document kind | no | yes |
| Source document | E-F9-31 source document | image or PDF with highlights | no | yes |
| Fields read | E-F9-31 fields and confidence | value and percentage | yes, before confirming | yes |
| Reject reason | E-F9-31 reason | text | yes | when rejecting |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Confirm | reading | HR | the degree or qualification verified, source "AI reading" (BR-F9-28) |
| Correct and confirm | reading | HR | the same, with the old and new values audited |
| Reject | reading | HR | not created; the reason kept; the employee told |
| Next | queue | HR | the next reading |

## States

- Normal: the queue, the source and the reading side by side.
- Empty: "No reading to verify".
- Loading: the document loads first; the reading follows.
- Error: the document cannot be shown: the reading cannot be confirmed until it is (D122).
- Read-only: readings already confirmed, corrected or rejected, from the employee's history.
- Offline: not available offline (HR data).

Shown entities (VD-15): [E-F9-31 Attribute reading](../../data/e-f09-31-attribute-reading.md),
[E-F9-29 Degree](../../data/e-f09-29-degree.md), [E-F9-12 Qualification](../../data/e-f09-12-certification.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-31 Attribute reading | Reading | In the queue, greyed, "Reading in progress" | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-31-attribute-reading-reading-desktop-{light,dark}.png` |
| E-F9-31 Attribute reading | Failed | In the queue, "Could not be read"; Try again, Enter by hand | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-31-attribute-reading-failed-desktop-{light,dark}.png` |
| E-F9-31 Attribute reading | To verify | In the queue; Confirm, Correct, Reject | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-31-attribute-reading-to-verify-desktop-{light,dark}.png` |
| E-F9-31 Attribute reading | Confirmed | Leaves the queue; read-only in the history | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-31-attribute-reading-confirmed-desktop-{light,dark}.png` |
| E-F9-31 Attribute reading | Corrected | Leaves the queue; the old and new values in the history | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-31-attribute-reading-corrected-desktop-{light,dark}.png` |
| E-F9-31 Attribute reading | Rejected | Leaves the queue; the reason in the history | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-31-attribute-reading-rejected-desktop-{light,dark}.png` |
| E-F9-29 Degree | To verify | The attribute drafted, shown "does not count yet" | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-29-degree-to-verify-desktop-{light,dark}.png` |
| E-F9-29 Degree | Verified | Badge "Verified"; a new record starts here; next: To verify (UC-F9-38); fields editable within the role | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-29-degree-verified-desktop-{light,dark}.png` |
| E-F9-29 Degree | Rejected | Badge "Rejected"; next: To verify (UC-F9-38); fields editable within the role | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-29-degree-rejected-desktop-{light,dark}.png` |
| E-F9-12 Qualification | To verify | Badge "To verify"; a new record starts here; next: Verified or Rejected (UC-F9-33, BR-F9-27); fields editable within the role | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-12-certification-to-verify-desktop-{light,dark}.png` |
| E-F9-12 Qualification | Verified | Badge "Verified"; a new record starts here; next: Expired (UC-F12-22); fields editable within the role | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-12-certification-verified-desktop-{light,dark}.png` |
| E-F9-12 Qualification | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U06 | `u06-hr/s-f09-36-readings-to-verify-e-f09-12-certification-rejected-desktop-{light,dark}.png` |

The states are those of the entity drafts and of the change note on E-F9-12.

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop: three columns. Phone: the document, then the reading below, one at a time.

## Accessibility

Each field read says its confidence in words ("low confidence") as well as the number; highlights in the document are
also listed as text; keyboard: next field, confirm, next reading.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-13 Keep employees' qualifications](../../flows/fl-f09-13-keep-qualifications.md)

## Open questions

None.

---

⬅️ [S-F9-35 Employee qualifications](s-f09-35-employee-qualifications.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-37 LinkedIn sourcing search](../02-recruit/s-f09-37-linkedin-sourcing-search.md)
