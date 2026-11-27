🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC08-07 Foundations, integration, federations, peer fundraising](README.md) › 🖥️ S-SC08-23 Federation

# 🖥️ S-SC08-23 Federation

**Status:** 🔄 waiting for the owner

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md): the dues, the invoices and the late clubs.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the clubs by region, the votes and the totals.

## Purpose

Affiliate clubs, compute their dues from their headcount and count their votes for the assembly.

## Entry points

Non-profit association › Member organisations; the season's declarations; the assembly's votes.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Season 2026-27   Clubs 112   Affiliated 104   Candidates 3   Late 5          [Compute dues]      |
| Club                    Region     Licensed  Dues       Paid       Votes   State                 |
| Judo Club Part-Dieu     Rhône      142       1,123.00   1,123.00   7       Affiliated            |
| Aikido Croix-Rousse     Rhône      38        447.00     0.00       2       Suspended             |
| Judo Annecy             Savoie     97        830.50     830.50     5       Affiliated            |
| Scale: 200.00 + 6.50 per licensed member    Votes: 1 per 20 members, minimum 1, cap 10           |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-07 step 3, U31 | desktop | ![FL-SC08-07 step 3, U31, light](../../images/07-foundations-integration-and-federations/u31-treasurer/3-federation-desktop-light.png) | ![FL-SC08-07 step 3, U31, dark](../../images/07-foundations-integration-and-federations/u31-treasurer/3-federation-desktop-dark.png) |
| FL-SC08-07 step 3, U31 | phone | ![FL-SC08-07 step 3, U31, light](../../images/07-foundations-integration-and-federations/u31-treasurer/3-federation-phone-light.png) | ![FL-SC08-07 step 3, U31, dark](../../images/07-foundations-integration-and-federations/u31-treasurer/3-federation-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-23-federation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-23-federation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-23-federation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-23-federation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-23-federation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-23-federation-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-23-federation-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-23-federation-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Club | E-SC08-18 club | link | no | yes |
| Region and discipline | E-SC08-18 region, discipline | choice lists | yes | yes |
| Licensed members | E-SC08-18 licensed members | number | club, secretary | yes |
| Dues | E-SC08-18 dues | amount in EUR | no | no |
| Dues paid | E-SC08-18 dues paid | amount in EUR | no | no |
| Votes | E-SC08-18 votes | number | no | no |
| Affiliated since | E-SC08-18 affiliated on | date | yes while Candidate | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Affiliate | header | secretary | the club is Affiliated with its statutes |
| Declare members | club's page | club representative | the headcount for the season |
| Compute dues | header | treasurer | the dues of every club, with the scale shown |
| Suspend | club | secretary, treasurer | the club is Suspended and its votes removed |

## States

- Normal: the clubs with their headcount, dues, payments and votes.
- Empty: No club yet, with Affiliate a club.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  declaration or statutes, with the document to provide.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC08-18 Member organisation](../../data/e-sc08-18-member-organisation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-18 Member organisation | Candidate | Badge "Candidate"; a new record starts here; next: Affiliated (UC-SC08-23); fields editable within the role | U31, U13 | `u31-treasurer/s-sc08-23-federation-e-sc08-18-member-organisation-candidate-{desktop,phone}-{light,dark}.png`, `u13-owner/s-sc08-23-federation-e-sc08-18-member-organisation-candidate-{desktop,phone}-{light,dark}.png` |
| E-SC08-18 Member organisation | Affiliated | Badge "Affiliated"; next: Suspended or Left (UC-SC08-23); fields editable within the role | U31, U13 | `u31-treasurer/s-sc08-23-federation-e-sc08-18-member-organisation-affiliated-{desktop,phone}-{light,dark}.png`, `u13-owner/s-sc08-23-federation-e-sc08-18-member-organisation-affiliated-{desktop,phone}-{light,dark}.png` |
| E-SC08-18 Member organisation | Suspended | Badge "Suspended"; next: Affiliated (UC-SC08-23); fields editable within the role | U31, U13 | `u31-treasurer/s-sc08-23-federation-e-sc08-18-member-organisation-suspended-{desktop,phone}-{light,dark}.png`, `u13-owner/s-sc08-23-federation-e-sc08-18-member-organisation-suspended-{desktop,phone}-{light,dark}.png` |
| E-SC08-18 Member organisation | Left | Badge "Left"; final: read-only, no next state; the history shows how it got here | U31, U13 | `u31-treasurer/s-sc08-23-federation-e-sc08-18-member-organisation-left-{desktop,phone}-{light,dark}.png`, `u13-owner/s-sc08-23-federation-e-sc08-18-member-organisation-left-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC08-07](../../flows/fl-sc08-07-foundations-integration-and-federations.md)

## Open questions

None.

---

⬅️ [S-SC08-22 Work integration](s-sc08-22-work-integration.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-24 Peer-to-peer fundraising](s-sc08-24-peer-fundraising.md)
