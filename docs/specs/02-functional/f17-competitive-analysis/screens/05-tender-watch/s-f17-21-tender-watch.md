🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-05 Tender watch](README.md) › 🖥️ S-F17-21 Tender watch

# 🖥️ S-F17-21 Tender watch

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md), who decides
- [U13 Owner](../../../../01-users/personas/u13-owner.md), who approves answers

## Purpose

List the public tenders matching the company, with deadlines and why they matched, and record each decision.

## Entry points

Competition menu, Tender watch; the daily opportunities notification.

## Wireframe

```text
Tender watch          Profile: codes 45*, department 69, 20k to 500k    [Edit]
-------------------------------------------------------------------------------
Deadline          Buyer        Title                          Amount    Decision
2026-12-04 12:00  City of X    Maintenance of school buildings 240 000   -
2026-11-20 17:00  Region Y     Roof repairs (closing soon)      85 000   skipped
-------------------------------------------------------------------------------
[Notice panel] why it matched, documents, [Answer] [Skip: reason]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-05 step 1, U03 | desktop | ![FL-F17-05 step 1, U03, light](../../images/05-tender-watch/u03-sales/1-tender-watch-desktop-light.png) | ![FL-F17-05 step 1, U03, dark](../../images/05-tender-watch/u03-sales/1-tender-watch-desktop-dark.png) |
| FL-F17-05 step 1, U03 | phone | ![FL-F17-05 step 1, U03, light](../../images/05-tender-watch/u03-sales/1-tender-watch-phone-light.png) | ![FL-F17-05 step 1, U03, dark](../../images/05-tender-watch/u03-sales/1-tender-watch-phone-dark.png) |
| FL-F17-05 step 1, U03 | tablet | ![FL-F17-05 step 1, U03, light](../../images/05-tender-watch/u03-sales/1-tender-watch-tablet-light.png) | ![FL-F17-05 step 1, U03, dark](../../images/05-tender-watch/u03-sales/1-tender-watch-tablet-dark.png) |
| Error E1, U03 | desktop | ![Error E1, U03, light](../../images/05-tender-watch/u03-sales/e1-tender-watch-refused-desktop-light.png) | ![Error E1, U03, dark](../../images/05-tender-watch/u03-sales/e1-tender-watch-refused-desktop-dark.png) |
| Error E1, U03 | phone | ![Error E1, U03, light](../../images/05-tender-watch/u03-sales/e1-tender-watch-refused-phone-light.png) | ![Error E1, U03, dark](../../images/05-tender-watch/u03-sales/e1-tender-watch-refused-phone-dark.png) |
| Error E1, U03 | tablet | ![Error E1, U03, light](../../images/05-tender-watch/u03-sales/e1-tender-watch-refused-tablet-light.png) | ![Error E1, U03, dark](../../images/05-tender-watch/u03-sales/e1-tender-watch-refused-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-21-tender-watch-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-21-tender-watch-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-21-tender-watch-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-21-tender-watch-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-21-tender-watch-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-21-tender-watch-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-21-tender-watch-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-21-tender-watch-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Deadline | E-F17-16 deadline | date and time | no | yes |
| Buyer | E-F17-16 buyer | text | no | yes |
| Title | E-F17-16 title | text | no | yes |
| Amount | E-F17-16 estimated amount | EUR | no | no |
| Decision | E-F17-16 decision | answer, skip | yes | no |
| Reason | E-F17-16 reason | text | yes | if skipped |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Answer | notice panel | sales, owner approves | F6 opportunity created |
| Skip | notice panel | sales | closed with the reason |
| Edit profile | header | owner | codes, areas, amounts saved |

## States

- Normal: matching opportunities by deadline with their decision.
- Empty: "No matching tender": shown when nothing matches; a link to edit the profile.
- Loading: the frame and titles show at once with placeholder rows for the opportunities; within 1 second (D408) the
  data replaces them, and a longer load shows a progress line saying what loads.
- Error: a source unreachable, shown as a banner with the last read.
- Read-only: marketing reads; decided opportunities are read-only.
- Offline: not available offline: notices are read from the sources on the server. D38 keeps only today's schedule, time
  and intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action
  is disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F17-16 Tender opportunity](../../data/e-f17-16-tender-opportunity.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-16 Tender opportunity | New | Badge "New"; a new record starts here; next: Answering, Skipped or Missed (UC-F17-21); fields editable within the role | U03, U13 | `u03-sales/s-f17-21-tender-watch-e-f17-16-tender-opportunity-new-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f17-21-tender-watch-e-f17-16-tender-opportunity-new-{desktop,phone}-{light,dark}.png` |
| E-F17-16 Tender opportunity | Missed | Badge "Missed"; final: read-only, no next state; the history shows how it got here | U03, U13 | `u03-sales/s-f17-21-tender-watch-e-f17-16-tender-opportunity-missed-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f17-21-tender-watch-e-f17-16-tender-opportunity-missed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; sales read and decide on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F17-05 Tender watch](../../flows/fl-f17-05-tender-watch.md)

## Open questions

None.

---

⬅️ [S-F17-20 Competitor assistant](../03-analyse-and-arm-sales/s-f17-20-competitor-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-22 Data costs](../01-set-up-and-profiles/s-f17-22-data-costs.md)
