🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-05 Maintenance and releases](README.md) › 🖥️ S-F20-22 Release notes

# 🖥️ S-F20-22 Release notes

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Show each upgrade's notes by capability and role, and "what is new" on sign-in.

## Entry points

Help, Release notes; the first sign-in after an upgrade.

## Wireframe

```text
Release notes 1.4 (2026-11-30)       Filter: my capabilities
-------------------------------------------------------------------------------
Accounting (F8): faster bank matching
HR (F9): leave requests show the balance
-------------------------------------------------------------------------------
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-05 step 2, U07 | desktop | ![FL-F20-05 step 2, U07, light](../../images/05-maintenance-and-releases/u07-administrator/2-release-notes-desktop-light.png) | ![FL-F20-05 step 2, U07, dark](../../images/05-maintenance-and-releases/u07-administrator/2-release-notes-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-22-release-notes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-22-release-notes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-22-release-notes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-22-release-notes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-22-release-notes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-22-release-notes-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f20-22-release-notes-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f20-22-release-notes-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Version | E-F20-14 version | text | no | yes |
| Items | E-F20-14 items | list | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Filter | header | everyone | by capability |
| Hide what is new | dialog | employee | not shown again |

## States

- Normal: notes for the user's capabilities.
- Empty: "No upgrade yet".
- Loading: the frame and titles show at once with placeholder rows for the notes; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: none beyond D122.
- Read-only: always read-only.
- Offline: Notes already opened stay readable. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F20-14 Upgrade release note](../../data/e-f20-14-upgrade-release-note.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-14 Upgrade release note | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F20-22); fields editable within the role | U01, U07 | `u01-employee/s-f20-22-release-notes-e-f20-14-upgrade-release-note-draft-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f20-22-release-notes-e-f20-14-upgrade-release-note-draft-desktop-{light,dark}.png` |
| E-F20-14 Upgrade release note | Published | Badge "Published"; next: Withdrawn (UC-F20-22); fields editable within the role | U01, U07 | `u01-employee/s-f20-22-release-notes-e-f20-14-upgrade-release-note-published-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f20-22-release-notes-e-f20-14-upgrade-release-note-published-desktop-{light,dark}.png` |
| E-F20-14 Upgrade release note | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U01, U07 | `u01-employee/s-f20-22-release-notes-e-f20-14-upgrade-release-note-withdrawn-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f20-22-release-notes-e-f20-14-upgrade-release-note-withdrawn-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone and desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F20-05 Maintenance and releases](../../flows/fl-f20-05-maintenance-and-releases.md)

## Open questions

None.

---

⬅️ [S-F20-21 Maintenance notices](s-f20-21-maintenance-notices.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-23 Incident report](../06-after-an-incident/s-f20-23-incident-report.md)
