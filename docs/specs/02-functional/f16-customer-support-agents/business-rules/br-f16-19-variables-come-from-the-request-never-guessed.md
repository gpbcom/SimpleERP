🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-19 Variables come from the request, never guessed

# 📏 BR-F16-19 Variables come from the request, never guessed

**Status:** ✅ specified

## Statement

A variable of a canned reply is filled only from the request or the records of its customer; a variable with no value,
or with several candidate values, is never filled by guess: sending is blocked until a person or the customer's record
supplies the value.

## Why

A reply with a wrong order number or date is worse than a late reply: it is wrong in the customer's hands. The owner
asked for canned replies
([D535](../../../06-decisions/f16-customer-support-agents/d535-benchmark-gaps-f16-customer-support-agents.md)); the AI
agent acts only as its procedure allows ([BR-F16-03](br-f16-03-agents-act-only-as-their-procedure-allows.md)).

## Examples

| Case | Result |
|---|---|
| Order number on an order's request | filled from the order |
| A new date the records do not hold | missing, sending blocked |
| Two open orders | the agent chooses, not guessed |
| An amount the agent may not read | restricted, not filled |
| The AI agent using a reply | same rule, hands over when a variable is missing |

## Applies to

- [UC-F16-23](../use-cases/07-live-chat-voice-and-contracts/uc-f16-23-use-canned-replies.md)
- [E-F16-07 Macro](../data/e-f16-07-macro.md)

## Exceptions

None.

## Configurable

The variables a reply may use, by the support lead.

## Open questions

None.

---

⬅️ [BR-F16-18](br-f16-18-work-beyond-the-prepaid-balance-needs-consent.md) · ⬆️ [Up](README.md)
