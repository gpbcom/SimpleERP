🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-11 Capacity, rounds and partners](README.md) › 🖥️ S-F9-29 Subcontractors

# 🖥️ S-F9-29 Subcontractors

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)
- [U10 Supplier](../../../../01-users/personas/u10-supplier.md)

## Purpose

Add subcontractors to projects and follow their documents, progress and invoices.

## Entry points

A project › Subcontractors.

## Wireframe

```text
+------------------------------------------------------------------+
| Project Lyon 3 › Subcontractors                [+ Subcontractor]  |
| Supplier    Scope              Price    Docs           Progress   |
| SARL Volt   Lot 4 electricity  18,000   URSSAF expired 50 %       |
| Plomb'Express Lot 5 plumbing   12,500   ok             20 %       |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-11 step 4, U02 | desktop | ![FL-F9-11 step 4, U02, light](../../images/11-capacity-rounds-and-partners/u02-manager/4-subcontractors-desktop-light.png) | ![FL-F9-11 step 4, U02, dark](../../images/11-capacity-rounds-and-partners/u02-manager/4-subcontractors-desktop-dark.png) |
| FL-F9-11 step 4, U02 | phone | ![FL-F9-11 step 4, U02, light](../../images/11-capacity-rounds-and-partners/u02-manager/4-subcontractors-phone-light.png) | ![FL-F9-11 step 4, U02, dark](../../images/11-capacity-rounds-and-partners/u02-manager/4-subcontractors-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-29-subcontractors-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-29-subcontractors-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-29-subcontractors-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-29-subcontractors-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-29-subcontractors-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-29-subcontractors-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-29-subcontractors-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-29-subcontractors-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Supplier, scope, price, documents, progress | E-F9-27 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Add | managers | Assignment |
| Ask documents | managers | Supplier asked |

## States

- Normal: add subcontractors to projects and follow their documents, progress and invoices.
- Empty: no subcontractor on this project.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done assignments.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F9-18 Project and task](../../data/e-f09-18-project-and-task.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-18 Project and task | New | Badge "New"; a new record starts here; next: Planned (UC-F9-18); fields editable within the role | U02 | `u02-manager/s-f09-29-subcontractors-e-f09-18-project-and-task-new-{desktop,phone}-{light,dark}.png` |
| E-F9-18 Project and task | Planned | Badge "Planned"; next: Active (UC-F9-31); fields editable within the role | U02 | `u02-manager/s-f09-29-subcontractors-e-f09-18-project-and-task-planned-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

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

⬅️ [S-F9-28 Customer project view](s-f09-28-customer-project-view.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-30 Scheduling board](../12-schedule-customer-requests/s-f09-30-scheduling-board.md)
