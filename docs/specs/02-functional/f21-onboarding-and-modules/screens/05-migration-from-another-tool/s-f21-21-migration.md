🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-05 Migration from another tool](README.md) › 🖥️ S-F21-21 Migration

# 🖥️ S-F21-21 Migration

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)

## Purpose

Bring data from a named tool with its ready mapping.

## Entry points

Guide, Team and data, "Coming from another tool".

## Wireframe

```text
Coming from another tool    [EBP] [Sage] [Pennylane] [Excel] [QuickBooks] ...
-------------------------------------------------------------------------------
EBP: how to export (4 files)                  [Upload]
customers.csv    412 rows   3 errors
articles.csv   1 240 rows   0 errors
-------------------------------------------------------------------------------
[Show errors] [Import]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-05 step 1, U07 | desktop | ![FL-F21-05 step 1, U07, light](../../images/05-migration-from-another-tool/u07-administrator/1-migration-desktop-light.png) | ![FL-F21-05 step 1, U07, dark](../../images/05-migration-from-another-tool/u07-administrator/1-migration-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/05-migration-from-another-tool/u07-administrator/e1-migration-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/05-migration-from-another-tool/u07-administrator/e1-migration-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-21-migration-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-21-migration-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-21-migration-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-21-migration-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-21-migration-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-21-migration-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f21-21-migration-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f21-21-migration-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Tool | E-F21-14 tool | list | yes | yes |
| Files | E-F21-14 files | files | yes | yes |
| Rows, errors | E-F21-14 | numbers | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Upload | header | administrator | files read and mapped |
| Import | footer | administrator | data imported |
| Show errors | footer | administrator | rows in error listed |

## States

- Normal: the tool chosen, its files and the preview.
- Empty: "Choose the tool you used".
- Loading: the frame and titles show at once with placeholder rows for the files; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: unsupported version, rows in error.
- Read-only: the owner reads.
- Offline: not available offline: files are read on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F21-14 Migration source](../../data/e-f21-14-migration-source.md),
[E-F21-17 Migration guide](../../data/e-f21-17-migration-guide.md),
[E-F21-07 Import job](../../data/e-f21-07-import-job.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-14 Migration source | Uploaded | Badge "Uploaded"; a new record starts here; next: Mapped (UC-F21-09); fields editable within the role | U07, U08 | `u07-administrator/s-f21-21-migration-e-f21-14-migration-source-uploaded-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-21-migration-e-f21-14-migration-source-uploaded-desktop-{light,dark}.png` |
| E-F21-14 Migration source | Mapped | Badge "Mapped"; next: Imported or Errors (UC-F21-09); fields editable within the role | U07, U08 | `u07-administrator/s-f21-21-migration-e-f21-14-migration-source-mapped-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-21-migration-e-f21-14-migration-source-mapped-desktop-{light,dark}.png` |
| E-F21-14 Migration source | Errors | Badge "Errors"; next: Mapped (UC-F21-09); fields editable within the role | U07, U08 | `u07-administrator/s-f21-21-migration-e-f21-14-migration-source-errors-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-21-migration-e-f21-14-migration-source-errors-desktop-{light,dark}.png` |
| E-F21-17 Migration guide | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U08 | `u07-administrator/s-f21-21-migration-e-f21-17-migration-guide-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-21-migration-e-f21-17-migration-guide-active-desktop-{light,dark}.png` |
| E-F21-07 Import job | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U08 | `u07-administrator/s-f21-21-migration-e-f21-07-import-job-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-21-migration-e-f21-07-import-job-active-desktop-{light,dark}.png` |

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

- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F21-05 Migration from another tool](../../flows/fl-f21-05-migration-from-another-tool.md)

## Open questions

None.

---

⬅️ [S-F21-20 Onboarding figures](../04-learn-and-improve/s-f21-20-onboarding-figures.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-22 Opening balance check](s-f21-22-opening-balance-check.md)
