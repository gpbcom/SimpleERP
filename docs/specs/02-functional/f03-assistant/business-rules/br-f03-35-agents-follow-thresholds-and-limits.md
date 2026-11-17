🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-35 Agents follow thresholds and amount limits

# 📏 BR-F3-35 Agents follow thresholds and amount limits

**Status:** ✅ specified

## Statement

An agent applies a change on its own only above its confidence threshold and below the amount limits that would apply to
a person in its role; otherwise it prepares the change for a person; everything it does is logged and reversible.

An agent acts alone only within a procedure an administrator switched to automatic, within its limits, every act audited
and a sample checked by a person; it never pays, sends a legal document, deletes or decides about a person alone: it
prepares those ([D439](../../../06-decisions/f03-assistant/d439-ai-autonomy-tiers.md)).

## Why

See [D301](../../../06-decisions/f03-assistant/d301-f3-benchmark-gaps.md).

Autonomy tiers: [D439](../../../06-decisions/f03-assistant/d439-ai-autonomy-tiers.md).

## Examples

| Case | Result |
|---|---|
| Accrual 820 EUR, confidence 96 %, limit 10 000 | Posted, logged |
| Bill 18 000 EUR | Prepared for the controller |

## Applies to

UC-F3-10, UC-F3-11

## Exceptions

None.

## Configurable

Threshold and limits per agent.

## Open questions

None.

---

⬅️ [BR-F3-34 All capabilities via the AI assistant](br-f03-34-every-capability-is-reachable-from-the-assistant.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F3-36 An audit agent checks the agents](br-f03-36-an-audit-agent-checks-agents.md)
