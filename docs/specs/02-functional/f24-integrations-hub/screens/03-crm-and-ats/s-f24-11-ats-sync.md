🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-03 CRM and ATS](README.md) › 🖥️ S-F24-11 ATS sync

# 🖥️ S-F24-11 ATS sync

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Sync an ATS both ways.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-03 step 2, U06 | desktop | ![FL-F24-03 step 2, U06, light](../../images/03-crm-and-ats/u06-hr/2-ats-desktop-light.png) | ![FL-F24-03 step 2, U06, dark](../../images/03-crm-and-ats/u06-hr/2-ats-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-11-ats-sync-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-11-ats-sync-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-11-ats-sync-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-11-ats-sync-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-11-ats-sync-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-11-ats-sync-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-11-ats-sync-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-11-ats-sync-offline-desktop-dark.png) |

## Fields and columns

As its entities.

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12, or the category's icon (BR-F24-16) | tile sized by BR-F24-16, name as accessible name | no | yes |

## Actions

As its use case's main flow.

## States

- Normal: the ATS's icon, mapping and sync state.
- Empty: "No ATS connected".
- Loading: the frame and titles show at once with placeholder rows for the sync; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: HR reads synced records.
- Offline: not available offline: sync runs online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F24-07 Field mapping](../../data/e-f24-07-field-mapping.md),
[E-F24-06 Sync job](../../data/e-f24-06-sync-job.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-07 Field mapping | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06 | `u06-hr/s-f24-11-ats-sync-e-f24-07-field-mapping-active-desktop-{light,dark}.png` |
| E-F24-06 Sync job | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06 | `u06-hr/s-f24-11-ats-sync-e-f24-06-sync-job-active-desktop-{light,dark}.png` |

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

⬅️ [S-F24-10 CRM sync](s-f24-10-crm-sync.md) · ⬆️ [Up](README.md) · ➡️ [S-F24-12 Mapping](s-f24-12-mapping.md)
