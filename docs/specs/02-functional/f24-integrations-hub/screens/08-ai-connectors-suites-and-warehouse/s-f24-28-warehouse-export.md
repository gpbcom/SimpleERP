🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-08 AI connectors, office suites, warehouse and firms](README.md) › 🖥️ S-F24-28 Warehouse export

# 🖥️ S-F24-28 Warehouse export

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): every pipeline, its fields, masking and runs.
- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md): the pipelines of their clients.

## Purpose

Send chosen records to the company's own warehouse, with every field's right and masking shown.

## Entry points

Integrations › Warehouse export; the reports screen's Export to warehouse action.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Warehouse export                          Active 2   Failed 0   Last run 2026-11-14 04:00 [+ New] |
|---------------------------------------------------------------------------------------------|
| PIPELINE      RECORDS     DESTINATION      SCHEDULE  LAST RUN   MASKED FIELDS   STATE        |
| Invoices      invoices    warehouse 1      daily     412 rows   customer name   Active       |
| Stock moves   stock       warehouse 1      hourly    1,030 rows none            Active       |
| FIELD            RIGHT      EXPORT                                                          |
| Customer name    readable   masked (hash)      Bank details   not readable   left out       |
| [Test run] [Run now] [Pause] [Retire]                                                       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-08 step 3, U07 | desktop | ![FL-F24-08 step 3, U07, light](../../images/08-ai-connectors-suites-and-warehouse/u07-administrator/3-warehouse-export-desktop-light.png) | ![FL-F24-08 step 3, U07, dark](../../images/08-ai-connectors-suites-and-warehouse/u07-administrator/3-warehouse-export-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-28-warehouse-export-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-28-warehouse-export-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-28-warehouse-export-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-28-warehouse-export-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-28-warehouse-export-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-28-warehouse-export-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-28-warehouse-export-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-28-warehouse-export-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Pipeline | E-F24-18 name | text | while Draft | yes |
| Records and destination | E-F24-18 records, destination | text | while Draft | yes |
| Schedule | E-F24-18 schedule | hourly, daily, weekly | yes | yes |
| Field, right and export | field choices | allowed, masked or left out | within the rights | yes |
| Last run | E-F24-18 last run | date, time and count | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New | header | administrator, IT provider administrator | creates a pipeline in Draft |
| Test run | row | administrator | sends a sample to the destination |
| Run now | row | administrator | runs the pipeline outside its schedule |
| Pause or retire | row | administrator | stops the runs, or ends the pipeline |

## States

- Normal: the pipelines with records, destination, schedule, last run and state, and the fields of the chosen one.
- Empty: No pipeline yet, with New and a note on which destinations are supported.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused field
  shows the right the administrator lacks; a failed run shows its reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F24-18 Export pipeline](../../data/e-f24-18-export-pipeline.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-18 Export pipeline | Draft | Badge "Draft"; a new record starts here; next: Active or Retired (UC-F24-30); fields editable within the role | U07, U11 | `u07-administrator/s-f24-28-warehouse-export-e-f24-18-export-pipeline-draft-desktop-{light,dark}.png`, `u11-provider-admin/s-f24-28-warehouse-export-e-f24-18-export-pipeline-draft-desktop-{light,dark}.png` |
| E-F24-18 Export pipeline | Active | Badge "Active"; next: Paused, Failed or Retired (UC-F24-30, BR-F24-09); fields editable within the role | U07, U11 | `u07-administrator/s-f24-28-warehouse-export-e-f24-18-export-pipeline-active-desktop-{light,dark}.png`, `u11-provider-admin/s-f24-28-warehouse-export-e-f24-18-export-pipeline-active-desktop-{light,dark}.png` |
| E-F24-18 Export pipeline | Paused | Badge "Paused"; next: Active or Retired (UC-F24-30); fields editable within the role | U07, U11 | `u07-administrator/s-f24-28-warehouse-export-e-f24-18-export-pipeline-paused-desktop-{light,dark}.png`, `u11-provider-admin/s-f24-28-warehouse-export-e-f24-18-export-pipeline-paused-desktop-{light,dark}.png` |
| E-F24-18 Export pipeline | Failed | Badge "Failed"; next: Active (UC-F24-30); fields editable within the role | U07, U11 | `u07-administrator/s-f24-28-warehouse-export-e-f24-18-export-pipeline-failed-desktop-{light,dark}.png`, `u11-provider-admin/s-f24-28-warehouse-export-e-f24-18-export-pipeline-failed-desktop-{light,dark}.png` |
| E-F24-18 Export pipeline | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U07, U11 | `u07-administrator/s-f24-28-warehouse-export-e-f24-18-export-pipeline-retired-desktop-{light,dark}.png`, `u11-provider-admin/s-f24-28-warehouse-export-e-f24-18-export-pipeline-retired-desktop-{light,dark}.png` |

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

- [FL-F24-08](../../flows/fl-f24-08-ai-connectors-suites-and-warehouse.md)

## Open questions

None.

---

⬅️ [S-F24-27 Office suites](s-f24-27-office-suites.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-29 Accounting firm sync](s-f24-29-accounting-firm-sync.md)
