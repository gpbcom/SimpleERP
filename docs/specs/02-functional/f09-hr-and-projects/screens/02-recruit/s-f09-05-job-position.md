🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-02 Recruit](README.md) ›
🖥️ S-F9-05 Job position

# 🖥️ S-F9-05 Job position

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Publish jobs and source candidates.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-02 step 1, U06 | desktop | ![FL-F9-02 step 1, U06, light](../../images/02-recruit/u06-hr/1-job-and-sourcing-desktop-light.png) | ![FL-F9-02 step 1, U06, dark](../../images/02-recruit/u06-hr/1-job-and-sourcing-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-05-job-position-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-05-job-position-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-05-job-position-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-05-job-position-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-05-job-position-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-05-job-position-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-05-job-position-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-05-job-position-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Publish jobs and source candidates, as the wireframe shows.
- Empty: No job position yet, with New job.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-06 Job position](../../data/e-f09-06-job-position.md),
[E-F9-07 Applicant](../../data/e-f09-07-applicant.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-06 Job position | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06 | `u06-hr/s-f09-05-job-position-e-f09-06-job-position-active-desktop-{light,dark}.png` |
| E-F9-07 Applicant | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06 | `u06-hr/s-f09-05-job-position-e-f09-07-applicant-active-desktop-{light,dark}.png` |

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

- [FL-F9-02 Recruit](../../flows/fl-f09-02-recruit.md)

## Open questions

None.

---

⬅️ [S-F9-04 My HR](../01-people/s-f09-04-my-hr.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-06 Applicant pipeline](s-f09-06-applicant-pipeline.md)
