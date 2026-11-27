🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-21 Non-standard clauses need legal approval

# 📏 BR-F15-21 Non-standard clauses need legal approval

**Status:** 🔄 waiting for the owner

## Statement

A clause whose wording is changed or written freely in a draft is non-standard: the contract cannot be exported for
signature until each non-standard clause is approved by the owner or by a lawyer, and the approval records the exact
wording approved.

## Why

Approved wording is the company's protection; a change that nobody reviewed can create a liability or break a legal
limit. The owner asked for contract drafting
([D534](../../../06-decisions/f15-legal-assistant/d534-benchmark-gaps-f15-legal-assistant.md)); the legal assistant
gives information, never advice ([BR-F15-02 Information, not advice](br-f15-02-information-not-advice.md)).

## Examples

| Case | Result |
|---|---|
| A standard clause as written | no approval needed |
| A variant of the library (payment in 45 days) | standard, no approval needed |
| A liability cap typed into a draft | non-standard, approval needed |
| A clause approved for one contract | not approved for the next |
| No lawyer in the company | the owner approves with a waiver of legal review |

## Applies to

- [UC-F15-17](../use-cases/07-equity-contracts-and-disputes/uc-f15-17-draft-a-contract-from-the-clause-library.md)
- [E-F15-18 Clause](../data/e-f15-18-clause.md)
- [E-F15-06 Contract record](../data/e-f15-06-contract-record.md)

## Exceptions

None.

## Configurable

Who may approve (owner, a named lawyer), by the owner.

## Open questions

None.

---

⬅️ [BR-F15-20 Simulations never change the register](br-f15-20-simulations-never-change-the-register.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F15-22 Votes count only within quorum and majority](br-f15-22-votes-count-only-within-quorum-and-majority.md)
