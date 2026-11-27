🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-03 Agents act only as their procedure allows

# 📏 BR-F16-03 Agents act only as their procedure allows

**Status:** ✅ specified

## Statement

An agent handles only requests classified into an intent it owns, reads only the data its procedure names, and uses only
its intent's allowed actions (REQ-T12-03); in shadow, actions are dry runs; amounts and limits of the procedure apply
(for example a refund at most the amount paid, prepared by the agent and paid only once a person approves it,
[D439](../../../06-decisions/f03-assistant/d439-ai-autonomy-tiers.md)); anything else goes to a person with the reason.

## Why

See [D238](../../../06-decisions/f16-customer-support-agents/d238-static-or-agentic.md).

## Examples

| Case | Result |
|---|---|
| A refund within the procedure's limit | Prepared in automatic, paid once a person approves (D439) |
| A request that fits no intent | Routed to a person |
| A refund above the paid amount | Refused, routed to a person |

## Applies to

Every F16 use case concerned.

## Exceptions

None.

## Configurable

Yes: per intent, its actions and limits.

## Open questions

None.

---

⬅️ [BR-F16-02 A sample is always reviewed](br-f16-02-a-sample-is-always-reviewed.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F16-04 Customers know, and can reach a person](br-f16-04-customers-know-and-can-reach-a-person.md)
