🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-06 After an incident](README.md) › 🖥️ S-F20-23 Incident report

# 🖥️ S-F20-23 Incident report

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Draft, approve and send the written incident report.

## Entry points

Incidents, closed incident; the owner's notification.

## Wireframe

```text
Incident report INC-12                          Due 2026-11-27
-------------------------------------------------------------------------------
Timeline: 09:00 slow, 09:20 cause found, 09:40 fixed
Cause: [disk full on a database node]   Measures: [alert at 80 %]
Customers affected: 40
-------------------------------------------------------------------------------
[Approve and send] (maintainer)
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-06 step 1, U48 | desktop | ![FL-F20-06 step 1, U48, light](../../images/06-after-an-incident/u48-hosting-engineer/1-incident-report-desktop-light.png) | ![FL-F20-06 step 1, U48, dark](../../images/06-after-an-incident/u48-hosting-engineer/1-incident-report-desktop-dark.png) |
| FL-F20-06 step 1, U48 | phone | ![FL-F20-06 step 1, U48, light](../../images/06-after-an-incident/u48-hosting-engineer/1-incident-report-phone-light.png) | ![FL-F20-06 step 1, U48, dark](../../images/06-after-an-incident/u48-hosting-engineer/1-incident-report-phone-dark.png) |
| Error E1, U48 | desktop | ![Error E1, U48, light](../../images/06-after-an-incident/u48-hosting-engineer/e1-incident-report-refused-desktop-light.png) | ![Error E1, U48, dark](../../images/06-after-an-incident/u48-hosting-engineer/e1-incident-report-refused-desktop-dark.png) |
| Error E1, U48 | phone | ![Error E1, U48, light](../../images/06-after-an-incident/u48-hosting-engineer/e1-incident-report-refused-phone-light.png) | ![Error E1, U48, dark](../../images/06-after-an-incident/u48-hosting-engineer/e1-incident-report-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-23-incident-report-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-23-incident-report-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-23-incident-report-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-23-incident-report-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-23-incident-report-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-23-incident-report-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f20-23-incident-report-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f20-23-incident-report-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Timeline | E-F20-15 timeline | text | yes | yes |
| Cause, measures | E-F20-15 | text | yes | yes |
| Customers | E-F20-15 customers | count | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Approve and send | footer | maintainer | sent to owners |

## States

- Normal: the draft with timeline, cause and measures.
- Empty: "No report to write".
- Loading: the frame and titles show at once with placeholder rows for the report; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a missing cause, refused.
- Read-only: owners read the sent report.
- Offline: not available offline: reports are sent online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F20-07 Service incident](../../data/e-f20-07-service-incident.md),
[E-F20-15 Incident report](../../data/e-f20-15-incident-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-07 Service incident | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U48 | `u13-owner/s-f20-23-incident-report-e-f20-07-service-incident-active-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f20-23-incident-report-e-f20-07-service-incident-active-{desktop,phone}-{light,dark}.png` |
| E-F20-15 Incident report | Draft | Badge "Draft"; a new record starts here; next: Approved (UC-F20-23); fields editable within the role | U13, U48 | `u13-owner/s-f20-23-incident-report-e-f20-15-incident-report-draft-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f20-23-incident-report-e-f20-15-incident-report-draft-{desktop,phone}-{light,dark}.png` |
| E-F20-15 Incident report | Approved | Badge "Approved"; next: Sent (UC-F20-23); fields editable within the role | U13, U48 | `u13-owner/s-f20-23-incident-report-e-f20-15-incident-report-approved-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f20-23-incident-report-e-f20-15-incident-report-approved-{desktop,phone}-{light,dark}.png` |
| E-F20-15 Incident report | Sent | Badge "Sent"; final: read-only, no next state; the history shows how it got here | U13, U48 | `u13-owner/s-f20-23-incident-report-e-f20-15-incident-report-sent-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f20-23-incident-report-e-f20-15-incident-report-sent-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; owners read on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F20-06 After an incident](../../flows/fl-f20-06-after-an-incident.md)

## Open questions

None.

---

⬅️ [S-F20-22 Release notes](../05-maintenance-and-releases/s-f20-22-release-notes.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-24 Service credits](s-f20-24-service-credits.md)
