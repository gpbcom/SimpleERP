🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-09 Administration reports](README.md) › 🖥️ S-F1-24 Access rights dashboard

# 🖥️ S-F1-24 Access rights dashboard

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

The access rights report of [D91](../../../../06-decisions/f01-administration/d91-administration-reports.md): who holds
which rights on what: roles and record rules.

## Entry points

Administration › Reports › Access rights.

## Wireframe

As drawn here.

```text
+------------------------------------------------------------------+
| Access rights dashboard                                          |
|------------------------------------------------------------------|
| User         Role       Record rules       Site                  |
| Ana Ruiz     Sales      own customers      Lyon                  |
|                           [Export for audit]  [Export]           |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-09 step 3, U07 | desktop | ![FL-F1-09 step 3, U07, light](../../images/09-administration-reports/u07-administrator/3-access-rights-dashboard-desktop-light.png) | ![FL-F1-09 step 3, U07, dark](../../images/09-administration-reports/u07-administrator/3-access-rights-dashboard-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-24-access-rights-dashboard-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-24-access-rights-dashboard-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-24-access-rights-dashboard-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-24-access-rights-dashboard-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-24-access-rights-dashboard-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-24-access-rights-dashboard-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-24-access-rights-dashboard-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-24-access-rights-dashboard-offline-desktop-dark.png) |

## Fields and columns

Per report, see [Reports](../../reports.md).

## Actions

| Action | Who | Result |
|---|---|---|
| Open | administrator, owner | The report |
| Export for audit | administrator, owner | PDF or spreadsheet |

## States

- Normal: the access rights report (D91), as the wireframe shows.
- Empty: a report with no data for the period says so, with the period chosen.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for the owner, who reads and exports the report.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Charts have a table alternative.

## Components

- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [FL-F1-09 Administration reports](../../flows/fl-f01-09-administration-reports.md)

## Open questions

None.

---

⬅️ [S-F1-23 Close the company](../14-close-a-company/s-f01-23-close-the-company.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-25 Connections and AI usage dashboard](s-f01-25-connections-and-ai-usage-dashboard.md)
