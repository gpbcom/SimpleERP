🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-03 CRM and ATS](README.md) › 🖥️ S-F24-13 History import

# 🖥️ S-F24-13 History import

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Import history once.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-03 step 4, U07 | desktop | ![FL-F24-03 step 4, U07, light](../../images/03-crm-and-ats/u07-administrator/4-history-desktop-light.png) | ![FL-F24-03 step 4, U07, dark](../../images/03-crm-and-ats/u07-administrator/4-history-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-13-history-import-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-13-history-import-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-13-history-import-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-13-history-import-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-13-history-import-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-13-history-import-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-13-history-import-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-13-history-import-offline-desktop-dark.png) |

## Fields and columns

As its entities.

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12, or the category's icon (BR-F24-16) | tile sized by BR-F24-16, name as accessible name | no | yes |

## Actions

As its use case's main flow.

## States

- Normal: the period, dry run and import.
- Empty: "Choose a period".
- Loading: the frame and titles show at once with placeholder rows for the import; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: finished imports read-only.
- Offline: not available offline: imports run online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F24-06 Sync job](../../data/e-f24-06-sync-job.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-06 Sync job | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f24-13-history-import-e-f24-06-sync-job-active-desktop-{light,dark}.png` |

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

- [FL-F24-03 CRM and ATS](../../flows/fl-f24-03-crm-and-ats.md)

## Open questions

None.

---

⬅️ [S-F24-12 Mapping](s-f24-12-mapping.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-14 Assistant actions](../04-run-and-control/s-f24-14-assistant-actions.md)
