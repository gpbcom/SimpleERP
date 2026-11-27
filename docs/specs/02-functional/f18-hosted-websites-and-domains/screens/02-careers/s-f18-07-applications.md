🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-02 Careers](README.md) › 🖥️ S-F18-07 Applications

# 🖥️ S-F18-07 Applications

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Handle one pipeline of applications.

## Entry points

Hosted websites and domains in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-02 step 3, U06 | desktop | ![FL-F18-02 step 3, U06, light](../../images/02-careers/u06-hr/3-pipeline-desktop-light.png) | ![FL-F18-02 step 3, U06, dark](../../images/02-careers/u06-hr/3-pipeline-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-07-applications-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-07-applications-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-07-applications-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-07-applications-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-07-applications-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-07-applications-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f18-07-applications-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f18-07-applications-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: applications by stage, channels merged per candidate.
- Empty: "No application yet".
- Loading: the frame and titles show at once with placeholder rows for the applications; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: hiring managers see their openings only.
- Offline: Applications last loaded stay readable; moves need the network. Nothing else is queued: D38 keeps only
  today's schedule, time and intervention records offline; a banner says the connection is lost and the actions come
  back with it.

Shown entities (VD-15): [E-F18-06 Application](../../data/e-f18-06-application.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-06 Application | Interview | Badge "Interview"; a new record starts here; next: New or Rejected (UC-F18-07, BR-F18-09); fields editable within the role | U06 | `u06-hr/s-f18-07-applications-e-f18-06-application-interview-desktop-{light,dark}.png` |
| E-F18-06 Application | New | Badge "New"; final: read-only, no next state; the history shows how it got here | U06 | `u06-hr/s-f18-07-applications-e-f18-06-application-new-desktop-{light,dark}.png` |
| E-F18-06 Application | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U06 | `u06-hr/s-f18-07-applications-e-f18-06-application-rejected-desktop-{light,dark}.png` |

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

- [FL-F18-02 Careers](../../flows/fl-f18-02-careers.md)

## Open questions

None.

---

⬅️ [S-F18-06 Job channels](s-f18-06-job-channels.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-08 Legal pages](../01-build-the-site/s-f18-08-legal-pages.md)
