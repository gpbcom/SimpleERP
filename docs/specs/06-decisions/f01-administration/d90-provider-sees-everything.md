🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D90 The provider sees everything

# 📜 D90 The provider sees everything

**Status:** ✅ decided

## Context

What the provider administrator sees inside a client company.

## Options

- Everything: administrator and every business role.
- Settings only.
- Chosen per session.

## Choice

Everything: inside a client company, the provider administrator holds the administrator role and every business role.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

An exception to BR-F1-02; every action is in the provider access log (D89) and the audit trail.

## Related

- [UC-F1-11](../../02-functional/f01-administration/use-cases/08-provider-and-client-companies/uc-f01-11-enter-a-client-company-to-support-it.md)
- [BR-F1-02](../../02-functional/f01-administration/business-rules/br-f01-02-administrator-sees-settings-only.md)

---

⬅️ [D89 Provider sessions are visible](d89-provider-sessions-visible.md) · ⬆️ [Up](README.md) ·
➡️ [D91 Administration reports](d91-administration-reports.md)
