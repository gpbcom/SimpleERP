🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-04 Accounting](README.md) › 🖥️ S-F22-03 Cost allocation

# 🖥️ S-F22-03 Cost allocation

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

See costs per department, project and client.

## Entry points

Unified platform cost management in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-04 step 1, U02 | desktop | ![FL-F22-04 step 1, U02, light](../../images/04-accounting/u02-manager/1-allocation-desktop-light.png) | ![FL-F22-04 step 1, U02, dark](../../images/04-accounting/u02-manager/1-allocation-desktop-dark.png) |
| FL-F22-04 step 1, U02 | phone | ![FL-F22-04 step 1, U02, light](../../images/04-accounting/u02-manager/1-allocation-phone-light.png) | ![FL-F22-04 step 1, U02, dark](../../images/04-accounting/u02-manager/1-allocation-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-03-cost-allocation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-03-cost-allocation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-03-cost-allocation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-03-cost-allocation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-03-cost-allocation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-03-cost-allocation-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f22-03-cost-allocation-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f22-03-cost-allocation-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: costs per department, project and client.
- Empty: "No allocation rule yet".
- Loading: the frame and titles show at once with placeholder rows for the allocation; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: managers their own.
- Offline: not available offline: computed online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F22-02 Metered call record](../../data/e-f22-02-metered-call-record.md),
[E-F22-09 Allocation rule](../../data/e-f22-09-allocation-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-02 Metered call record | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U02, U05 | `u02-manager/s-f22-03-cost-allocation-e-f22-02-metered-call-record-recorded-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f22-03-cost-allocation-e-f22-02-metered-call-record-recorded-desktop-{light,dark}.png` |
| E-F22-09 Allocation rule | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U05 | `u02-manager/s-f22-03-cost-allocation-e-f22-09-allocation-rule-active-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f22-03-cost-allocation-e-f22-09-allocation-rule-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F22-04 Accounting](../../flows/fl-f22-04-accounting.md)

## Open questions

None.

---

⬅️ [S-F22-02 Cost breakdown](../01-see-and-set-up/s-f22-02-cost-breakdown.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-04 Providers](../01-see-and-set-up/s-f22-04-providers.md)
