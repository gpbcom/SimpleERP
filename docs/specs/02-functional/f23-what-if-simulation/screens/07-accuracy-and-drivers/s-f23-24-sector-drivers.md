🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-07 Accuracy and drivers](README.md) › 🖥️ S-F23-24 Sector drivers

# 🖥️ S-F23-24 Sector drivers

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Change sector drivers in a scenario.

## Entry points

A scenario, Sector drivers.

## Wireframe

```text
Sector drivers (Restaurants)
-------------------------------------------------------------------------------
Driver      Formula                 Now     Scenario
Occupancy   covers over seats       72 %    [80 %]
Ticket      sales over covers       31.40   [31.40]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-07 step 2, U13 | desktop | ![FL-F23-07 step 2, U13, light](../../images/07-accuracy-and-drivers/u13-owner/2-sector-drivers-desktop-light.png) | ![FL-F23-07 step 2, U13, dark](../../images/07-accuracy-and-drivers/u13-owner/2-sector-drivers-desktop-dark.png) |
| FL-F23-07 step 2, U13 | phone | ![FL-F23-07 step 2, U13, light](../../images/07-accuracy-and-drivers/u13-owner/2-sector-drivers-phone-light.png) | ![FL-F23-07 step 2, U13, dark](../../images/07-accuracy-and-drivers/u13-owner/2-sector-drivers-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-24-sector-drivers-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-24-sector-drivers-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-24-sector-drivers-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-24-sector-drivers-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-24-sector-drivers-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-24-sector-drivers-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f23-24-sector-drivers-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f23-24-sector-drivers-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Driver | E-F23-14 name | text | no | yes |
| Formula | E-F23-14 formula | text | no | yes |
| Now | E-F23-14 source | number | no | yes |
| Scenario | E-F23-03 change | number | yes | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Change | row | owner, manager | change saved |
| Run | footer | owner, manager | impact computed |

## States

- Normal: the sector's drivers with values.
- Empty: "No sector driver for your sector".
- Loading: the frame and titles show at once with placeholder rows for the drivers; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an out-of-range value.
- Read-only: readers see values only.
- Offline: not available offline: scenarios run on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F23-14 Sector driver](../../data/e-f23-14-sector-driver.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-14 Sector driver | Available | Badge "Available"; a new record starts here; next: Used (UC-F23-03); fields editable within the role | U02, U13 | `u02-manager/s-f23-24-sector-drivers-e-f23-14-sector-driver-available-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f23-24-sector-drivers-e-f23-14-sector-driver-available-{desktop,phone}-{light,dark}.png` |
| E-F23-14 Sector driver | Used | Badge "Used"; final: read-only, no next state; the history shows how it got here | U02, U13 | `u02-manager/s-f23-24-sector-drivers-e-f23-14-sector-driver-used-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f23-24-sector-drivers-e-f23-14-sector-driver-used-{desktop,phone}-{light,dark}.png` |

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

- [FL-F23-07 Accuracy and drivers](../../flows/fl-f23-07-accuracy-and-drivers.md)

## Open questions

None.

---

⬅️ [S-F23-23 Forecast accuracy](s-f23-23-forecast-accuracy.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-25 Collaborative budget](../08-budgets-rolling-group-and-valuation/s-f23-25-collaborative-budget.md)
