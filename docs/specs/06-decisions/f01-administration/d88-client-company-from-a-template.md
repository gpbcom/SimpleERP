🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D88 Client company from a template

# 📜 D88 Client company from a template

**Status:** ✅ decided

## Context

What the IT provider sets when it creates a client company.

## Options

- The name and the first administrator.
- The whole setup for the client.
- From a template company.
- Resource limits.

## Choice

From one of the provider's template companies: its configuration (roles, forms, sector pack) is copied, never its data.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The client's first administrator then finishes the guided setup (UC-F1-01).

## Related

- [UC-F1-10](../../02-functional/f01-administration/use-cases/08-provider-and-client-companies/uc-f01-10-create-a-client-company-on-the-platform.md)
- [BR-F1-19](../../02-functional/f01-administration/business-rules/br-f01-19-templates-copy-configuration-only.md)

---

⬅️ [D87 Allowed domains](d87-allowed-domains.md) · ⬆️ [Up](README.md) ·
➡️ [D89 Provider sessions are visible](d89-provider-sessions-visible.md)
