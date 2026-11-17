🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-01 People](README.md) ›
🖥️ S-F9-19 Contract editor

# 🖥️ S-F9-19 Contract editor

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Edit contract templates.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-01 step 5, U06 | desktop | ![FL-F9-01 step 5, U06, light](../../images/01-people/u06-hr/5-contract-editor-desktop-light.png) | ![FL-F9-01 step 5, U06, dark](../../images/01-people/u06-hr/5-contract-editor-desktop-dark.png) |
| Error E1, U06 | desktop | ![Error E1, U06, light](../../images/01-people/u06-hr/e1-blocking-issue-desktop-light.png) | ![Error E1, U06, dark](../../images/01-people/u06-hr/e1-blocking-issue-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-19-contract-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-19-contract-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-19-contract-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-19-contract-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-19-contract-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-19-contract-editor-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-19-contract-editor-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-19-contract-editor-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Edit contract templates, as the wireframe shows.
- Empty: No contract template yet, with New template.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-19 Contract template](../../data/e-f09-19-contract-template.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-19 Contract template | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F9-19); fields editable within the role | U06 | `u06-hr/s-f09-19-contract-editor-e-f09-19-contract-template-draft-desktop-{light,dark}.png` |
| E-F9-19 Contract template | Published | Badge "Published"; next: Archived (UC-F9-19); fields editable within the role | U06 | `u06-hr/s-f09-19-contract-editor-e-f09-19-contract-template-published-desktop-{light,dark}.png` |
| E-F9-19 Contract template | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U06 | `u06-hr/s-f09-19-contract-editor-e-f09-19-contract-template-archived-desktop-{light,dark}.png` |

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

- [FL-F9-01 People](../../flows/fl-f09-01-people.md)

## Open questions

None.

---

⬅️ [S-F9-18 Field service](../06-plan-and-deliver-work/s-f09-18-field-service.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-20 Equality and pay transparency](../07-fair-pay-and-speaking-up/s-f09-20-equality-and-pay-transparency.md)
