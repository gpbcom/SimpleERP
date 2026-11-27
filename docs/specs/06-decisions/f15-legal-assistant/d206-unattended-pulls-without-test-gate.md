🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚖️ [Decisions: F15 Legal assistant](README.md) ›
📜 D206 Unattended pulls, no test-set gate

# 📜 D206 Unattended pulls, no test-set gate

**Status:** ✅ decided

## Context

Q14: an unattended refresh (D205) could fail the test set of D200, which would block it.

## Options

- Apply anyway and mark the answers under review.
- Keep blocking (D200).
- Apply and say nothing.

## Choice

The owner: "Take D205 and remove D200." Law packs are refreshed on schedule and the new texts always applied, with no
test-set gate. D200 and its rule BR-F15-06 are withdrawn.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Answer quality is followed through users' feedback (D186); law packs carry no test set.

Revised by D448 on 2026-11-12: law refreshes stay ungated; F15's evaluation set (REQ-T07-05) gates changes of model and
prompts only.

## Related

- [D200](d200-legal-quality-test-set.md)
- [D205](d205-law-packs-fed-from-official-apis.md)
- [Q14](../../07-questions/q14-failing-law-pack-refresh.md)

---

⬅️ [D205 Law packs fed from official APIs](d205-law-packs-fed-from-official-apis.md) · ⬆️ [Up](README.md) ·
➡️ [D207 Copyrighted standards: a register and own copies](d207-copyrighted-standards-register.md)
