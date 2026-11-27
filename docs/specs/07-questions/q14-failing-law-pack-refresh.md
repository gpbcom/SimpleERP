🏠 [Specs](../README.md) › ❓ [Questions](README.md) › ❓ Q14 A law pack refresh that fails its test set

# ❓ Q14 A law pack refresh that fails its test set

**Status:** ✅ answered

## Question

When an unattended refresh of a law pack (D205) lowers its test-set score (D200), what happens?

## Why it matters

D200 says a drop blocks the update; D205 says packs stay up to date without any human intervention. A blocked refresh
would keep the previous law until someone acts, possibly past a change in the law.

## Options

- (Recommended) Apply the new texts anyway (the law must be current), mark the answers of the failing areas with "answer
  quality under review", tell the administrators, and retry the test set at each pull.
- Keep blocking until the next refresh passes (D200 as written).
- Apply and say nothing.

## Owner

The owner of SimpleERP.

## Answer

The owner, 2026-11-10: "Take D205 and remove D200." New texts are always applied unattended; there is no test-set gate
([D206](../06-decisions/f15-legal-assistant/d206-unattended-pulls-without-test-gate.md)).

---

⬅️ [Q13 E-invoicing platforms](q13-e-invoicing-platforms.md) · ⬆️ [Up](README.md) ·
➡️ [Q15 Copyrighted technical standards](q15-copyrighted-standards.md)
