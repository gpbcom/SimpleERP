🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚖️ [Decisions: F15 Legal assistant](README.md) ›
📜 D205 Law packs fed from official APIs

# 📜 D205 Law packs fed from official APIs

**Status:** ✅ decided

## Context

Who reviews a law pack before it is published.

## Options

- simple-ERP and a lawyer of the country.
- simple-ERP maintainers.
- Nobody, community ratings.

## Choice

No validation: the owner, "Law pack will be fed directly from official APIs so that there is no need to validation. It
MUST be periodically pulled so that it stays up to date without any human intervention. This applies to EU regulation as
well as technical norms and standards."

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

A law pack describes its official sources and is refreshed on a schedule, unattended; EU regulation (EUR-Lex) and sector
technical rules and standards follow the same rule (BR-F15-09). D200's test-set gate is withdrawn
([D206](d206-unattended-pulls-without-test-gate.md)).

Revised by D448 on 2026-11-12: the unattended pulls feed the law corpus with raw official texts only; the country pack's
rule values change only through signed pack updates (D294, REQ-T11-01); copyrighted standards are excluded from the
pulls and kept as register entries (D207).

## Related

- [F15 Legal assistant](../../02-functional/f15-legal-assistant/README.md)
- [D199](d199-law-packs.md)
- [D200](d200-legal-quality-test-set.md)

---

⬅️ [D204 Legal assistant reports](d204-legal-reports.md) · ⬆️ [Up](README.md) ·
➡️ [D206 Unattended pulls, no test-set gate](d206-unattended-pulls-without-test-gate.md)
