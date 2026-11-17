🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-03 Runs](README.md) › 🖥️ S-F22-11 Live run

# 🖥️ S-F22-11 Live run

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Follow a run's cost live and stop it.

## Entry points

Unified platform cost management in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-03 step 2, U07 | desktop | ![FL-F22-03 step 2, U07, light](../../images/03-runs/u07-administrator/2-live-desktop-light.png) | ![FL-F22-03 step 2, U07, dark](../../images/03-runs/u07-administrator/2-live-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/03-runs/u07-administrator/e1-stopped-desktop-light.png) | ![Error E1, U07, dark](../../images/03-runs/u07-administrator/e1-stopped-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-11-live-run-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-11-live-run-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-11-live-run-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-11-live-run-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-11-live-run-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-11-live-run-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f22-11-live-run-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f22-11-live-run-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the run's live cost with Stop.
- Empty: "No run".
- Loading: the frame and titles show at once with placeholder rows for the run; within 1 second (D408) the data replaces
  them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: managers their own runs.
- Offline: not available offline: runs are followed online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F22-10 Run estimate](../../data/e-f22-10-run-estimate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-10 Run estimate | Running | Badge "Running"; a new record starts here; next: Done (UC-F22-11); fields editable within the role | U07 | `u07-administrator/s-f22-11-live-run-e-f22-10-run-estimate-running-desktop-{light,dark}.png` |
| E-F22-10 Run estimate | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f22-11-live-run-e-f22-10-run-estimate-done-desktop-{light,dark}.png` |

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

- [FL-F22-03 Runs](../../flows/fl-f22-03-runs.md)

## Open questions

None.

---

⬅️ [S-F22-10 Estimate](s-f22-10-estimate.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-12 Forecast](../04-accounting/s-f22-12-forecast.md)
