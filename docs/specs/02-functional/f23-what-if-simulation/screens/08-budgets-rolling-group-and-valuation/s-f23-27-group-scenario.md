🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-08 Budgets, rolling forecasts, group and valuation](README.md) › 🖥️ S-F23-27 Group scenario

# 🖥️ S-F23-27 Group scenario

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): every company, the eliminations and the group
  total.

## Purpose

Run a scenario on a group of companies and show the consolidated result after eliminating intercompany flows.

## Entry points

What-if simulation › Group scenario; a scenario's Run on a group action; the consolidation screen.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Group scenario   Scenario: Supplier +8 %   Group: Acme group (3)                      [Run]   |
|---------------------------------------------------------------------------------------------|
| LINE         ACME FR     ACME DE     ACME ES    ELIMINATIONS   GROUP     VS BASELINE        |
| Sales        2,100 k     1,400 k     800 k      -420 k         3,880 k  +0.5 %             |
| Margin       510 k       310 k       120 k      0              940 k    -6.2 %             |
| Cash         180 k       90 k        45 k       0              315 k    -48 k              |
| Unmatched flows: 0     Missing baselines: 0     [Open eliminations] [Compare]                |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-08 step 3, U05 | desktop | ![FL-F23-08 step 3, U05, light](../../images/08-budgets-rolling-group-and-valuation/u05-accounting/3-group-scenario-desktop-light.png) | ![FL-F23-08 step 3, U05, dark](../../images/08-budgets-rolling-group-and-valuation/u05-accounting/3-group-scenario-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-27-group-scenario-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-27-group-scenario-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-27-group-scenario-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-27-group-scenario-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-27-group-scenario-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-27-group-scenario-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f23-27-group-scenario-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f23-27-group-scenario-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Company columns | result per company | amounts in the company's currency, group in the group's | no | yes |
| Eliminations | mirrored intercompany flows | amount with the two companies | no | yes |
| Group | consolidated result | amount with currency | no | yes |
| Unmatched and missing | flows and companies left out | count and list | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Run | header | accounting | runs the scenario on each company and consolidates |
| Open eliminations | toolbar | accounting | lists each mirrored flow and its two entries |
| Compare | toolbar | accounting, owner | compares with the baseline or another scenario |

## States

- Normal: the result per company, the eliminations and the group total against the baseline.
- Empty: No group run yet, with the scenario and group to pick.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); unmatched flows
  or a failed balance are listed with their companies and amounts.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

- [FL-F23-08](../../flows/fl-f23-08-budgets-rolling-group-and-valuation.md)

## Open questions

None.

---

⬅️ [S-F23-26 Rolling forecast](s-f23-26-rolling-forecast.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-28 Valuation](s-f23-28-valuation.md)
