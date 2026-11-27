🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-09 Administration reports](README.md) › 🖥️ S-F1-12 Users overview dashboard

# 🖥️ S-F1-12 Users overview dashboard

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

The users overview of [D91](../../../../06-decisions/f01-administration/d91-administration-reports.md): active, invited
and deactivated users per site and role, last sign-in. (Proposed) Until the owner places it, it also opens the GDPR
register draft (D93) of FL-F1-09's first two steps.

## Entry points

Administration › Reports › Users overview.

## Wireframe

```text
+------------------------------------------------------------------+
| Users overview dashboard                                         |
|------------------------------------------------------------------|
|  Users overview                                                |
|  GDPR register (draft to complete)                             |
|                                         [Open]  [Export]         |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-09 step 1, U07 | desktop | ![FL-F1-09 step 1, U07, light](../../images/09-administration-reports/u07-administrator/1-open-gdpr-register-desktop-light.png) | ![FL-F1-09 step 1, U07, dark](../../images/09-administration-reports/u07-administrator/1-open-gdpr-register-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-12-administration-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-12-administration-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-12-administration-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-12-administration-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-12-administration-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-12-administration-reports-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-12-administration-reports-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-12-administration-reports-offline-desktop-dark.png) |

## Fields and columns

Per report, see [Reports](../../reports.md).

## Actions

| Action | Who | Result |
|---|---|---|
| Open | administrator, owner | The report |
| Export | administrator, owner | PDF or spreadsheet |

## States

- Normal: the users overview (D91) and the GDPR register draft (D93), as the wireframe shows.
- Empty: a report with no data for the period says so, with the period chosen.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for the owner, who reads and exports but does not edit the register.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- The GDPR register can be marked "to review".

Shown entities (VD-15):
[E-F1-22 Record of processing activities](../../data/e-f01-22-record-of-processing-activities.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-22 Record of processing activities | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f01-12-users-overview-dashboard-e-f01-22-record-of-processing-activities-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

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

⬅️ [S-F1-11 Provider access log](../08-provider-and-client-companies/s-f01-11-provider-access-log.md) ·
⬆️ [Up](README.md) ·
➡️ [S-F1-13 Automatic provisioning](../10-bring-users-in-at-scale/s-f01-13-automatic-provisioning.md)
