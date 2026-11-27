🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-07 Compliance and safety](README.md) › 🖥️ S-F12-17 Safety registers

# 🖥️ S-F12-17 Safety registers

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Keep the risk assessment and safety registers.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-07 step 2, U02 | desktop | ![FL-F12-07 step 2, U02, light](../../images/07-compliance-and-safety/u02-manager/2-safety-registers-desktop-light.png) | ![FL-F12-07 step 2, U02, dark](../../images/07-compliance-and-safety/u02-manager/2-safety-registers-desktop-dark.png) |
| FL-F12-07 step 2, U02 | phone | ![FL-F12-07 step 2, U02, light](../../images/07-compliance-and-safety/u02-manager/2-safety-registers-phone-light.png) | ![FL-F12-07 step 2, U02, dark](../../images/07-compliance-and-safety/u02-manager/2-safety-registers-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-17-safety-registers-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-17-safety-registers-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-17-safety-registers-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-17-safety-registers-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-17-safety-registers-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-17-safety-registers-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-17-safety-registers-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-17-safety-registers-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Keep the risk assessment and safety registers, as the wireframe shows.
- Empty: No risk assessed yet, with Start the assessment.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F12-26 Risk assessment](../../data/e-f12-26-risk-assessment.md),
[E-F12-27 Safety register](../../data/e-f12-27-safety-register.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-26 Risk assessment | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U21 | `u02-manager/s-f12-17-safety-registers-e-f12-26-risk-assessment-active-{desktop,phone}-{light,dark}.png`, `u21-production-planner/s-f12-17-safety-registers-e-f12-26-risk-assessment-active-{desktop,phone}-{light,dark}.png` |
| E-F12-27 Safety register | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U21 | `u02-manager/s-f12-17-safety-registers-e-f12-27-safety-register-active-{desktop,phone}-{light,dark}.png`, `u21-production-planner/s-f12-17-safety-registers-e-f12-27-safety-register-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F12-07 Compliance and safety](../../flows/fl-f12-07-compliance-and-safety.md)

## Open questions

None.

---

⬅️ [S-F12-16 Compliance file](s-f12-16-compliance-file.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-18 Waste register](s-f12-18-waste-register.md)
