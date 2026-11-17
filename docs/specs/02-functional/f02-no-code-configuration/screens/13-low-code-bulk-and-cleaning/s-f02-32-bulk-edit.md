🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-13 Low code, bulk work and data cleaning](README.md) › 🖥️ S-F2-32 Bulk edit

# 🖥️ S-F2-32 Bulk edit

**Status:** ✅ specified

## Personas

- - [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): their lists.
- - [U05 Accounting](../../../../01-users/personas/u05-accounting.md): accounting records.

## Purpose

Choose the change, preview what it does to the selected records and run it or undo it.

## Entry points

Any list › select rows › Edit in bulk; Administration › Bulk operations (the list of past operations).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Bulk edit: 212 customers selected                                    [Preview] [Apply]      |
| ------------------------------------------------------------------------------------------- |
| FIELD            NEW VALUE                       [+ Add a field]                            |
| Account manager  Claire P.                                                                  |
| Tag             to review                                                                   |
| PREVIEW  200 will change   12 skipped: 9 on a locked status, 3 no right on the field        |
| Dupont SA      account manager: Marc D. -> Claire P.        (sample of 5)    [Export preview] |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-13 step 2, U16 | desktop | ![FL-F2-13 step 2, U16, light](../../images/13-low-code-bulk-and-cleaning/u16-office-worker/2-bulk-edit-desktop-light.png) | ![FL-F2-13 step 2, U16, dark](../../images/13-low-code-bulk-and-cleaning/u16-office-worker/2-bulk-edit-desktop-dark.png) |
| FL-F2-13 step 2, U16 | desktop | ![FL-F2-13 step 2, U16, light](../../images/13-low-code-bulk-and-cleaning/u16-office-worker/2-bulk-edit-desktop-light.png) | ![FL-F2-13 step 2, U16, dark](../../images/13-low-code-bulk-and-cleaning/u16-office-worker/2-bulk-edit-desktop-dark.png) |
| FL-F2-13 step 2, U16 | phone | ![FL-F2-13 step 2, U16, light](../../images/13-low-code-bulk-and-cleaning/u16-office-worker/2-bulk-edit-phone-light.png) | ![FL-F2-13 step 2, U16, dark](../../images/13-low-code-bulk-and-cleaning/u16-office-worker/2-bulk-edit-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-32-bulk-edit-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-32-bulk-edit-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-32-bulk-edit-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-32-bulk-edit-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-32-bulk-edit-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-32-bulk-edit-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f02-32-bulk-edit-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f02-32-bulk-edit-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Selection | E-F2-31 selection | filter and count | no | yes |
| Changes | E-F2-31 changes | field and new value | yes | yes |
| Preview | E-F2-31 counts and sample | numbers and rows | no | yes |
| Skipped | E-F2-31 skipped | count and reasons | no | yes |
| Undo until | E-F2-31 undo until | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Preview | header | the user | counts and a sample, nothing changed |
| Apply | header | the user | the operation runs in the background |
| Undo | result | the user who ran it, the administrator | the changed records return to their old values |
| Export preview | preview | the user | a spreadsheet of the records and their new values |

## States

- Normal: the selection, the fields to change, the preview and, after a run, the result.
- Empty: No record selected: select rows in a list, then choose Edit in bulk.
- Loading: The preview counts are computed as the user chooses, with progress.
- Error: the error message pattern (D122); an invalid value is refused under its field in the preview.
- Read-only: a finished operation whose undo window passed: the result, without the Undo button.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F2-31 Bulk operation](../../data/e-f02-31-bulk-operation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-31 Bulk operation | Previewed | Badge "Previewed"; a new record starts here; next: Applying (BR-F2-29); fields editable within the role | U16, U05 | `u16-office-worker/s-f02-32-bulk-edit-e-f02-31-bulk-operation-previewed-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f02-32-bulk-edit-e-f02-31-bulk-operation-previewed-desktop-{light,dark}.png` |
| E-F2-31 Bulk operation | Applying | Badge "Applying"; next: Applied or Failed (UC-F2-32); fields editable within the role | U16, U05 | `u16-office-worker/s-f02-32-bulk-edit-e-f02-31-bulk-operation-applying-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f02-32-bulk-edit-e-f02-31-bulk-operation-applying-desktop-{light,dark}.png` |
| E-F2-31 Bulk operation | Applied | Badge "Applied"; next: Undone, Partly undone or Expired (BR-F2-29); fields editable within the role | U16, U05 | `u16-office-worker/s-f02-32-bulk-edit-e-f02-31-bulk-operation-applied-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f02-32-bulk-edit-e-f02-31-bulk-operation-applied-desktop-{light,dark}.png` |
| E-F2-31 Bulk operation | Failed | Badge "Failed"; next: Applying (UC-F2-32); fields editable within the role | U16, U05 | `u16-office-worker/s-f02-32-bulk-edit-e-f02-31-bulk-operation-failed-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f02-32-bulk-edit-e-f02-31-bulk-operation-failed-desktop-{light,dark}.png` |
| E-F2-31 Bulk operation | Undone | Badge "Undone"; final: read-only, no next state; the history shows how it got here | U16, U05 | `u16-office-worker/s-f02-32-bulk-edit-e-f02-31-bulk-operation-undone-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f02-32-bulk-edit-e-f02-31-bulk-operation-undone-desktop-{light,dark}.png` |
| E-F2-31 Bulk operation | Partly undone | Badge "Partly undone"; final: read-only, no next state; the history shows how it got here | U16, U05 | `u16-office-worker/s-f02-32-bulk-edit-e-f02-31-bulk-operation-partly-undone-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f02-32-bulk-edit-e-f02-31-bulk-operation-partly-undone-desktop-{light,dark}.png` |
| E-F2-31 Bulk operation | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U16, U05 | `u16-office-worker/s-f02-32-bulk-edit-e-f02-31-bulk-operation-expired-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f02-32-bulk-edit-e-f02-31-bulk-operation-expired-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

On a phone, the selection and the preview are readable and a mass action can be confirmed; choosing many fields needs a
larger screen.

## Accessibility

The counts and the reasons are text; the confirmation names the number of records; keyboard: next field, preview, apply.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-13 Low code, bulk work and data cleaning](../../flows/fl-f02-13-low-code-bulk-and-cleaning.md)

## Open questions

None.

---

⬅️ [S-F2-31 Script step editor](s-f02-31-script-step-editor.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-33 Time-based rule](s-f02-33-time-based-rule.md)
