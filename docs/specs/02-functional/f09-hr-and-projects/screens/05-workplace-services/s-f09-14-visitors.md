🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-05 Workplace services](README.md) › 🖥️ S-F9-14 Visitors

# 🖥️ S-F9-14 Visitors

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)

## Purpose

Welcome visitors.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-05 step 3, U16 | desktop | ![FL-F9-05 step 3, U16, light](../../images/05-workplace-services/u16-office-worker/3-visitors-desktop-light.png) | ![FL-F9-05 step 3, U16, dark](../../images/05-workplace-services/u16-office-worker/3-visitors-desktop-dark.png) |
| FL-F9-05 step 3, U16 | phone | ![FL-F9-05 step 3, U16, light](../../images/05-workplace-services/u16-office-worker/3-visitors-phone-light.png) | ![FL-F9-05 step 3, U16, dark](../../images/05-workplace-services/u16-office-worker/3-visitors-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-14-visitors-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-14-visitors-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-14-visitors-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-14-visitors-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-14-visitors-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-14-visitors-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-14-visitors-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-14-visitors-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Welcome visitors, as the wireframe shows.
- Empty: No visitor expected yet, with Register a visitor.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F9-15 Visitor](../../data/e-f09-15-visitor.md),
[E-F9-42 Reception kiosk](../../data/e-f09-42-reception-kiosk.md),
[E-F9-43 Visitor badge](../../data/e-f09-43-visitor-badge.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-15 Visitor | Checked | Badge "Checked"; a new record starts here; next: Planned (UC-F9-14); fields editable within the role | U16 | `u16-office-worker/s-f09-14-visitors-e-f09-15-visitor-checked-{desktop,phone}-{light,dark}.png` |
| E-F9-15 Visitor | Planned | Badge "Planned"; final: read-only, no next state; the history shows how it got here | U16 | `u16-office-worker/s-f09-14-visitors-e-f09-15-visitor-planned-{desktop,phone}-{light,dark}.png` |
| E-F9-42 Reception kiosk | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U16 | `u16-office-worker/s-f09-14-visitors-e-f09-42-reception-kiosk-active-{desktop,phone}-{light,dark}.png` |
| E-F9-43 Visitor badge | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U16 | `u16-office-worker/s-f09-14-visitors-e-f09-43-visitor-badge-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F9-13 Approvals and lunch](s-f09-13-approvals-and-lunch.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-15 Planning](../06-plan-and-deliver-work/s-f09-15-planning.md)
