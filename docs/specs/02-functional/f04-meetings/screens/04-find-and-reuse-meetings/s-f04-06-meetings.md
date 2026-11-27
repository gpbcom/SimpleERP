🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-04 Find and reuse meetings](README.md) › 🖥️ S-F4-06 Meetings

# 🖥️ S-F4-06 Meetings

**Status:** ✅ specified

## Personas

- Every internal persona, for the meetings they may see (BR-F4-04)

## Purpose

Find meetings and their outcomes (D227).

## Entry points

Meetings in the menu; a record's Meetings tab.

## Wireframe

```text
+------------------------------------------------------------------+
| Meetings      [Search...]  [Customer v] [Kind v] [Ask about meetings]|
| Tue 10 Nov  Durand SA, kitchen   Teams  checked       3 actions   |
| Mon  9 Nov  Weekly site meeting  in person  NOT CHECKED           |
| Next: Weekly site meeting Mon 16 Nov  [Agenda draft]              |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-04 step 1, U03 | desktop | ![FL-F4-04 step 1, U03, light](../../images/04-find-and-reuse-meetings/u03-sales/1-search-and-ask-desktop-light.png) | ![FL-F4-04 step 1, U03, dark](../../images/04-find-and-reuse-meetings/u03-sales/1-search-and-ask-desktop-dark.png) |
| Error E1, U03 | desktop | ![Error E1, U03, light](../../images/04-find-and-reuse-meetings/u03-sales/e1-nothing-found-desktop-light.png) | ![Error E1, U03, dark](../../images/04-find-and-reuse-meetings/u03-sales/e1-nothing-found-desktop-dark.png) |
| Error E1, U03 | tablet | ![Error E1, U03, light](../../images/04-find-and-reuse-meetings/u03-sales/e1-nothing-found-tablet-light.png) | ![Error E1, U03, dark](../../images/04-find-and-reuse-meetings/u03-sales/e1-nothing-found-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-06-meetings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-06-meetings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-06-meetings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-06-meetings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-06-meetings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-06-meetings-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-06-meetings-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-06-meetings-offline-phone-dark.png) |

## Fields and columns

Date, title, source, status, actions; next occurrences with agenda drafts.

## Actions

| Action | Who | Result |
|---|---|---|
| Search, filter | every internal persona | Meetings they may see |
| Ask about meetings | every internal persona | The AI assistant over transcripts |

## States

- Normal: Find meetings and their outcomes (D227), as the wireframe shows.
- Empty: "No meetings yet."
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: meetings shared with the user for reading.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.
- Not checked highlighted.

Shown entities (VD-15): [E-F4-01 Meeting](../../data/e-f04-01-meeting.md),
[E-F4-02 Transcript](../../data/e-f04-02-transcript.md),
[E-F4-17 Meeting summary](../../data/e-f04-17-meeting-summary.md),
[E-F4-22 Meeting agenda](../../data/e-f04-22-meeting-agenda.md),
[E-F4-04 Action item](../../data/e-f04-04-action-item.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U02, U03 | `u02-manager/s-f04-06-meetings-e-f04-01-meeting-planned-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-06-meetings-e-f04-01-meeting-planned-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U02, U03 | `u02-manager/s-f04-06-meetings-e-f04-01-meeting-live-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-06-meetings-e-f04-01-meeting-live-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U02, U03 | `u02-manager/s-f04-06-meetings-e-f04-01-meeting-ended-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-06-meetings-e-f04-01-meeting-ended-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U02, U03 | `u02-manager/s-f04-06-meetings-e-f04-01-meeting-waiting-for-review-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-06-meetings-e-f04-01-meeting-waiting-for-review-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U02, U03 | `u02-manager/s-f04-06-meetings-e-f04-01-meeting-checked-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-06-meetings-e-f04-01-meeting-checked-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-02 Transcript | Live | Badge "Live"; a new record starts here; next: Complete (BR-F4-03); fields editable within the role | U02, U03 | `u02-manager/s-f04-06-meetings-e-f04-02-transcript-live-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-06-meetings-e-f04-02-transcript-live-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-02 Transcript | Complete | Badge "Complete"; next: Checked (BR-F4-03); fields editable within the role | U02, U03 | `u02-manager/s-f04-06-meetings-e-f04-02-transcript-complete-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-06-meetings-e-f04-02-transcript-complete-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-02 Transcript | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U02, U03 | `u02-manager/s-f04-06-meetings-e-f04-02-transcript-checked-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-06-meetings-e-f04-02-transcript-checked-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-17 Meeting summary | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U03 | `u02-manager/s-f04-06-meetings-e-f04-17-meeting-summary-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-06-meetings-e-f04-17-meeting-summary-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-22 Meeting agenda | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U03 | `u02-manager/s-f04-06-meetings-e-f04-22-meeting-agenda-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-06-meetings-e-f04-22-meeting-agenda-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F4-04 Action item | Open | Badge "Open"; a new record starts here; next: Done (UC-F4-27); fields editable within the role | U02, U03 | `u02-manager/s-f04-06-meetings-e-f04-04-action-item-open-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f04-06-meetings-e-f04-04-action-item-open-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

A table with headers; status as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F4-04 Find and reuse meetings](../../flows/fl-f04-04-find-and-reuse-meetings.md)

## Open questions

None.

---

⬅️ [S-F4-05 Meeting review](../03-review-a-meeting/s-f04-05-meeting-review.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-07 Meeting settings](../06-set-up-meetings-and-calendars/s-f04-07-meeting-settings.md)
