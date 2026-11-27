🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-06 Business tools](README.md) › 🖥️ S-F24-23 HR and payroll import

# 🖥️ S-F24-23 HR and payroll import

**Status:** ✅ specified

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Import employees and pay history from HR and payroll software.

## Entry points

Catalogue, Payroll and HR.

## Wireframe

```text
HR and payroll import    [Silae] [PayFit] [Lucca]   (with icons)
-------------------------------------------------------------------------------
PayFit: employees 48, contracts 52, absences 610, payslips 1 152   [Dry run] [Import]
Sync: daily until 2027-01-01
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-06 step 3, U06 | desktop | ![FL-F24-06 step 3, U06, light](../../images/06-business-tools/u06-hr/3-hr-and-payroll-import-desktop-light.png) | ![FL-F24-06 step 3, U06, dark](../../images/06-business-tools/u06-hr/3-hr-and-payroll-import-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-23-hr-and-payroll-import-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-23-hr-and-payroll-import-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-23-hr-and-payroll-import-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-23-hr-and-payroll-import-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-23-hr-and-payroll-import-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-23-hr-and-payroll-import-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-23-hr-and-payroll-import-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-23-hr-and-payroll-import-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12 | tile | no | yes |
| Kinds | E-F24-06 | list | yes | yes |
| History | E-F24-06 | months | yes | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Dry run | footer | HR | counts and errors |
| Import | footer | HR | imported |

## States

- Normal: the tool, counts and sync.
- Empty: "Choose your tool".
- Loading: the frame and titles show at once with placeholder rows for the import; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: rows in error listed.
- Read-only: the administrator reads.
- Offline: not available offline: imports run online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F24-06 Business tools](../../flows/fl-f24-06-business-tools.md)

## Open questions

None.

---

⬅️ [S-F24-22 E-invoicing platform](s-f24-22-e-invoicing-platform.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-24 My connections](../07-employees-and-their-tools/s-f24-24-my-connections.md)
