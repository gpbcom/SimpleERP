🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-07 Roadmap, beta, credits and changelog](README.md) › 🖥️ S-F25-28 Module changelog

# 🖥️ S-F25-28 Module changelog

**Status:** 🔄 waiting for the owner

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): every entry of the installed modules, with
  the actions.
- [U01 Employee](../../../../01-users/personas/u01-employee.md): the entries that touch their screens, on a phone.

## Purpose

Show what changed in each release for the installed modules, in plain words.

## Entry points

Settings › What changed; the release banner; the AI assistant.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| What changed        Module [All installed v]    Release [All v]    Action needed 1          |
|---------------------------------------------------------------------------------------------|
| 3.5.0  2026-11-10                                                                            |
|  ! Payroll        Payslip export has a new file layout. Review your export settings. [Open]  |
|    Stock          Counts open faster on a phone.                                             |
|    Customers      The quote list shows the validity date.                                    |
| 3.4.0  2026-11-03                                                                            |
|    Accounting     Bank lines match by reference first.                         [Mark as read] |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-07 step 4, U07 | desktop | ![FL-F25-07 step 4, U07, light](../../images/07-roadmap-beta-and-credits/u07-administrator/4-module-changelog-desktop-light.png) | ![FL-F25-07 step 4, U07, dark](../../images/07-roadmap-beta-and-credits/u07-administrator/4-module-changelog-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-28-module-changelog-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-28-module-changelog-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-28-module-changelog-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-28-module-changelog-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-28-module-changelog-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-28-module-changelog-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f25-28-module-changelog-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f25-28-module-changelog-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Release and date | release number, date | text | no | yes |
| Module | installed module | text | no | yes |
| Entry | what changed in plain words | text | no | yes |
| Action needed | yes or no, with a link | badge | no | no |
| Read | read by the administrator | yes or no | administrator | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Filter | toolbar | administrator, employees | shows a module or a release |
| Open | entry | administrator, employees | shows what changed, why and what to do |
| Open the screen | action | administrator | goes to the screen to review |
| Mark as read | entry | administrator | keeps the entry in the history |

## States

- Normal: the entries of the installed modules by release, with the actions flagged.
- Empty: Nothing changed yet in your modules, with the link to the roadmap.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a release not
  yet written is named, with its date.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: The last changelog read is shown with its date; marking as read waits for the network.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

On a phone the changelog is one column of entries for the employee's own screens; the administrator's actions are
reachable from the entry.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F25-07](../../flows/fl-f25-07-roadmap-beta-and-credits.md)

## Open questions

None.

---

⬅️ [S-F25-27 Report credits](s-f25-27-report-credits.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-29 Work contract](../08-team-builds-a-ticket/s-f25-29-work-contract.md)
