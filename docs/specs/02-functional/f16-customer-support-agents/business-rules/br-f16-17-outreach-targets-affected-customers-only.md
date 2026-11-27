🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-17 Outreach targets affected customers only

# 📏 BR-F16-17 Outreach targets affected customers only

**Status:** ✅ specified

## Statement

An outreach is sent only to the customers whose own records match the stated cause, selected by a query on those
records; it is never sent to a whole customer list, and a customer who opted out of service messages is left out.

## Why

A message to customers who are not affected creates doubt and requests; to everyone, it is spam. The owner asked for
proactive outreach
([D535](../../../06-decisions/f16-customer-support-agents/d535-benchmark-gaps-f16-customer-support-agents.md)); a
service message is not marketing
([CR-FR-063](../../../10-country-packs/france/consumer/cr-fr-063-electronic-marketing-consent.md)).

## Examples

| Case | Result |
|---|---|
| Orders of batch 7 delayed | the 214 customers who ordered it |
| A selection that returns every customer | refused, narrower cause asked |
| A customer with no order in the batch | not contacted |
| A customer who opted out of service messages | left out and listed |
| A second message when the cause is solved | the same audience, no more |

## Applies to

- [UC-F16-21](../use-cases/07-live-chat-voice-and-contracts/uc-f16-21-warn-customers-before-they-ask.md)
- [E-F16-15 Outreach](../data/e-f16-15-outreach.md)
- [E-F16-15 Outreach](../data/e-f16-15-outreach.md)

## Exceptions

None.

## Configurable

The audience size above which a second approval is needed, by the owner.

## Open questions

None.

---

⬅️ [BR-F16-16 Callers are told they speak with an AI](br-f16-16-callers-are-told-they-speak-with-an-ai.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F16-18](br-f16-18-work-beyond-the-prepaid-balance-needs-consent.md)
