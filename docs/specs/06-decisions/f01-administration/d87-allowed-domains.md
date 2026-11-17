🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D87 Allowed domains

# 📜 D87 Allowed domains

**Status:** ✅ decided

## Context

Which email domains, and which default role, for accounts auto-created by single sign-on (D55).

## Options

- Set by the administrator.
- Provider groups map to roles.
- Both.

## Choice

Set by the administrator: the allowed domains (such as acme.fr), the default role and the default site; anyone else is
refused.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

No group-to-role mapping.

## Related

- [UC-F1-09](../../02-functional/f01-administration/use-cases/07-set-up-single-sign-on/uc-f01-09-set-up-single-sign-on.md)
- [BR-F1-18](../../02-functional/f01-administration/business-rules/br-f01-18-allowed-domains.md)

---

⬅️ [D86 Administrators keep a password](d86-administrators-keep-a-password.md) · ⬆️ [Up](README.md) ·
➡️ [D88 Client company from a template](d88-client-company-from-a-template.md)
