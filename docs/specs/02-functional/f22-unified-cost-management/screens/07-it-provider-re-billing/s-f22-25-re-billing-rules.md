🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-07 IT provider re-billing](README.md) › 🖥️ S-F22-25 Re-billing rules

# 🖥️ S-F22-25 Re-billing rules

**Status:** ✅ specified

## Personas

- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)

## Purpose

Set per client how costs are re-billed.

## Entry points

Provider space, Re-billing.

## Wireframe

```text
Re-billing rules                                     [Copy to clients]
-------------------------------------------------------------------------------
Client               Margin   Included   Rounding   Preview Nov
Transport example    15 %     50.00      1 EUR      34.50
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-07 step 1, U11 | desktop | ![FL-F22-07 step 1, U11, light](../../images/07-it-provider-re-billing/u11-provider-admin/1-re-billing-rules-desktop-light.png) | ![FL-F22-07 step 1, U11, dark](../../images/07-it-provider-re-billing/u11-provider-admin/1-re-billing-rules-desktop-dark.png) |
| Error E1, U11 | desktop | ![Error E1, U11, light](../../images/07-it-provider-re-billing/u11-provider-admin/e1-re-billing-rules-refused-desktop-light.png) | ![Error E1, U11, dark](../../images/07-it-provider-re-billing/u11-provider-admin/e1-re-billing-rules-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-25-re-billing-rules-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-25-re-billing-rules-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-25-re-billing-rules-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-25-re-billing-rules-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-25-re-billing-rules-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-25-re-billing-rules-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f22-25-re-billing-rules-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f22-25-re-billing-rules-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Client | E-F22-17 client | name | no | yes |
| Margin | E-F22-17 margin | percent | yes | yes |
| Included | E-F22-17 included | EUR | yes | no |
| Rounding | E-F22-17 rounding | list | yes | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Save | row | IT provider | rule saved |
| Copy | header | IT provider | rule copied |

## States

- Normal: rules per client with previews.
- Empty: "No client".
- Loading: the frame and titles show at once with placeholder rows for the rules; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a negative margin, refused.
- Read-only: clients never see rules of others.
- Offline: not available offline: set online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F22-17 Re-billing rule](../../data/e-f22-17-re-billing-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-17 Re-billing rule | Active | Badge "Active"; a new record starts here; next: Changed (UC-F22-25); fields editable within the role | U11 | `u11-provider-admin/s-f22-25-re-billing-rules-e-f22-17-re-billing-rule-active-desktop-{light,dark}.png` |
| E-F22-17 Re-billing rule | Changed | Badge "Changed"; next: Active (UC-F22-16); fields editable within the role | U11 | `u11-provider-admin/s-f22-25-re-billing-rules-e-f22-17-re-billing-rule-changed-desktop-{light,dark}.png` |

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

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F22-07 IT provider re-billing](../../flows/fl-f22-07-it-provider-re-billing.md)

## Open questions

None.

---

⬅️ [S-F22-24 Cost KPIs](../06-savings-and-kpis/s-f22-24-cost-kpis.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-26 Client statements](s-f22-26-client-statements.md)
