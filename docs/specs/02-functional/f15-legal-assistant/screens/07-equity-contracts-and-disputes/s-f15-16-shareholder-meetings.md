🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-07 Equity, contracts, meetings and disputes](README.md) › 🖥️ S-F15-16 Shareholder meetings

# 🖥️ S-F15-16 Shareholder meetings

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): every meeting, its votes and its minutes.
- [U50 Shareholder](../../../../01-users/personas/u50-shareholder.md): the convocation, the documents and their vote,
  from a phone.

## Purpose

Prepare, convene, count the votes of and close a shareholders' general meeting.

## Entry points

Administration › Company records › Shareholder meetings; the shareholder's portal.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| General meeting: ordinary, 2026-12-15 10:00              Convened   [Open] [Close] [Minutes] |
|---------------------------------------------------------------------------------------------|
| Convocation sent 2026-11-24 (notice 15 days)   Quorum required 25%   Present 78%            |
| RESOLUTION                        MAJORITY   FOR    AGAINST  ABSTAIN  RESULT                |
| 1 Approve the accounts 2025       50%+1      90.0   5.0      5.0      Adopted               |
| 2 Allocate the result             50%+1      88.0   12.0     0.0      Adopted               |
| 3 Approve the 2026 equity plan    2/3        65.0   35.0     0.0      Rejected              |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-07 step 5, U13 | desktop | ![FL-F15-07 step 5, U13, light](../../images/07-equity-contracts-and-disputes/u13-owner/5-shareholder-meetings-desktop-light.png) | ![FL-F15-07 step 5, U13, dark](../../images/07-equity-contracts-and-disputes/u13-owner/5-shareholder-meetings-desktop-dark.png) |
| FL-F15-07 step 5, U13 | phone | ![FL-F15-07 step 5, U13, light](../../images/07-equity-contracts-and-disputes/u13-owner/5-shareholder-meetings-phone-light.png) | ![FL-F15-07 step 5, U13, dark](../../images/07-equity-contracts-and-disputes/u13-owner/5-shareholder-meetings-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/07-equity-contracts-and-disputes/u13-owner/e1-the-quorum-is-not-reached-desktop-light.png) | ![Error E1, U13, dark](../../images/07-equity-contracts-and-disputes/u13-owner/e1-the-quorum-is-not-reached-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/07-equity-contracts-and-disputes/u13-owner/e1-the-quorum-is-not-reached-phone-light.png) | ![Error E1, U13, dark](../../images/07-equity-contracts-and-disputes/u13-owner/e1-the-quorum-is-not-reached-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-16-shareholder-meetings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-16-shareholder-meetings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-16-shareholder-meetings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-16-shareholder-meetings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-16-shareholder-meetings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-16-shareholder-meetings-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-16-shareholder-meetings-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-16-shareholder-meetings-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Meeting | E-F15-19 type, date | text and date | while Planned | yes |
| Convocation | E-F15-19 sent on, notice | date and days | no | yes |
| Quorum | E-F15-19 required, present | two percentages | no | yes |
| Resolution | E-F15-19 resolutions | text and majority | while Planned | yes |
| Votes and result | E-F15-19 votes | percentages and badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send convocation | header | owner | sends the notice and documents to every holder |
| Vote | phone | shareholder | casts or changes the holder's vote |
| Open meeting | header | owner | counts the quorum |
| Close meeting | header | owner | freezes the votes and drafts the minutes |
| Adjourn | header | owner | postpones when the quorum is not reached |

## States

- Normal: the meeting with its convocation, quorum, resolutions and results.
- Empty: No meeting yet, with New meeting.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a late
  convocation or a missing quorum shows the date or the figure.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F15-19 General meeting](../../data/e-f15-19-general-meeting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-19 General meeting | Planned | Badge "Planned"; a new record starts here; next: Convened or Cancelled (UC-F15-18); fields editable within the role | U13, U50 | `u13-owner/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-planned-{desktop,phone}-{light,dark}.png`, `u50-shareholder/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-planned-{desktop,phone}-{light,dark}.png` |
| E-F15-19 General meeting | Convened | Badge "Convened"; next: Held, Adjourned or Cancelled (BR-F15-22, UC-F15-18); fields editable within the role | U13, U50 | `u13-owner/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-convened-{desktop,phone}-{light,dark}.png`, `u50-shareholder/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-convened-{desktop,phone}-{light,dark}.png` |
| E-F15-19 General meeting | Held | Badge "Held"; next: Minuted (UC-F15-18); fields editable within the role | U13, U50 | `u13-owner/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-held-{desktop,phone}-{light,dark}.png`, `u50-shareholder/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-held-{desktop,phone}-{light,dark}.png` |
| E-F15-19 General meeting | Adjourned | Badge "Adjourned"; next: Planned (UC-F15-18); fields editable within the role | U13, U50 | `u13-owner/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-adjourned-{desktop,phone}-{light,dark}.png`, `u50-shareholder/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-adjourned-{desktop,phone}-{light,dark}.png` |
| E-F15-19 General meeting | Minuted | Badge "Minuted"; final: read-only, no next state; the history shows how it got here | U13, U50 | `u13-owner/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-minuted-{desktop,phone}-{light,dark}.png`, `u50-shareholder/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-minuted-{desktop,phone}-{light,dark}.png` |
| E-F15-19 General meeting | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U13, U50 | `u13-owner/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-cancelled-{desktop,phone}-{light,dark}.png`, `u50-shareholder/s-f15-16-shareholder-meetings-e-f15-19-general-meeting-cancelled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The owner's screen is desktop only. The shareholder opens the convocation, the documents and the vote on a phone and
sees only their own voting right.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F15-07](../../flows/fl-f15-07-equity-contracts-and-disputes.md)

## Open questions

None.

---

⬅️ [S-F15-15 Contract drafting](s-f15-15-contract-drafting.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-17 IP portfolio](s-f15-17-ip-portfolio.md)
