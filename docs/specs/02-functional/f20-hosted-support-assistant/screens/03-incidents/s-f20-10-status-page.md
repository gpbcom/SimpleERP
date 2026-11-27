🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-03 Incidents](README.md) › 🖥️ S-F20-10 Status page

# 🖥️ S-F20-10 Status page

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

The status page of a wide incident, which customers read. The incident itself is handled on
[S-F20-28 Incident handling](s-f20-28-incident-handling.md).

## Entry points

Hosted support assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-03 step 2, U48 | desktop | ![FL-F20-03 step 2, U48, light](../../images/03-incidents/u48-hosting-engineer/2-status-page-desktop-light.png) | ![FL-F20-03 step 2, U48, dark](../../images/03-incidents/u48-hosting-engineer/2-status-page-desktop-dark.png) |
| FL-F20-03 step 2, U48 | phone | ![FL-F20-03 step 2, U48, light](../../images/03-incidents/u48-hosting-engineer/2-status-page-phone-light.png) | ![FL-F20-03 step 2, U48, dark](../../images/03-incidents/u48-hosting-engineer/2-status-page-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-10-incidents-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-10-incidents-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-10-incidents-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-10-incidents-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-10-incidents-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-10-incidents-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f20-10-incidents-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f20-10-incidents-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the status page of the incident, as customers read it.
- Empty: "All systems normal".
- Loading: the frame and titles show at once with placeholder rows for the incidents; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: customers read the status page.
- Offline: not available offline: incidents are run online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F20-07 Service incident](../../data/e-f20-07-service-incident.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-07 Service incident | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U48 | `u48-hosting-engineer/s-f20-10-status-page-e-f20-07-service-incident-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F20-09 My requests](../01-talk-it-through/s-f20-09-my-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-11 Proactive alerts](s-f20-11-proactive-alerts.md)
