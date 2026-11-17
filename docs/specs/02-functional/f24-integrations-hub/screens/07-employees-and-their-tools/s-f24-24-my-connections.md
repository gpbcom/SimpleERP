🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-07 Employees and their tools](README.md) › 🖥️ S-F24-24 My connections

# 🖥️ S-F24-24 My connections

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Let an employee connect their own calendar and mail and see where their data goes.

## Entry points

Profile, My connections, on the phone or desktop.

## Wireframe

```text
My connections
-------------------------------------------------------------------------------
[calendar icon] Work calendar   connected, both ways
[mail icon]     Mail            [Connect]
My data goes to: [PayFit icon] payroll, [Lucca icon] absences
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-07 step 1, U01 | desktop | ![FL-F24-07 step 1, U01, light](../../images/07-employees-and-their-tools/u01-employee/1-my-connections-desktop-light.png) | ![FL-F24-07 step 1, U01, dark](../../images/07-employees-and-their-tools/u01-employee/1-my-connections-desktop-dark.png) |
| FL-F24-07 step 1, U01 | phone | ![FL-F24-07 step 1, U01, light](../../images/07-employees-and-their-tools/u01-employee/1-my-connections-phone-light.png) | ![FL-F24-07 step 1, U01, dark](../../images/07-employees-and-their-tools/u01-employee/1-my-connections-phone-dark.png) |
| Error E1, U01 | desktop | ![Error E1, U01, light](../../images/07-employees-and-their-tools/u01-employee/e1-my-connections-refused-desktop-light.png) | ![Error E1, U01, dark](../../images/07-employees-and-their-tools/u01-employee/e1-my-connections-refused-desktop-dark.png) |
| Error E1, U01 | phone | ![Error E1, U01, light](../../images/07-employees-and-their-tools/u01-employee/e1-my-connections-refused-phone-light.png) | ![Error E1, U01, dark](../../images/07-employees-and-their-tools/u01-employee/e1-my-connections-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-24-my-connections-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-24-my-connections-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-24-my-connections-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-24-my-connections-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-24-my-connections-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-24-my-connections-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f24-24-my-connections-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f24-24-my-connections-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12 or category fallback | tile | no | yes |
| Connection | E-F24-05 | name and state | no | yes |
| Tools | E-F24-02 | list with purpose | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Connect | row | employee | signed in |
| Ask a question | footer | employee | administrator told |

## States

- Normal: own connections and tools receiving data.
- Empty: "No connection": allowed kinds listed.
- Loading: the frame and titles show at once with placeholder rows for the connections; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: not allowed, with whom to ask.
- Read-only: tools list is read-only.
- Offline: The list last loaded stays visible; connecting needs the network. Nothing else is queued: D38 keeps only
  today's schedule, time and intervention records offline; a banner says the connection is lost and the actions come
  back with it.

Shown entities (VD-15): [E-F24-05 Calendar link](../../data/e-f24-05-calendar-link.md),
[E-F24-02 Tool connection](../../data/e-f24-02-tool-connection.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-05 Calendar link | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U07 | `u01-employee/s-f24-24-my-connections-e-f24-05-calendar-link-active-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f24-24-my-connections-e-f24-05-calendar-link-active-desktop-{light,dark}.png` |
| E-F24-02 Tool connection | Proposed | Badge "Proposed"; a new record starts here; next: Active (UC-F24-21); fields editable within the role | U01, U07 | `u01-employee/s-f24-24-my-connections-e-f24-02-tool-connection-proposed-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f24-24-my-connections-e-f24-02-tool-connection-proposed-desktop-{light,dark}.png` |
| E-F24-02 Tool connection | Active | Badge "Active"; next: Revoked (UC-F24-17); fields editable within the role | U01, U07 | `u01-employee/s-f24-24-my-connections-e-f24-02-tool-connection-active-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f24-24-my-connections-e-f24-02-tool-connection-active-desktop-{light,dark}.png` |
| E-F24-02 Tool connection | Revoked | Badge "Revoked"; final: read-only, no next state; the history shows how it got here | U01, U07 | `u01-employee/s-f24-24-my-connections-e-f24-02-tool-connection-revoked-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f24-24-my-connections-e-f24-02-tool-connection-revoked-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone first.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F24-07 Employees and their tools](../../flows/fl-f24-07-employees-and-their-tools.md)

## Open questions

None.

---

⬅️ [S-F24-23 HR and payroll import](../06-business-tools/s-f24-23-hr-and-payroll-import.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-25 Icon library](../05-keep-the-catalogue/s-f24-25-icon-library.md)
