🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D453 An optional SIRET on a site

# 📜 D453 An optional SIRET on a site

**Status:** ✅ decided

## Context

[Q11](../../07-questions/q11-establishment-siret.md): in France each establishment has its own SIRET, used by payroll
declarations (DSN) and some registers, while a site has no legal identity of its own (D36).

## Options

- A site may carry an optional SIRET.
- Each establishment is a separate company.
- Not needed.

## Choice

Confirmed by the owner on 2026-11-12: the SIRET is kept on the site, optional. It is 14 digits and starts with the
company's SIREN (CR-FR-001).

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- The site entity has an optional SIRET field.
- Payroll (F13) and the HR registers (F9) declare per site when it has one.
- The e-invoicing connection registers the sites' SIRETs with the platform (D454).

## Related

- [E-F1-02 Company site](../../02-functional/f01-administration/data/e-f01-02-company-site.md)
- [Q11](../../07-questions/q11-establishment-siret.md)

---

⬅️ [D452](../ux/d452-repository-maintainer-and-hosting-engineer.md) · ⬆️ [Up](README.md) ·
➡️ [D454](../f08-accounting/d454-e-invoicing-platforms.md)
