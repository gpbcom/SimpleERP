🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-11 Capacity, rounds and partners](README.md) › 🖥️ S-F9-28 Customer project view

# 🖥️ S-F9-28 Customer project view

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)

## Purpose

Show a customer their project's progress, milestones and shared items, and take milestone validations.

## Entry points

The customer portal › Projects.

## Wireframe

```text
+----------------------------------------+
| ERP Durand   62 % done                  |
| Next milestone: Design approved  12-05  |
|   [Validate]  [Refuse with a comment]   |
| Shared tasks: 8   Documents: 4          |
+----------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-11 step 3, U09 | phone | ![FL-F9-11 step 3, U09, light](../../images/11-capacity-rounds-and-partners/u09-customer/3-customer-project-view-phone-light.png) | ![FL-F9-11 step 3, U09, dark](../../images/11-capacity-rounds-and-partners/u09-customer/3-customer-project-view-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f09-28-customer-project-view-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f09-28-customer-project-view-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f09-28-customer-project-view-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f09-28-customer-project-view-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f09-28-customer-project-view-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f09-28-customer-project-view-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-28-customer-project-view-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-28-customer-project-view-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Progress, milestones, shared tasks | E-F9-18 | validation |

## Actions

| Action | Who | Result |
|---|---|---|
| Validate, refuse | customer | Milestone decided |

## States

- Normal: show a customer their project's progress, milestones and shared items, and take milestone validations.
- Empty: nothing shared yet: "Your project team will share items here".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done milestones.
- Offline: Not available offline: a portal page served live
  ([D407](../../../../06-decisions/technical/d407-front-end.md)).

Shown entities (VD-15): [E-F9-18 Project and task](../../data/e-f09-18-project-and-task.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-18 Project and task | New | Badge "New"; a new record starts here; next: Planned (UC-F9-18); fields editable within the role | U09 | `u09-customer/s-f09-28-customer-project-view-e-f09-18-project-and-task-new-phone-{light,dark}.png` |
| E-F9-18 Project and task | Planned | Badge "Planned"; next: Active (UC-F9-31); fields editable within the role | U09 | `u09-customer/s-f09-28-customer-project-view-e-f09-18-project-and-task-planned-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone first; desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-11 Capacity, rounds and partners](../../flows/fl-f09-11-capacity-rounds-and-partners.md)

## Open questions

None.

---

⬅️ [S-F9-27 Rounds](s-f09-27-rounds.md) · ⬆️ [Up](README.md) · ➡️ [S-F9-29 Subcontractors](s-f09-29-subcontractors.md)
