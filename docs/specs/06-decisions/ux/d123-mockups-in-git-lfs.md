🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D123 Mockup images in Git LFS

# 📜 D123 Mockup images in Git LFS

**Status:** ✅ decided

## Context

How the PNG images are stored in the repository.

## Options

- Git LFS.
- Plain files in git.
- Not committed, published.

## Choice

Git LFS: the images (and the fonts they use) are stored with Git LFS, declared in `.gitattributes`.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Each machine needs git-lfs; the images count against the repository's LFS quota.

## Related

- [UX](../../04-ux/README.md)
- [Views](../../04-ux/views/README.md)

---

⬅️ [D122 Error message standard](d122-error-message-standard.md) · ⬆️ [Up](README.md) ·
➡️ [D124 Mockups with each step](d124-mockups-with-each-step.md)
