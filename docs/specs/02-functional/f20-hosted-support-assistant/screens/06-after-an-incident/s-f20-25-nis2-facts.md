🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-06 After an incident](README.md) › 🖥️ S-F20-25 NIS2 facts

# 🖥️ S-F20-25 NIS2 facts

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Fill and send the fact sheet for customers subject to NIS2.

## Entry points

Incident page, NIS2; the owner's notification.

## Wireframe

```text
NIS2 facts, INC-12                Due 2026-11-21 09:00
-------------------------------------------------------------------------------
Start 09:00   Nature: outage   Services: invoicing   Data: none
Measures: node replaced, alert added
Customers: 3 declared subject                 [Send] [Update]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-06 step 3, U48 | desktop | ![FL-F20-06 step 3, U48, light](../../images/06-after-an-incident/u48-hosting-engineer/3-nis2-facts-desktop-light.png) | ![FL-F20-06 step 3, U48, dark](../../images/06-after-an-incident/u48-hosting-engineer/3-nis2-facts-desktop-dark.png) |
| FL-F20-06 step 3, U48 | phone | ![FL-F20-06 step 3, U48, light](../../images/06-after-an-incident/u48-hosting-engineer/3-nis2-facts-phone-light.png) | ![FL-F20-06 step 3, U48, dark](../../images/06-after-an-incident/u48-hosting-engineer/3-nis2-facts-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-25-nis2-facts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-25-nis2-facts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-25-nis2-facts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-25-nis2-facts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-25-nis2-facts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-25-nis2-facts-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f20-25-nis2-facts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f20-25-nis2-facts-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Facts | E-F20-17 facts | text | yes | yes |
| Sent | E-F20-17 sent | date and time | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Send | footer | hosting engineer | sheet sent |
| Update | footer | hosting engineer | update sent |

## States

- Normal: the facts and customers concerned.
- Empty: "No declared customer affected".
- Loading: the frame and titles show at once with placeholder rows for the facts; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a missing fact, refused.
- Read-only: owners read.
- Offline: not available offline: sent online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F20-17 NIS2 fact sheet](../../data/e-f20-17-nis2-fact-sheet.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-17 NIS2 fact sheet | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-F20-26); fields editable within the role | U13, U48 | `u13-owner/s-f20-25-nis2-facts-e-f20-17-nis2-fact-sheet-draft-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f20-25-nis2-facts-e-f20-17-nis2-fact-sheet-draft-{desktop,phone}-{light,dark}.png` |
| E-F20-17 NIS2 fact sheet | Sent | Badge "Sent"; next: Updated (UC-F20-26); fields editable within the role | U13, U48 | `u13-owner/s-f20-25-nis2-facts-e-f20-17-nis2-fact-sheet-sent-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f20-25-nis2-facts-e-f20-17-nis2-fact-sheet-sent-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F20-06 After an incident](../../flows/fl-f20-06-after-an-incident.md)

## Open questions

None.

---

⬅️ [S-F20-24 Service credits](s-f20-24-service-credits.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-26 Help on the phone](../07-employees-help/s-f20-26-help-on-the-phone.md)
