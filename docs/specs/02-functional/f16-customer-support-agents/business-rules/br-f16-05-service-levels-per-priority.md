🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-05 Service levels per priority

# 📏 BR-F16-05 Service levels per priority

**Status:** ✅ specified

## Statement

Each request gets a priority from its intent and customer, and the service-level policy of that priority sets a
first-response and a resolution target counted in the support team's business hours; a request about to miss its target
is flagged and one that misses it is marked breached.

## Why

Customers and contracts need response times (D473); SC14 support contracts promise them.

## Examples

| Case | Result |
|---|---|
| Normal priority, first response target 4 business hours | request at 10:00 Monday answered 13:30 | met |
| Urgent priority, resolution 8 business hours | resolved next day 15:00 | breached, lead told |
| Request waiting for the customer | clock paused | met |

## Applies to

- [UC-F16-07 Set service levels and follow targets](../use-cases/04-human-agent-workspace/uc-f16-07-set-service-levels-and-follow-targets.md)
- [UC-F16-12 Follow a request's status](../use-cases/05-customer-side/uc-f16-12-follow-a-requests-status.md)
- [UC-F16-13 Ask for a person](../use-cases/05-customer-side/uc-f16-13-ask-for-a-person.md)
- [UC-F16-05 Monitor resolution and accuracy](../use-cases/03-review-and-monitor/uc-f16-05-monitor-resolution-and-accuracy.md)

## Exceptions

The clock pauses while waiting for the customer's reply.

## Configurable

The support lead sets priorities, targets and business hours per policy.

## Open questions

None.

---

⬅️ [BR-F16-04 Customers know, and can reach a person](br-f16-04-customers-know-and-can-reach-a-person.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F16-06 One person on a request at a time](br-f16-06-one-person-on-a-request-at-a-time.md)
