🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-06 Cashless, cinemas, tours and photographers](README.md) ›
🖥️ S-SC16-22 Cinema

# 🖥️ S-SC16-22 Cinema

**Status:** ✅ specified

## Personas

- [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md): the programme, the tickets sold and the
  closing of each screening.
- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md): the programme choices, the report and the
  distributors.

## Purpose

Schedule screenings, count their admissions and receipts, compute the tax and the distributor's share and report to the
national film centre.

## Entry points

Events and culture › Cinema; the box office; the week's report.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Cinema week 11 to 17 Nov        Report through Cinedi due 2026-11-22  [Schedule] [Close] [Send]  |
| Screening  Film             Screen  Time    Admissions  Receipts   Tax, due on    State          |
| SC-2210    The Long Shore   2       20:30   96          744.00     81.30, 13 Nov  Shown          |
| SC-2211    The Long Shore   2       22:45   54          418.50     45.73, 13 Nov  Reported       |
| SC-2212    Petit Pierre     1       18:00   -           -          -              On sale        |
| Week: 18 screenings, 1,210 admissions, 9,372.50 EUR, one slip per film, version and screen       |
| Distributors: 3                                                                                  |
| Tax due at each collection: first part 1,004.73 EUR, due; second part 19.41 EUR, due             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-06 step 2, U44 | desktop | ![FL-SC16-06 step 2, U44, light](../../images/06-cashless-cinemas-tours-and-photos/u44-box-office-agent/2-cinema-desktop-light.png) | ![FL-SC16-06 step 2, U44, dark](../../images/06-cashless-cinemas-tours-and-photos/u44-box-office-agent/2-cinema-desktop-dark.png) |
| FL-SC16-06 step 2, U44 | phone | ![FL-SC16-06 step 2, U44, light](../../images/06-cashless-cinemas-tours-and-photos/u44-box-office-agent/2-cinema-phone-light.png) | ![FL-SC16-06 step 2, U44, dark](../../images/06-cashless-cinemas-tours-and-photos/u44-box-office-agent/2-cinema-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-22-cinema-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-22-cinema-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-22-cinema-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-22-cinema-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-22-cinema-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-22-cinema-read-only-desktop-dark.png) |
| Sales off (no CNC approval) | desktop | ![Sales off, light](../../images/states/s-sc16-22-cinema-sales-off-desktop-light.png) | ![Sales off, dark](../../images/states/s-sc16-22-cinema-sales-off-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-22-cinema-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-22-cinema-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Film | E-SC16-20 film | text | yes while Scheduled | yes |
| Screen | E-SC16-20 room | link | yes while Scheduled | yes |
| Time | E-SC16-20 starts at | date and time | yes while Scheduled | yes |
| Admissions | E-SC16-20 admissions | number | no | no |
| Receipts | E-SC16-20 receipts | amount in EUR | no | no |
| Tax | E-SC16-20 tax | amount in EUR: 10.72 % of the price paid plus 0.232 % of the rest (CIBS L452-5, CR-FR-248), dated at each collection (L452-9); a part under its threshold shows "not due": the first part at 80 EUR or less over the decree's period or a single screening in the week, the second part at 30 EUR or less a year (L452-11, BR-SC16-17) | no | no |
| Distributor share | E-SC16-20 distributor share | amount in EUR | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Schedule | header | programmer | a screening in state Scheduled |
| Open sales | screening | programmer | the screening is On sale |
| Close | screening | cashier | the admissions and receipts are fixed and the screening is Shown |
| Send report | header | owner | the week's report, one slip per film, version and screen, goes to the national film centre through Cinedi within 5 days after the cinema week (Wednesday to Tuesday); the shown screenings are Reported |

## States

- Normal: the screenings with film, screen, time, admissions, receipts, tax and state.
- Empty: No screening yet, with Schedule.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a seat sold
  twice, a screening without its figures, a film without terms, with the screening.
- Read-only: the record in a locked state: values shown, no action offered.
- Sales off: while the cinema (E-SC16-03) has no CNC approval number of its ticketing system or no date of the
  delivery and installation declaration, no ticket is sold at the box office or online; a banner names what is missing
  and links to the cinema to record it (BR-SC16-17, UC-SC16-22 2e,
  [D575](../../../../06-decisions/foundations/d575-answers-of-2026-11-27-on-the-last-open-points.md) point 13).
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC16-20 Screening](../../data/e-sc16-20-screening.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-20 Screening | Scheduled | Badge "Scheduled"; a new record starts here; next: On sale or Cancelled (UC-SC16-22); fields editable within the role | U44, U43 | `u44-box-office-agent/s-sc16-22-cinema-e-sc16-20-screening-scheduled-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-22-cinema-e-sc16-20-screening-scheduled-{desktop,phone}-{light,dark}.png` |
| E-SC16-20 Screening | On sale | Badge "On sale"; next: Shown or Cancelled (BR-SC16-17, UC-SC16-22); fields editable within the role | U44, U43 | `u44-box-office-agent/s-sc16-22-cinema-e-sc16-20-screening-on-sale-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-22-cinema-e-sc16-20-screening-on-sale-{desktop,phone}-{light,dark}.png` |
| E-SC16-20 Screening | Shown | Badge "Shown"; next: Reported (BR-SC16-17); fields editable within the role | U44, U43 | `u44-box-office-agent/s-sc16-22-cinema-e-sc16-20-screening-shown-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-22-cinema-e-sc16-20-screening-shown-{desktop,phone}-{light,dark}.png` |
| E-SC16-20 Screening | Reported | Badge "Reported"; final: read-only, no next state; the history shows how it got here | U44, U43 | `u44-box-office-agent/s-sc16-22-cinema-e-sc16-20-screening-reported-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-22-cinema-e-sc16-20-screening-reported-{desktop,phone}-{light,dark}.png` |
| E-SC16-20 Screening | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U44, U43 | `u44-box-office-agent/s-sc16-22-cinema-e-sc16-20-screening-cancelled-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-22-cinema-e-sc16-20-screening-cancelled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC16-06](../../flows/fl-sc16-06-cashless-cinemas-tours-and-photos.md)

## Open questions

None.

---

⬅️ [S-SC16-21 Cashless payments](s-sc16-21-cashless.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-23 Tour](s-sc16-23-touring.md)
