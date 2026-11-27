🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-02 Recruit](README.md) ›
🖥️ S-F9-37 LinkedIn sourcing search

# 🖥️ S-F9-37 LinkedIn sourcing search

**Status:** 🔄 waiting for the owner

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md): the searches they own.

## Purpose

Search LinkedIn with a rich set of criteria and shortlist the profiles the AI assistant ranked.

## Entry points

HR and projects › Recruitment › a job position › LinkedIn sourcing; the AI assistant
([BR-F3-34](../../../f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md)).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| LinkedIn sourcing: site manager        LinkedIn account: Claire P. (linked)   [Run search]   |
|---------------------------------------------------------------------------------------------|
| CRITERIA                            | RANKED PROFILES (48 found, 12 shortlisted)             |
| Titles      site manager            | Score  Profile             Reason               Keep   |
| Skills      planning, site safety   | 92     Julien R., Lyon     8 of 9 criteria met  [x]    |
| Seniority   senior                  | 88     Sonia M., Vienne    32 km away           [x]    |
| Experience  5 to 15 years           | 61     Marc T., Grenoble   outside the radius   [ ]    |
| Location    Lyon, 40 km             |                                                        |
| Languages   French, English B2      |                                                        |
| Employers   exclude Acme Bâtiment   |                                                        |
| Keywords    "gros oeuvre" AND NOT intern                                                     |
| Open to work  [x]                   |             [Save search] [Build the sequence]         |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-14 step 2, U06 | desktop | ![FL-F9-14 step 2, U06, light](../../images/14-source-candidates-on-linkedin/u06-hr/2-linkedin-sourcing-search-desktop-light.png) | ![FL-F9-14 step 2, U06, dark](../../images/14-source-candidates-on-linkedin/u06-hr/2-linkedin-sourcing-search-desktop-dark.png) |
| FL-F9-14 step 3, U06 | desktop | ![FL-F9-14 step 3, U06, light](../../images/14-source-candidates-on-linkedin/u06-hr/3-linkedin-sourcing-search-desktop-light.png) | ![FL-F9-14 step 3, U06, dark](../../images/14-source-candidates-on-linkedin/u06-hr/3-linkedin-sourcing-search-desktop-dark.png) |
| Error E3, U06 | desktop | ![Error E3, U06, light](../../images/14-source-candidates-on-linkedin/u06-hr/e3-forbidden-criterion-desktop-light.png) | ![Error E3, U06, dark](../../images/14-source-candidates-on-linkedin/u06-hr/e3-forbidden-criterion-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-37-linkedin-sourcing-search-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-37-linkedin-sourcing-search-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-37-linkedin-sourcing-search-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-37-linkedin-sourcing-search-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-37-linkedin-sourcing-search-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-37-linkedin-sourcing-search-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-37-linkedin-sourcing-search-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-37-linkedin-sourcing-search-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Criteria | E-F9-44 criteria | lists, ranges, text with AND, OR, NOT | yes | titles or keywords |
| LinkedIn account | E-F24-02 | name and state | link or sign in again | yes |
| Score and reason | E-F9-45 score, reason, criteria met and missed | 0 to 100 and a sentence | no | yes |
| Keep | E-F9-45 state | check box | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Run search | header | HR | the search runs through Unipile (UC-F9-40) |
| Keep | row | HR | the profile is shortlisted |
| Add a profile | results | HR | a profile added by its LinkedIn address and scored |
| Build the sequence | results | HR | opens S-F9-38 with the shortlist |

## States

- Normal: the criteria on the left, the ranked profiles on the right, each with its reason.
- Empty: No profile found yet, with Run search. Set the criteria and run the search.
- Loading: Searching LinkedIn and scoring: the profiles appear as they are scored.
- Error: the error message pattern (D122); a forbidden criterion is refused under its field
  ([BR-F9-40](../../business-rules/br-f09-40-no-criterion-the-law-forbids-in-hiring.md)).
- Read-only: a closed search: its criteria and its shortlist, without actions.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-44 Sourcing search](../../data/e-f09-44-sourcing-search.md),
[E-F9-45 Prospect](../../data/e-f09-45-prospect.md), [E-F9-06 Job position](../../data/e-f09-06-job-position.md),
[E-F24-02 Tool connection](../../../f24-integrations-hub/data/e-f24-02-tool-connection.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-44 Sourcing search | Draft | the header's badge and actions | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-44-sourcing-search-draft-desktop-{light,dark}.png` |
| E-F9-44 Sourcing search | Running | the header's badge and actions | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-44-sourcing-search-running-desktop-{light,dark}.png` |
| E-F9-44 Sourcing search | Ranked | the header's badge and actions | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-44-sourcing-search-ranked-desktop-{light,dark}.png` |
| E-F9-44 Sourcing search | Failed | the header's badge and actions | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-44-sourcing-search-failed-desktop-{light,dark}.png` |
| E-F9-44 Sourcing search | Closed | the header's badge and actions | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-44-sourcing-search-closed-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Found | the row's Keep box | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-45-prospect-found-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Shortlisted | the row's Keep box | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-45-prospect-shortlisted-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Discarded | the row's Keep box | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-45-prospect-discarded-desktop-{light,dark}.png` |
| E-F9-06 Job position | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-06-job-position-active-desktop-{light,dark}.png` |
| E-F24-02 Tool connection | Proposed | Badge "Proposed"; a new record starts here; next: Active (UC-F24-21); fields editable within the role | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f24-02-tool-connection-proposed-desktop-{light,dark}.png` |
| E-F24-02 Tool connection | Active | Badge "Active"; next: Revoked (UC-F24-17); fields editable within the role | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f24-02-tool-connection-active-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Connected | Badge "Connected"; next: Waiting for HR, Applicant, Declined or No answer (UC-F9-41, UC-F9-42, BR-F9-37); fields editable within the role | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-45-prospect-connected-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Waiting for HR | Badge "Waiting for HR"; next: Applicant, Declined or No answer (UC-F9-42, UC-F9-41, BR-F9-37); fields editable within the role | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-45-prospect-waiting-for-hr-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Declined | Badge "Declined"; next: Erased (BR-F9-39); fields editable within the role | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-45-prospect-declined-desktop-{light,dark}.png` |
| E-F9-45 Prospect | No answer | Badge "No answer"; next: Erased (BR-F9-39); fields editable within the role | U06 | `u06-hr/s-f09-37-linkedin-sourcing-search-e-f09-45-prospect-no-answer-desktop-{light,dark}.png` |
| E-F9-45 Prospect | Erased | Not shown: the record is gone in this state, so no screen shows it | U06 | None: system state, the user never sees it |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

The score is read as a number and a word ("strong match"); the reason is text, not a colour; keyboard: next profile,
keep, open.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-14 Source candidates on LinkedIn](../../flows/fl-f09-14-source-candidates-on-linkedin.md)
- [FL-F9-02 Recruit](../../flows/fl-f09-02-recruit.md)

## Open questions

None.

---

⬅️ [S-F9-36 Readings to verify](../13-keep-qualifications/s-f09-36-readings-to-verify.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-38 Outreach sequence](s-f09-38-outreach-sequence.md)
