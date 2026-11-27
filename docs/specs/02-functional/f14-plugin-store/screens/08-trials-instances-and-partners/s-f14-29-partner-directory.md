🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-08 Trials, test instances, partners and themes](README.md) › 🖥️ S-F14-29 Partner directory

# 🖥️ S-F14-29 Partner directory

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the directory and their enquiries.
- [U51 Reseller partner](../../../../01-users/personas/u51-reseller-partner.md): their own listing, enquiries and
  ranking factors.

## Purpose

Find a partner for an implementation, read why it ranks where it does, send an enquiry; the partner keeps their listing.

## Entry points

Plugin store › Partners; the onboarding checklist; the AI assistant.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Partner directory       Country [Spain v] Language [Spanish v] Sector [Services v]  [Search] |
|---------------------------------------------------------------------------------------------|
| PARTNER          RANK  SCORE  PROJECTS  RATING  CERTIFIED  LANGUAGES    [Enquiry]           |
| Norte Systems    1     84     31        4.7     yes        es, en        [Why this rank?]   |
| Sur Consulting   2     79     18        4.5     yes        es            [Why this rank?]   |
| Why this rank: projects 40%, ratings 30%, certification 20%, response time 10%              |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-08 step 3, U13 | desktop | ![FL-F14-08 step 3, U13, light](../../images/08-trials-instances-and-partners/u13-owner/3-partner-directory-desktop-light.png) | ![FL-F14-08 step 3, U13, dark](../../images/08-trials-instances-and-partners/u13-owner/3-partner-directory-desktop-dark.png) |
| FL-F14-08 step 3, U13 | phone | ![FL-F14-08 step 3, U13, light](../../images/08-trials-instances-and-partners/u13-owner/3-partner-directory-phone-light.png) | ![FL-F14-08 step 3, U13, dark](../../images/08-trials-instances-and-partners/u13-owner/3-partner-directory-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-29-partner-directory-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-29-partner-directory-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-29-partner-directory-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-29-partner-directory-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-29-partner-directory-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-29-partner-directory-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f14-29-partner-directory-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f14-29-partner-directory-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Partner | E-F14-24 partner | name and logo | partner, for their own | yes |
| Countries, languages, sectors | E-F14-24 coverage | lists | partner | yes |
| Services | E-F14-24 services | list | partner | yes |
| Projects and ratings | E-F14-24 evidence | numbers | no | no |
| Ranking factors | E-F14-24 score parts | percentages | no | yes |
| Certification | E-F14-24 certification | text and evidence | partner | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Search | header | owner, administrator | the partners that match |
| Why this rank? | row | everyone | the factors and weights of the ranking |
| Enquiry | row | owner, administrator | sends a lead to the partner |
| Edit listing | partner view | partner | changes the partner's own listing |
| Rate | row | owner | rates a partner after a project |

## States

- Normal: the partners that match the filters, ranked, with the factors on demand.
- Empty: No partner matches, with Widen the search.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a failed search
  shows the reason and keeps the filters.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F14-24 Partner listing](../../data/e-f14-24-partner-listing.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-24 Partner listing | Applied | Badge "Applied"; a new record starts here; next: Listed or Declined (UC-F14-31); fields editable within the role | U13, U51 | `u13-owner/s-f14-29-partner-directory-e-f14-24-partner-listing-applied-{desktop,phone}-{light,dark}.png`, `u51-reseller-partner/s-f14-29-partner-directory-e-f14-24-partner-listing-applied-desktop-{light,dark}.png` |
| E-F14-24 Partner listing | Listed | Badge "Listed"; next: Suspended or Withdrawn (UC-F14-31); fields editable within the role | U13, U51 | `u13-owner/s-f14-29-partner-directory-e-f14-24-partner-listing-listed-{desktop,phone}-{light,dark}.png`, `u51-reseller-partner/s-f14-29-partner-directory-e-f14-24-partner-listing-listed-desktop-{light,dark}.png` |
| E-F14-24 Partner listing | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U13, U51 | `u13-owner/s-f14-29-partner-directory-e-f14-24-partner-listing-declined-{desktop,phone}-{light,dark}.png`, `u51-reseller-partner/s-f14-29-partner-directory-e-f14-24-partner-listing-declined-desktop-{light,dark}.png` |
| E-F14-24 Partner listing | Suspended | Badge "Suspended"; next: Listed (UC-F14-31); fields editable within the role | U13, U51 | `u13-owner/s-f14-29-partner-directory-e-f14-24-partner-listing-suspended-{desktop,phone}-{light,dark}.png`, `u51-reseller-partner/s-f14-29-partner-directory-e-f14-24-partner-listing-suspended-desktop-{light,dark}.png` |
| E-F14-24 Partner listing | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U13, U51 | `u13-owner/s-f14-29-partner-directory-e-f14-24-partner-listing-withdrawn-{desktop,phone}-{light,dark}.png`, `u51-reseller-partner/s-f14-29-partner-directory-e-f14-24-partner-listing-withdrawn-desktop-{light,dark}.png` |

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

- [FL-F14-08](../../flows/fl-f14-08-trials-instances-and-partners.md)

## Open questions

None.

---

⬅️ [S-F14-28 Free trials](s-f14-28-free-trials.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-30 Website themes](s-f14-30-website-themes.md)
