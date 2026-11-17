🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F23-20 Group scenarios eliminate intercompany flows

# 📏 BR-F23-20 Group scenarios eliminate intercompany flows

**Status:** 🔄 waiting for the owner

## Statement

A group scenario eliminates every flow between companies of the group before showing the consolidated result: each flow
is mirrored in both companies and removed from the group's sales, costs, receivables and payables, and a flow that
cannot be mirrored is listed, never silently kept or dropped.

## Why

Counting internal trade twice overstates both revenue and cost and misleads the decision. The owner asked for group
scenarios ([D542](../../../06-decisions/f23-what-if-simulation/d542-benchmark-gaps-f23-what-if-simulation.md)); the
accounting already mirrors and eliminates intercompany
([BR-F8-07](../../f08-accounting/business-rules/br-f08-07-intercompany-mirrored-and-eliminated.md)).

## Examples

| Case | Result |
|---|---|
| A sells 100 k to B | 100 k removed from group sales and group costs |
| A loan between two companies | removed from the group's debt and receivables |
| A flow in one currency and a mirror in another | translated as the consolidation does, then eliminated |
| A flow with no mirror | listed as unmatched, not eliminated |
| A dividend inside the group | removed from the group result |

## Applies to

- [UC-F23-33](../use-cases/08-budgets-rolling-group-and-valuation/uc-f23-33-run-a-group-scenario.md)
- [BR-F8-07](../../f08-accounting/business-rules/br-f08-07-intercompany-mirrored-and-eliminated.md)

## Exceptions

None.

## Configurable

No: the consolidation mapping is the accounting's
([UC-F8-13](../../f08-accounting/use-cases/05-close-report-and-consolidate/uc-f08-13-consolidate-the-group.md)).

## Open questions

None.

---

⬅️ [BR-F23-19 Each rolling forecast keeps its version](br-f23-19-each-rolling-forecast-keeps-its-version.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F23-21 Valuations show their method and assumptions](br-f23-21-valuations-show-their-method-and-assumptions.md)
