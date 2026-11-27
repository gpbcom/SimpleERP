🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-09 Administration reports](README.md) › 🖥️ S-F1-26 Security events dashboard

# 🖥️ S-F1-26 Security events dashboard

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

The security events report of [D91](../../../../06-decisions/f01-administration/d91-administration-reports.md): failed
sign-ins, two-factor resets, provider sessions, and administrators' password sign-ins under single sign-on.

## Entry points

Administration › Reports › Security events.

## Wireframe

As drawn here.

```text
+------------------------------------------------------------------+
| Security events dashboard                                        |
|------------------------------------------------------------------|
| When          Event                 User        Site             |
| 12/11 09:14   Failed sign-in (3)    p.martin    Lyon             |
|                                                  [Export]        |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-09 step 5, U07 | desktop | ![FL-F1-09 step 5, U07, light](../../images/09-administration-reports/u07-administrator/5-security-events-dashboard-desktop-light.png) | ![FL-F1-09 step 5, U07, dark](../../images/09-administration-reports/u07-administrator/5-security-events-dashboard-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-26-security-events-dashboard-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-26-security-events-dashboard-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-26-security-events-dashboard-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-26-security-events-dashboard-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-26-security-events-dashboard-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-26-security-events-dashboard-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-26-security-events-dashboard-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-26-security-events-dashboard-offline-desktop-dark.png) |

## Fields and columns

Per report, see [Reports](../../reports.md).

## Actions

| Action | Who | Result |
|---|---|---|
| Open | administrator, owner | The report |
| Export | administrator, owner | PDF or spreadsheet |

## States

- Normal: the security events report (D91), as the wireframe shows.
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

⬅️ [S-F1-25 Connections and AI usage dashboard](s-f01-25-connections-and-ai-usage-dashboard.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-27 Sessions and devices](../15-security-and-group-data/s-f01-27-sessions-and-devices.md)
