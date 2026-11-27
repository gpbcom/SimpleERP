🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-07 Similar features, catalogue, co-funding and maintenance](README.md) › 🖥️ S-F19-28 Co-funding

# 🖥️ S-F19-28 Co-funding

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the fundings they proposed and the ones they can pledge to.

## Purpose

Share the cost of a feature with other customers: publish a funding, pledge and follow the goal.

## Entry points

Feature factory › Co-funding; the feature request's page; the hosted store's funding section.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Co-funding: Lease reminders by email      Goal 1,200 EUR     Deadline 2027-01-12 (41 days left) |
|---------------------------------------------------------------------------------------------|
| Raised 900 EUR of 1,200 (75 %)      Pledgers 6       What you get: the feature, first year free |
| [==============================------------]                                               |
| Your pledge: 200 EUR (excl. VAT)     Charged only if the goal is met by the deadline.          |
| [Pledge] [Change amount] [Withdraw]                                                          |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-07 step 3, U13 | desktop | ![FL-F19-07 step 3, U13, light](../../images/07-catalogue-and-co-funding/u13-owner/3-co-funding-desktop-light.png) | ![FL-F19-07 step 3, U13, dark](../../images/07-catalogue-and-co-funding/u13-owner/3-co-funding-desktop-dark.png) |
| FL-F19-07 step 3, U13 | phone | ![FL-F19-07 step 3, U13, light](../../images/07-catalogue-and-co-funding/u13-owner/3-co-funding-phone-light.png) | ![FL-F19-07 step 3, U13, dark](../../images/07-catalogue-and-co-funding/u13-owner/3-co-funding-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/07-catalogue-and-co-funding/u13-owner/e1-the-funding-goal-is-not-reached-desktop-light.png) | ![Error E1, U13, dark](../../images/07-catalogue-and-co-funding/u13-owner/e1-the-funding-goal-is-not-reached-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/07-catalogue-and-co-funding/u13-owner/e1-the-funding-goal-is-not-reached-phone-light.png) | ![Error E1, U13, dark](../../images/07-catalogue-and-co-funding/u13-owner/e1-the-funding-goal-is-not-reached-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-28-co-funding-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-28-co-funding-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-28-co-funding-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-28-co-funding-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-28-co-funding-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-28-co-funding-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-28-co-funding-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-28-co-funding-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Feature and goal | E-F19-18 funding goal | text and amount | by the proposer while Draft | yes |
| Deadline | E-F19-18 deadline | date | by the proposer while Draft | yes |
| Raised and pledgers | E-F19-18 total, count | amount and number | no | no |
| Your pledge | E-F19-18 amount | amount excluding VAT | yes until the goal is met | yes |
| What pledgers get | E-F19-18 reward | text | by the proposer while Draft | yes |
| State | E-F19-18 state | badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Publish funding | header | proposing owner | the funding becomes visible to hosted customers |
| Pledge | page | owner | records the pledge, charges nothing |
| Change or withdraw | pledge | owner | possible until the goal is met |
| Close the funding | header | proposing owner | ends it early, every pledge lapses |

## States

- Normal: the funding with the amount raised, the days left and the owner's own pledge.
- Empty: No funding open, with Propose a funding for a feature.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a goal not
  reached shows that every pledge lapsed and nothing was charged.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F19-18 Funding pledge](../../data/e-f19-18-funding-pledge.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-18 Funding pledge | Pledged | Badge "Pledged"; a new record starts here; next: Charged, Lapsed or Withdrawn (BR-F19-22, UC-F19-29); fields editable within the role | U13 | `u13-owner/s-f19-28-co-funding-e-f19-18-funding-pledge-pledged-{desktop,phone}-{light,dark}.png` |
| E-F19-18 Funding pledge | Charged | Badge "Charged"; next: Refunded (UC-F19-22); fields editable within the role | U13 | `u13-owner/s-f19-28-co-funding-e-f19-18-funding-pledge-charged-{desktop,phone}-{light,dark}.png` |
| E-F19-18 Funding pledge | Lapsed | Badge "Lapsed"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f19-28-co-funding-e-f19-18-funding-pledge-lapsed-{desktop,phone}-{light,dark}.png` |
| E-F19-18 Funding pledge | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f19-28-co-funding-e-f19-18-funding-pledge-withdrawn-{desktop,phone}-{light,dark}.png` |
| E-F19-18 Funding pledge | Refunded | Badge "Refunded"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f19-28-co-funding-e-f19-18-funding-pledge-refunded-{desktop,phone}-{light,dark}.png` |

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

- [FL-F19-07](../../flows/fl-f19-07-catalogue-and-co-funding.md)

## Open questions

None.

---

⬅️ [S-F19-27 Fixed-price catalogue](s-f19-27-fixed-price-catalogue.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-29 Maintenance plan](s-f19-29-maintenance-plan.md)
