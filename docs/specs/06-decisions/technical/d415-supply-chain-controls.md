🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D415 Supply chain controls

# 📜 D415 Supply chain controls

**Status:** ✅ decided

## Context

Step 19g of the technical interview, from TC-12 and TC-17.

## Options

- Dependencies locked, scanned and licence-checked, or scanned only.
- Signed images with provenance, or registry trust.
- The open-core boundary in separate repositories, or folders.
- AI models licence-checked, or any model.

## Choice

Confirmed by the owner on 2026-11-12: locked, scanned and AGPL-compatible dependencies; signed images with provenance;
separate repositories for the closed services, checked in CI; any AI model (no licence gate on models).

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The supply chain chapter's target design.

Clarified on 2026-11-12 after the review (R26, the owner's yes): the models shipped in the images by default are
licence-checked like dependencies; models users add stay free of any gate.

## Related

- [Supply chain controls](../../../technical/security/supply-chain-and-licences.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D414 Security design](d414-security-design.md) · ⬆️ [Up](README.md) ·
➡️ [D416 Observability design](d416-observability-design.md)
