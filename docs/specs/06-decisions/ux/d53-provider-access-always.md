🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D53 Provider access to client data

# 📜 D53 Provider access to client data

**Status:** ✅ decided

## Context

Whether an IT provider administrator (U11) can act inside a client company's data.

## Options

- Only with the client's consent, time-limited and audited.
- Always.
- Never.

## Choice

Always: the IT provider administrator can enter any client company at any time.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

- The provider processes each client's personal data on the client's behalf, so under the GDPR (Article 28) it acts as a
  processor, which usually calls for a data processing agreement between them.
- The audit trail (T3) records what the provider does inside a client company, as for any user (D12).

## Related

- [IT provider administrator](../../01-users/personas/u11-provider-admin.md)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)
- [Privacy and GDPR](../../05-non-functional/privacy-gdpr.md)

---

⬅️ [D52 F1 Administration scope](../f01-administration/d52-f1-scope.md) · ⬆️ [Up](README.md) ·
➡️ [D54 Guided setup with a sector pack](../f01-administration/d54-guided-setup.md)
