🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎯 [Decisions: Vision](README.md) ›
📜 D568 The product is named SimpleERP

# 📜 D568 The product is named SimpleERP

**Status:** ✅ decided

## Context

Until 2026-11-27 the product was written in lower case with a hyphen between its two words, its repository and its
technical slug in lower case too. On 2026-11-27 the owner asked to move to "SimpleERP" everywhere: documents,
mock-ups and their images, the logo, the repository.

## Options

- Change only the text people read, and keep the old lower-case slug in technical names.
- Change the text and the repository, and use a lower-case slug where a system requires lower case.
- Change everything, the local checkout folder included.

## Choice

The product is named **SimpleERP** in every text, mock-up and image, and the repository is `gpbcom/SimpleERP`; where
a system requires lower case (container images, persona and folder slugs, host names), the slug is `simpleerp`.

## Decided by

The owner, on 2026-11-27.

## Consequences

- The wordmark reads "Simple" in the text colour and "ERP" in the primary indigo, with no hyphen, and the symbol is a
  bold capital "S" ([Logo](../../04-ux/visual-identity/logo.md)).
- Every mock-up was updated and its light and dark images rendered again from it.
- The persona of the project's own maintainers is U47 `u47-simpleerp-maintainer`.
- Images are published as `ghcr.io/gpbcom/simpleerp-<name>`; GitHub redirects the old repository address.

## Related

- [Logo](../../04-ux/visual-identity/logo.md), [Brand](../../04-ux/visual-identity/brand.md)

---

⬅️ [D567](../f25-devops-agents/d567-the-agent-team-roles-contract-worktrees-one-commit-verification.md) · ⬆️ [Up](README.md) ·
➡️ [D569](d569-roadmap-option-a-in-twelve-phases.md)
