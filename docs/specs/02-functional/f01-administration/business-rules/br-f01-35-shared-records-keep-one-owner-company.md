🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-35 Shared records keep one owner company

# 📏 BR-F1-35 Shared records keep one owner company

**Status:** ✅ specified

## Statement

A shared record has exactly one owner company, the only one that changes it; the other companies read it or use it in
their own documents and may only propose changes. A rule becomes active only once the owner company approves it, and
ending a rule never deletes what another company already built on a record.

## Why

Two companies editing the same record would break each company's isolation and the audit of who changed what. The
owner's answer: "Shared group data"
([D520](../../../06-decisions/f01-administration/d520-benchmark-gaps-f01-administration.md)).

## Examples

| Case | Result |
|---|---|
| Lyon edits a shared customer's address | it becomes a proposal to the owner company |
| Lyon adds its own credit limit to the shared customer | allowed: private fields belong to Lyon |
| A rule is saved by the administrator | draft until the owner approves it |
| A rule ends | Lyon keeps its invoices and a read-only copy of the shared fields it used |
| Two companies both claim the same customer | refused: one is the owner, the other links to it |

## Applies to

- [UC-F1-26 Share master data across the group](../use-cases/15-security-and-group-data/uc-f01-26-share-master-data-across-the-group.md)
- [E-F1-25 Sharing rule](../data/e-f01-25-sharing-rule.md)
- [UC-F7-15 Trade between group companies](../../f07-purchasing-and-stock/use-cases/06-benchmark-additions/uc-f07-15-trade-between-group-companies.md)

## Exceptions

None.

## Configurable

No: one owner per shared record, always.

## Open questions

None.

---

⬅️ [BR-F1-34](br-f01-34-purges-are-logged-and-never-touch-legal-records.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-36](br-f01-36-acting-as-a-user-needs-consent-and-is-audited.md)
