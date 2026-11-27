🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F16-08 No duplicate action

# 📏 BR-F16-08 No duplicate action

**Status:** 🔄 waiting for the owner

## Statement

An agent never repeats the same action (refund, cancellation, plan change, re-send) on the same order or customer within
the guard window; a second request for it is answered with the first action's result.

## Why

Duplicate refunds are the costliest agent error (D473).

## Examples

| Case | Result |
|---|---|
| Customer writes twice for the same duplicate charge | second answered with the first refund, no new refund |
| Refund already done by a person in the back-office tool | agent sees it, does not refund again |
| Same action on another order | allowed |

## Applies to

- [UC-F16-08 Support requests in the agent workspace](../use-cases/04-human-agent-workspace/uc-f16-08-work-requests-in-the-agent-workspace.md)
- [UC-F16-01 Resolve a customer request automatically](../use-cases/01-resolve-a-request/uc-f16-01-resolve-a-customer-request-automatically.md)

## Exceptions

A person may repeat an action with a reason, logged.

## Configurable

The guard window per action, (Proposed) 30 days for refunds.

## Open questions

None.

---

⬅️ [BR-F16-07 Refund limits per intent](br-f16-07-refund-limits-per-intent.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F16-09 Satisfaction asked once per resolved request](br-f16-09-satisfaction-asked-once-per-resolved-request.md)
