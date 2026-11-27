🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚖️ [Decisions: F15 Legal assistant](README.md) ›
📜 D448 Law texts apart from signed rule packs

# 📜 D448 Law texts apart from signed rule packs

**Status:** ✅ decided

## Context

R11: D205 pulls standards with no validation while Q15 and BR-F15-10 treat them as copyrighted; REQ-T11-01 refuses
unsigned packs; D206 removed the legal test-set gate against REQ-T07-05.

## Options

- Raw law texts apart from signed rule packs; standards excluded; F15's set gates models and prompts.
- Keep D205 as written.

## Choice

Two things are kept apart. **Raw official texts** (Légifrance, EUR-Lex, official guidance, case law) are pulled
unattended into the law corpus (D205, BR-F15-09) and answer legal questions. **The country pack's rule values** (the CR
rules SimpleERP computes and enforces with) are signed and versioned (REQ-T11-01) and change only through a pack update
after a flagged change (D294), never through a pull. **Copyrighted standards** are excluded from the unattended pulls:
only register entries from open sources (ISO Open Data, the legal texts that cite them) and companies' own licensed
copies (D207, BR-F15-10). **F15's evaluation set** (REQ-T07-05) gates changes of model and prompts, never a law refresh,
which stays ungated (D206).

## Decided by

The owner, on 2026-11-12, who asked that the reviewer's proposed fix be applied (R11, PROGRESS.md, step 21); the values
are the reviewer's, nothing new is set.

## Consequences

Revises D205, D206, D199 and D207. BR-F15-09, REQ-T11-01, REQ-T11-03, REQ-T07-05 and E-F15-04 say so.

## Related

- [F15 Legal assistant](../../02-functional/f15-legal-assistant/README.md)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md)
- [D205](d205-law-packs-fed-from-official-apis.md)
- [D206](d206-unattended-pulls-without-test-gate.md)
- [D207](d207-copyrighted-standards-register.md)
- Independent review of 2026-11-12 (the independent review of 2026-11-12, not kept in the repository)

---

⬅️ [D447](../vision/d447-country-pack-updates-free-hosted-only-named.md) · ⬆️ [Up](README.md) ·
➡️ [D449 Call recording off by default; call scoring high-risk](../f04-meetings/d449-call-recording-off-by-default.md)
