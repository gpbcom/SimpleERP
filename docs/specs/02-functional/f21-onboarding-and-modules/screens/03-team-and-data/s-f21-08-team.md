🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-03 Team and data](README.md) › 🖥️ S-F21-08 Team

# 🖥️ S-F21-08 Team

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Invite users and give roles.

## Entry points

Onboarding and module activation in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-03 step 1, U07 | desktop | ![FL-F21-03 step 1, U07, light](../../images/03-team-and-data/u07-administrator/1-invite-desktop-light.png) | ![FL-F21-03 step 1, U07, dark](../../images/03-team-and-data/u07-administrator/1-invite-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-08-team-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-08-team-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-08-team-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-08-team-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-08-team-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-08-team-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f21-08-team-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f21-08-team-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: invitations with roles and states.
- Empty: "Only you so far".
- Loading: the frame and titles show at once with placeholder rows for the team; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner reads.
- Offline: not available offline: invitations are sent online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F21-03 Team and data](../../flows/fl-f21-03-team-and-data.md)

## Open questions

None.

---

⬅️ [S-F21-07 Identity](../01-first-run/s-f21-07-identity.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-09 Import](s-f21-09-import.md)
