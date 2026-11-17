🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚖️ [Decisions: F15 Legal assistant](README.md) ›
📜 D207 Copyrighted standards: a register and own copies

# 📜 D207 Copyrighted standards: a register and own copies

**Status:** ✅ decided

## Context

AFNOR and ISO forbid putting their standards into AI systems (Q15,
[Sector technical standards](../../05-non-functional/sector-technical-standards.md)).

## Options

- A register, and companies' own licensed copies.
- A register only.
- A licence first.

## Choice

Free law and official guidance in full, pulled unattended (D205). Standards as a register: reference, title, edition,
the laws that cite them, where to get them, built from ISO Open Data and from legal texts, with notes in simple-ERP's
own words; AFNOR's catalogue is never scraped. A company may add its own licensed copies to its private corpus, opt-in,
after attesting an AI-use licence from the rights holder. An AFNOR licence is sought later.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F15-10; the register is pulled daily from ISO Open Data like the law (D205).

Revised by D448 on 2026-11-12: standards are excluded from D205's unattended pulls; register entries come from open
sources only.

## Related

- [Q15](../../07-questions/q15-copyrighted-standards.md)
- [D205](d205-law-packs-fed-from-official-apis.md)

---

⬅️ [D206 Unattended pulls, no test-set gate](d206-unattended-pulls-without-test-gate.md) · ⬆️ [Up](README.md) ·
➡️ [D208 Meeting sources](../f04-meetings/d208-meeting-sources.md)
