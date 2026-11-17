🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D516 Naming rules and the seven classes of names

# 📜 D516 Naming rules and the seven classes of names

**Status:** 🔄 draft (GH-2 step S1, from the naming review page / D516)

## Context

Step S1 of the [plan](../../../tickets/GH-2/resources/flowcharts-screens/PLAN.md) started early: the owner's naming
review page (https://claude.ai/artifact/Agsh192gnVYmkBM4YKaH1o) holds the naming rules, the 92 items of the 42 shared
names, the 130 proposed new items and the 907 chart words ([naming
map](../../../tickets/GH-2/resources/flowcharts-screens/naming/README.md)).

## Options

- The rules as proposed on the review page.
- For the 130 new items, the owner's first classification or Claude's; after comparing them the owner answered "Keep
  your choices and save them."

## Choice

Five naming rules:
1. **The AI is always "AI assistant".** U37 Professional's assistant, a person, is renamed "Professional's assistant" so
   the two never
   clash.
2. **A person acting is the persona; the record is the entity.** "Customer" acting is U09 Customer; the record kept
   about them is "Customer record" (E-F6-01). The same for Supplier (U10, E-F7-01) and Employee (U01, E-F9-01).
3. **Generic words are always qualified.** "Order", "request", "report", "template", "rule", "provider", "plan",
   "session" and "review" never stand alone: they name the precise item (sales order, purchase order, production order).
4. **A technical entity mirroring a functional one keeps its name.** The "same item" pairs (Company, Provider session,
   AI feature setting, Connector, Plugin installation, Tool connection) keep one name and link to each other.
5. **Every name has one of seven classes:**
   - persona: a kind of user who signs in;
   - role on a record: a user in a role on one record (organiser, owner, deputy);
   - entity: a record the app stores;
   - screen or report: computed and shown, not stored;
   - outside party: an organisation, person or system outside simple-ERP;
   - AI or system actor: simple-ERP or its AI acting;
   - not a name: a generic word to reword.

## Decided by

The owner, on 2026-11-12, on the naming review page (rules agreed; answer 20 of the [interview
record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md)).

## Consequences

- The 130 new items are classed: 73 entities, 26 screens or reports, 20 outside parties, 5 roles on a record, 4 AI or
  system actors, 1 persona (Configurator) and 1 not a name ("Record", whose chart is reworded). One new persona instead
  of 32.
- U37 is renamed "Professional's assistant" (change note on the roles and personas).
- [D496](d496-one-wording-in-charts-and-prose-reviewed-first.md) applies the approved names in every chart and prose
  page.

## Related

- [Naming map of the flow charts](../../../tickets/GH-2/resources/flowcharts-screens/naming/README.md)
- [Shared names](../../../tickets/GH-2/resources/flowcharts-screens/naming/CLASHES.md)
- [Proposed new items](../../../tickets/GH-2/resources/flowcharts-screens/naming/NEW-ITEMS.md)
- [Roles](../../01-users/roles.md)
- [D496 One wording in charts and prose, reviewed first](d496-one-wording-in-charts-and-prose-reviewed-first.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md)

---

⬅️ [D515](../f09-hr-and-projects/d515-the-engine-proposes-automatic-mode-enabled-by-hand-stops-on-a-problem.md) ·
⬆️ [Up](README.md) ·
➡️ [D517 The drafts' open points, answered on 2026-11-13](d517-the-drafts-open-points-answered-on-2026-11-13.md)
