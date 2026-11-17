🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F20-21 Access ends at its time limit and is audited

# 📏 BR-F20-21 Access ends at its time limit and is audited

**Status:** 🔄 waiting for the owner

## Statement

Every access to a customer's screen or app by a support person has a time limit set by the customer's administrator (240
minutes at most), a visible banner, and a record; it ends by itself at its limit, cannot be extended, and never changes
data.

## Why

Access that does not end, or that nobody sees, is a standing risk; a record is what lets the customer check what was
done. The owner asked for consented screen sharing
([D539](../../../06-decisions/f20-hosted-support-assistant/d539-benchmark-gaps-f20-hosted-support-assistant.md)).
(Proposed) The France-pack rule on remote access consent is written later.

## Examples

| Case | Result |
|---|---|
| Granted for 30 minutes at 14:00 | ends at 14:30 by itself |
| The engineer asks to extend | a new request and a new grant are needed |
| A read-only view as Accounting | personal data masked, no change possible |
| The administrator presses Stop | ends at once, reason Revoked |
| A request asking for 6 hours | refused |

## Applies to

- [UC-F20-30](../use-cases/08-engineers-sharing-and-reports/uc-f20-30-share-the-screen-or-a-time-limited-view.md)
- [E-F20-20 Access grant](../data/e-f20-20-access-grant.md)
- [E-F20-11 Assistant policy](../data/e-f20-11-assistant-policy.md)
- [E-F20-19 Engineer call](../data/e-f20-19-engineer-call.md)

## Exceptions

None.

## Configurable

The default limit (30 minutes), by the customer's administrator; the 240-minute ceiling is fixed.

## Open questions

None.

---

⬅️ [BR-F20-20 Calls follow the plan's times](br-f20-20-calls-follow-the-plans-times.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F20-22 Reports contain no personal data](br-f20-22-reports-contain-no-personal-data.md)
