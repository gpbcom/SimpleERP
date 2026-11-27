🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-11 Capacity, rounds and partners](README.md) › 🖥️ S-F9-26 Capacity planning

# 🖥️ S-F9-26 Capacity planning

**Status:** ✅ specified

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Show planned load against available hours per person and week, and rebalance.

## Entry points

Projects › Capacity.

## Wireframe

```text
+------------------------------------------------------------------+
| Capacity  weeks 49-52   [By person v]                             |
| Person      w49     w50       w51      w52                        |
| Lea Roux    32/35   46/35 !   0 (off)  28/35                      |
| Tom Petit   20/35   24/35     30/35    35/35                      |
| Unassigned demand: SAP consultant 60 h in w50   [Subcontract]     |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-11 step 1, U24 | desktop | ![FL-F9-11 step 1, U24, light](../../images/11-capacity-rounds-and-partners/u24-engagement-manager/1-capacity-planning-desktop-light.png) | ![FL-F9-11 step 1, U24, dark](../../images/11-capacity-rounds-and-partners/u24-engagement-manager/1-capacity-planning-desktop-dark.png) |
| FL-F9-11 step 1, U24 | phone | ![FL-F9-11 step 1, U24, light](../../images/11-capacity-rounds-and-partners/u24-engagement-manager/1-capacity-planning-phone-light.png) | ![FL-F9-11 step 1, U24, dark](../../images/11-capacity-rounds-and-partners/u24-engagement-manager/1-capacity-planning-phone-dark.png) |
| Error E1, U24 | desktop | ![Error E1, U24, light](../../images/11-capacity-rounds-and-partners/u24-engagement-manager/e1-capacity-planning-refused-desktop-light.png) | ![Error E1, U24, dark](../../images/11-capacity-rounds-and-partners/u24-engagement-manager/e1-capacity-planning-refused-desktop-dark.png) |
| Error E1, U24 | phone | ![Error E1, U24, light](../../images/11-capacity-rounds-and-partners/u24-engagement-manager/e1-capacity-planning-refused-phone-light.png) | ![Error E1, U24, dark](../../images/11-capacity-rounds-and-partners/u24-engagement-manager/e1-capacity-planning-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-26-capacity-planning-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-26-capacity-planning-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-26-capacity-planning-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-26-capacity-planning-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-26-capacity-planning-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-26-capacity-planning-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-26-capacity-planning-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-26-capacity-planning-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Person, week, planned and available hours | E-F9-25 | drag to move |

## Actions

| Action | Who | Result |
|---|---|---|
| Move | engagement managers | Allocation moved |
| Subcontract | managers | UC-F9-32 |

## States

- Normal: show planned load against available hours per person and week, and rebalance.
- Empty: no allocation yet: "Plan project tasks first".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: past weeks.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F9-18 Project and task](../../data/e-f09-18-project-and-task.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-18 Project and task | New | Badge "New"; a new record starts here; next: Planned (UC-F9-18); fields editable within the role | U24 | `u24-engagement-manager/s-f09-26-capacity-planning-e-f09-18-project-and-task-new-{desktop,phone}-{light,dark}.png` |
| E-F9-18 Project and task | Planned | Badge "Planned"; next: Active (UC-F9-31); fields editable within the role | U24 | `u24-engagement-manager/s-f09-26-capacity-planning-e-f09-18-project-and-task-planned-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-11 Capacity, rounds and partners](../../flows/fl-f09-11-capacity-rounds-and-partners.md)

## Open questions

None.

---

⬅️ [S-F9-25 Surveys and exit interviews](../10-listen-to-employees/s-f09-25-surveys-and-exit-interviews.md) ·
⬆️ [Up](README.md) · ➡️ [S-F9-27 Rounds](s-f09-27-rounds.md)
