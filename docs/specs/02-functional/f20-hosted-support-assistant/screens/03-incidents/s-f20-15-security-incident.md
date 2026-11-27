🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-03 Incidents](README.md) › 🖥️ S-F20-15 Security incident

# 🖥️ S-F20-15 Security incident

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Handle a security incident or breach.

## Entry points

Hosted support assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-03 step 4, U48 | desktop | ![FL-F20-03 step 4, U48, light](../../images/03-incidents/u48-hosting-engineer/4-breach-desktop-light.png) | ![FL-F20-03 step 4, U48, dark](../../images/03-incidents/u48-hosting-engineer/4-breach-desktop-dark.png) |
| FL-F20-03 step 4, U48 | phone | ![FL-F20-03 step 4, U48, light](../../images/03-incidents/u48-hosting-engineer/4-breach-phone-light.png) | ![FL-F20-03 step 4, U48, dark](../../images/03-incidents/u48-hosting-engineer/4-breach-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-15-security-incident-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-15-security-incident-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-15-security-incident-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-15-security-incident-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-15-security-incident-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-15-security-incident-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f20-15-security-incident-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f20-15-security-incident-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the security incident with containment and notifications.
- Empty: "No security incident".
- Loading: the frame and titles show at once with placeholder rows for the incident; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner reads.
- Offline: not available offline: handled online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F20-07 Service incident](../../data/e-f20-07-service-incident.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-07 Service incident | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U48 | `u13-owner/s-f20-15-security-incident-e-f20-07-service-incident-active-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f20-15-security-incident-e-f20-07-service-incident-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F20-03 Incidents](../../flows/fl-f20-03-incidents.md)

## Open questions

None.

---

⬅️ [S-F20-14 Slowness](../02-diagnose-and-fix/s-f20-14-slowness.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-16 Quality](../04-govern-the-assistant/s-f20-16-quality.md)
