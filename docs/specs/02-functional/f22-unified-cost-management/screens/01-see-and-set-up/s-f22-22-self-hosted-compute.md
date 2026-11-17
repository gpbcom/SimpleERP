🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-01 See and set up](README.md) › 🖥️ S-F22-22 Self-hosted compute

# 🖥️ S-F22-22 Self-hosted compute

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Record the machines of local models and their hourly cost.

## Entry points

Costs, Providers, "Self-hosted".

## Wireframe

```text
Self-hosted compute                                     [Add machine]
-------------------------------------------------------------------------------
Machine        Price      Life   Power   kWh price   Per hour   November
gpu-server-1   6 000.00   36 m   400 W   0.25        0.33       72.60
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-01 step 7, U07 | desktop | ![FL-F22-01 step 7, U07, light](../../images/01-see-and-set-up/u07-administrator/7-self-hosted-compute-desktop-light.png) | ![FL-F22-01 step 7, U07, dark](../../images/01-see-and-set-up/u07-administrator/7-self-hosted-compute-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-22-self-hosted-compute-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-22-self-hosted-compute-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-22-self-hosted-compute-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-22-self-hosted-compute-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-22-self-hosted-compute-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-22-self-hosted-compute-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f22-22-self-hosted-compute-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f22-22-self-hosted-compute-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Machine | E-F22-15 name | text | yes | yes |
| Price, life | E-F22-15 | EUR, months | yes | yes |
| Power, kWh price | E-F22-15 | W, EUR | yes | yes |
| Per hour | E-F22-15 | EUR | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Add machine | header | administrator | machine saved |

## States

- Normal: machines with costs.
- Empty: "No local machine": local models on the hosted platform show its rate.
- Loading: the frame and titles show at once with placeholder rows for the machines; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a missing price, flagged.
- Read-only: owner reads.
- Offline: not available offline: set online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F22-02 Metered call record](../../data/e-f22-02-metered-call-record.md),
[E-F22-15 Compute machine](../../data/e-f22-15-compute-machine.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-02 Metered call record | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U07, U48 | `u07-administrator/s-f22-22-self-hosted-compute-e-f22-02-metered-call-record-recorded-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f22-22-self-hosted-compute-e-f22-02-metered-call-record-recorded-{desktop,phone}-{light,dark}.png` |
| E-F22-15 Compute machine | In service | Badge "In service"; a new record starts here; next: Retired (UC-F22-01); fields editable within the role | U07, U48 | `u07-administrator/s-f22-22-self-hosted-compute-e-f22-15-compute-machine-in-service-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f22-22-self-hosted-compute-e-f22-15-compute-machine-in-service-{desktop,phone}-{light,dark}.png` |
| E-F22-15 Compute machine | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U07, U48 | `u07-administrator/s-f22-22-self-hosted-compute-e-f22-15-compute-machine-retired-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f22-22-self-hosted-compute-e-f22-15-compute-machine-retired-{desktop,phone}-{light,dark}.png` |

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

- [FL-F22-01 See and set up](../../flows/fl-f22-01-see-and-set-up.md)

## Open questions

None.

---

⬅️ [S-F22-21 Currencies](s-f22-21-currencies.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-23 Savings](../06-savings-and-kpis/s-f22-23-savings.md)
