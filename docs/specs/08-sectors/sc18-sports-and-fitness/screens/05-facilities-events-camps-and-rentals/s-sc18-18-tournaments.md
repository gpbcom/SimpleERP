🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-05 Facilities, events, camps and rentals](README.md) ›
🖥️ S-SC18-18 Tournaments

# 🖥️ S-SC18-18 Tournaments

**Status:** ✅ specified

## Personas

- [U53 Coach](../../../../01-users/personas/u53-coach.md): the tournaments they run.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their entry and the published draw.

## Purpose

Run a tournament from entries to the published draw, the schedule and the results.

## Entry points

Sports and fitness › Tournaments; the club's site; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Tournament: Club championship 2026                                         Drawn                 |
| Category        Entries   Min   Fee     State                                                    |
| Men singles     32        8     15 EUR  Drawn                                                    |
| Women singles   14        8     15 EUR  Drawn                                                    |
| Veterans        5         8     15 EUR  Merged with Men singles                                  |
| [Close the entries]  [Make the draw]  [Publish the draw]  [Print the schedule]                   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-05 step 2, U53 | phone | ![FL-SC18-05 step 2, U53, light](../../images/05-facilities-events-camps-and-rentals/u53-coach/2-tournaments-phone-light.png) | ![FL-SC18-05 step 2, U53, dark](../../images/05-facilities-events-camps-and-rentals/u53-coach/2-tournaments-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-18-tournaments-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-18-tournaments-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-18-tournaments-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-18-tournaments-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-18-tournaments-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-18-tournaments-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-18-tournaments-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-18-tournaments-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Name | E-SC18-14 name | text | yes while Draft | yes |
| Categories | E-SC18-14 categories | list | yes while Draft | yes |
| Dates and courts | E-SC18-14 dates, courts | dates and courts | yes while Draft | yes |
| Entry fee | E-SC18-14 fee | amount | yes while Draft | yes |
| Entries | E-SC18-14 entries | list of players | no | no |
| Draw published on | E-SC18-14 draw published on | date and time | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New tournament | header | coach, owner | a tournament is created Draft |
| Open | header | coach | the tournament becomes Open |
| Close the entries | header | coach | the tournament becomes Closed |
| Make the draw | header | coach | the tournament becomes Drawn |
| Publish the draw | header | coach | the draw goes to all the players |

## States

- Normal: the tournament with its entries, draw, schedule and results.
- Empty: No tournament yet, with New tournament.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); too few entries
  or an unpublished draw, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-14 Tournament](../../data/e-sc18-14-tournament.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-14 Tournament | Draft | Badge "Draft"; a new record starts here; next: Open (UC-SC18-18); fields editable within the role | U53, U09 | `u53-coach/s-sc18-18-tournaments-e-sc18-14-tournament-draft-phone-{light,dark}.png`, `u09-customer/s-sc18-18-tournaments-e-sc18-14-tournament-draft-phone-{light,dark}.png` |
| E-SC18-14 Tournament | Open | Badge "Open"; next: Closed or Cancelled (UC-SC18-18); fields editable within the role | U53, U09 | `u53-coach/s-sc18-18-tournaments-e-sc18-14-tournament-open-phone-{light,dark}.png`, `u09-customer/s-sc18-18-tournaments-e-sc18-14-tournament-open-phone-{light,dark}.png` |
| E-SC18-14 Tournament | Closed | Badge "Closed"; next: Drawn or Cancelled (UC-SC18-18); fields editable within the role | U53, U09 | `u53-coach/s-sc18-18-tournaments-e-sc18-14-tournament-closed-phone-{light,dark}.png`, `u09-customer/s-sc18-18-tournaments-e-sc18-14-tournament-closed-phone-{light,dark}.png` |
| E-SC18-14 Tournament | Drawn | Badge "Drawn"; next: Running (BR-SC18-18); fields editable within the role | U53, U09 | `u53-coach/s-sc18-18-tournaments-e-sc18-14-tournament-drawn-phone-{light,dark}.png`, `u09-customer/s-sc18-18-tournaments-e-sc18-14-tournament-drawn-phone-{light,dark}.png` |
| E-SC18-14 Tournament | Running | Badge "Running"; next: Finished (UC-SC18-18); fields editable within the role | U53, U09 | `u53-coach/s-sc18-18-tournaments-e-sc18-14-tournament-running-phone-{light,dark}.png`, `u09-customer/s-sc18-18-tournaments-e-sc18-14-tournament-running-phone-{light,dark}.png` |
| E-SC18-14 Tournament | Finished | Badge "Finished"; final: read-only, no next state; the history shows how it got here | U53, U09 | `u53-coach/s-sc18-18-tournaments-e-sc18-14-tournament-finished-phone-{light,dark}.png`, `u09-customer/s-sc18-18-tournaments-e-sc18-14-tournament-finished-phone-{light,dark}.png` |
| E-SC18-14 Tournament | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U53, U09 | `u53-coach/s-sc18-18-tournaments-e-sc18-14-tournament-cancelled-phone-{light,dark}.png`, `u09-customer/s-sc18-18-tournaments-e-sc18-14-tournament-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coach and the member use the phone, the owner and the treasurer a desktop, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-05](../../flows/fl-sc18-05-facilities-events-camps-and-rentals.md)

## Open questions

None.

---

⬅️ [S-SC18-17 Court booking](s-sc18-17-court-booking.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-19 Holiday camps](s-sc18-19-holiday-camps.md)
