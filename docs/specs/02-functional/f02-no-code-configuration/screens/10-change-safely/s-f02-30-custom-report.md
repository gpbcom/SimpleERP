🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-10 Change safely](README.md) › 🖥️ S-F2-30 Custom report

# 🖥️ S-F2-30 Custom report

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

A report built with no-code configuration: a record type, its filters, columns and chart. The impact of a
change lists the custom reports it touches
([UC-F2-23](../../use-cases/10-change-safely/uc-f02-23-see-the-impact-of-a-change-before-publishing.md), answer S2-11 of
2026-11-13).

## Entry points

Configuration › Reports; the impact of a change (S-F2-22).

## Wireframe

As drawn here.

```text
+------------------------------------------------------------------+
| Custom report                                                    |
|------------------------------------------------------------------|
| Record type  [Invoice v]   Filter [Unpaid, > 30 days]            |
| Columns      Customer, Amount, Due date                          |
| Chart        [Bar by month v]                                    |
|                               [Preview]  [Save]                  |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-10 step 5, U07 | desktop | ![FL-F2-10 step 5, U07, light](../../images/10-change-safely/u07-administrator/5-custom-report-desktop-light.png) | ![FL-F2-10 step 5, U07, dark](../../images/10-change-safely/u07-administrator/5-custom-report-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-30-custom-report-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-30-custom-report-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-30-custom-report-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-30-custom-report-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-30-custom-report-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-30-custom-report-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-30-custom-report-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-30-custom-report-offline-desktop-dark.png) |

## Fields and columns

Record type, filters, columns, grouping and chart, as the wireframe shows.

## Actions

| Action | Who | Result |
|---|---|---|
| Save | administrator | The report, in its menu |
| Preview | administrator | The first rows and the chart |

## States

- Normal: the report being built, as the wireframe shows.
- Empty: no record matches the filters: the report says so, with the filters shown.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for a user who may run the report but not change it.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F2-26 Configuration draft](../../data/e-f02-26-configuration-draft.md),
[E-F2-10 Configuration version](../../data/e-f02-10-configuration-version.md),
[E-F2-01 Custom field](../../data/e-f02-01-custom-field.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-26 Configuration draft | Open | Badge "Open"; a new record starts here; next: Published or Discarded (UC-F2-09); fields editable within the role | U07 | `u07-administrator/s-f02-30-custom-report-e-f02-26-configuration-draft-open-desktop-{light,dark}.png` |
| E-F2-26 Configuration draft | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-30-custom-report-e-f02-26-configuration-draft-published-desktop-{light,dark}.png` |
| E-F2-26 Configuration draft | Discarded | Badge "Discarded"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-30-custom-report-e-f02-26-configuration-draft-discarded-desktop-{light,dark}.png` |
| E-F2-10 Configuration version | Published | Badge "Published"; a new record starts here; next: Superseded (UC-F2-09); fields editable within the role | U07 | `u07-administrator/s-f02-30-custom-report-e-f02-10-configuration-version-published-desktop-{light,dark}.png` |
| E-F2-01 Custom field | Draft | Badge "Draft"; a new record starts here; next: Live (UC-F2-01); fields editable within the role | U07 | `u07-administrator/s-f02-30-custom-report-e-f02-01-custom-field-draft-desktop-{light,dark}.png` |
| E-F2-01 Custom field | Live | Badge "Live"; next: Archived (UC-F2-01); fields editable within the role | U07 | `u07-administrator/s-f02-30-custom-report-e-f02-01-custom-field-live-desktop-{light,dark}.png` |
| E-F2-01 Custom field | Archived | Badge "Archived"; next: Live (UC-F2-01); fields editable within the role | U07 | `u07-administrator/s-f02-30-custom-report-e-f02-01-custom-field-archived-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Charts have a table alternative.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

- [FL-F2-10 Change safely](../../flows/fl-f02-10-change-safely.md)

## Open questions

None.

---

⬅️ [S-F2-29 Request type settings](../12-set-up-request-types/s-f02-29-request-type-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-31 Script step editor](../13-low-code-bulk-and-cleaning/s-f02-31-script-step-editor.md)
