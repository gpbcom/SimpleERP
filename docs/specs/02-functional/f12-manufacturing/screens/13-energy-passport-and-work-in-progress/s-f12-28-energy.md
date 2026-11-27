🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-13 Energy, passport and work in progress](README.md) › 🖥️ S-F12-28 Energy

# 🖥️ S-F12-28 Energy

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Show energy per work centre, operation and product, with its cost.

## Entry points

Manufacturing › Energy.

## Wireframe

```text
+------------------------------------------------------------------+
| Energy  November   2,840 MWh   510,000 EUR                        |
| Product       kWh/unit  method     cost/unit                      |
| Bracket B-20  0.9       meter      0.16 EUR                       |
| Panel P-10    2.4       estimated  0.43 EUR                       |
| Meter gaps: Press P1 (12-02 to 12-03)                             |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-13 step 1, U21 | desktop | ![FL-F12-13 step 1, U21, light](../../images/13-energy-passport-and-work-in-progress/u21-production-planner/1-energy-desktop-light.png) | ![FL-F12-13 step 1, U21, dark](../../images/13-energy-passport-and-work-in-progress/u21-production-planner/1-energy-desktop-dark.png) |
| FL-F12-13 step 1, U21 | phone | ![FL-F12-13 step 1, U21, light](../../images/13-energy-passport-and-work-in-progress/u21-production-planner/1-energy-phone-light.png) | ![FL-F12-13 step 1, U21, dark](../../images/13-energy-passport-and-work-in-progress/u21-production-planner/1-energy-phone-dark.png) |
| Error E1, U21 | desktop | ![Error E1, U21, light](../../images/13-energy-passport-and-work-in-progress/u21-production-planner/e1-energy-refused-desktop-light.png) | ![Error E1, U21, dark](../../images/13-energy-passport-and-work-in-progress/u21-production-planner/e1-energy-refused-desktop-dark.png) |
| Error E1, U21 | phone | ![Error E1, U21, light](../../images/13-energy-passport-and-work-in-progress/u21-production-planner/e1-energy-refused-phone-light.png) | ![Error E1, U21, dark](../../images/13-energy-passport-and-work-in-progress/u21-production-planner/e1-energy-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-28-energy-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-28-energy-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-28-energy-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-28-energy-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-28-energy-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-28-energy-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-28-energy-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-28-energy-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Energy, method, cost | E-F12-23 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Export | planner, owner | File |

## States

- Normal: show energy per work centre, operation and product, with its cost.
- Empty: no meter or run time yet: "Connect meters or record run times".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: always: computed.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F12-23 Energy reading](../../data/e-f12-23-energy-reading.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-23 Energy reading | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U21 | `u21-production-planner/s-f12-28-energy-e-f12-23-energy-reading-recorded-{desktop,phone}-{light,dark}.png` |

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
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

- [FL-F12-13 Energy, passport and work in progress](../../flows/fl-f12-13-energy-passport-and-work-in-progress.md)

## Open questions

None.

---

⬅️ [S-F12-27 Work instructions](../10-people-and-tools/s-f12-27-work-instructions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-29 Product passport](s-f12-29-product-passport.md)
