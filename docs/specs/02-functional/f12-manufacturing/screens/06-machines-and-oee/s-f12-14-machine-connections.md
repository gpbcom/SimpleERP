🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-06 Machines and OEE](README.md) › 🖥️ S-F12-14 Machine connections

# 🖥️ S-F12-14 Machine connections

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Connect machines and sensors.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-06 step 2, U07 | desktop | ![FL-F12-06 step 2, U07, light](../../images/06-machines-and-oee/u07-administrator/2-oee-desktop-light.png) | ![FL-F12-06 step 2, U07, dark](../../images/06-machines-and-oee/u07-administrator/2-oee-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-14-machine-connections-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-14-machine-connections-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-14-machine-connections-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-14-machine-connections-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-14-machine-connections-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-14-machine-connections-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f12-14-machine-connections-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f12-14-machine-connections-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Connect machines and sensors, as the wireframe shows.
- Empty: No connected machine yet, with Connect a machine.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F12-13 Machine signal](../../data/e-f12-13-machine-signal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-13 Machine signal | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U07, U21 | `u07-administrator/s-f12-14-machine-connections-e-f12-13-machine-signal-recorded-desktop-{light,dark}.png`, `u21-production-planner/s-f12-14-machine-connections-e-f12-13-machine-signal-recorded-{desktop,phone}-{light,dark}.png` |

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

## Shown in

- [FL-F12-06 Machines and OEE](../../flows/fl-f12-06-machines-and-oee.md)

## Open questions

None.

---

⬅️ [S-F12-13 OEE measure](s-f12-13-oee-measure.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-15 Pick for production](../02-plan-production/s-f12-15-pick-for-production.md)
