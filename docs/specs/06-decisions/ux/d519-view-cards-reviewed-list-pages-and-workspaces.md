🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D519 View cards reviewed: list pages and workspaces

# 📜 D519 View cards reviewed: list pages and workspaces

**Status:** ✅ decided

## Context

Step S5 of GH-2's plan derived one view card per entity by the view rules VR-1 to VR-15 and put the 824 cards to the
owner on a review page, capability by capability (VD-09,
[D492](d492-view-content-derived-by-rules-reviewed-per-capability.md)). The owner confirmed 810 cards as they were and
asked for 14 changes, read on 2026-11-13 at 12:34; two of the notes were clarified at 12:36.

## Options

- For each card: confirm it, or change it with a note.
- For VC-1 to VC-6 and VC-10: give each list its existing personas (Recommended), or create new personas.
- For VC-13: each employee's calendar compared side by side, or the meeting agenda, or both.
- The interview record (the owner's interview of 2026-11-13 on wording and views, not kept in the repository) keeps the owner's answers,
  not every option.

## Choice

The 810 confirmed cards become list pages as they are; the 14 changes are applied as below. The owner's notes, word for
word:

| # | Card | The owner's note | Applied |
|---|---|---|---|
| VC-1 | [E-F3-03 Suggested question](../../02-functional/f03-assistant/data/e-f03-03-suggested-question.md) | "Create persona(s) related to this enitity." | U07 and U13, who curate the suggested questions; the other AI assistant users are left out |
| VC-2 | [E-F3-04 Assistant change batch](../../02-functional/f03-assistant/data/e-f03-04-assistant-change-batch.md) | "Create persona(s) related to this enitity." | the users who asked for the changes (the F3 use cases' personas) and U07 |
| VC-3 | [E-F3-07 Personal connection](../../02-functional/f03-assistant/data/e-f03-07-personal-connection.md) | "Create persona(s) related to this enitity." | every AI assistant user, for their own connections |
| VC-4 | [E-F3-08 Outside call](../../02-functional/f03-assistant/data/e-f03-08-outside-call.md) | "Create persona(s) related to this enitity." | U07 only |
| VC-5 | [E-F3-12 Conversation folder](../../02-functional/f03-assistant/data/e-f03-12-conversation-folder.md) | "Create persona(s) related to this enitity." | every AI assistant user, for their own folders |
| VC-6 | [E-F3-14 Answer feedback](../../02-functional/f03-assistant/data/e-f03-14-answer-feedback.md) | "Create persona(s) related to this enitity." | every AI assistant user for their own feedback, U07 and U13 to curate it |
| VC-7 | [E-F3-22 AI assistant request](../../02-functional/f03-assistant/data/e-f03-22-ai-assistant-request.md) | "The AI assitant MUST be usabe by everyone BUT disable the tools that could grant an Employee an unlegitimate access." | every persona, for their own requests; BR-F3-34 extended: the tools that would read or change what the user's role may not are disabled |
| VC-8 | [E-F9-03 Department](../../02-functional/f09-hr-and-projects/data/e-f09-03-department.md) | "All personas MUST see this list." | the Department list (Team was merged into it) for every persona |
| VC-9 | [E-F4-06 Scorecard](../../02-functional/f04-meetings/data/e-f04-06-scorecard.md) | "Add HR to the personas" | U06 Human resources added |
| VC-10 | [E-F4-08 Key moment](../../02-functional/f04-meetings/data/e-f04-08-key-moment.md) | "Create persona(s) related to this enitity." | the personas of the meeting use cases and U02, their managers, to confirm on the Key moments list |
| VC-11 | [E-F4-16 Client video meeting](../../02-functional/f04-meetings/data/e-f04-16-client-video-meeting.md) | "All employee types." | every employee persona added |
| VC-12 | [E-F4-18 Recording notice](../../02-functional/f04-meetings/data/e-f04-18-recording-notice.md) | "Add HR to this Personas list" | U06 Human resources added |
| VC-13 | [E-F4-22 Meeting agenda](../../02-functional/f04-meetings/data/e-f04-22-meeting-agenda.md) | "All employes MUST have one. Provide the ability to compare one employee agenda to others" | E-F4-26 Employee calendar, its list with a side-by-side comparison (BR-F4-32); BR-F4-31 every meeting has an agenda, compared between employees' meetings; both lists for every employee persona |
| VC-14 | [E-F6-03 Quote](../../02-functional/f06-customers-and-sales/data/e-f06-03-quote.md) | "Add Manager, Owner, and Planner here at the very least." | U02 Manager, U13 Owner and the ten planner roles of E-F1-06 (D517) |

The two clarifications, word for word: VC-1 to VC-6 and VC-10, "Give each list its existing personas (Recommended)";
VC-13, "both": every employee has a calendar compared with others, and every meeting has an agenda, comparable between
employees' meetings.

How the words were read: "every AI assistant user" is a persona of the F3 use cases (U01 to U07, U12 to U16); "all
personas" is U01 to U48; "all employee types" are the personas inside the company (01-users): U01, U02, U03, U04, U05,
U06, U07, U12, U13, U14, U15, U16, U17, U18, U19, U20, U21, U22, U23, U24, U25, U26, U27, U28, U29, U30, U31, U33, U34,
U35, U36, U37, U38, U39, U40, U41, U42, U43, U44, U45, that is every persona but the outside users U08 to U11, the
volunteer U32 and U46 to U48; the planner personas are the planner roles of E-F1-06 Role (D517): U29, U25, U22, U24,
U21, U23, U38, U34, U43, U28.

Two more answers, at 13:51, word for word: VC-15, 11 personas a use case gives a list but the permission matrix refused
(Orders U05; Invoices U02, U03; Leads U09, U16; Purchase orders U01, U05; Payment providers U09; Work centres U05, U07;
Payroll entries U01), "Read access where the use case needs it (Recommended)": each gets read access in its capability's
permissions page, limited to what its use case does, and Payment providers also goes to U07, who connects payment tools
(UC-F24-21); VC-16, "all employee types" for the client video meetings, "Yes, the 40 internal personas (Recommended)":
the reading above stands.

## Decided by

The owner, on 2026-11-13 at 12:34, 12:36 and 13:51, in the GH-2 interview round on the wording and the views
(interview record (the owner's interview of 2026-11-13 on wording and views, not kept in the repository), sections "View cards (S5)" and
"List pages (S5): permission conflicts and "all employee types"").

## Consequences

- One list page per entity, 825 in all, in each capability's `screens/00-lists/` folder, named "S-<capability>-L<nn>
  <View>" after the entity's number ([list view template](../../_templates/list-view.md)); technical entities under
  their T capability and in the Administration menu (VD-11).
- One workspace per persona in `04-ux/views/<persona>/workspace.md`, embedding the views of its use cases (VD-10).
- The F3 lists whose use cases name their personas without a name (UC-F3-01 to UC-F3-08) take those personas, as the
  owner's answer gives each list its existing personas; the lists the owner confirmed for fewer personas say whom they
  leave out, and why.
- VC-7 extends
  [BR-F3-34](../../02-functional/f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md).
- [E-F4-26 Employee calendar](../../02-functional/f04-meetings/data/e-f04-26-employee-calendar.md),
  [BR-F4-31](../../02-functional/f04-meetings/business-rules/br-f04-31-every-meeting-has-an-agenda.md) and
  [BR-F4-32](../../02-functional/f04-meetings/business-rules/br-f04-32-who-sees-a-colleagues-calendar.md) are added
  (VC-13).
- VC-15: the permissions pages of F6, F7, F11, F12 and F13 give the 11 personas their use cases gave a list read access
  limited to what the use case does, and the 7 lists embed them; no list leaves out a persona the permissions refuse any
  longer.
- Each workspace opens a view on the persona's default saved view; the rule is proposed on the workspace pages.
- The new check `check_views.py` of GH-2 proves every entity has its list page and every persona its workspace.

## Related

- [D484 Aggregated list view per record type](d484-aggregated-list-view-per-record-type-and-persona-workspaces.md)
- [D492 View content derived by rules, reviewed](d492-view-content-derived-by-rules-reviewed-per-capability.md)
- [D493 Persona workspaces from the use cases](d493-persona-workspaces-from-the-use-cases.md)
- [D494 Settings and technical records as admin lists](d494-settings-and-technical-records-as-admin-lists.md)
- [D495 Views listed under each capability menu](d495-views-listed-under-each-capabilitys-menu.md)
- [D517 The drafts open points](../foundations/d517-the-drafts-open-points-answered-on-2026-11-13.md)
- Interview record (the owner's interview of 2026-11-13 on wording and views, not kept in the repository)

---

⬅️ [D518 LinkedIn sourcing through Unipile](../f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md) ·
⬆️ [Up](README.md) ·
➡️ [D520 Benchmark gaps of F1 Administration](../f01-administration/d520-benchmark-gaps-f01-administration.md)
