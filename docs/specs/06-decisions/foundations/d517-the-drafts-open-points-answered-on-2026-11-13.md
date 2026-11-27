🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D517 The drafts' open points, answered on 2026-11-13

# 📜 D517 The drafts' open points, answered on 2026-11-13

**Status:** ✅ decided

## Context

The drafts of GH-2 steps S4 and S4b (D484 to D516, the T13 pages, the scheduling, map and qualification pages and the
change notes) left 18 points marked as proposed, listed in the drafts' open
points (the owner's interview notes of 2026-11 for the specifications, not kept in the repository). Step S0 added three new shared names
(S0-1 to S0-3). The owner was asked all of them on 2026-11-13, each with its proposal.

## Options

For each point: the proposal of the drafts, or another answer. The interview
record (the owner's interview of 2026-11-13 on wording and views, not kept in the repository) keeps the owner's answers, not every option.

## Choice

Every point as proposed. The owner's words are kept as given.

| # | Point | Decision | The owner's answer |
|---|---|---|---|
| 1 | Map right and operational plans | No: the map right covers geographic maps of records; plans inside operational screens (S-F10-09 Floor, the seat map) follow that screen's own rights | "No (Recommended)" |
| 2 | The outside-call log and BR-F3-33 | The call log tab of S-F3-13 for the administrator only, and an exception line in BR-F3-33 | "Admin only + exception (Recommended)" |
| 3 | Automatic mode on a problem | It stops for that work request only; the setting stays on for the others | "That request only (Recommended)" |
| 4 | "Work requests" in UC-F16-08 | UC-F16-08 says "support requests" (D516's rule on generic words) | "UC-F16-08 says support requests (Recommended)" |
| 5 | Field workers and addresses | No map; a "Directions" button on an address opens the phone's own navigation app | "Directions button (Recommended)" |
| 6 | Planner roles | U29, U25, U22, U24, U21, U23, U38, U34, U43, U28; the managers U02 and U13 | "As proposed (Recommended)" |
| 7 | Who switches automatic mode on | The administrator or the planners' manager, per team and request type | "Admin or planners' manager (Recommended)" |
| 8 | Default order of the scheduling objectives | Legal and required attributes always hard; then lateness, travel, customer preferences, fairness, cost; adjustable per request type | "As proposed (Recommended)" |
| 9 | Retention of live positions | Two months at most; the CNIL guidance is read with the France country pack (CR-FR-211) | "Two months at most (Recommended)" |
| 10 | Scoring and thresholds | Weights of preferred attributes 1 to 5, a score of 0 to 100, AI readings proposed to HR above 80 % confidence (fields under it marked) | "As proposed (Recommended)" |
| 11 | The customer's arrival screen | The arrival time, a small map near their address and the visitor's first name, during the window only | "As proposed (Recommended)" |
| 12 | Employees sending their own documents | Allowed; HR still confirms every reading | "Yes, HR confirms (Recommended)" |
| 13 | Requests that need no field work | Not turned into work requests | "No (Recommended)" |
| 14 | CR-FR-058 and the scheduling engine | Stays proposed and to read, read in Q17's batches; a lawyer for what stays unread | "Read in batches (Recommended)" |
| 15 | T13 software and performance targets | As named in the drafts: OpenStreetMap tiles, BAN, Nominatim, OSRM or Valhalla, an open-source solver, and the targets of REQ-T13-01 to 08 | "As named in the drafts (Recommended)" |
| 16 | The legal references of CR-FR-208 | Stays proposed and to read, read in Q17's batches; a lawyer for what stays unread | "Read in batches (Recommended)" |
| 17 | E-F1-09 "AI feature setting" | Keeps its name (its technical twin E-T07-02 is the same item) | "Keep; S2 waits (Recommended)" |
| 18 | The 847 chart words not reviewed | Step S2 applies only the 60 reviewed words; the rest wait for the owner's review page | "Keep; S2 waits (Recommended)" |
| S0-1 | New shared name "Round" (E-SC04-05, E-F9-26) | Merged into E-F9-26 Round; E-SC04-05 stays as a redirect, its home-care specifics a sector extension of E-F9-26 | "Merge into E-F9-26 (Recommended)" |
| S0-2 | New shared name "Recipe" (E-SC06-01, E-F12-25) | Merged into E-F12-25 Recipe; E-SC06-01 stays as a redirect, its kitchen specifics a sector extension of E-F12-25 | "Merge into E-F12-25 (Recommended)" |
| S0-3 | New shared name "Webhook subscription" (E-T05-02, E-F24-13) | The same item: both pages stay and link each other | "Same item (Recommended)" |

## Decided by

The owner, on 2026-11-13, in the GH-2 interview round on the wording, the aggregated views and scheduling (interview
record (the owner's interview of 2026-11-13 on wording and views, not kept in the repository)): "Go, everything run the tests ONLY on the
modified pages."

## Consequences

- The drafts lose their proposed mark on points 1 to 13 and 15, and cite this decision where they state the answer.
- Points 14 and 16 stay proposed and to read until the law is read in batches.
- Point 4: UC-F16-08 is named "Support requests in the agent workspace"; its file keeps its name.
- S0-1 and S0-2: E-SC04-05 and E-SC06-01 keep their IDs as short pages pointing to E-F9-26 and E-F12-25, whose
  "Fields" section gains a sector extension; every link to them points to the surviving entity.
- S0-3: E-T05-02 and E-F24-13 link each other in their "Relations" section.

## Related

- The drafts' open points (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)
- Interview record (the owner's interview of 2026-11-13 on wording and views, not kept in the repository)
- [D516 Naming rules and the seven classes of names](d516-naming-rules-and-the-seven-classes-of-names.md)
- [D502 Records on a map for planners and managers only](../ux/d502-records-on-a-map-for-planners-and-managers-only.md)
- [D515 The engine proposes; automatic mode enabled by hand, stops on a
  problem](../f09-hr-and-projects/d515-the-engine-proposes-automatic-mode-enabled-by-hand-stops-on-a-problem.md)

---

⬅️ [D516 Naming rules and the seven classes of names](d516-naming-rules-and-the-seven-classes-of-names.md) ·
⬆️ [Up](README.md) ·
➡️ [D518 LinkedIn sourcing through Unipile](../f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md)
