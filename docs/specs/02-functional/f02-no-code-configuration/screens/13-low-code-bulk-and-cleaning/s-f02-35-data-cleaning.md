🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-13 Low code, bulk work and data cleaning](README.md) › 🖥️ S-F2-35 Data cleaning

# 🖥️ S-F2-35 Data cleaning

**Status:** ✅ specified

## Personas

- - [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the cleaning rules.
- - [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): review of the proposals.

## Purpose

Define cleaning rules, review the proposed merges and archivals, and undo a merge.

## Entry points

No-code configuration › Data cleaning; the duplicate warning when a record is created.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Data cleaning: customers                    Rule: same tax number or 90 % alike      [Run now] |
| ------------------------------------------------------------------------------------------- |
| GROUP   RECORDS                               SIMILARITY   LINKED DOCUMENTS                 |
| 1       Dupont SA | Dupont S.A.               97 %         9 invoices, 3 tasks   [Review]   |
| 2       Martin et fils | Martin & Fils        92 %         4 quotes              [Review]   |
| REVIEW  Survivor: Dupont SA   Address: keep the newer   Tax number: same   [Merge] [Not a duplicate] |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-13 step 5, U07 | desktop | ![FL-F2-13 step 5, U07, light](../../images/13-low-code-bulk-and-cleaning/u07-administrator/5-data-cleaning-desktop-light.png) | ![FL-F2-13 step 5, U07, dark](../../images/13-low-code-bulk-and-cleaning/u07-administrator/5-data-cleaning-desktop-dark.png) |
| FL-F2-13 step 5, U07 | desktop | ![FL-F2-13 step 5, U07, light](../../images/13-low-code-bulk-and-cleaning/u07-administrator/5-data-cleaning-desktop-light.png) | ![FL-F2-13 step 5, U07, dark](../../images/13-low-code-bulk-and-cleaning/u07-administrator/5-data-cleaning-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-35-data-cleaning-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-35-data-cleaning-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-35-data-cleaning-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-35-data-cleaning-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-35-data-cleaning-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-35-data-cleaning-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-35-data-cleaning-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-35-data-cleaning-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Rule | E-F2-34 name, kind | text | yes | yes |
| Group | records found as probable duplicates | list | no | yes |
| Similarity | score | percent | no | yes |
| Survivor and values | chosen by the user | field by field | yes | yes |
| Linked documents | links re-pointed on a merge | counts | no | yes |
| Undo until | end of the undo window | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Run now | header | the administrator | the rule scans and lists proposals |
| Merge | review | the reviewer | the records are merged, links kept (BR-F2-32) |
| Not a duplicate | review | the reviewer | the pair is never proposed again |
| Archive stale | stale list | the reviewer | the selected records are archived |
| Undo | merge history | the reviewer, the administrator | the merge is reversed |

## States

- Normal: the rules, the groups found and the review of the chosen group.
- Empty: No duplicate or stale record found by the rules. Run a rule to scan again.
- Loading: The scan runs in the background with its progress; groups appear as they are found.
- Error: the error message pattern (D122); conflicting values must be chosen before a merge.
- Read-only: a merge past its undo window: the survivor, the values kept and the links, without Undo.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F2-34 Cleaning rule](../../data/e-f02-34-cleaning-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-34 Cleaning rule | Draft | Badge "Draft"; a new record starts here; next: Active (UC-F2-35); fields editable within the role | U07, U16 | `u07-administrator/s-f02-35-data-cleaning-e-f02-34-cleaning-rule-draft-desktop-{light,dark}.png`, `u16-office-worker/s-f02-35-data-cleaning-e-f02-34-cleaning-rule-draft-{desktop,phone}-{light,dark}.png` |
| E-F2-34 Cleaning rule | Active | Badge "Active"; next: Paused (UC-F2-35); fields editable within the role | U07, U16 | `u07-administrator/s-f02-35-data-cleaning-e-f02-34-cleaning-rule-active-desktop-{light,dark}.png`, `u16-office-worker/s-f02-35-data-cleaning-e-f02-34-cleaning-rule-active-{desktop,phone}-{light,dark}.png` |
| E-F2-34 Cleaning rule | Paused | Badge "Paused"; next: Active (UC-F2-35); fields editable within the role | U07, U16 | `u07-administrator/s-f02-35-data-cleaning-e-f02-34-cleaning-rule-paused-desktop-{light,dark}.png`, `u16-office-worker/s-f02-35-data-cleaning-e-f02-34-cleaning-rule-paused-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; on a phone, the groups can be read and a clear duplicate merged, while rules need a larger screen.

## Accessibility

The side-by-side review is a table with the differences marked in words; keyboard: next group, merge.

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

⬅️ [S-F2-34 Translation mode](s-f02-34-translation-mode.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-L01 Custom fields](../00-lists/s-f02-l01-custom-fields.md)
