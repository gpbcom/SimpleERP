🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D91 Administration reports

# 📜 D91 Administration reports

**Status:** ✅ decided

## Context

Which administration reports F1 offers.

## Options

- Users overview.
- Access review.
- Connections and AI usage.
- Security events.

## Choice

All four: users overview (active, invited, deactivated per site and role, last sign-in), access review (who holds which
rights on what, exportable), connections and AI usage (calls per connection, AI requests per feature and provider,
fallbacks, requests sent outside), and security events (failed sign-ins, two-factor resets, provider sessions,
administrators' password sign-ins under single sign-on).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The reports read the audit trail (T3).

## Related

- [F1 Administration](../../02-functional/f01-administration/README.md)
- [Reports](../../02-functional/f01-administration/reports.md)

---

⬅️ [D90 The provider sees everything](d90-provider-sees-everything.md) · ⬆️ [Up](README.md) ·
➡️ [D92 Notification channels](d92-notification-channels.md)
