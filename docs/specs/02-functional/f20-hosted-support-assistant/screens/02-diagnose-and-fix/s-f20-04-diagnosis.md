🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-02 Diagnose and fix](README.md) › 🖥️ S-F20-04 Diagnosis

# 🖥️ S-F20-04 Diagnosis

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Diagnose on the cluster.

## Entry points

Hosted support assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-02 step 1, U48 | desktop | ![FL-F20-02 step 1, U48, light](../../images/02-diagnose-and-fix/u48-hosting-engineer/1-diagnose-desktop-light.png) | ![FL-F20-02 step 1, U48, dark](../../images/02-diagnose-and-fix/u48-hosting-engineer/1-diagnose-desktop-dark.png) |
| FL-F20-02 step 1, U48 | phone | ![FL-F20-02 step 1, U48, light](../../images/02-diagnose-and-fix/u48-hosting-engineer/1-diagnose-phone-light.png) | ![FL-F20-02 step 1, U48, dark](../../images/02-diagnose-and-fix/u48-hosting-engineer/1-diagnose-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-04-diagnosis-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-04-diagnosis-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-04-diagnosis-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-04-diagnosis-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-04-diagnosis-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-04-diagnosis-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f20-04-diagnosis-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f20-04-diagnosis-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: resources read, correlations and the cause with confidence.
- Empty: "No diagnosis running".
- Loading: the frame and titles show at once with placeholder rows for the diagnosis; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: customers see the explanation only.
- Offline: not available offline: the cluster is read online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F20-05 Cluster reading](../../data/e-f20-05-cluster-reading.md),
[E-F20-04 Diagnosis](../../data/e-f20-04-diagnosis.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-05 Cluster reading | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U48 | `u48-hosting-engineer/s-f20-04-diagnosis-e-f20-05-cluster-reading-recorded-{desktop,phone}-{light,dark}.png` |
| E-F20-04 Diagnosis | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U48 | `u48-hosting-engineer/s-f20-04-diagnosis-e-f20-04-diagnosis-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F20-02 Diagnose and fix](../../flows/fl-f20-02-diagnose-and-fix.md)

## Open questions

None.

---

⬅️ [S-F20-03 Screenshots](../01-talk-it-through/s-f20-03-screenshots.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-05 Explanation](s-f20-05-explanation.md)
