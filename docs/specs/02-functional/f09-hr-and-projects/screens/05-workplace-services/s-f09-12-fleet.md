🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-05 Workplace services](README.md) › 🖥️ S-F9-12 Fleet

# 🖥️ S-F9-12 Fleet

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Manage the fleet.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-05 step 1, U06 | desktop | ![FL-F9-05 step 1, U06, light](../../images/05-workplace-services/u06-hr/1-fleet-desktop-light.png) | ![FL-F9-05 step 1, U06, dark](../../images/05-workplace-services/u06-hr/1-fleet-desktop-dark.png) |
| Error E1, U06 | desktop | ![Error E1, U06, light](../../images/05-workplace-services/u06-hr/e1-contract-expired-desktop-light.png) | ![Error E1, U06, dark](../../images/05-workplace-services/u06-hr/e1-contract-expired-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-12-fleet-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-12-fleet-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-12-fleet-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-12-fleet-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-12-fleet-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-12-fleet-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-12-fleet-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-12-fleet-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Manage the fleet, as the wireframe shows.
- Empty: No vehicle yet, with Add a vehicle.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F9-13 Company vehicle](../../data/e-f09-13-company-vehicle.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-13 Company vehicle | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06, U07 | `u06-hr/s-f09-12-fleet-e-f09-13-company-vehicle-active-desktop-{light,dark}.png`, `u07-administrator/s-f09-12-fleet-e-f09-13-company-vehicle-active-desktop-{light,dark}.png` |

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

- [FL-F9-05 Workplace services](../../flows/fl-f09-05-workplace-services.md)

## Open questions

None.

---

⬅️ [S-F9-11 Appraisals and skills](../04-grow/s-f09-11-appraisals-and-skills.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-13 Approvals and lunch](s-f09-13-approvals-and-lunch.md)
