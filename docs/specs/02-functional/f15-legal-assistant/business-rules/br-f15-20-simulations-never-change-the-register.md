🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-20 Simulations never change the register

# 📏 BR-F15-20 Simulations never change the register

**Status:** ✅ specified

## Statement

A funding-round simulation never writes to the share register or the cap table: it reads the register, computes on a
copy, and becomes Executed only when real movements of the register match it.

## Why

A simulation is a question of 'what if'; mixing it with the register would let a draft pass for ownership. The owner
asked for full equity ([D534](../../../06-decisions/f15-legal-assistant/d534-benchmark-gaps-f15-legal-assistant.md)).

## Examples

| Case | Result |
|---|---|
| A saved scenario | the register and the cap table are unchanged |
| A shared copy | read-only, no personal data of private holders |
| Real subscriptions registered for the round | the simulation can be marked Executed |
| Subscriptions that differ from the simulation | the simulation stays Shared, with the gap shown |
| Two scenarios | compared side by side, each its own copy |

## Applies to

- [UC-F15-16](../use-cases/07-equity-contracts-and-disputes/uc-f15-16-simulate-a-fundraising-dilution.md)
- [E-F15-17 Funding round](../data/e-f15-17-funding-round.md)
- [E-F15-15 Shareholding](../data/e-f15-15-shareholding.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F15-19](br-f15-19-grants-follow-the-plan-approved-by-shareholders.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F15-21 Non-standard clauses need legal approval](br-f15-21-non-standard-clauses-need-legal-approval.md)
